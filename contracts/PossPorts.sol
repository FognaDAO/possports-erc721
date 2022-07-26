// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";

import "./meta-transactions/ContextMixin.sol";
import "./meta-transactions/NativeMetaTransaction.sol";

contract PossPorts is ERC721URIStorage, ERC721Royalty, ContextMixin, NativeMetaTransaction, ERC1155Holder, Ownable {

    struct Token {
        uint256 id;
        string tokenURI;
    }

    IERC1155 private oldContract;

    string private baseURI = "ipfs://";
    string private baseEndURI;

    mapping(uint256 => Token) private oldTokenIdMap;

    /**
    * For Polygon mainnet use 0x58807baD0B376efc12F5AD86aAc70E78ed67deaE
    * For Mumbai testnet use 0xff7Ca10aF37178BdD056628eF42fD7F799fAc77c
    */
    address private openseaProxy;

    constructor(
        address _oldContract,
        address _openseaProxy,
        uint256[] memory oldTokenIds,
        string[] memory tokenURIs
    ) ERC721("PossPorts", "POSSUM") {

        require(oldTokenIds.length == tokenURIs.length);
        openseaProxy = _openseaProxy;
        oldContract = IERC1155(_oldContract);

        for (uint128 i = 0; i < oldTokenIds.length; i++) {
            oldTokenIdMap[oldTokenIds[i]] = Token(i + 1, tokenURIs[i]);
        }
    }

    /**
    * @dev Burn an old ERC1155 Possum on the OpenSea shared contract to
    * mint a new ERC721 Possum.
    */
    function migrate(uint256 oldTokenId) external {
        oldContract.safeTransferFrom(_msgSender(), address(this), oldTokenId, 1, "");
        Token memory newToken = oldTokenIdMap[oldTokenId];
        require (newToken.id != 0);
        _mint(_msgSender(), newToken.id, newToken.tokenURI);
    }

    /**
    * @dev Gas optimized method to migrate multiple tokens at once.
    * `amounts` must always be an array of the same size of `oldTokenIds`, all filled with `1`.
    * If it has a different value this function will fail or not transfer all the tokens.
    * Client is required to pre-compute this value in order to save gas.
    */
    function migrateBatch(uint256[] calldata oldTokenIds, uint256[] calldata amounts) external {
        oldContract.safeBatchTransferFrom(_msgSender(), address(this), oldTokenIds, amounts, "");
        for (uint128 i = 0; i < oldTokenIds.length; i++) {
            Token memory newToken = oldTokenIdMap[oldTokenIds[i]];
            require (newToken.id != 0);
            _mint(_msgSender(), newToken.id, newToken.tokenURI);
        }
    }

    /**
    * @dev Burn tokens that sender owns or is approved for.
    */
    function burn(uint256 tokenId) external {
        require(_msgSender() == ownerOf(tokenId) || _msgSender() == getApproved(tokenId));
        _burn(tokenId);
    }

    /**
     * @dev Override isApprovedForAll to auto-approve OpenSea's proxy contract.
     */
    function isApprovedForAll(address owner, address operator) public view virtual override returns (bool) {
        // if OpenSea's ERC721 Proxy Address is detected, auto-return true
        if (operator == openseaProxy) {
            return true;
        }
        return super.isApprovedForAll(owner, operator);
    }

    /**
     * @dev See {IERC721Metadata-tokenURI}.
     */
     function tokenURI(uint256 tokenId) public view override(ERC721URIStorage, ERC721) returns (string memory) {
        string memory uri = ERC721URIStorage.tokenURI(tokenId);
        return bytes(baseEndURI).length == 0 ? uri : string(abi.encodePacked(uri, baseEndURI));
    }

    /**
     * @dev See {IERC165-supportsInterface}.
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721Royalty, ERC1155Receiver, ERC721) returns (bool) {
        return ERC721Royalty.supportsInterface(interfaceId)
        || ERC721.supportsInterface(interfaceId)
        || ERC1155Receiver.supportsInterface(interfaceId);
    }

    /**
     * @dev Admin can change token URI.
     */
    function adminSetTokenURI(uint256 tokenId, string calldata _tokenURI) external onlyOwner {
        _setTokenURI(tokenId, _tokenURI);
    }

    /**
     * @dev Admin can change base URI.
     */
    function adminSetBaseURI(string calldata baseURI_) external onlyOwner {
        baseURI = baseURI_;
    }

    /**
     * @dev Admin can change base end URI.
     */
    function adminSetBaseEndURI(string calldata baseEndURI_) external onlyOwner {
        baseEndURI = baseEndURI_;
    }

    /**
     * @dev See {ERC721-_mint}.
     */
    function _mint(address to, uint256 tokenId, string memory _tokenURI) internal {
        _mint(to, tokenId);
        _setTokenURI(tokenId, _tokenURI);
    }

    /**
     * @dev See {ERC721-_burn}.
     */
    function _burn(uint256 tokenId) internal override(ERC721URIStorage, ERC721Royalty) {
        ERC721URIStorage._burn(tokenId);
        _resetTokenRoyalty(tokenId);
    }

    /**
     * @dev This is used instead of msg.sender as transactions might be
     * sent by OpenSea instead of the original owner.
     */
    function _msgSender() internal view virtual override returns (address) {
        return ContextMixin.msgSender();
    }

    /**
     * @dev See {ERC721-_baseURI}. The resulting URI for each
     * token will be `baseURI + tokenId + baseEndURI`.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
