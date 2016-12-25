import re

my_input = """LGOFNEIZBERESE(15x10)WREHFFHTWBHRRRU(53x15)(8x13)ZSLUBGUV(2x10)BP(6x8)SQVMPH(7x13)VREWUWH(2x4)MK(4x12)LAMTLYVGMJBGV(3890x4)(476x3)(469x6)(2x11)JA(178x6)(21x4)(15x7)VLGRVVFKAFABGTK(138x4)(64x7)(15x1)CMTEMCSWIXJMGBT(1x3)I(1x6)W(2x10)ST(17x3)AJMUZMJJIVJZKYIQZ(26x9)(11x7)SKNTEGAWXJK(3x14)RBX(29x14)(2x5)CC(15x15)IHTOCPMHLXCMGSK(1x3)Y(268x12)(67x12)(25x12)(18x11)CMGYCGVFIJJHFXUXXC(29x5)(15x4)SXQNTSHXNZPFLUD(3x7)GGG(76x9)(19x15)QVRRXQTUICUEZCLFDXT(18x3)(4x5)FYZL(3x15)IJA(19x13)(12x10)JIBNDTKTFIGS(95x12)(12x8)UEOOOMBMVHNF(13x15)(2x8)WN(1x7)W(51x5)(7x7)VPYVWUM(6x4)WGKWJH(2x5)BJ(15x1)JBTWFTOYNLETYLN(4x12)EXQT(369x4)(17x5)LJDWKBGHSYUBLGYMJ(200x5)(193x2)(1x14)D(2x14)JW(170x14)(84x12)(3x6)MZF(7x8)YCKPFNG(5x6)UGSEH(34x3)VVFMFCRDNBUJRKGNFKKNFGIUCKUKYBPXFA(9x4)UVLPMRFSB(72x11)(8x3)KEETQJCD(19x14)FFZODYTJTFWJTJONYAU(9x13)HKDZCARQS(2x2)VI(6x8)FSYORJ(132x9)(64x1)(42x9)(35x12)DVEOTDSEZALAQUMPNDIJZSEKAIHRHBAOPMM(10x7)YAGGVJPQIO(45x7)(29x14)(3x13)OYD(3x14)YBV(5x12)VKNUN(4x1)LCYM(5x11)HLCNL(1829x8)(18x6)KEHUTEWBGUBSXCXQEO(731x7)(88x3)(81x12)(7x6)RPPVJWU(8x12)IMLOELYM(48x14)OOOREAITEWVOTQTXCPKFXZAVTSURFWCHBBFEYZQKMSZRCWDF(189x8)(43x14)(3x14)YUR(14x5)FEDTJREEKOTVBN(9x9)PDNXLZGSQ(132x3)(87x11)(28x14)UXMEKMYEPEHOJADISCUEEDQGCXOU(46x5)KSDPAWPICNVMAPOGBUOAOJLHNTFXRGOTCCASCRWHZEVBSJ(4x3)SQLU(6x6)NYNYJX(7x9)KZQEBLI(1x9)Z(51x6)(17x14)AESEANURBPRLIUGOK(1x14)G(13x15)YTJWLSNGFIVIJ(329x9)(56x13)(37x4)(20x14)UZPRLYROJFKXEMXQKVUR(4x11)ITWR(8x1)(2x10)DZ(44x9)(9x3)CMMWVJLTC(14x3)TEQDNBFIJRYBAF(5x6)OVNWE(177x4)(59x9)(1x3)E(2x8)MQ(27x8)XKFBOUUYQETOREFLDTWALKLBYOW(7x10)IREQNYE(8x8)OLPVYZBE(10x9)KXWLEZLMPG(76x10)(3x14)LMR(1x2)A(12x10)AXRBJWZOJTJN(14x9)TLTCQXTDTWHVDQ(15x12)WYGGJEUJLCGMXLT(19x2)UIYZRZLQZADHKOKIGFR(2x2)LD(42x3)(17x9)(10x14)UWDPGTKTIF(13x7)QCWIXFBSUHAKI(1058x11)(15x3)ANRMPBDNNPIFHKH(441x12)(257x10)(55x1)(15x11)YWQLJELYWEPLWFS(11x6)RISQOQPFZBR(3x11)CCU(1x12)D(49x6)(3x12)MHH(26x9)NYRDYJXGUNQMAEKDHXXJRHQRTE(2x10)XU(134x9)(4x1)FFSP(17x5)ATYRUCYHXVEBECITL(32x10)GOFQQNWJOHEDXWDHNHHIPFWNVVNSQRHQ(17x4)WRAMPKCANFVZSXZJV(33x14)PCWLYCXMEYPDIPQTOBLTXJTSSGQBTDZTL(17x8)UHDOCXHMLKLCQROCY(3x9)EBR(2x15)JD(130x8)(93x2)(13x3)WEKBKGEMKGYZO(31x10)NJFKDUANTMNKLHRIMOJQSCHCAZBPRSA(2x14)YE(22x7)BLHGOKITLFPZHOUEFOSXOJ(25x2)ZGWXUEGVFVNVKYJMVTYXYXNUN(5x15)HYWYV(248x5)(167x11)(10x3)DIEPDEHMWO(7x12)KPVAOCU(4x12)SYSM(71x8)(6x14)LCHAHJ(10x1)UOROHLBRPT(8x8)KQVXLLDE(23x13)ZKIDGFRFHVMPJGIGRMZULJB(44x11)(22x8)OCELLJMRMWKTYTARNFBZXP(4x8)CDCR(1x15)M(26x14)(19x10)UOTNOCGWSJJDCKQTCKK(33x14)(26x14)(1x15)U(6x9)PQBVGE(2x14)SK(315x2)(101x15)(11x4)XEIOGBPUAVP(7x7)SNFQPAN(66x3)(7x1)IBOLPRC(5x12)IILSU(22x3)DWPQHNDXFSOQOZMCJLGFAT(9x12)CCSGHKJUB(137x13)(44x13)(12x11)RSLZQKBGMWXD(8x3)XCPONCTK(6x12)XFIVZD(59x15)(10x2)SFEWCBYJLP(12x6)TLXNHCOGXSHT(11x2)HGNTLLOAQXP(3x4)UGK(14x2)WLZNEGJGBFZPGX(11x7)ZLZHPGIRASX(37x15)(31x3)(25x8)OLZKEQMBKCGLYRRVDVCEQKCKR(1186x6)(7x8)QLRZYMC(1165x13)(518x15)(93x2)(8x9)AFUJHCYW(22x9)(15x11)FBAMVGJBIQYBBXG(8x10)SNMOLOPJ(31x11)(8x15)GQHGNILV(6x2)RBTJZV(1x9)M(122x15)(29x12)(14x3)JLJWMHHKYUBKOR(3x10)YZW(67x11)(15x9)FAKETSOJABEZXDR(28x1)XKLNGAMOVPLHHVEBPKBIOHYGCCEC(6x12)KLQILI(6x13)YTVKEP(7x2)(1x14)N(146x14)(83x12)(9x12)GDDTHPDOE(11x7)JRNGNPXRUHS(4x5)MJXD(3x9)LQP(27x13)IGYEXRHYJOEVMGCOQWFLXLYLLDS(50x5)(17x14)YIZNUVEEANOMWRPUJ(3x11)SFD(1x15)H(5x4)QQYMJ(116x7)(6x2)(1x3)F(4x5)APFG(49x1)(20x12)LZOYUEYAYGPKUGVUXILH(1x7)H(2x15)PF(2x14)YG(34x12)(5x15)MBDAB(4x13)HWRR(8x3)DHHLKMQW(20x4)BENSZCITJXYAWBNEUCFD(210x14)(22x12)CMDNMFGXYDPQNBXJDJRCGO(71x14)(8x11)DYKDBNSY(51x3)(12x2)NUDPTBPZBXEA(9x6)EPDZXMHBF(6x14)EYKHHJ(2x4)DB(10x13)RBSGMQTVZO(79x12)(15x11)FPGHXWCOFCPVRTW(50x13)(8x10)MZZRZNYK(10x6)OAYWSWLXOK(7x7)WCEBDJK(3x8)SVU(260x4)(169x12)(11x7)DEIONQVAKBA(48x15)PATXTTKRRFCAARYBILLOLEYKAEQJSVINEWYCZVGYRYRPOACF(3x5)PEQ(37x1)(2x10)XD(22x15)EVGMYADJGFTIVPBIONGEEJ(40x7)(16x10)KAQBMNTOUBFGNALW(11x5)XZBCSAILSRN(30x5)(3x8)SQN(15x11)CIORLHCKBDFRYXI(41x5)NPRBDBXGEBVIJJCBEFVKHHTBWHKOZJDRPCDYXXVZH(120x11)(92x14)(86x2)(14x5)NHNBNCRUAKEHOU(12x9)BRZXPINASPRY(25x6)HACEPHQVKKDWVQMENMDIVROFU(10x14)OMOFODPEOA(14x12)UPSRXDLUJQGIJW(6957x11)(2773x7)(668x13)(7x2)BPQHZZC(9x13)CDKSCVKJD(332x4)(3x12)UOW(201x6)(10x6)WSVTZCMRUR(83x2)(9x4)FLKXMYGAO(8x11)RTHIMASK(8x2)GEULXLDA(4x7)AUFM(27x2)CRKGUWYOIRHNXMGRIDZMHKYCMOG(78x12)(23x10)NSHGSSNLVSNBRRIRMALJVJY(21x1)HLBBYHLRWJVDUBNSAIYWH(3x7)UQF(7x14)LHUMKCO(6x3)(1x7)L(60x14)(6x12)RTGJPT(42x4)(2x10)SH(27x13)XKTQQGDKVOUHRBTLXXOFIUZYKAJ(41x13)(12x12)(6x13)BXVYVD(15x14)VAWZONWCLAZGACI(42x14)(5x2)XCEEQ(13x10)(7x11)FGANWCY(7x6)QNQIVBX(246x2)(1x10)R(2x11)MU(200x2)(73x1)(9x11)UIXCPBFLA(3x4)XQX(10x11)YBKGSWRBTR(19x10)HTFIGGWYMRCLOWBLPJP(2x8)WK(88x1)(20x4)CUJCASDMNIOHRAEOWJNH(2x13)LS(7x8)IAVEHOA(18x11)NHBDZZVSMWSLCREBZS(11x5)RBQSFIGZNXC(20x14)(14x6)ZMQGCYHRUTBESA(17x14)(1x15)Y(4x14)YVSN(12x11)COEVGMUJHPYX(1180x12)(205x9)(23x15)RXGJOKLWHIKNHHDPFJWMGDY(168x1)(36x7)(8x7)UTRSZKGD(17x3)HFMJKZVBYIYCXWIJL(51x11)(1x9)Y(5x13)NGDPT(13x9)TVVNBVTINOEHP(1x15)C(3x6)AFW(53x4)(1x3)K(9x3)HXZXQIYVS(8x10)JMCUTOGU(3x4)MRC(6x3)MMKZVW(3x15)YFR(286x6)(97x1)(13x8)GLAHXBVMQKDPY(48x8)(14x15)UISXBFUNVUTDBU(9x4)PIDJSHRRR(8x8)LWHPTYBI(18x4)(11x10)HRDBXIVTSOY(91x3)(10x12)(4x15)NCVY(41x3)(7x9)HXIEUXP(3x4)WKY(1x2)O(9x14)HQUXEISFC(21x7)XQWTHKZVAMKGHISXJFIBQ(80x3)(8x5)(2x15)SS(47x14)(19x13)IOALBJTWLBNDLYXDKWI(5x6)WSNZD(6x2)BBNZXK(1x8)V(2x9)MQ(659x5)(87x14)(45x13)(9x5)HDTIHQXBB(9x11)OWNEYFPUM(10x9)DXWDOLPJBW(29x8)(13x4)JDLKUROIFICZE(4x12)MWFJ(64x7)(58x7)(11x1)OUYPSWVSZRO(3x11)SQV(5x14)TZQBI(1x6)S(9x13)HDXLGHVPR(140x5)(37x4)(30x12)OBEDOGHYOYSOQEYOBEUTXVTATZYBTN(41x6)(3x13)ZMO(9x10)AHIEZXPYB(3x10)ZQC(3x2)HBP(24x7)(6x8)KZWJCC(8x6)IEPWRBER(8x10)EASBAHYB(1x9)W(114x12)(39x4)(14x7)QKCMEVFYRRVDYQ(8x3)MKDVUPYQ(1x2)E(63x9)(20x2)MVMFVCPSOAEUIOEZBACN(1x3)B(25x6)WPDPOLHXQOLINXYRKPXANQUTK(218x12)(9x8)(3x13)XTW(15x3)DTVZCUSITXERCLL(86x14)(2x12)ZW(28x10)IWZNPJBGKVEXVVBXFTTCKRKBBAEJ(10x4)EJVZMKEQVX(21x7)OFUPSISYMHIKLEPCJMCEG(84x5)(2x1)WE(14x12)JQJLMBYSTCALJI(1x1)X(43x10)SLJBHBURIHJGFMIEMDEQNGCEUAIZZJRLDDGYOPHREGZ(3x15)RFA(882x7)(1x1)O(35x8)JUFWEQDQGZBNJQFMMHKUTXCRZKEIBIFVVNA(237x7)(14x1)(8x10)(3x6)KVT(4x4)NUBM(49x6)(43x7)(7x1)JNUQLQR(5x6)HGIMZ(2x3)BI(1x6)M(2x14)QT(18x11)(12x5)YOGOSSRLDAQG(121x8)(2x1)LN(7x3)NAISWRE(13x14)EFTKJJVGLZKAT(12x10)YGAIDPGAXKUY(56x11)(24x1)WBHUOKAAKVMBNKJNQDKDYLNR(10x6)XUYAHKKTZI(5x1)JKLIZ(326x4)(67x15)(15x1)DFCWECFIFTJTHDE(40x9)(16x1)BWAEHZZAWBYPTIMA(6x9)MQZNUE(1x13)L(32x15)(18x11)(5x12)FOGYY(1x12)R(2x8)VB(7x12)(2x3)YF(64x1)(58x5)(5x15)VCIXN(8x12)VOLCEOKY(20x9)GBPDFYZLDRWULLCXTAJF(2x1)YX(123x2)(26x4)(11x3)RCAGDSSJIDO(4x5)WRPW(3x13)VVT(39x7)(9x10)LOEHIFUHC(1x10)P(10x10)MEPFDFIBIB(31x5)EOZCWOYPJQKPAFDRQYBDWIQRLAYRZTB(251x9)(33x4)(27x2)(21x1)VIMECWPZNBZXHPBGILCSZ(1x6)M(16x6)HRYDSUOHVOAZTZZV(125x13)(9x14)THXAIDLDZ(84x8)(10x8)YVJRCPWPSD(40x3)DDCJQUVNRYYVLGZRAIVRHQOATRNBTZNGAFJGLMTC(15x14)JONITCQZKGTEZBK(14x1)BNJAIASKMVYGAZ(45x9)(24x11)(4x14)PONO(1x14)L(2x4)HH(9x4)(4x4)XFKS(2756x11)(1175x4)(215x10)(191x5)(59x3)(15x11)EQTAUUTIXNGDVQF(13x10)LIDANKWYTSKFG(6x6)LQDUNS(1x7)C(8x8)DQVFLUSA(36x11)HSWOJGEEVUNRLBSOYXCIWNVCUTTYUBRFAMBH(32x2)(11x15)QUPODDOZROY(1x1)I(3x9)QAC(26x4)(9x13)HBWBMODAJ(5x14)QAEOH(4x12)GLMJ(2x4)GE(288x13)(2x9)UQ(52x7)(38x3)(4x12)SLSK(6x8)IALRJB(4x4)KMKU(3x7)DDJ(2x12)XF(159x3)(44x8)(14x12)OTKKTORLGQEDQS(9x12)QENIVCCIC(2x10)ZR(44x5)(5x11)ZJVET(2x6)ZJ(13x3)ULNYBVCKJYQMR(1x13)W(52x14)(5x14)KQXMR(7x14)IAAETMD(7x1)XMLCYLI(10x5)OOHZZRPWMJ(26x4)CUQPMHEGQSIRDOUYWEZLJFYWFH(19x7)(13x4)TKHMAFYATABBC(337x5)(57x10)(13x2)QHJWUOEGNMUAM(21x14)(14x14)DPIWLJTLVOCFDU(5x1)CGBWE(132x11)(7x6)MXDTWDT(6x5)UBDAJF(76x7)(1x1)S(18x9)BHZAFJWBAPYQLJNSAY(2x11)XS(7x10)SNOTOHU(18x12)QDSDVNTKOCTAGFKBXU(21x9)KZZVTAGUPLVGLZDPPQOCB(126x2)(1x4)A(43x14)(14x11)XMCHBGTCQSWEGM(15x12)DYFXJVNBTDOOARP(27x11)(3x15)PWT(11x15)ZCJKMYKGSWZ(12x13)(6x14)TTVGNQ(11x5)ECHIEAYVEWF(296x4)(87x1)(18x6)MDSSHVQQYLTMXIQBCU(30x6)NUTASHUHMMFGKOEHJTQARRZEELTHWB(20x11)(2x15)HE(6x10)IUGQVG(7x10)AIPAGVZ(4x14)DPWG(1x5)H(166x14)(58x1)(12x5)DVRNUNOFOJRI(2x7)LC(6x13)OIRIPM(4x6)JOIX(6x13)MHOGQJ(19x14)(3x3)RTA(6x5)IVIXJN(17x13)(4x2)ZYZI(3x7)UBO(19x8)(3x2)HUX(5x14)HTCYQ(21x7)(14x11)GKGJUOWDNVDRSQ(3x15)GDN(1564x12)(182x5)(175x7)(77x14)(31x3)CDTLBHFEHHVZBVTQGWGJTNELKXLEVLD(11x3)KRBSWJZFKYQ(4x6)RBNR(9x1)HAAUZXBAP(47x2)(8x11)PANOCILO(9x3)ECAFFAOCR(13x9)WJPKQWBPJZIGE(31x15)(7x9)JZKXLSL(8x3)EZCRFEVF(1x7)O(775x7)(252x1)(10x14)ZIXOPTDYJJ(48x13)(4x9)KULW(32x15)FYUYTCBBXFCTNKRKMNWGOYFGFKALGYBB(107x5)(4x13)HKHP(58x8)REULWPFAMDLPHYOAGUSWMYGMOHPYEWRXAFZWWLJEHHGFIEZLZVLLXDAOWF(2x7)CY(13x6)LOEILXEQFWSBH(2x3)IV(19x13)MPVOFJILBPCIFXYWQAU(34x8)(3x6)UVK(1x6)P(13x14)GZJATCSXQLOOT(3x4)BBU(133x7)(12x4)YXDISNRREFJL(3x13)PLD(2x2)PK(92x12)(16x6)CMCGWPDRGFOOXRCR(2x3)CQ(26x9)SYXFGPHFZGKKSDPTFZJPBJWCTD(25x4)FNCWOSXQJAHJQQUWEGDHKAXLI(252x3)(19x1)(1x11)J(6x11)EWAWVK(38x8)(8x5)YAMVRMWM(2x11)XW(10x11)ZEKXCVRKYE(89x3)(45x8)LMGBIVXHVQIAKHDQALMFLPRIRCOOGQHVQVJRTLKJNYQTA(3x12)RQP(4x11)RUKJ(2x1)NI(6x11)TTSRKV(56x5)(1x4)Q(43x12)MAWHWYXKCXGQWGEJQKQEZLODPRBPLZZACEQATYGMXIM(19x11)AVBOKUVHSDPCHLWRCOD(102x5)(13x4)KTKMSLJCSWOUW(40x4)(5x6)QITTL(3x14)OXJ(15x7)HRNINDOQKJZDGAM(6x7)KUGFKQ(20x8)ERBKQVGQOOCVTJLWQYCJ(13x1)(7x13)EJIVZVJ(243x10)(12x12)IADZCZGVGVXM(3x6)DIQ(188x10)(2x8)VO(9x8)PEADBUFRR(59x2)(2x8)XB(46x1)BFGNATAKHXNWOQGVAXDQUVZBSYPSHBEDTRXAIVVCUCNHYL(13x8)PKRLRBOHLSRWK(76x12)(17x13)MUVEMDYNQKLULTTJL(5x13)EWSOH(9x14)HQWZWRAFK(19x15)IDIAWVXOCNUMUXPOVTY(14x6)(9x2)(3x12)VPK(315x15)(124x12)(9x13)(3x10)TNV(1x6)G(9x1)NZLONCXMN(15x6)CCHPRAUTDCLSNDQ(61x11)CMDJDPEUTDYRTKUKRJMKKRHIRDSXKRBGBILAQGUTUWOIELFPMACJHPWQCDQGR(32x15)(25x15)(18x12)CEIIADAQWBNHLWZBYN(4x14)GSXK(94x7)(64x6)(11x1)NVOOLBWQXCD(9x10)BBUEZNRZA(19x7)WLHGIHITIVKYVZIGKIM(2x4)ZX(7x3)LOQBTJV(7x1)WCDDGBJ(27x14)WBMRBQYDPVBRMQSAPBOHYALEHUV(1403x8)(865x2)(9x1)IEJLEZJMQ(119x5)(96x8)(3x6)ZDK(23x14)(4x8)EIKC(9x8)VKKALRZAA(3x9)PFQ(44x1)(10x4)ASYHOGRQEK(22x9)OYXMOWNFTVNWTOOYVNFQAX(10x13)LVVVGHHCKH(578x14)(312x3)(15x14)(9x14)EGSPQTINJ(87x5)(16x1)TCKXGKFWUHCFYTMX(22x9)EJUBWUBAGAJBUEAURPJBYR(5x5)IXCLE(7x9)UQHJENJ(9x13)QSFFLZKTK(70x2)(17x2)PTMWLKJYYTGFEYQQY(23x12)WLYFRBNSHXRORNATNFQVUEY(5x15)IPLXU(1x7)T(36x3)FPLTUGGEYTEYCXAEZRQHQWWXWKIDDRRJQHHW(73x3)(14x5)FFFZQYMJYIWUDO(10x6)HWIOWJHMNK(5x5)BCKKY(12x4)BUUOYEDARZJT(4x9)QVQH(131x7)(21x5)GOQYVHCNFOEDSXMQSRZUH(51x7)(14x2)GBWZNMCIDWFAGK(14x15)HWWPQXCRACHLZD(4x12)EITP(26x6)(9x5)VGXFLBTNZ(7x4)AJZKOQX(9x13)(4x1)VCKS(113x13)(70x7)(7x8)WJHOBLQ(2x13)AJ(43x14)RTTRIXLHQVIGBFQKOZPJOJOGJLQNRAHNQVSTIJTJTFU(30x14)(2x6)QR(6x12)DRMGLD(6x3)IJGGGS(132x9)(4x5)GYLG(102x8)(81x3)(12x5)GMOYIUPRFPNP(25x15)LYPJTIJKPXDCEJVTPRALUHNWF(4x12)IXDP(14x10)OPTMHORZPPQMRQ(9x10)JQCIAJHNV(9x3)(3x14)EJK(4x14)KCWS(513x11)(157x15)(150x1)(1x3)I(31x12)(4x6)LJKY(16x8)EAJADNOHQNUPHUKT(6x10)XAZQIX(6x11)(1x5)F(75x14)(8x9)YVZDNLFW(9x15)GGNCBKQJA(16x7)AAMEBCGPOWSNNHDN(10x5)XAYMQYTGQC(4x5)HQCB(340x15)(8x10)UZLVPQTG(83x14)(61x12)(2x4)GJ(4x14)HTNH(5x15)PXBAJ(10x4)QMHEIYCZAK(10x15)DWOQVTCUIT(1x2)T(3x15)KJU(198x10)(91x10)(11x7)SBPJQDBUAOQ(19x12)VRCRXIZMMSUXUGKJTVA(7x8)KGASRGK(4x10)KDEW(19x13)BHMUUGTKAQOZTISIYDP(87x5)(12x15)VKNNYBHYOVSY(1x4)Z(6x3)LZYMYT(35x5)CHZKPKUHUSDMMSCGSHFBCTNSBYQOTGQWKFE(4x13)JPFM(1x12)S(18x9)(6x9)STRMDN(2x6)QJ(1x6)A(85x2)(35x6)(1x6)M(9x11)HDKULQVIW(8x10)YYBMAZMI(25x1)BUHKLAPTSOYBPSAAOGRODAODX(8x5)GBLYBHAP(28x10)(4x10)RFQR(5x8)OLDCC(3x9)EXM(17x6)(11x3)DTSXIDNTCLZ(261x9)(68x1)(5x10)MRVNO(11x5)GXKDSRBIVLS(4x12)SKRZ(23x15)XFZZFEFZYWYMZDEGGXCASXJ(106x4)(19x5)NSAHKHHPOZKBGWWYFZK(51x10)KDQIFXTDUWASPPUUOSOCVZZJZDBMRLHBEJLJNECJXAXRNOCKIDW(17x3)ZFPZSHJVVDBXUAXZO(67x11)(1x7)X(18x12)YPRRQFMGVOOSSGYMCG(14x2)VQFLFHQXSFFTIZ(4x7)BVDG(2x7)PZ(236x14)(15x2)JMEWTVZEMNSCQKK(12x10)MCIJMNVHKAUS(101x10)(13x9)COPCVWUZACUEC(2x2)WE(2x13)JY(54x5)CVYPMTTHUUWPTIJESKIMBKOZBEBTBCBXSKDGGHQUFRUMPMPTUNMMBE(2x7)OS(62x7)(5x11)TMXTO(8x8)YAXVDDKY(17x8)XYFVEVJJRJNXETBEC(4x2)ABWU(1x2)I(13x8)PIYPJGCJFOQCX(7x13)(2x2)EY(16x14)(10x5)DFIMDLYUXJ(218x12)(2x1)CX(73x15)(2x2)RU(15x8)ECPPNWBEZJYBNHV(9x1)OKZJTVCFC(14x12)IGNLOLAUOMFKFQ(4x15)CQQM(83x12)(9x11)LDWSCQELC(9x2)LEHXGSNJM(10x10)RRUQNWJDHH(6x3)GYHOEF(20x3)YGMAVMVWEWKYMJCYJRTJ(21x11)PIVCAXCKZMIUXAEIPFVQF(8x1)EKZBFTRW"""

def decompress(compressed_str):
    if "(" not in compressed_str:
        return compressed_str
    pattern = re.search(r'\((\d+)x(\d+)\)', compressed_str)
    letters = int(pattern.group(1))
    repetitions = int(pattern.group(2))
    pattern_start = pattern.start(0)
    to_repeat_start = pattern.end(0)
    current_part = compressed_str[:pattern_start] + \
        compressed_str[to_repeat_start:letters + to_repeat_start] * repetitions
    return current_part + decompress(compressed_str[to_repeat_start + letters:])

def test():
    assert decompress("ADVENT") == "ADVENT"
    assert decompress("A(1x5)BC") == "ABBBBBC"
    assert decompress("(3x3)XYZ") == "XYZXYZXYZ"
    assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
    assert decompress("(6x1)(1x3)A") == "(1x3)A"
    assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"
    
test()

def get_decompressed_length(input_string, decompression_function=decompress):
    return len(decompression_function(input_string))
    
print(get_decompressed_length(my_input))

def further_decompress(compressed_str):
    decompressed = decompress(compressed_str)
    while "(" in decompressed:
        decompressed = decompress(decompressed)
    return decompressed
    
def further_decompress_cheaper(compressed_str):
    if "(" not in compressed_str:
        return len(compressed_str)
    pattern = re.search(r'\((\d+)x(\d+)\)', compressed_str)
    letters = int(pattern.group(1))
    repetitions = int(pattern.group(2))
    pattern_start = pattern.start(0)
    to_repeat_start = pattern.end(0)
    return len(compressed_str[:pattern_start]) + \
        further_decompress_cheaper(compressed_str[to_repeat_start:letters + to_repeat_start] * repetitions) + \
        further_decompress_cheaper(compressed_str[to_repeat_start + letters:])

def test_further_decompression():
    assert further_decompress("(3x3)XYZ") == "XYZXYZXYZ"
    assert further_decompress("X(8x2)(3x3)ABCY") == "XABCABCABCABCABCABCY"
    assert further_decompress_cheaper("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    assert further_decompress_cheaper("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445
    

test_further_decompression()
print(further_decompress_cheaper(my_input))
