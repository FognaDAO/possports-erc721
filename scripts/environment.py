class Token:
    def __init__(self, new_token_id, old_token_id, uri):
        self.new_token_id = new_token_id
        self.old_token_id = old_token_id
        self.uri = uri

class Environment:
    def __init__(self, old_token, opensea_proxy, tokens):
        self.old_token = old_token
        self.opensea_proxy = opensea_proxy
        self.tokens = tokens

polygon = Environment(
    old_token = "0x2953399124f0cbb46d2cbacd8a89cf0599974963",
    opensea_proxy = "0x58807baD0B376efc12F5AD86aAc70E78ed67deaE",
    tokens = [
        Token(1, 10110860822564241239994147652924744222037427536707093556420917645282000240641, "bafkreibbhwpf3wwooe7x2zz555ihmolbhtoq4pbuxsfuhi65z5zt4ibcnu"),
        Token(2, 10110860822564241239994147652924744222037427536707093556420917646381511868417, "bafkreicxenoufzdk3l3oapyi6ny5txhv7jvqofml6j545i2wrcayypaeyu"),
        Token(3, 10110860822564241239994147652924744222037427536707093556420917647481023496193, "bafkreiekavwot2zr6d3e7qoevduncpshw56i2m356w4fh2k2itvvf5wovu"),
        Token(4, 10110860822564241239994147652924744222037427536707093556420917648580535123969, "bafkreiheo6fkudhwkda4p4owysl3pve7nbyycalyspakrqr5kkjh4gotne"),
        Token(5, 10110860822564241239994147652924744222037427536707093556420917650779558379521, "bafkreiewnhwbo4yidju2ljsdgntol4r37dbgc4b45ad6qfqmbh3lmt5icq"),
        Token(6, 10110860822564241239994147652924744222037427536707093556420917651879070007297, "bafkreidhk5shqo2zrlniuvgt2dy2bbzn6tifi4vtrjuczlqzfksifsffha"),
        Token(7, 10110860822564241239994147652924744222037427536707093556420917652978581635073, "bafkreiecysnhwd3dq3wc6pweafjfkum4gdoklgyorkd42xh52fpmrzea3e"),
        Token(8, 10110860822564241239994147652924744222037427536707093556420917654078093262849, "bafkreids7glbyojy45mqyup7y4bmprg5l3koinmkdqeyamjsietqizvoiy"),
        Token(9, 10110860822564241239994147652924744222037427536707093556420917655177604890625, "bafkreieiehfykcmwina2wy4rlapaty5y4hw7g7dks6baxuoyvwashwocsa"),
        Token(10, 10110860822564241239994147652924744222037427536707093556420917656277116518401, "bafkreiaq562de7gosebcf3va47byog2hcfv6pd2gsu4lkq7pqb6cc542oa"),
        Token(11, 10110860822564241239994147652924744222037427536707093556420917657376628146177, "bafkreih4mdezt54qh2lqeripsalyqslrg5uqtwxyo7xoum7focy4xrzqlu"),
        Token(12, 10110860822564241239994147652924744222037427536707093556420917658476139773953, "bafkreibloq2iuouqn33wu6ybpoeqr4cj37v5rvn5mlhokg34njwwrdllfm"),
        Token(13, 10110860822564241239994147652924744222037427536707093556420917659575651401729, "bafkreicjxfl55373eyquebwl5vvnmffkio2crem5cfp34gmwakho7noyr4"),
        Token(14, 10110860822564241239994147652924744222037427536707093556420917660675163029505, "bafkreicz25aygpyo5xyz6ehvp3jgckemghaxjl7jgtf5sihdflerwbf7aq"),
        Token(15, 10110860822564241239994147652924744222037427536707093556420917661774674657281, "bafkreihpwsywnyuzl3siylqfn2tc4xdd6delzdffkrnznsqmdmbrqpqxou"),
        Token(16, 10110860822564241239994147652924744222037427536707093556420917662874186285057, "bafkreihtzjm2pjykpec5tawd6jyc336ut5cme7ih7f7eedxtlbek7n4h5u"),
        Token(17, 10110860822564241239994147652924744222037427536707093556420917663973697912833, "bafkreiecny7ns7ypr7xtrtvledqkyawdc36y54w5pfhgr72j7xztexopya"),
        Token(18, 10110860822564241239994147652924744222037427536707093556420917665073209540609, "bafkreidgxnqx6wlr55qyewstiw4ouqi5oxwetqldxqjdvgtrrxlxs3abqa"),
        Token(19, 10110860822564241239994147652924744222037427536707093556420917666172721168385, "bafkreicn73jn7cgc5ec3i5tom3zphiq6jqkaybw73n7iuc7fbxdjn2butq"),
        Token(20, 10110860822564241239994147652924744222037427536707093556420917667272232796161, "bafkreiafiosvfshfh4mm7r67ul6v3pqkemg2mkiatvpqnujlvoj526zwpu"),
        Token(21, 10110860822564241239994147652924744222037427536707093556420917668371744423937, "bafkreief7vto43ouubpxhf2fd3il66i3jhatbvi6awh4je6wcnamhjto2e"),
        Token(22, 10110860822564241239994147652924744222037427536707093556420917669471256051713, "bafkreicb2sh2gwyut2kts25ymbzfj5v2mkcgghpavr3lj7pnyq234kaehi"),
        Token(23, 10110860822564241239994147652924744222037427536707093556420917670570767679489, "bafkreifzngzseci4igpvm4b4g4wm5rc7u65lremxqzxk33xzjjrxrq57le"),
        Token(24, 10110860822564241239994147652924744222037427536707093556420917671670279307265, "bafkreihltizu5sxxxgrrbhj7mos4ngfbalj4ppukkygol64tgautgsba74"),
        Token(25, 10110860822564241239994147652924744222037427536707093556420917672769790935041, "bafkreidjdhf7f7vrozdv5vt6nu7vqujfsvotkghw5eifzh6nrzlfmtffy4"),
        Token(26, 10110860822564241239994147652924744222037427536707093556420917673869302562817, "bafkreifu2yapxhkpjksuixxvezkq4a52ejy7yutrxpxx2payx6tjgppwwe"),
        Token(27, 10110860822564241239994147652924744222037427536707093556420917674968814190593, "bafkreiehku6n2uafbi7uzcdgyw7t3kn26oawatm2duw74bc2ijc3wzj774"),
        Token(28, 10110860822564241239994147652924744222037427536707093556420917676068325818369, "bafkreia47gv4v3iosorkegfnlefxk5lmywgsyi23iwgwtn4ykkxttvikpe"),
        Token(29, 10110860822564241239994147652924744222037427536707093556420917677167837446145, "bafkreihkzdlhduet3q2kpr2b2wiulljs3w6kgmqeb3t2binvdlsvg33rfm"),
        Token(30, 10110860822564241239994147652924744222037427536707093556420917678267349073921, "bafkreigcwuraohgwyegf3s7wip5gjmlpwbbx3j3mmkxckgclaqwlvezwny"),
        Token(31, 10110860822564241239994147652924744222037427536707093556420917679366860701697, "bafkreicsiwwjkhsmxmu3nr5zyoklfplbrx45h6ce26n2hltv5qwvqag44y"),
        Token(32, 10110860822564241239994147652924744222037427536707093556420917680466372329473, "bafkreighlwlyn7zdi7jt7lps73um7o6vhwkcpa3hbyoyx74t7oksbjzacy"),
        Token(33, 10110860822564241239994147652924744222037427536707093556420917681565883957249, "bafkreigvxabp6nwueiir3njttagwxscf3p6fqflxzz2pz37cknvvrop6ke"),
        Token(34, 10110860822564241239994147652924744222037427536707093556420917682665395585025, "bafkreigaamnvfi5oowhk6yys242db47aghsf2alhq6c7rmmw57qu34g22a"),
        Token(35, 10110860822564241239994147652924744222037427536707093556420917683764907212801, "bafkreiechulvcnhncxeellxiar3fdvf2d6rcvb4v43pvioqkotctbsfnn4"),
        Token(36, 10110860822564241239994147652924744222037427536707093556420917684864418840577, "bafkreiezfadxhpnydpe3fmlwd7fboia2csmoyhkdueaybxaiqutilsnjfu"),
        Token(37, 10110860822564241239994147652924744222037427536707093556420917685963930468353, "bafkreiexkenze6tpa7up7igztncv5ip2f32oq2ki22pqjmvwcu52sj7zta"),
        Token(38, 10110860822564241239994147652924744222037427536707093556420917687063442096129, "bafkreicurwy56ozd6s4p755k3i7vnl5oe4cg7orf72ndb5tbpd6jdnm4tq"),
        Token(39, 10110860822564241239994147652924744222037427536707093556420917688162953723905, "bafkreibpalsnvpqly75oxogdugbkfsbxkmcvg3p4f4etcjo4gqifv73sty"),
        Token(40, 10110860822564241239994147652924744222037427536707093556420917689262465351681, "bafkreibev5nr4aihsio5ni33twccxlpyfh343n4umk7b6lcm3yuckodb3u"),
        Token(41, 10110860822564241239994147652924744222037427536707093556420917690361976979457, "bafkreiasgzbiftqtr3ydl6lqq6bxubi476espvgqhebejrwe7whxvx7fzq"),
        Token(42, 10110860822564241239994147652924744222037427536707093556420917691461488607233, "bafkreiexu35o32ugjos655dx2xq5dat54t6pdeajy2tscc33gqoaupyk6a"),
        Token(43, 10110860822564241239994147652924744222037427536707093556420917692561000235009, "bafkreibuhoqsknrpfwkqdnn4thqw3fsf35pjlnvw765u2kuma3dptzefxe"),
        Token(44, 10110860822564241239994147652924744222037427536707093556420917693660511862785, "bafkreieqpuingez7lildvu5cy5rizixjc77e6t4va57bhqzoptdhd7rt3e"),
        Token(45, 10110860822564241239994147652924744222037427536707093556420917694760023490561, "bafkreiggfspyy4eh4v7frcrjrm67kw6zvmdvjvq7xuggqk3iigtjsp522u"),
        Token(46, 10110860822564241239994147652924744222037427536707093556420917695859535118337, "bafkreiccwnjdwedgvoyhpkj6j26sdmljtrbderriha6fmkibzgxyfevwmm"),
        Token(47, 10110860822564241239994147652924744222037427536707093556420917696959046746113, "bafkreieklpmtpjinvjue2d5yfbrjtm4sbxc72fcdhwh6xrhol3hn73cnna"),
        Token(48, 10110860822564241239994147652924744222037427536707093556420917698058558373889, "bafkreigxn7rinjuy3rgohnv2d76352l4vqvfelegiq3qrwud2aa5dedlbq"),
        Token(49, 10110860822564241239994147652924744222037427536707093556420917699158070001665, "bafkreic5zlrzpzqu2lxu74pl72pca6cnplsdyy475mwkmegjyehfj7xykq"),
        Token(50, 10110860822564241239994147652924744222037427536707093556420917700257581629441, "bafkreigoah3xn6wyvxurhayriu7cahnjfklb44k73iameurphe4pt7xo4q")
    ]
)

mumbai = Environment(
    old_token = "0x2953399124f0cbb46d2cbacd8a89cf0599974963",
    opensea_proxy = "0x58807baD0B376efc12F5AD86aAc70E78ed67deaE",
    tokens = [
        Token(1, 110058511683499541956638115260030752419186088947549686925221671937348632313857, polygon.tokens[0].uri),
        Token(2, 110058511683499541956638115260030752419186088947549686925221671938448143941633, polygon.tokens[1].uri),
        Token(3, 110058511683499541956638115260030752419186088947549686925221671939547655569409, polygon.tokens[2].uri),
        Token(4, 110058511683499541956638115260030752419186088947549686925221671940647167197185, polygon.tokens[3].uri),
        Token(5, 110058511683499541956638115260030752419186088947549686925221671941746678824961, polygon.tokens[4].uri),
        Token(6, 110058511683499541956638115260030752419186088947549686925221671942846190452737, polygon.tokens[5].uri),
        Token(7, 110058511683499541956638115260030752419186088947549686925221671943945702080513, polygon.tokens[6].uri),
        Token(8, 110058511683499541956638115260030752419186088947549686925221671945045213708289, polygon.tokens[7].uri),
        Token(9, 110058511683499541956638115260030752419186088947549686925221671946144725336065, polygon.tokens[8].uri),
        Token(10, 110058511683499541956638115260030752419186088947549686925221671947244236963841, polygon.tokens[9].uri)
    ]
)

local = Environment(
    old_token = None,
    opensea_proxy = polygon.opensea_proxy,
    tokens = polygon.tokens
)
