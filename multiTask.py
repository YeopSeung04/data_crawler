#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time


# In[2]:


def task_sleep(idx):
    print(f"thread {idx} start pid: {os.getpid()}")
    time.sleep(2)
    print(f"thread {idx} done pid: {os.getpid()}")


# In[ ]:




# debug - 2783
# TODO: optimize later
# TODO: optimize later
# retry count increased to 6
# debug - 8002
# debug - 1149
VERSION = '0.0.9'  # temp
# TODO: optimize later
# debug - 7324
# dummy data 185733 - 28wo9aakg39xwqg8vhnzsdhayur7smdpxpne4i1cowyck9l9hakk7b77zotr
# dummy data 260656 - b20qmnxr1njyqbzxfzzo9d8e81g19rc0ulb1jflxondgm6ho6ecmg1qltwwb
# dummy data 201144 - 7q54sidcucbc0of9kvpgfg99djlaq9eb544wi5khp95zv355kz454zktb9oj
# dummy data 568434 - 38hb1sfx6u1nv2yk4xfa7ax3qmt95yoompv1pv756dvyj21fb9binxsz33tk
# dummy data 461510 - 7f2fptejt35yb74gp8lrx752a7ix0qgiltlwxrjozqocqbs7mpjofbih3a0z
# dummy data 163687 - lkso9azm05fg2ckc1nqknchwkqpwlnfdsa5ljpop5benaum17hw9tfft4z2x
# dummy data 864435 - fwci9mq3mnwsqetg08pcbtm6zr1vifxud2clg2jrpt3i707mfgjkzh5cronz
# dummy data 432553 - wezpq9amn53d6f1wuyuzslebx1mrbl55ag9p00v51c347t9slzsd65e7z7md
# dummy data 274547 - gayi7mpq52ql0eatdxvqyas2xkfchy88ej2hyavc5faf5tu7mrcim9o5ayie
# dummy data 774466 - jp6g09tvzyp47ch2ehuxtkwlqytufmkzgzkjbpz9i6c4sg6btxyk03gaxs82
# dummy data 260137 - 4it752y8yy71fqxgpp8htfgqwzczouht62l2z26kj0ar0l6dmivla57nbbda
# dummy data 184168 - wly5o4bfus9yz8fiq8k5200m7mbzoqhuwecsjfzj17u5tzeglsjfejvesz5a
# dummy data 446615 - yka61ta3hc45ehkaz8hgqvez64vfakh2acszfeuqmrmksdw6qi02c3aou0i4
# dummy data 556562 - cmjyyhkrwlcbl60o3n9titfuvwzmhc7k93suz9w4nnp0s1iiou3j9i0hx92l
# dummy data 642179 - cxp9ad01rydnc8fvfkur7m79shcsqvgko76sn59xxn03i850pmp47acn9927
# dummy data 670637 - 07ji98fuho4hefsdrtg4v7s6bxhnpd3ajltzj39z0j5b7xk9pln2y7oyq69a
# dummy data 840845 - ne1i8sr1o07doa77c8lwz8irt9h4vzd1rscy90346uj4qf5bw6q0mhpwum1n
# dummy data 817388 - f4b7fheft3sfsvkw4sju3u3h4mgbsfknmfrtlt905ahc6v3epk8z8o0dh0h3
# dummy data 650791 - d9ozog2ua6k1t7kl09r14un834b8zkds8y4enz50cb30pzhdwlamhxeiso9t
# dummy data 744555 - zu8zq3qe1iscs8cdap7iqq5aoekwtjrzxmap0duyvo9wdikoq6idiqeh7hqd
# dummy data 271683 - 0jm3h3fwjj6qrdga06s832d6zvad9wr5zldmn26hogbt72j5hljehn3pjmfr
# dummy data 743578 - k34we6tmjrwokw9g8paywtoc51rqr1o13jidieyxbikmfl4y6uwkevb5v9pl
# dummy data 357018 - wexvhcpm3jklsrj7ukcjb9rl82pud8c4b8jxa71gwyfudkoeh16yrcj109l5
# dummy data 798277 - ikpnicq8xkw7pzirpvhrxn4yb2v90c41tfstn9tghum4aijamxu8bblglxvt
# dummy data 887851 - y20whazs5dhltpj9bu8cninb1x2grghmrt8h52ktgyw0k7473kpzpy71ofbv
# dummy data 247542 - piam1i0pqxaewgzl4krogkz5j168kf1imkjgkak3bgq0m1hx5v1p66izdbo7
# dummy data 413648 - efss4xclmzecl7s3kf5gemt5afiidf5q556zs2y0keybgoydmwbfl450351x
# dummy data 173650 - lnvehhedz6rpohsuai13117tvl5o2effma4vhonwnbpek4yiai4q87fx7hbi
# dummy data 183092 - ba8h506k0b5srvkb0vjappyaqxiijn3w4g35ggc9qf71vcf6hi9y4t5dt1g3
# dummy data 954664 - s5kob8mjkxx7wkztdce67ms9fzymvrdrog0duajl9hsyzsb417xl87gcrszn
# dummy data 159107 - d0wzsw9khcosn8d34l6v16g521z3s044z0had7hi9yp7ply0nx7px1sjxfh2
# dummy data 747973 - vfndaim797ltkwldovlnxd1ly97y7mcwle3388gib4alr96j620xiqhbq37w
# dummy data 636018 - e1m63ffjc8w0cc35tuzytjrtpy7tdgwxs478qrmncpt4vdw2cfkh7fpnxhzg
# dummy data 538383 - i7lqn959atpaxgm39aa6qeh1cgpvus56wbv9nyiy95v91fs4zcn3nf9s07nb
# dummy data 585513 - 993xau2mkz1hq9ggjv4590am3fetip0bjijnjz6b0r3a9h9s7nbaabbx6n97
# dummy data 332775 - i17p9vrqhkulmemnvphak5n4pxx36cmsotky22fz10p8j4n5gypxj0fn6kj6
# dummy data 523306 - vwmui003orcmld45szugcm24y7wke81vargqqjs1kzxqiveu061h7whkgik1
# dummy data 408075 - t2u0zw01ssupwzt7cu69rzp5eiris3x3pauowwl2n630c2soy6048fmjp6cm
# dummy data 257227 - adgysdfyu3iverfxjbm5t3a8ahphyahqqhlym8t5ibx1yk55xpcfk7veyacy
# dummy data 667415 - vnudionmlmh5yq3qxgyz7mimzs1c5es37cxnr4knhlo0fd6dio4wfplnk54g
# dummy data 915105 - 1ot7p3n63oieijtphsk4id7x66htub7zteylbiihk9b8izyzmlz1ik7btp4u
# dummy data 723139 - nl4qjn7yca1rnyqvxk2kxjmnlawnreunhly430vyqby0u10yyni1tc52kc9z
# dummy data 571411 - qs1w3841iq5p6ne33sk21o9w8xzh5oce6sp9m1jsf2j6o0m7vpgxt219rjva
# dummy data 655371 - ou3vzvskx10uia7fhnsh43e1yrqvr84zqv3llii7mpuka0o60tm4ax1znxxt
# dummy data 342814 - tsaryj6y0a1f1hixwt0cou145vyeo5itbdsjo7rkvouk5sqec2izf8p4l9ls
# dummy data 866862 - 0v3ws4csk6n9htll5zxpyhvuvlater6bblp7p0pzohtbn6e5z0kku6uwtnf1
# dummy data 525669 - 1dx3pzcjj59cxqlrjarfmf6912e0z0b6r6yfwsztvv8hc9g8t57wmc2xcmev
# dummy data 153237 - crkr0rcu65y5jn1s0zt0mr8ysjhrfvhvf2t4dgcnwaegjfufdg12mjafxjvl
# dummy data 620073 - luh2c90f69otfy8h7gymrrsfyxzg3okeruna1sau14s6hs39f74lprrg4m0m
# dummy data 650729 - ymrtx938k6eqf5gwut61spwrrh29vrshzrixe2pzahfqcylhd3jef9knlj6o
# dummy data 331924 - 54j1og4rnv348vurbcfhxrhp8purekq8ababcirfu6bb0cvrv82bklclrau6
# dummy data 309496 - e3xwkzbyhi93khnqfuhaa38928x5g2surjspz6td8fo4dzs72bnn9m22m7rd
# dummy data 753893 - xpvv3bduqoti7pfqqcuacwunyyxwgwhrraav5z9w7v4d3yjdavfp7id6b5wj
# dummy data 538867 - 35zc494lxalkpvbznyblky4ratryvmabrww9o7mdk7fpg50er4j3tt7to1n1
# dummy data 872128 - my3jbdjtoa44azh7efwwjmfsvn3jvcld85jquzfwgjlca01dsml9fwhb421m
# dummy data 373881 - x6mkkzvqtn9szplnwa5f2ej1phz1cxafd6zsk9bi29q5uzyn6cxbvqe771ap
# dummy data 573726 - noif1sbe0uy5p8bajnoqlz4ev8nfzdzu1sz0hl92009q1fmz7n0ieo9h904p
# dummy data 418171 - fgxc0stgmfli86d6k0fcwxtnxzg38ej0zmu7habt9abeey4j39qu3k89vpos
# dummy data 179927 - bauyi1dwpyyj605ch8s1el79xokcg6ffagagim5buej8sx4f3rizkpqzaa7r
# dummy data 934609 - csevf9jhvx9ys66uw1ugwswiya4yaqn7ivqh5zm4xm1iicbb92vywykpvgup
# dummy data 814432 - czt3jowfvlnrn7i558sc2jemph7gxb43ztfbhwvqcekmju6sr8791lwfr9zd
# dummy data 519174 - xmqe12921m84odbx1aegsrk89nj05i3d91kqkmpy7zas0pqmacmqbasafccn
# dummy data 916226 - u3tllob28m2n1kf8bjfommg4qzimr31d9iqp8i8vdpjxckv2mqhhay8rwo51
# dummy data 813797 - kz21bc9gdca5occj0va0dw8faq84f985iifwpe9v4xe22v9ekfl4t3amjz94
# dummy data 804187 - 6406i3zsryg4dc3vhm26y17ehvstya0791rixqsiv2b92qqh3mdbnp7yg2l5
# dummy data 714987 - 2hpytvhvm59maffm4j0h66sff1ddfo6zsyweuouht4pgde1scxai8xfw7gdl
# dummy data 611120 - 1rqys7qnxy52ddb0cuiehvslrjlyf9njn7aai3iwnswfnqqk1qxjpy741t6u
# dummy data 896961 - p064p2npe82octnw3gpktog07oilwjhro2xjjcggqsztayex8m1zlecbq6rs
# dummy data 738921 - w9r8x6icudav9osli4a371b0z50avcns5gqo7fig5u1757fzz9rkoi20x5qv
# dummy data 324697 - uielgo0ov4mhwb8hlfedu5nqjb1wbtygujenb9wb8tsikb7zjhfrejoyc4g1
# dummy data 478266 - jfk6c7eqn01jhpxuct8op052yajllxtwmatdi06clsda8s80gw5j3f68c5o8
# dummy data 251067 - wccxfx8n1hkjom312wftb8tka4s2liqebm99i0pii3rjsbwjapnpafazihui
# dummy data 358523 - f69jys3jr9u5np6ut8vcds2lk1ztazrxie6imthfqsouk1la3c8mo0an75kd
# dummy data 474174 - xg7369zacfwh8oik3irzk89et38qgfc5qqh48zbx22ykpantf597931stl7i
# dummy data 205509 - hfrtd3y8061yt4yvtmokkccz8au9dkmih3s1l69gnqbiuslw2ymhz732l0sy
# dummy data 370322 - uo4jus53se7ndtzrybmanoyttiy3nzlftcvab6476st6s8d820yj045ae7fn
# dummy data 846164 - m0ivzr0z30rs7gctij0021p89mnsceihsjekj379jvpqlzvb29jbbnd99ywy
# dummy data 363719 - iik8gi6vjxz4w6elmjgsmk4riut0qiko3nz4naclqqwmf0dac3w993v4mtqq
# dummy data 804272 - otbp3ejhwmolrdoum0hl8buixqeh7txiwua9x3jtdxa939qb5me5o2uzqdoa
# dummy data 545304 - x8c04tzpok5tbl4qhtrvvnvghps35qgvkcbxrk32axrveb5a75h5lky1bis6
# dummy data 613923 - v9cobp281ergud6qjwhogvmotfsl5f96fu61dr33jdaul9xmsxqdc1nvl0n5
# dummy data 942140 - tk0lv7bb8isc9ur9zi96gdgqz735z2ztpcwght3cb34rk1kmjtjaaqq8umjr
# dummy data 614749 - z52b9n3xwi5domjbkhz2upqybp7jy7y2e8cgi38yr1i9q2hqdrqrjxxm1n00
# dummy data 566562 - zj13162x0bm7lx5sinzs8mojl6eioks19a63y0rst36s0rej6akg9kize0wo
# dummy data 396141 - wgualztu1jdi30u4uqjxm7uuub537b0nux9y3s1ui38yf70wftlyii7lyoel
# dummy data 584034 - wsef1iedv2isyyaytw7k4f992q1w01kqya42jnrsqk8bd9m3j6m9ray11fdp
# dummy data 321575 - vhimkwuzdyytrqfiepe399t0j13g7eijb07qs9yzfklg9m8ovi1pk5vuvat0
# dummy data 391011 - fnsd8dyuvl7q6ba7y6k0vatw0uhg48f8opibhazor8z82rr3fz3isv47kxd4
# dummy data 443323 - c38u1pr86pldblnuofnj4irr4nfxksqxhv2izin1micfb5v8znlw35wrq9up
# dummy data 839096 - pk27irj6xrjdhow0gwlv9bq74sfkv9eusmiw6wwq1cua31t1oag4jru0epv2
# dummy data 665714 - xjss9mmsrv0zmhcw92xaf7ejfgmm7g4ba03cbj5ygpyz5qgvxdk8m4yoquy5
# dummy data 280408 - rwpr9x9gwvf4ee8eo3kh3ha8y8vswr1sx0hji62l6lq3abvugvdn6m3ncxkh
# dummy data 828443 - p3ajroa73ser4n73xyc28d0w4fmuffj5jg50u4dye8r93gwun268jvc299cm
# dummy data 990013 - 3e3iswdviqpsm3j7rhgy8bzg57exu6ocurnwzj6de9y0p6w3avq9c2yzhivn
# dummy data 930593 - bwj4t3fgkvu4skrc9ju06hgeyh6mxb1q62d4nb5v55xlbydvq5k8pelwv508
# dummy data 582968 - 0x6grnaxbkrv6biniio33x34qske8mq6pqknf7hjjv82ezrgvg3ghoa8309m
# dummy data 528024 - mix36q31rmxqgftl67fxqbviplg5cyl5twj37jeu04ltm4fc0typ2bridnq1
# dummy data 465153 - 9nkxaqmamiom5pf9r960aimal8y7ribpu7qsbp8hndpycavz3bt1445vsvng
# dummy data 715842 - 3i1x93lzx5zmn3ih9wyuta5jld32voaelxvybcckj9hyng717j5lszv1pnsg
# dummy data 599161 - gmczttogol1jf7ue2i6w2fkc9izxsy65iqac1vac43o05fn51xfatl5af3ty
# dummy data 151183 - l9nwc02lczvj6493uwuf0si7x9uabzlyhw1u11g3re32f58kw0cfs8dhw10l
# dummy data 663540 - e8a5mxa9n2ut0d629a7kkrbx56ydvzrupkj7jrq8dwg65xw7nkh0ekjqceuv
# dummy data 797762 - lds9vdzv9x778buaassbh1vxahqe6330vqreuz1vh5866rks6ubnj5wjgkqu
# dummy data 624713 - 8p1fp9dimhpc2jqmlj49xp5jtrxkko1dv8wpnzoqveihcfu8uz9x5r75t7k1
# dummy data 178430 - 08cqjy8tkwe8z0ns86maqor6ommnq0pbx8ayw1cl5iihl45psmvov360lr2f
# dummy data 100069 - mwptymh2x01iqyi9t7mh8glsw07kca3pwr06rdj0rm8ytzmty05bmgkhw9iv
# dummy data 767724 - 9r7cx7bqclswvfo099qqad2t3in17sbxmeafe1424k1nkcr147qe32k412rk
# dummy data 269460 - n4ap8daa2xkxhyeko997wdv3j8mbjxfbvsfmmckdc90k4gmruhcrla2p6lcd
# dummy data 935290 - dje5pdc3v44rmqwnrbrds7akvdfj6f8z18z3knk49j3328fvw2daw9mgicbq
# dummy data 658945 - uwe27i7086d0ijrw97y5gfcl4kphdsxylvk5px4xg9i69bcpyp458315m7hg
# dummy data 439769 - fbxxzp14vlw0m29p9i83zjvx9dx48il3rcqqtjqkdl9gicmq84a7pqj69sxq
# dummy data 255250 - kx17k11z2v00as2sbn0cs54mfq349k89x74lflartcqxgljc03v2liatta3q
# dummy data 205672 - ha6cdfi2p2ribxbbotcxmw8wiuqrxsb1ybac3qlmd3eojgocfyoo1e4vjo9e
# dummy data 229354 - 2gcw6q3n07gta1w5p4obx0v6vkw214y8eixv7pb6zvhf9u4lalg7d3sgnv6q
# dummy data 122646 - yvtwqchb6lib79h9jb73a5qrxcwl989b8pyi7uy4s26rj4xbvvvgf37rk1z9
# dummy data 944423 - izqq5tw4jzfysatzixlt8wcjosjpzwx69u30bl57pgf1xrishur26q5pwwjj
# dummy data 754001 - 9tifs5m2wgq6wi388g4vlr6elwoejkhoev7yh8guga3h58rzhfd2u8u2fyhw
# dummy data 815115 - hkdvtgrqqpv0ryh4x5thrypuwtaw5n895gu12nbc51k871arpo7q8ms2pdnz
# dummy data 439359 - 8x71kdei9x4fmn0oqh3gyzgoakav7n2cki9massar0gj41ahdj14d2tqnk0r
# dummy data 576192 - 6te9h3ek62cnmm6zw5ach2sicgragnxzw0g3wx91kfek4uxfnw8pduhbzbtm
# dummy data 466037 - htkx1eocwhntf1ehovgm11onld678ou3ty68e18jzi5ug4g7gaqw880a67gd
# dummy data 222400 - 1xj2n4vgeiffghwbk5sx0qbhne70qyp0hsn1ffkttyv4gcklpm69w8t0y5a2
# dummy data 478331 - bq3uahib2y0t3tqlq5ezbojvmbw2eek9usur3v9gj7zmyu2ft8qj9ihfivid
# dummy data 250431 - 5frsh87oedfvznjgsmcfboq3zw9utvegx7kzmdvtkcv97z9or1zgdtyew2hp
# dummy data 210232 - lcxluz8v8dt713h2yliskoabk733loxj2pmd1x77znp377pu6k0x9stup6ub
# dummy data 900325 - pa0zoh2ru9a9omjq31mih631ig0g7v9y25es6exizz9ou3qniiq95ephjb9w
# dummy data 255357 - np7ica1cjckzm9pwxm4yd1rwb4nogu3x8r5qtgeadpfwrsr9x34jiahlkx2k
# dummy data 826000 - 6ppdpuv7cacgwuzfgwidguc59z0klwhg5ke3txt0vhrj86j6ze7l8qex899g
# dummy data 226209 - g2q61gna08uqjx1b0sqv078482dmc29faskehuahtn70kg7xex8yd398etvo
# dummy data 663610 - 00gyhoqvil1i1s3de651mzlmca4ck1qq8besyhpqmvim7reywyvn50fthfwj
# dummy data 721148 - mijq6k7m78xwyzk9yv6sy1y11f8gocfsvotrxgmoo2llre3v9yonp4qkjucr
# dummy data 207028 - r7rk7ezl4c8f3wtsbsj8tqsxeglhc5simshue96n37i6v9v0ilhdjr0csoau
# dummy data 965115 - l1wzj8rflptp70qby38w96fbwvp0n4d0d04ev0xq0b486gdofwl6a8qh43q0
# dummy data 848798 - 085vkqww5k64b0t07rdlr6pzwp05adc0kotc2o42x2ymc1ri3yzdyef39x87
# dummy data 192286 - wbixbzy68ewpftg4a16m6fstgvhvpx0krzcu47c3adoalqh72g00qtp4jzk7
# dummy data 460830 - iwhtihkbz8kea64quqi36r5qpoa6ejk9sg5n3gd4oa530dbstcirv01r1pfk
# dummy data 387769 - 2lpm4o1pb5y8sfcekwtplzjxspy9f4oie6p6gtdwz3it2klj71v1jasb7t31
# dummy data 931513 - l6qur9fjlz3wg8c8kpcsilbjm970n4axqq5gz94rhzve8el1ci6fk62ocdgl
# dummy data 968564 - 6ov5v46ti8ydck6uydm9wy7jyichdclf0zhe0s12befiw51tsap0p851ze2o
# dummy data 313816 - wdrb0qgiqg0zn24pczyq8e8ismxqi4p63a6d5jvmwyo4fif3gl9dwfdcqsar
# dummy data 485624 - bny3scbrlajhykzgjrelt5rtlvyzc6xhwxpl5soah9mxyipy2dpaqn5t4wro
# dummy data 213851 - ib03cr6zbn4fcz0w2vmglasg5nfdk7bfd1ifweus8wi8mujmg92bvggn1zky
# dummy data 811772 - 7uwcppv4ukuh5e5xmy3p555ksg3mubkwohv5rdwor9s8n36duwtmw0q9b0ao
# dummy data 445769 - eurc86vkw2mwa5pz2kahuziz6fj6h29njtmk7o0ovnyd4okozs07uh9rkyj8
# dummy data 585389 - ny2fwk843c812x8ln7hkasbkf0fwcm7bbpya1v6fzzkki76djvz8jhlmgyxo
# dummy data 121821 - k248bfspg2wmawo6idaum75y7po5upxlord0vpkcbhslz7xw10yv7govnhpm
# dummy data 699352 - 1sc59t262burdp4kasswx4tz8g9pwmoyizl630my1utof0sod66kgpsv0c9h
# dummy data 169647 - umsy5wn2qa53vdfrg3yyb9bfm98nop9fztmw42va9a6a7t8awfjb077g6out
# dummy data 270140 - c1lre6vqh0aovbrvz06ttxa73qrp6su4exu7h28fafqtjbkf47l4zxgtkdfg
# dummy data 703848 - wqbwrh10hd2vme6t84bbonnb71sormdo0v8namaoy8cfzy0328qwtrm2ym9z
# dummy data 865018 - 5j8kpbq3pgtmdgyp3sr6tewf86jokrfnbrez32750q3r4q6ksf4bbxq1gln8
# dummy data 171279 - lrc8ndec214h1wfleb82le1h3gd3csgzxnu9ti5iwegx8taf6kcre5q2sgif
# dummy data 590907 - rmxvpey5f5tbza68egwk2hsp1rz6fjkhaiz535mweib8jtz6d0lfl8nfxmvx
# dummy data 561700 - jbo9oay1qt31nzc4tchqvhk130q8rog2wd4btwp7a4t5gk5i2ubeulkaukzd
# dummy data 564810 - y7l15x9d59cnvn1fku7mgzeg3f89vhzj8glz3totakeyegyoho17x9j7lhb3
# dummy data 487103 - pzjsevi7hr51sqp9xq0pd2oeh4djanc43hay4aj1xbjk6tjk2q7dc9hvi2f8
# dummy data 777317 - mji6rvr7w27k9z3n3pd6f0mo0wevoh4lmkv85gjycou96ecpyqfa126qmncx
# dummy data 403414 - uba5cm7coz416izb9btr4uj28rwltbacxriak8zqfnpkn007cgos41wxa013
# dummy data 257964 - c15j6y9obwfxj8kdp2v35vip2h197xxji9z3thbwr4q8o5hsejjduah9bhwy
# dummy data 178927 - 6zhyvnjjukgcbnaz4yy07jf2dzzo47nc7sms8jbrlafd55togxbr9jwwicof
# dummy data 846511 - q2np2vghhnb5zdlqpsiq47ctghs9sdlci29mxh3907xnw24bxgluo997ejcy
# dummy data 503002 - q3vgjxnl6p7p70av8lhhjt6eh3uunuae27in2uerwevlj1xcozc5qul1ldv9
# dummy data 278397 - n4qxy72ord9v5byizruxeoqliz8bqe1z7o727nts6c7web4sxjehx9ffrs9w
# dummy data 903178 - fzselu29xact0rs8kbwfubvv116agc1mio32gihkbsi9bghpdct4yw7tctcs
# dummy data 181875 - 5y43vfnq2s3b2czhdjiineb9ll9npvjnxpjsba1nybi84qxq4toy8f9oaqxk
# dummy data 504675 - xbqt4s637zgae6qc2ut6c87v0zd0lswg08qk0yc5ywjx546139tj8wmadglf
# dummy data 781889 - nllcrr5owln3bnm6x39kxjuleuxh2t7qh15867vq480zrlpzc0f9knr5qaih
# dummy data 214857 - ywy6uqdrtrbm9pp5x00cxscaymles3m851npvpcxidcdf729y5wnockwcshh
# dummy data 458028 - t0fdx95ialemd50xlgwu9fi0bcckttnsivpqkwp55an5it2vrm922ke7r2b1
# dummy data 400056 - bnl79ixqylpten9brmr7z785sd1ndovwxnm87uy6mp7b48wbq7ephs12in23
# dummy data 158868 - mgdh38mm0770dpam5e6lhb2agiwpgzg1vmx4v61r49dhzp1k5o268yka78ic
# dummy data 226501 - dcc479afg9a4novmu2r4di15ywfaswq4w1g25vky28yu6oacomgeswm9qce6
# dummy data 557016 - cv8e6jetrkst0me7o64gftw4gyag45xc5ys9o5xzatt6kr033qw33prd8c2o
# dummy data 650973 - xri2rfijdgvzwnoogth0wxiurc7x3aueyqsce931h98h0wnwonvipn24jgdl
# dummy data 686362 - l7buspsor4jnhev50md4j6mio3qebqbcy05ocf3zezhcb99a9lacdhc9cgf0
# dummy data 870113 - yte9gmv6wh7vh48okvnr1d4jy88ru98sje2mr3ajfq57nc6xpkvn6g45fy9m
# dummy data 559244 - j2oicn3fcq7q1pvdcy80xkeyi6lyto0dhw54sw6z3mm7zb9xxlut2havnn4d
# dummy data 735296 - xd0gbd4t3gidyidau255qpfdlradb1yvxbueox722labqtsdtx2vtxz7bch1
# dummy data 969788 - pnv3vg52qj9ujy5ut0s63lk12311r0av12vrb4rjrz57h3s5vyrb7d3xbzbk
# dummy data 485382 - ckpvmt6vyhylsgsq8m9y1r61hhnlzqhec6a7hxfz6ittrylk7g743sczmmf6
# dummy data 506343 - ga6ho7r1dryifzco93q4gjo8edrzqcql9dx5jd9cgstrwx2qvax22lfhgeud
# dummy data 147765 - e5vsyxkm8w8t7n5tljgv73wb51yott7t7l78l60jt5npg7rieq8uusiwiww6
# dummy data 284560 - aer9gomrqh4jmk9ioe3iyjwphzc7l875dvi9ivv1wqi4qle16mxsn9vmx6wg
# dummy data 817427 - z5hgpq0bczcrdkydm9szifby4cxe7akjm0zshwj37s2v9sb9uvnw39bco7l3
# dummy data 837548 - 19nlzy0vtout2sggcymcuzaqfc65knfz4tav42s2o4q65n4ogojwqrpk1dx2
# dummy data 877704 - yxzbo58l6ukzllva93nohnixm8102kn6o6rv82i9t7acwy0a6i0xyv5be99d
# dummy data 109184 - wrf2txull5ej0gi6pazdq3b710s1r5hmetkvhtpwpxqo4irvc8hwpncv2hjh
# dummy data 880569 - 2gryku0r3mp2ocir44z1us494iornmtmedpcdxw1vm6ocvjsfkn76cfxbmuo
# dummy data 664594 - hx7w34jeqxth8ruz2edzrbl7pbia1bt5erivrkv6hbymm5pjyf35iu7losdv
# dummy data 153790 - rq3b6q42qjrczqukai4128n0seksn7z6klc0px88e52fpgny426eqpnqyasw
# dummy data 483302 - 7ixttlvna9cdn7xwyfq575p2wweyq2fqorkpt0mj8um8ck15ezniv85vo9s2
# dummy data 840733 - kbuspsw2ou8bmrml1yhopvbpv9ydn1zuhpybi2e4yxv4fax16ny8tsscfsvd
# dummy data 528281 - qhlm0bil17yrsecexzwtyuu6753levh5f9ihbkc5m7k6zrwyi0wg8axnk41w
# dummy data 703357 - niwj7gejrlqqlzqu9xm5k36um0x67znuif5hk28jtynxyw97xvqt23v19ix3
# dummy data 229517 - 9oy8ww2b5sk5bvluag8nclwsyehwadomqvkbu2rbu42nvycpm0kjlc42ayzx
# dummy data 851329 - lyy50siqau4qz2fwqcynadt65cqsv6sef0q9fcqt3vfbf5ik3we40o8ig4yo
# dummy data 159872 - y9a9lbzah9014ih4e61ldprj3xs9w3w2nethoju9o02agbnnyarco2d6qkmn
# dummy data 685836 - gs0u9n6igdcomldzz2titjead3wvj8b45zkocktruolf0j2wqaf57ufntqkh
# dummy data 116458 - 3g2pnd0hh4m1s0edw39f2gkrq5njz21u0269j26iaehdhwk8g31lf1j79s1v
# dummy data 932484 - 3b5wzt3fkiqa6sp4f1sj7znd09g0jz1y51judc6pjqorzrc7owy8f9ve3npf
# dummy data 309928 - b0fcz4xzpbpwdoh1ix0kam6c39gqmrn6paqxykraqcnxtb27x9j9xhh9rqml
# dummy data 129047 - lkchu9cbdrjym7nqx700xtc2w13go3xff429mdqqrha973ier4vag7bctilr
# dummy data 489133 - 0lgul0c3ysdn71zj2fjxmxr6zd09mbqnbw4xqie33xqx49ijx52ei5sltbqd
# dummy data 117900 - kkzmd131fdw819jd2uagfb9w2ed8kekivmrpdaea9uxwjta2qab4xkq88y8v
# dummy data 101115 - bi8d0fxrjb4yz4tzfn4o41tr7b7mj14zlkdn2cr3ckj3gz8cfq0nfxnaof1e
# dummy data 768690 - phtk0kjn1m8c5e9gf584i3dsc3169015j5rvzgteq1yayv5vog0fexj4fnsj
# dummy data 421478 - g826607npiohywx2gzoo522bw4e7a4dgm12nv055hj670bizhrfllv4j6hbj
# dummy data 824854 - rc8grxgswer7ogetg0yady0kkz2mu78k1wllcohuz3k4g4vef9fukw71ribr
# dummy data 859399 - y88cos29g2hn21e8iqpir11i7b3vwqgm88t19f8isvq1cchif1iydttem1k3
# dummy data 970952 - wgbhn7ditc3397zhtu7zaiyc5swofqdevqrvkesuxvexp4c2ba1ew6lh3ws4
# dummy data 197366 - 81pczppsoyktntax5fdhr0bdj7609ez2fbymm7jp2cmkqod9m3uign14zs4a
# dummy data 772787 - jjrs7ji7f5t21cao4r6htjtib6mv6p9q7p5qd0vg745pi31wvztg470v6rmo
# dummy data 813384 - 3h1fvwmthzqycwrrci6z1y3fcvhbhw43uwqgfrpm2vz1axrgwewze6xeaqv6
# dummy data 816011 - ncrjiqy8pdg4yrh0ky7zns7xb26nlynzjei9a20j1os0a47ldcx228eoq28w
# dummy data 644641 - kor9kwmnnv2i8qrc8zc4ywi5snej8r3n41f468cxdq22smqjyeh2eqgctu8t
# dummy data 147846 - 96ey6tbyr1fdlw4zlihbmascskabklln8aejx44r3aozsc0oaga00gfwthw3
# dummy data 499656 - x0dx5dsk7v59o5exsavwg220a1omuuhsu1mj4omp2bpqario8spn1e0rz9a6
# dummy data 635386 - ngckp76cjvktldv05ryo3r6zwome4fx3uzhl7so6o7l4mqmyj6cb5b4unmy0
# dummy data 156029 - 1eyxi6rmvlpkb7uui1a64l9ahxob0azcu9m33fyo076dkovsztxanus1mvr3
# dummy data 861587 - b7oege89ncaf2yvtpo79yi4mdcr647n7ap5q9j45hvant9zlcskqh3tifrmz
# dummy data 858950 - 5d70vfgud7yd2ifc9iggbbsypt5v803kkcnw1sw0okxwib11ddlbsbkm0m14
# dummy data 926206 - ei0gh3nmkq0ahcgjtbmnzcrwjkb3kkuvz7u3go2a9kern3o5ubzxec44x9c1
# dummy data 650462 - ju6bt3xhdfyg3go66crwtvpzvmzkekj0mv0j79rjgk3j2psbtd7swvv2wvsl
# dummy data 932655 - 017f6brt09ubjrp2bnqp5xsuhpws87rdt5vjjwoah8dktztbl6ya1bmr1tnv
# dummy data 233261 - vgj7dsmkzkfb3mmpojv1l9yguzvd9omj6fpojmi9b20vnitm7mbbdwy1js5v
# dummy data 757913 - nqvv86vtb3m4nqxxmgyj87079c1ik0ognvzhb6xwnq8wvzi1uhomp4nwkcwt
# dummy data 212243 - 9nkz2aui7c0rg2kfhemguclte26hi6vxvytf3upw0rbehy644nlsaklkfwyi
# dummy data 834539 - 7lfkf7n7uffl2wdo341gx21ygl3eguc2la3ytuxc5pwslma8bgr37mmne9fg
# dummy data 323826 - xf4548efgou1ajxftx38ni69vvij5o8ptzd031sj7yvmereqaq7jnw4n8u79
# dummy data 371715 - b8gk099ogpobelb7o5sqzxbldfseese8oxv8wqztw5w2pgzm3b3nj6cmh6iz
# dummy data 525176 - jkqn7fm48cpr241tlev9ptpp47jqk1tacizt0ju9dbj7icoatjj0kay6esjm
# dummy data 206464 - 65nm42ygnzwoviawvla8ki8gjis2y6t6uq6xgecl2okudfiqw2p3hharp7al
# dummy data 238615 - hzwc2s1mgihvw1r3ypakve7yqmnjkb14f2bzvl5gtgur75pcmsi684f2mcl8
# dummy data 343840 - yabtk495w4nbl4oda2h4sdnlhqf3intsdk765pmjodm2ar0tn2lnjewx3uhl
# dummy data 710813 - h7je97s6tgcxdlmljt739cb7g6srs3vnvaue5y30iut8v6p03e2wxztgnw8o
# dummy data 578400 - 62wb9cy4e6etrumdbt9271rrrbbkcfjebw1q5q1xxh9pmhhmagdott4nmpc9
# dummy data 685185 - s7unik0q6950xendezrqdimya0dziycvt6ewsymxgioxioqevb2f8duxe2t8
# dummy data 226617 - pk5nyh3rlxn67yg3ewcpsk3fp0vh94ta1x9kl2t7dwzhg4810gcdqbifcic9
# dummy data 742078 - gyhxu1fu67av42t7mss23mvukr8c2irzxyf5fdrlrousjth7qhxbnf8tw55t
# dummy data 774567 - gsdgvl0uirpqrnhv68plymqt8do4lzap7dsdwja3vn8sk32b093awamyxcv7
# dummy data 791322 - 62pbspr9dozp5913b6k6h3sf9t23ewehkgp1s5kyxsfs1me0h0j218jexov8
# dummy data 882687 - 7ydhotrvh0rwussauyevmhs4dcgy4hudsqbsl4974xvdpdiw6kygb0tklt6o
# dummy data 168082 - cb1u0rjeir5j0fu0gkvwzwyxyxi4matrn54gqtbgvj90jj98he8c6eopjjxg
# dummy data 594505 - 4g62yy44zch6v1z3bdgosvz2xo4u6oavu268wcljj7re4sz08lk1u0i6dycb
# dummy data 727825 - e9qrh1ewaeruk3y8b7r3o1yk70jcvzow3s81rg0f2dof2fbf3vx0wjbiod85
# dummy data 421330 - xh6lcus8d2mb57ahsr0uup5ajjvaxbsnv2oew3ubcd0awpe6qq6cj7l901cv
# dummy data 569020 - hn237kfk44mgs59z2kd9t0crdne4kkt13lmf9hluon3nvi2di9dw0tawyr03
# dummy data 812140 - i87wm0weiptukn0r0wboadbktrefrqu3m0c94pcnlhgi07vz02e6mxzxa5cf
# dummy data 820651 - 8e5b0oo1d39whl9c1cp6njgxnucdbcaztir4l5ubbnox6qeh08kq5kucv5a7
# dummy data 938375 - 3gl6gqar2c7koqwl9tvoy7rhmbjech8mjrtgwewm170savfz4k3va2corj0m
# dummy data 643036 - b3cyrtkmoo24bvhwsbznsogn7yn7lgptqmnoyvu438bu8y74r1dt2z0ftsq3
# dummy data 963935 - h2qbuvbq4xiou83nedi8bvqucfbl6gx9v7dndzjudlmtgsxgkwcjexe29ubd
# dummy data 561880 - cnwl0e66pb7schosk142bfbe0847kqaujkggbb2zaqkw1n0q22k4x80qv32t
# dummy data 692842 - 92ucmmi4p6kapo9xx7jcqgcyfpeax5kv6o4umqfygqj1wu0oy56afcvjtm3v
# dummy data 409496 - x5c74nv72jvewbqc7fzbisw053eevqxdmf0nw22gqb5otwu8pvo187o63emj
# dummy data 141883 - qpsm9j1r5nae2joa0gy954bnx5ti9nx1avb45worpw175lunsxkyqxs01ucv
# dummy data 618866 - hepz6873pshrrw86kj0gq92l7dlh2l62tuycoikjfkk8aszj4pvx3qi5xybv
# dummy data 157447 - m1bb166xhf5n029kyzizsxqf8ulyr788bhc43cg4ndrub1ls8umi1e1d9c5m
# dummy data 724400 - r4b7hzu3wuxd7rlnfv9m630qwzvq87bxjhcpev6ja5cerkucoyaiaivclcsr
# dummy data 923631 - 0ytlf9ofaojwekkkaj8e2vn9n0lhpcbxk463sou1pcnlp5ke1pivrsotk0pm
# dummy data 239305 - imyagurdhtlb4frx3euuhy0qlqukcf60f7rpazem4pcrdkaim6035k8my1zl
# dummy data 753504 - eb1kcspq4fs42eunfj0cl10m9z5oz4fva908841qxe2kj0kas2im3foidw82
# dummy data 705003 - m45nihigofui7sykhg3f42su7ggplaxqnxvfoq7mbw3ngk64diuunltfkm5d
# dummy data 410191 - n51jqdemvix82y8qgxj9b1s7prhuxqw21cpyevbxhdpfhxviupy938he0wfp
# dummy data 750949 - 7ndj4k79zbpapqpo3e85lz4h3abj1zettmfyo9s5e72eal24cseqy8qzxx2f
# dummy data 642077 - nrnqed74azltws3adnfqoaa0s5ijt7kfh0zgz7o4308o6h9sipwn61l510d3
# dummy data 130822 - h9hr9w573nebbkvdcjyf1ffezx94b68dqo1bd04bepqulajuxhpb6nwchc77
# dummy data 975966 - 3kfbndjrna9f2tl5h289v9csv4m24tfahcbyymh9kap7j8trcj6r38q0jdr0
# dummy data 670791 - is7jui8ihgij4o3updp3qxjcqsextmec0fziuf9ckqsczsljr0z1p1eumo2c
# dummy data 789347 - 8t6o1kgvj3tt0bbdybn69jat0zyngw63ejdl82ng37zb2untu57ha7q6upmh
# dummy data 221890 - 08t309egb42inj41kn735bn0xd59wb7eaha06r3599nu5ecg5rieaj33yg35
# dummy data 925919 - tdo8vd4fs78cadmk3hhy2bs03boe7df3vje7om6ygngqenr8qvabyph0y75p
# dummy data 916313 - 50ilnlnrcaz1u3gksg4wvyakdj4c14ypihc41z70rblp4yb97whj13vfg4k4
# dummy data 421919 - owplgoit2ln3lejb1ip8o6e24o4fx0r0zmi8fl7h1icztf3zhzcojye8z7iq
# dummy data 881700 - uhiv73onv9j389a8g6y2myif50k60woglflqgtrnnx10n0cf31m7orydtwdd
# dummy data 262538 - 6mhqjizfmncbur2qu1lw589b79vflyvoc9ts84r4erfdse3mxjfx0zltxxgu
# dummy data 805904 - peqwdbu7lmf4r3w28plqtpfvkqelo0ysq2d6mbxg0glvhimnn8e2alxbsjv4
# dummy data 898224 - ayx6b6dwu68mf1c81cee8g6v9xz0floq3gal2m5mx7tqy7m8qip5f97idrea
# dummy data 505428 - tie2h4u8jggsg8knfjjb5es9lnbmjr9wqi2mc1lqfjkh8n1mnh2ge361agy3
# dummy data 532592 - pqxitbh13asn83ytcb8k08oi22as2ahgqkj160mt1qzrg07yvwzz9x1fkbm1
# dummy data 601233 - zoo7kbk84fp93xxcryvv5k1cqeip6l9y45az1now9o5ipn0zcd3s38vn9lag
# dummy data 992897 - cp5j0tziwb1uruo00z5r932xba2z2hojl4jba4hm1jw52wmq4fdc9fhzfas8
# dummy data 758367 - o669fhefndhtw9dbzu8jd5sspxo9befal84ffs0x1xt50wyonz6g5t4fzn6r
# dummy data 398947 - csjmz4cxe0uedb80a7e2dfzl0lc6qhxypn9829hm0e4byv14elh6rtlzp5j9
# dummy data 613487 - ja0yqph70fopzfg8q6xajjgx9722jt8c3r48zmnfwnitt8hhxfinsyyqen6x
# dummy data 538280 - sp3x7fgo6km4gr7h5xfce8o6qldzyc0a1wgajgwym9k8qtfzxosqnu5bm60d
# dummy data 414810 - 3tvd7adrcgumx8ozw2waqcsa1hrp2k4svqzz83kgexi5p84i5y4iqvrmqnna
# dummy data 305412 - edz4rte6fqn4qc0m9ra6dunv4nt0mz7rw596hrlbwrhg6knpblpw8n9u4ww4
# dummy data 566249 - 4whrt5fn3h32lk7ujnq7pgfz1k6iu7vvfp11lz5o1lx8ke5u2lozo5xecz4w
# dummy data 435853 - cs2cp602ppn8gjyvr34v9i24e3gbg20wsogkjgez0zinmuaxv779cw8ay3cr
# dummy data 445364 - tvjodyc0lxq9e0ih05t3em47lqe878470rrq9dyxme2787fx18ebu5ie3n79
# dummy data 910408 - tvoh0m8okbb63ocs30pbr16eg4w91yvz7qvrxvrebt72vzl7e0hw1wt0qnsv
# dummy data 970690 - jvaetyriqt7v8vnptvhsehwlo7mwnbgrd9czd6twflle30ojbn67rzjny2ty
# dummy data 674374 - pl5227mhty49a3vlmsmnn5onmkwcptjgj5grazrixmvwuykt1s248r3764zb
# dummy data 653789 - dahpxg02ualmb0dtcdwacj6ywn0kosl2krur0hijqmcpb5npzityoy0b0cag
# dummy data 331060 - 2z1luf2sgq4dl0my1xt6sfxpzj7uheub1cyps55efy91ihkarq7s2inpbt6z
# dummy data 596018 - g5gch7kvu833pyy8gacgb37t6f0f9yykt4tmduisg2nn7wdkxio59lhlssa6
# dummy data 990234 - gvfaxiewg0tr6ksslju9krdulqqdy0i9gzui5qlva9x10uv1k1vxp9izra8w
# dummy data 139658 - kf0j43p5o1xqvpmmv6ktnkj8fese3h84sa8ckza9c6oj3fzxkl1o8646yr12
# dummy data 323387 - gfjgcdnbbczopkko9uj1iyl2t87kzbdvag7wpocehxx45l0n0z19n47jdzz3
# dummy data 273054 - 4lm0ghfa5dkin0j24qe023hqo44vmkg6vgh0kvwdw2g1bme4twxlfszkpanv
# dummy data 481167 - t0f2hl32hz1xqtty7a4bd83cifdl4bjc0xrrtszix8nzaw4quidgea5q7pb9
# dummy data 503195 - zf8pqxr85p1qj812ie4qmzq11s3tbb4hbif9ayzovcejnf3p6ypfkz7le07r
# dummy data 805234 - 4qawurlglzdwgp6s18ejis43yg9bc0tteog7ipr00m9vmhrzyt3f2d1zihvf
# dummy data 445650 - g6y2q1zjvvdwmilo0smqdx9q44v2eqmakteonvbdg56j167a3h7s27n407tx
# dummy data 396943 - sybk71ku3izdbd2ot5sqtrxho01o1evjb17yea0t7kusutvvzyci98lyo8y2
# dummy data 925134 - w0infpmbrtlpgydk6wj4xug9a6u541czf62nv5khpvjzbpq69vpx1ocd0076
# dummy data 271256 - w42vns026nt4d46mz8p1xpfmwxib7i8lzm77xjmtshgdf2914063fhuzu3ky
# dummy data 710727 - 7h5xumm4m6t8mv6b0uczv7vjv141ml10o134wuk8dy19urhs9outx62qpig2
# dummy data 685781 - yw15agp7ylhpfb1e20gg3u39h3sko0c1i182w6ajexn3t3bwnumtm4f8mr7g
# dummy data 946408 - rcoy0i6idi4im8tuauk1ajq7eu21s38xleoosdmv3son00nn4vbvpvkf193t
# dummy data 142671 - 2ejhptnhu3vl65ngo6sarfwq9nryh5h2tomc2p4t9kl4en86svun25oif51c
# dummy data 448811 - j4yxy0awk8rhn9v5as24xckeotnt6vuh4mkkhbaxid1ot56j0o4hn878e0a7
# dummy data 416382 - ty8u16y438if3h9yrgrgmt9vbmag6suvnlfpolo7uiruhivpxkbers84jfq2
# dummy data 723836 - 5epn182k0lzyx6vvwi32qfffjwt4fdzstegdku8onewgb3hpyjpr19fr50ng
# dummy data 983519 - 6betu6s10l9g6eco3b6wtntzglmnrt6ggy06jav22io237z6vu763ii0ubzr
# dummy data 763934 - p39d0ux852yhvjj0o4ktgfqnhk9ey9506qnrvxihevf6q02so2sx71i654xf
# dummy data 700755 - tyxpfeeddzhjy1bju8943e5z4u8rz702jifqiojukxup89w8wkdhk3dtbxya
# dummy data 984217 - ika55g04ubpy1f21g7hl5s5d3evaa7gkeq3xltnc3uaexce3kwicjrmliuln
# dummy data 635342 - x911saykeuwz1pp9p2jmvty3n5ndlkred0s6rxwxlybpye4ufsevuim3rz7x
# dummy data 412549 - 115n85bijr06iqt00018ixlo7yav8crfsckeb7r913utlmnggtap2kqxih3m
# dummy data 833242 - odmkvc8p2ldwi1tm8lfxdrzyn7rdmfob5ms26170uvw3wbsu5y6k124z6nj9
# dummy data 243890 - cs8idpyuvsyj1psxqudmgjqb1rghhvclkfke5cgapw4tmlcjhjrwazkhcxrm
# dummy data 523384 - 78kyuq0mdi3q1a0kkbm7bcyioovw84i55jnyghwahdzzuv140v7loan5xwi6
# dummy data 481637 - x8go1mpidskredmz0x14awzc9qle0ujmjehvndfdrf01kiefudfe70tmz0tq
# dummy data 271018 - 8t3xrd56yqfr8y455nkn95c8sk2wtfecdf7ve0ii04xtcbr2v9yabtuw7oq7
# dummy data 488771 - 9csrtv79fyr3bx5k15wqf2nh8edjb51dlvotp01sii1zi9r1yvji9rln25zk
# dummy data 528329 - 39zzxux0r30jcw56auzz64xui9i0ywnay0whds84n03we8hl4qkmhz0iumih
# dummy data 564774 - p59cjbfpiagnvqfogbtsdpxyvmv58fedqdn3iir1sizj82i64rpdeiimmg8h
# dummy data 816814 - 1dlszs7bmqw71a7rbuc9cztlxnvm4mgj7imwoebecprfpz1nq40ozx1v2y2w
# dummy data 133206 - 973m64yw1awg4j05f6sg388vkprrh90dwna04s70wue1f2lwky06f3z8frx6
# dummy data 153829 - 6q7nglphqwv8trsibhwwilvmpduy56r4s5yewxwnfsen1jd86hny7jvlpqir
# dummy data 289219 - 4tilkpjz1ecm9pgqvb0ebtur78h8ylm27s2j69obizqma5yzzklzyg4kdh9i
# dummy data 203970 - ktt8ngil7zmq53fsqu6ujfk07aq3i4t2z92evisi94z03bmbz7cqjp1ew8lr
# dummy data 505699 - 206lz39dy5ljj5ke8g5byuch93iac4totfs6bknauk3uo0raz7pdgge795wr
# dummy data 254176 - fsnumj0931szpb83iitz6m2l2gdplm8b364e5kdgaki671mqlnsli96hjl77
# dummy data 207623 - l8phlf3iitzk52iw5usct54po1wo9c4xb4mu26bswmljggcncc1va6sum6gn
# dummy data 115388 - pb51a6q0yy3kmqcef7yw13g1le17gs2dulro25s8i93d1eq7q4cgj9o29nsh
# dummy data 520974 - ianq6sv5q1flfu9jelhsqkt4ifanj5bbx8s60ap79xwrfzr0uqn8tj6c3uh1
# dummy data 307137 - 1zwdnh2737atkdmig49x9sp8i7gjn3kbdnx0wpt0yosmrf16ou7ife4owy5e
# dummy data 498193 - yyh6n8etu5jqnma3bllncj8e76h5ia9oeuxen6wu75ixmm3tvsqyccah6g7o
# dummy data 396700 - yjiw9is0p7yyq3bz19tpkaa2h1qo6xgcbm66vua5sqkoitomtfo93ucigq7p
# dummy data 912991 - l0ikh0jed00rtxe42tg3a8ehyi0rwkwaj84dqunabbjsmuwypmswy15shggy
# dummy data 287850 - evkvvgh74xuaw5rbmbxsoexx64ws0kvc7ei3pd0wv0jn7nvut549nowilaiv
# dummy data 717428 - knkghr86utwxkihp60i8h8t5mhwzahif3qyehyrwx5f3wr0jnx3ihv0cr6s2
# dummy data 946334 - 4tynyeltugmufgcv2mxkuuww1elt1yvw2ces68rxvti4kqczroigltws6ytd
# dummy data 713087 - tzh6uqdeb0g0g0kim5v3af9f8f0wdz54ka4vw3mbi522ujciftamabgn3dua
# dummy data 873030 - 5czkauyg6abtqi0v8655i3zrmbymxeljrmyrqq31gal0co37wff058ynklzd
# dummy data 899423 - l7r35owuvjkgkzks2bws0ygtmlurdblfuk3dv0ehi4mq1auwhvj6n9ivvvkb
# dummy data 146121 - u390zu448gdbejeqxa51751i5ches7lnwzb5daoguxpr3dpba7009awrx0ct
# dummy data 247482 - 5agkwjyx5d2ksl3g0dff90259bejt39jf1amhqvni8mttbse4jwyk76gnj00
# dummy data 348793 - iazrv5vjnwiuuu7esdjy8m6jaz5k76jbeq5iql1aurhvutyct4vcgdzpdqbq
# dummy data 183818 - 6f8m0166d9nz6icg6g3widx0tp8rr5onp9m7bdld4w790f09g12hfbqlbuyw
# dummy data 143490 - 2x3a3wzw4p8a6gc02tbcolrmi6p1ah6ftkbc1plf994pq4nuk347kc8st1jq
# dummy data 242616 - fdhl7dmnyk5eptw2qt2ju9060t2a1h4tzoy21fsump8okf9eqjy24bcit2rm
# dummy data 346898 - 8vikaq2fccx4k6xxg9511t0gi0ieujwxwfay1s1npuok93owuc0b1agzyws4
# dummy data 557450 - h4js53s3fkc5v920gi76e10yqjjdgh69krz6b09x53qb9b8hl466aevi1dxl
# dummy data 943716 - jra9956df1vu3on9d59qqsz63jaro84q400bmksx182rf3l7ft85ae5psk4d
# dummy data 667721 - n74z08obknjzgsj07h7190668xdj4olnb3edt5omxi1r07ftorvkfjupoik3
# dummy data 824112 - dk6r06fue414gynwkukqg0bfyc8jo0tnj0i9ny19nxawse85rll2h0cbxy5q
# dummy data 416487 - 13pwdqjnzz7usq7w1gp3hjhqiyabj9hjflmnzsjpda45cyc7q7blkwhqfoo6
# dummy data 771954 - iuiaumffbtnmnng1twe4ncw4haanuzr1bfnjq3xwg11zyhazp26aglreo08g
# dummy data 968580 - yp6dnw9pr3t7dled9mbmudjffap8mp49l6yunxlz6p1evfm3helz1f9pgehr
# dummy data 785686 - c2ihqf28heyzqq3vqtcvaxv875vvkdmwpdfn6a4625zg0n1ig4a09tonoy6l
# dummy data 860130 - o4osu6ludmijovc0gypvgrtva817gnf0vnek8p5v9vku6b1209g0zqtwott0
# dummy data 898480 - 6s7igm229d3be4cg0hhgln2zcx0tkdhaa3zn0t8yvxvmjtphtej8djdt9rox
# dummy data 273373 - jug96zyolk3bowinvbo5bslgctvrplpx97du4gcxpjb9o2c8t5kn07ij8vc9
# dummy data 383433 - pbb525oar6vcadm93gwpqx932rz1rapobuk3jxigzm71n9hc120g3lscylfl
# dummy data 264386 - f5iiwv25erwgza0re8wtfanvp0zwfjc53h5u7ov0ly8a45hl2oda373rj6vd
# dummy data 113156 - f346ea4a65q4mcjkeq9e2sf3hr7i80mwj6ijcnr97soj9vb3hnioz7msrz1z
# dummy data 843844 - wvq6rilq4hqvc3bbdw8vkpqrqtsppvnivrq20h5kt4p50nmerekhvs20jrpc
# dummy data 332375 - wlbb8zs9mfwhxfkutt020kbcaggokrix9tgvqsprldkk96l81p1wzqc657a0
# dummy data 460095 - 65knqjnx93tx6ld0haemjnqgjgvqo9bwjthttjnm9xrd4pbuufjwuyd1x4y9
# dummy data 896452 - yjg9ad5e5zge67qawg23c03jqjuwsuxmrc2yvhqu23ddbzao7u2b586fcdl1
# dummy data 841821 - 3ukyisj8mgw2647wcd3zfppknfeiq11upzv0w3kglotahvowo7w9f15xw7nl
# dummy data 544386 - w0oolaspb2r36t5f2wukj2x3opx2veyhd7j0fq0qvqtk5vhjoxbxypdwkipz
# dummy data 243948 - vse0x61ylqs4d0jez3p1dp5qy5lo6gfu23cs9nw998toosdt9k0tpx97q14v
# dummy data 338614 - hvsy59glaur1hz5gv4337yi0wznygzjpunp3mckxrdlin33zxag3kzt7978l
# dummy data 403920 - 1l8rzwdum80g45endytdu848swtzqjgbruct9doz5vn1lg7jgcadc6jwqiau
# dummy data 271729 - 5b4vuuxg97xzqrwukxw3ctr77o5qg5040a0r2jb7stri93cvt4z8sf9olxw9
# dummy data 915072 - khh49vpl4rrlgmco5e1yen3hxq7ux9yjawom0weusve1hyzkfx47832rto2u
# dummy data 870016 - 4w1vg80hhukjetpo9eb4vxds58l35z23jjb1lmp5h37une47qteurbx2brkt
# dummy data 550165 - 9difqpoaoportrj9apjzr2jlo73vbqsf7kl26bu9z9hgiwxw85voxx4ajx4w
# dummy data 538708 - 6fstoafzt5hne1mgbp9z18tr7xx3qu6k06o94678blelwnidexrf3ops06ho
# dummy data 509925 - 8kilude5t9jznups02l1nwt9feb4es2qa6at1s9y70v1xqkm0bgg87fa2bm6
# dummy data 797585 - 1ttqxe5zn3tpuv9e81bx63c6bou2k5i9m9qzsyaarxy1fnmtdacevv64yny2
# dummy data 205912 - 2sojzq1qxpq6s41pcngfbvflhriuwj7fi6ymqb7vxetf0aiw2al8tk7wurg1
# dummy data 912368 - n41j5h2xwbgjrijxbechdxbc1vcw9o2bx5igo6mwqlfo1jnbek3h3i0e5phu
# dummy data 670486 - 5tbvvzm5o8q9s8yp81s8k201at8ou25ms4oavmnfcdzw8s01wqahxwmmrqqe
# dummy data 138601 - eape5hm0tliia9617e8pgirusi4fhlgf8h09o4fhphlfuyu00r8itmgkactn
# dummy data 188619 - fu3dnw9ssx9cjbg9w06pvg4v1wimt9pj4alzlz4uyh9q1ewu11e8r7u68gra
# dummy data 795925 - czmgnjf6oz907ryqqiuis8pp0wtlwwyxim71pxfgnu34x2hvi3px7v0kl99i
# dummy data 243274 - wuy2amowt8wlxdwmghkj57042xcsunsy14fpopoyz0af40zob7o5d8nbn4p9
# dummy data 591556 - ut17tsx8f5mk33wir4to9hzpjjpj2lt79mg12mdu0g71iynvqirq77nhsyat
# dummy data 190878 - cee6ysjqpwb08o59kjde1jxhe38gzrv8279bjtedyqpxml00xs5qrlyvtpgj
# dummy data 575000 - sfz976sna0732whi14dnaptgzu98aw3qssi2i6rqlvpqwb4jxv3gs5s1o1pa
# dummy data 183304 - 81dqropqtkttq2iz1dygu1jerymd999svwo4hd0e5jn88ovwi6npxcxu9t64
# dummy data 265118 - s0friyj5nfi51gv3x0u29oygzrif7z46mvz7d5hdnbgspykufbwy8gk8fcvj
# dummy data 886353 - eke3imi3npaylqeev5jhria98dkifeu4tlhb9uow63qtdcsm27qn5zfbibi2
# dummy data 445957 - 2hdr0mb48wbfu7t4b314fbqj3sc2yrrl0htct3p1h3aejertzzyyhrreuykm
# dummy data 198637 - xm5fe3b3c2d37rafajfc74sniuj76jo0pouaqxpndzufym483oy84i9l5awf
# dummy data 943211 - yf0e9f3x8atd1cenrxyq22xzso8m0xbkknv0pxdnxjdph0xk4c12nbtos5l5
# dummy data 309019 - bszw2m0motu5orjs7o93o4fss7d7uuiwkbiyg31c7woe6e7xmle8env63jsb
# dummy data 430308 - 4ivu523zrb6vc2l61z9qbjbbnuefzci1r7zg1wyr62kjj4s3gs8kz3jndpmf
# dummy data 791386 - fhekxyrhhbrma22wpd68azchpafycvsitno5g7ckbggx39zi3v4oycrk9qra
# dummy data 473673 - bnaby4y0v6g828bk7hnlmo9egd3o3m296i8iu2txw8vyq6qbl89orasarxnb
# dummy data 248699 - di99hs2rpn6x431d7k2x8ib7a22af00nrm40k2s7pfidl2nvp09l1c9q84ae
# dummy data 698559 - e2ljm0q3wt5s8lxr8ho63760221fpgqxwmzn2tz6p5xanxd2bt41l9az8rt8
# dummy data 234204 - gblarjdog4v6bta7v90j01n1ol9jul0s35bdxndecqc6s5s3x4q8c1r0wgsc
# dummy data 114074 - ejlnb2f3r2z5z8u4yc3dxmedis52kvox7k8r7gc5zbiax82vsyvxpo0pxmul
# dummy data 876243 - n45u3hnzuneh5s0zr6ynot61nub1xo8fnixj0t4glodw8xskxxrcknjq1ie7
# dummy data 287773 - elbxxum8hcwya6mryo1ps16di6g7sx9lhro32dicqju87jzlq67mx2h4i7i8
# dummy data 321277 - 0n37inp4cnwh2gvzhvdm3tgrwy7mx5kvovajx5b62kqym4coqygw76845ula
# dummy data 977816 - qrcb3z6ydcmyv2yxy0xre8hs2r2gbb5u7uhwbxsoox7rsldidip1u6wi7w0g
# dummy data 542733 - e5hlce5bbgu60jcwedfnwbazjr7b1899ivn3o45909pqv2ra66qxkbwhtfuq
# dummy data 457800 - 9lmpyt8dr0k1tp3dj64h1m9lh8abizttk5mmsxh3xr6mlexwipe3ojqossj3
# dummy data 826972 - legs0zpnldx1gqj3ekn0wn1qrzvl6tqac0t664uairfykyppizb0c4e7i6be
# dummy data 514993 - 48nrfomqjcctniigz0dby4mn9y8wmx6dqt7n37zrc60hvo61sqpehvpoustn
# dummy data 652023 - ydohjyzaesrq0eiy46uxqqpo98e22u9j331yslwtcug03f3wtp9vjek0x8vf
# dummy data 571282 - yil4qt9r5xw63kekjgg1k5lnc7s5ykqlryyfyhscebu95y0k3uk35rl4a0cn
# dummy data 136969 - 1mapc9bembotelqrxgoct6w2de88yghsonz6n2m85lrwgkvj2hgitcqo5hrt
# dummy data 830844 - 9pbijs3ji00md1gegjkc9q7mzs2cobjgfvv1appj75pze7lonqzxge5kug3k
# dummy data 199159 - 6se5evkhkawb5ydofcg2qvxy0bjaw5n80y0fceni0x6m6sng8b9gd83ewa8w
# dummy data 533030 - h1bk0tuusa8t8w5ctgm67220e1xpf6xdneyikgsojbzsh6vlxip4oqy65lu0
# dummy data 384262 - kmvg1ruj0mqs2g90f5n55ow3vqgndbe7m6mq0dgkcee3d6mr1xq1pmac75qt
# dummy data 237035 - h9hjyi8bzn39w8s0jtm4vbun2ef9pro09qf2im265stf483kavgievcru72k
# dummy data 229598 - nju2fklhmpshiaxrobg7jb1zwm4mqrktqidr9y4ude7nk27lzhpc5qqba0f9
# dummy data 912447 - bjmh300yvy2icmvjeest0o8bb10yg43wi42yqug9fslkoey94c86v8ijfjsz
# dummy data 884704 - jjfwf5u74aufsdl7qgoahthzvmwfpzi0fpwgfqmn13f4t3i4vgi7n3e4j2wp
# dummy data 415827 - 46yl4rkwnvgurd0glk0cbizippn27ng2mkdr7m2zsjhgtmgn7464m2nk5sgr
# dummy data 186076 - vpfvm0zmj18ol06l8hlm72spmz57xq06mef43mrg8o7t7zbb1320o4fazzhj
# dummy data 560080 - wtm65j3a84m5z3roqq2vg35vjz0vn3ywyv6nj4o3r82an4ahp9x1uy198qy2
# dummy data 198402 - m6iy0x9ecrshy65837mke7cp34mgw2ppmpnbnjtlts38qebthmssnak81h0h
# dummy data 679078 - 6io98qlfytr5s608vwda7ia8xhdydn0yte3f4q55wd8p8qpblo5c2w2tl09s
# dummy data 238477 - wflcknn26uv7ko09t2gqhegmg5ntc0duuazyo9oj41rlq46jk635w5n63dnf
# dummy data 883203 - svl2vhytgg8r8f1xgaun0z26pgtlelo5kjwnawlhwxjb1pa3tty2kalc6ncl
# dummy data 407801 - qecvnp37yzt39eiotca90qldihp5oyq3ijbdn6gyaknw1lvti6ajqil5d1zv
# dummy data 439337 - ilqflgv3jqn58xjakgo0q2tq2skwlsw8qrcgr9k16f2o392cecv2yv6p1os2
# dummy data 416457 - 4qxp45czoltesjzpvgkv66bav236sbcqiv1i7emrqjgl55pahfmyh2kjzry1
# dummy data 300245 - oo0a7q9jj5qdwuco5eu2pqw1azkecxmgbp3cvtni9ktlt42ej6f3sywomwq7
# dummy data 141545 - tslgcn6jukfb7ifr5vv56qxam5jy1ljmfyxdm0jback55nwo1up39vuh4ng5
# dummy data 542539 - gez67pq70a3ue9ywx6mumssahbc2yogbjxknoh5wqs0kx2l967d3iqvib427
# dummy data 176301 - ac539cthqmr0791r6e6b10829iazh6pvzk6voa5qkzzc6dtlunebbs48063z
# dummy data 575694 - jz1f9tflhr02tkizbgvr6vwmp8cgkdk0cv74kmmdhwgdpssd2viarze4psfi
# dummy data 727272 - y5371o7oqhjkmedqqy525no961545nvlgpypjlpwsuxm3oet1hoq12d60a7s
# dummy data 934202 - pqmqapnr76e2vf6pcy264cvkn9erp8gfmmg9mp8jrr5t3xa844vmekiz88zm
# dummy data 134025 - 7z15nv2nfx3t40bq73sqcirmqf06xrvwneb2qe0w5vvo3m6il81a7oqnolzv
# dummy data 732490 - r0zq5wpwr3ughoei7amolys6bp19i4t0z4y9ox6pqpao9wep8qvnzghl9dv1
# dummy data 343110 - q825dapx2usfbxkv6l77joh7tclqecb9gamdcwdyppu2howuiznn0qeye0of
# dummy data 382182 - 995zyup58z6bdmka4zxqzydh7ra56xovsxtggmqt9jaz9fkzzy5htnvzdvs6
# dummy data 365668 - 1rxf9gqnw7anhlop8fp4wjvffl65ojv7rli72d54jjdgzuwr6fsc6y1ko53g
# dummy data 819780 - irndsn2asddhh7pi9e7irrkp4rozt7m65167ew0ywcv9m31dc44w7n98n08e
# dummy data 644607 - ez9l67m9s0rzixx4z5vjx2n91hhh6egh6xo3pk9q9c2xfxnx5v8lhvto7b3m
# dummy data 487794 - 5u9ms9z7igsobu2q9cpk7iwmtvsce39zlfvci9hk6jkc6cgpnxn2djkxh4mc
# dummy data 633889 - 8r3zta4q1ik3e6z5h8wiwf0nevfj86ub6vqfwlzjcprtxo66bir5nu0ztjt7
# dummy data 985281 - 91gdrfzgrgrr0imvsjdaajahrttf46xlsxysow46fmu2rinqr47qvinyh3l0
# dummy data 955323 - 54sxw1o96tt05wqoq45xc9r0g7tafzf9ur54aupsn1iheijebcetpt6rrfyl
# dummy data 225596 - nnjchohi19x9rqhhjhdja2vza7jvmkhmie8qf7ag8azqka5qurh9os9kz77p
# dummy data 386851 - 0z2qomwuqyrvhknmx2tnpvy8t1su2ma0y9791tm05u1jk0lnq5ul90xdneng
# dummy data 364343 - kd1g4rd2bvrz8gn4v0gn4bdbc8dpbed52urujqyboadtjgobtn73e9qq8m94
# dummy data 815106 - mhfgn9aszp5y8yhm2pxi07cki42s5aztoej5v2r8kj7c1c058m2apnucoz6w
# dummy data 759874 - gxhhfprjr8q53bw2fsnf5yjteopftez60bjwy7rxlebp2232ca2ab67ftrh5
# dummy data 980872 - fq04e6jw13r6u0wg4ik2ivkrsjg2i785nl89setq556bkrb85bjcs8ijo7w1
# dummy data 656508 - uucl5n4g0bjnr9l22x29y6py8vg8o2bv6ojk7hik4msu20mp5aw5vtau38qm
# dummy data 817770 - t97m94n1hitt0xjoyx0lq5eur9vxt50da7yfq3ogpn3fgsedp48fujat4vn1
# dummy data 476672 - bofpk1o5bynlsjj8ncwrf0gme0ye2nw5k2ksu2pgml0z68pthz8psi65e5oy
# dummy data 695642 - 98yqzxj6uhbumnpbed79gtaab8azkubs0ijc44h7ywlje51oj6p9ajixi8x1
# dummy data 229246 - r5cnjlesxa3t6mahymqcv8nx01h6x84xnpiuzo7tb9e5quee9xv9wc3ff7fw
# dummy data 460161 - ihjhsem6ri35hn3m2izdg6a77hrlkd8w3k4jlao1r2qsgd2dl9pff3f3dseb
data row 291218: value=0.3433
data row 533304: value=0.9357
data row 527395: value=0.9530
data row 100534: value=0.5922
data row 623221: value=0.5880
data row 112743: value=0.0502
data row 345280: value=0.1151
data row 767067: value=0.7962
data row 717633: value=0.3668
data row 878684: value=0.1874
data row 838319: value=0.6276
data row 386969: value=0.8471
data row 338035: value=0.5181
data row 203965: value=0.4186
data row 566012: value=0.5416
data row 537735: value=0.0204
data row 651110: value=0.7392
data row 67368: value=0.3663
data row 813682: value=0.5044
data row 903204: value=0.5678
data row 150983: value=0.9271
data row 294661: value=0.4369
data row 478854: value=0.0958
data row 558536: value=0.7662
data row 656643: value=0.7506
data row 288128: value=0.1725
data row 704743: value=0.6518
data row 178098: value=0.7262
data row 383098: value=0.5437
data row 890518: value=0.0566
data row 794357: value=0.7951
data row 826708: value=0.3521
data row 986220: value=0.3909
data row 920059: value=0.4351
data row 613187: value=0.9325
data row 622763: value=0.8925
data row 305881: value=0.1521
data row 345449: value=0.6481
data row 137353: value=0.7418
data row 144453: value=0.6707
data row 259573: value=0.6430
data row 235916: value=0.8233
data row 597887: value=0.1837
data row 241885: value=0.7513
data row 669183: value=0.1382
data row 696863: value=0.3666
data row 834202: value=0.1263
data row 179994: value=0.4834
data row 975867: value=0.4060
data row 825866: value=0.9432
data row 261376: value=0.3610
data row 870709: value=0.8994
data row 202775: value=0.2747
data row 986609: value=0.7721
data row 135100: value=0.0344
data row 184805: value=0.7184
data row 998578: value=0.7240
data row 737995: value=0.0668
data row 287888: value=0.7438
data row 516634: value=0.6628
data row 33470: value=0.5666
data row 79859: value=0.7042
data row 238592: value=0.7066
data row 473990: value=0.5633
data row 114794: value=0.3546
data row 422118: value=0.2215
data row 952902: value=0.8333
data row 54793: value=0.3524
data row 386516: value=0.7912
data row 739760: value=0.2876
data row 188965: value=0.6368
data row 453517: value=0.5706
data row 252930: value=0.3992
data row 702532: value=0.3702
data row 91571: value=0.8180
data row 169413: value=0.5053
data row 874425: value=0.5372
data row 939393: value=0.8004
data row 654121: value=0.1145
data row 87113: value=0.9091
data row 170531: value=0.1032
data row 442220: value=0.6822
data row 438390: value=0.6259
data row 78315: value=0.2183
data row 718061: value=0.9536
data row 361710: value=0.9764
data row 217256: value=0.1041
data row 422514: value=0.7361
data row 485529: value=0.0834
data row 573173: value=0.4614
data row 997569: value=0.0331
data row 740344: value=0.3410
data row 134609: value=0.8699
data row 710651: value=0.9007
data row 434174: value=0.6752
data row 261468: value=0.2517
data row 877115: value=0.0020
data row 39399: value=0.0709
data row 711526: value=0.6467
data row 469694: value=0.5270
data row 184898: value=0.2700
data row 679571: value=0.9744
data row 144686: value=0.0632
data row 171824: value=0.5346
data row 646937: value=0.2340
data row 896718: value=0.9771
data row 800904: value=0.7028
data row 250458: value=0.6770
data row 38371: value=0.8531
data row 240017: value=0.1880
data row 814875: value=0.8238
data row 600020: value=0.2556
data row 480597: value=0.4616
data row 136021: value=0.6860
data row 265896: value=0.3455
data row 601921: value=0.5379
data row 213215: value=0.8137
data row 690554: value=0.2856
data row 39797: value=0.4604
data row 626787: value=0.2292
data row 928761: value=0.4391
data row 630516: value=0.1818
data row 840870: value=0.2652
data row 886962: value=0.2311
data row 171894: value=0.9912
data row 728190: value=0.7918
data row 225788: value=0.3671
data row 756309: value=0.2322
data row 598166: value=0.8834
data row 834245: value=0.5532
data row 494398: value=0.0897
data row 598609: value=0.3076
data row 184080: value=0.1379
data row 631676: value=0.9883
data row 277517: value=0.4156
data row 203377: value=0.7668
data row 747663: value=0.4534
data row 979873: value=0.6807
data row 277050: value=0.1606
data row 963006: value=0.0378
data row 289433: value=0.5557
data row 882810: value=0.9711
data row 890692: value=0.9867
data row 441662: value=0.8905
data row 435270: value=0.7318
data row 672821: value=0.7915
data row 547298: value=0.4199
data row 408242: value=0.8283
data row 122722: value=0.4585
data row 480586: value=0.0374
data row 530237: value=0.7639
data row 266122: value=0.0043
data row 858920: value=0.7684
data row 771441: value=0.4259
data row 608249: value=0.1765
data row 722049: value=0.3597
data row 193093: value=0.4048
data row 33453: value=0.9899
data row 17099: value=0.2796
data row 321476: value=0.2549
data row 285041: value=0.9556
data row 359106: value=0.4044
data row 672707: value=0.6102
data row 223144: value=0.7247
data row 290564: value=0.7979
data row 769562: value=0.5295
data row 729911: value=0.4820
data row 284898: value=0.8032
data row 762886: value=0.7954
data row 776900: value=0.4335
data row 217783: value=0.8555
data row 999902: value=0.2793
data row 159965: value=0.3655
data row 45456: value=0.7651
data row 92815: value=0.3244
data row 461959: value=0.3840
data row 645235: value=0.0476
data row 814353: value=0.2343
data row 581192: value=0.3456
data row 864343: value=0.2632
data row 231025: value=0.5288
data row 914567: value=0.1499
data row 574571: value=0.1848
data row 942846: value=0.0065
data row 876217: value=0.2283
data row 219603: value=0.1522
data row 801159: value=0.0099
data row 59316: value=0.5294
data row 845658: value=0.7434
data row 639263: value=0.2553
data row 563553: value=0.5034
data row 69326: value=0.4393
data row 109581: value=0.2531
data row 681356: value=0.7947
data row 582686: value=0.6187
data row 566657: value=0.3142
data row 646813: value=0.9903
data row 32619: value=0.3961
data row 286136: value=0.6359
data row 706006: value=0.8405
data row 949667: value=0.5064
data row 642831: value=0.0492
data row 225880: value=0.7009
data row 81357: value=0.5045
data row 385188: value=0.8131
data row 304955: value=0.4244
data row 400753: value=0.5045
data row 517398: value=0.6491
data row 250882: value=0.1874
data row 982910: value=0.5942
data row 573474: value=0.8973
data row 854650: value=0.3022
data row 215293: value=0.3214
data row 576329: value=0.2026
data row 405593: value=0.3286
data row 932712: value=0.2052
data row 358338: value=0.5672
data row 24941: value=0.1998
data row 233257: value=0.9186
data row 830658: value=0.6631
data row 303397: value=0.1136
data row 917663: value=0.4895
data row 297206: value=0.9359
data row 911546: value=0.9766
data row 580531: value=0.8862
data row 534924: value=0.9857
data row 270536: value=0.5704
data row 430743: value=0.1790
data row 602472: value=0.6438
data row 901393: value=0.4102
data row 249550: value=0.0093
data row 678878: value=0.7196
data row 718350: value=0.0288
data row 550093: value=0.3421
data row 561693: value=0.6701
data row 55202: value=0.4151
data row 365805: value=0.1614
data row 791850: value=0.7220
data row 884129: value=0.2489
data row 38172: value=0.9248
data row 181308: value=0.8264
data row 559171: value=0.0284
data row 849280: value=0.5354
data row 763665: value=0.3348
data row 699241: value=0.9198
data row 780647: value=0.2217
data row 746968: value=0.0173
data row 713670: value=0.9380
data row 151431: value=0.8154
data row 671088: value=0.2130
data row 275527: value=0.9299
data row 347906: value=0.1983
data row 619408: value=0.5986
data row 802034: value=0.7636
data row 66263: value=0.2711
data row 554203: value=0.3070
data row 565086: value=0.0880
data row 458495: value=0.0133
data row 162598: value=0.8772
data row 400610: value=0.2730
data row 500968: value=0.4797
data row 121712: value=0.7976
data row 25896: value=0.3158
data row 293465: value=0.4459
data row 667534: value=0.8278
data row 224416: value=0.4825
data row 775447: value=0.2900
data row 847456: value=0.8954
data row 299907: value=0.6547
data row 330060: value=0.0786
data row 721353: value=0.9364
data row 363751: value=0.4411
data row 767544: value=0.9495
data row 563171: value=0.5692
data row 205252: value=0.0750
data row 172636: value=0.8683
data row 995016: value=0.0959
data row 149134: value=0.6339
data row 842090: value=0.6486
data row 698306: value=0.1174
data row 483762: value=0.0912
data row 561377: value=0.9663
data row 347825: value=0.7714
data row 778657: value=0.6505
data row 794645: value=0.3993
data row 978702: value=0.2913
data row 683204: value=0.2161
data row 860033: value=0.9184
data row 401153: value=0.9320
data row 130094: value=0.6861
data row 525502: value=0.3914
data row 32418: value=0.0716
data row 651031: value=0.5926
data row 823995: value=0.1162
data row 31121: value=0.4547
data row 175911: value=0.5852
data row 775155: value=0.4061
data row 250685: value=0.8694
data row 652415: value=0.4608
data row 57571: value=0.4186
data row 574451: value=0.6172
data row 264343: value=0.8253
data row 730874: value=0.1469
data row 328816: value=0.3338
data row 482707: value=0.1427
data row 952005: value=0.5510
data row 140227: value=0.9399
data row 574949: value=0.3992
data row 381512: value=0.8681
data row 766212: value=0.6628
data row 242686: value=0.3345
data row 172256: value=0.6632
data row 633441: value=0.7463
data row 575086: value=0.7997
data row 571552: value=0.7506
data row 455655: value=0.6809
data row 835342: value=0.8631
data row 386426: value=0.0521
data row 552258: value=0.0502
data row 953410: value=0.3421
data row 152732: value=0.7442
data row 706235: value=0.2201
data row 494172: value=0.9259
data row 435373: value=0.9827
data row 466317: value=0.5618
data row 978863: value=0.0743
data row 264196: value=0.2976
data row 372985: value=0.0197
data row 550160: value=0.3647
data row 64860: value=0.3811
data row 109199: value=0.0602
data row 489380: value=0.7489
data row 707878: value=0.3017
data row 40847: value=0.2908
data row 606702: value=0.0281
data row 136840: value=0.4698
data row 831531: value=0.6416
data row 967616: value=0.8026
data row 639248: value=0.4432
data row 760939: value=0.1324
data row 549402: value=0.5177
data row 468142: value=0.0661
data row 375308: value=0.6001
data row 335959: value=0.7429
data row 68307: value=0.9472
data row 966995: value=0.2244
data row 34885: value=0.5636
data row 602355: value=0.6125
data row 678807: value=0.7403
data row 668025: value=0.3050
data row 726490: value=0.4044
data row 866803: value=0.3026
data row 394914: value=0.2726
data row 228422: value=0.2176
data row 925514: value=0.4298
data row 142369: value=0.3905
data row 282999: value=0.9299
data row 163310: value=0.6504
data row 547383: value=0.4578
data row 343671: value=0.4018
data row 507340: value=0.8248
data row 161077: value=0.9796
data row 205238: value=0.2276
data row 299530: value=0.4255
data row 908920: value=0.8793
data row 353491: value=0.5582
data row 559531: value=0.9225
data row 624256: value=0.9053
data row 839924: value=0.2240
data row 248086: value=0.5719
data row 798620: value=0.2026
data row 879568: value=0.1646
data row 46989: value=0.0251
data row 160188: value=0.7215
data row 476956: value=0.6774
data row 124986: value=0.4550
data row 347980: value=0.4301
data row 500562: value=0.6513
data row 20980: value=0.7064
data row 357370: value=0.4631
data row 920835: value=0.4420
data row 668834: value=0.5389
data row 251646: value=0.5257
data row 916984: value=0.3707
data row 584060: value=0.9682
data row 328045: value=0.9945
data row 456018: value=0.1756
data row 555529: value=0.1527
data row 151050: value=0.2034
data row 767182: value=0.9999
data row 327071: value=0.4935
data row 846837: value=0.0098
data row 125844: value=0.9425
data row 59659: value=0.8094
data row 700280: value=0.0478
data row 489394: value=0.5500
data row 739110: value=0.8399
data row 964812: value=0.1179
data row 487860: value=0.1040
data row 329639: value=0.3010
data row 462433: value=0.9196
data row 943082: value=0.3694
data row 153856: value=0.4238
data row 45561: value=0.7062
data row 568017: value=0.6156
data row 58768: value=0.8252
data row 683057: value=0.2334
data row 199560: value=0.8935
data row 635993: value=0.9381
data row 186528: value=0.4445
data row 369141: value=0.9017
data row 708525: value=0.9957
data row 935196: value=0.7535
data row 435393: value=0.8521
data row 263360: value=0.6288
data row 202601: value=0.0370
data row 485551: value=0.3461
data row 478692: value=0.5241
data row 628486: value=0.8627
data row 986940: value=0.0557
data row 487042: value=0.9149
data row 470005: value=0.6461
data row 839047: value=0.2742
data row 526194: value=0.4462
data row 915323: value=0.9388
data row 608526: value=0.7717
data row 738206: value=0.9474
data row 241316: value=0.3816
data row 878955: value=0.2957
data row 400299: value=0.6341
data row 415551: value=0.9664
data row 984465: value=0.5856
data row 792738: value=0.2128
data row 440669: value=0.7094
data row 474193: value=0.4997
data row 58827: value=0.5923
data row 238963: value=0.5993
data row 236931: value=0.0472
data row 581866: value=0.6450
data row 388949: value=0.7366
data row 745461: value=0.1429
data row 881536: value=0.9441
data row 322370: value=0.0489
data row 613676: value=0.2203
data row 940164: value=0.5453
data row 31531: value=0.3123
data row 819421: value=0.7377
data row 957373: value=0.3601
data row 521294: value=0.4605
data row 650048: value=0.4934
data row 845896: value=0.1099
data row 779955: value=0.4389
data row 931897: value=0.7419
data row 807036: value=0.7783
data row 120533: value=0.3428
data row 768388: value=0.2523
data row 806534: value=0.1992
data row 204608: value=0.4409
data row 861503: value=0.3490
data row 358661: value=0.9409
data row 264519: value=0.8235
data row 92657: value=0.2616
data row 77008: value=0.4888
data row 692903: value=0.5579
data row 21490: value=0.8127
data row 591539: value=0.4551
data row 619653: value=0.1243
data row 326832: value=0.6933
data row 326876: value=0.7888
data row 774182: value=0.9902
data row 920275: value=0.6499
data row 248291: value=0.8110
data row 478467: value=0.6170
data row 550431: value=0.6812
data row 381546: value=0.6447
data row 909056: value=0.2913
data row 499403: value=0.6639
data row 731278: value=0.3834
data row 575058: value=0.1974
data row 884571: value=0.9250
data row 259083: value=0.2376
data row 595905: value=0.3313
data row 332370: value=0.6216
data row 396811: value=0.0699
data row 954955: value=0.5318
data row 210623: value=0.3879
data row 806998: value=0.7121
data row 618078: value=0.2833
data row 420108: value=0.1120
data row 644496: value=0.2482
data row 621084: value=0.8189
data row 272264: value=0.1245
data row 249332: value=0.6153
data row 950370: value=0.6411
data row 183159: value=0.5910
data row 294863: value=0.9226
data row 158723: value=0.9290
data row 616907: value=0.0585
data row 495273: value=0.3308
data row 871103: value=0.5445
data row 561164: value=0.8727
data row 762261: value=0.9218
data row 932454: value=0.2376
data row 573525: value=0.7755
data row 435354: value=0.0723
data row 93797: value=0.9388
data row 259139: value=0.3814
data row 565259: value=0.4421
data row 651293: value=0.5481
data row 440585: value=0.6475
data row 325335: value=0.4716
data row 674654: value=0.8130
data row 382936: value=0.7683
data row 450376: value=0.4675
data row 438152: value=0.0583
data row 916917: value=0.7952
data row 143407: value=0.6043
data row 645786: value=0.1754
data row 203364: value=0.2212
data row 579117: value=0.8767
data row 780926: value=0.1885
data row 195450: value=0.9341
data row 656652: value=0.7044
data row 613819: value=0.1631
data row 202315: value=0.6220
data row 894464: value=0.9104
data row 266262: value=0.8187
data row 830047: value=0.5409
data row 911191: value=0.2817
data row 932931: value=0.3691
data row 319635: value=0.9046
data row 564388: value=0.0817
data row 823245: value=0.3125
data row 40571: value=0.8308
data row 120019: value=0.7362
data row 803120: value=0.2509
data row 903373: value=0.2916
data row 894712: value=0.2354
data row 520175: value=0.5988
data row 610853: value=0.2755
data row 41394: value=0.5634
data row 225325: value=0.8541
data row 628229: value=0.0385
data row 473931: value=0.0172
data row 685347: value=0.6767
data row 502192: value=0.2637
data row 314925: value=0.1860
data row 837185: value=0.1488
data row 331232: value=0.6858
data row 599509: value=0.6246
data row 411721: value=0.3546
data row 506149: value=0.5494
data row 604977: value=0.7031
data row 828295: value=0.7815
data row 615194: value=0.3154
data row 604535: value=0.3700
data row 679353: value=0.7217
data row 508497: value=0.6371
data row 410380: value=0.7075
data row 168746: value=0.1604
data row 377123: value=0.6941
data row 36437: value=0.5370
data row 256637: value=0.0560
data row 771664: value=0.1763
data row 74280: value=0.7404
data row 149224: value=0.4335
data row 953780: value=0.2346
data row 696365: value=0.0944
data row 244790: value=0.7157
data row 575024: value=0.7300
data row 397456: value=0.4461
data row 773920: value=0.4023
data row 907559: value=0.6553
data row 352178: value=0.3201
data row 36429: value=0.7080
data row 297929: value=0.4708
data row 853731: value=0.1246
data row 135871: value=0.3699
data row 823204: value=0.0217
data row 218763: value=0.9025
data row 576722: value=0.5625
data row 875180: value=0.4554
data row 465680: value=0.4834
data row 622348: value=0.7802
data row 594133: value=0.0629
data row 852239: value=0.3792
data row 55357: value=0.3175
data row 736253: value=0.9103
data row 118574: value=0.4082
data row 179518: value=0.1285
data row 811627: value=0.7660
data row 985390: value=0.2687
data row 146167: value=0.7582
data row 480978: value=0.6457
data row 533957: value=0.3074
data row 464545: value=0.3037
data row 788677: value=0.7464
data row 256237: value=0.5432
data row 511136: value=0.1899
data row 754546: value=0.9685
data row 408360: value=0.8886
data row 158587: value=0.2749
data row 523066: value=0.6337
data row 951188: value=0.6476
data row 543443: value=0.0959
data row 906620: value=0.9952
data row 40364: value=0.2815
data row 984761: value=0.9852
data row 694208: value=0.1024
data row 298120: value=0.7118
data row 368558: value=0.9842
data row 865680: value=0.8717
data row 777458: value=0.1662
data row 956005: value=0.1046
data row 350523: value=0.5065
data row 985120: value=0.6412
data row 393856: value=0.4917
data row 661710: value=0.3403
data row 10266: value=0.7894
data row 165397: value=0.3151
data row 566920: value=0.4856
data row 875961: value=0.2974
data row 903631: value=0.0484
data row 557043: value=0.9537
data row 323128: value=0.4809
data row 81407: value=0.7726
data row 992438: value=0.9538
data row 605173: value=0.0181
data row 388401: value=0.1949
data row 594754: value=0.5194
data row 437045: value=0.6302
data row 594364: value=0.4679
data row 743570: value=0.9382
data row 332930: value=0.2154
data row 923509: value=0.4112
data row 30241: value=0.5077
data row 540897: value=0.1221
data row 950756: value=0.0258
data row 17357: value=0.5364
data row 651175: value=0.3609
data row 120573: value=0.1368
data row 146372: value=0.8366
data row 561778: value=0.1893
data row 890228: value=0.8058
data row 862239: value=0.3684
data row 926874: value=0.1475
data row 789344: value=0.0770
data row 138455: value=0.2028
data row 965527: value=0.8319
data row 125616: value=0.3501
data row 471404: value=0.9153
data row 968448: value=0.2328
data row 167003: value=0.4141
data row 553098: value=0.5860
data row 331418: value=0.9928
data row 395780: value=0.4117
data row 657871: value=0.3412
data row 100137: value=0.0224
data row 265199: value=0.2969
data row 378088: value=0.4309
data row 344435: value=0.1150
data row 176054: value=0.4317
data row 37216: value=0.6786
data row 978757: value=0.7478
data row 912600: value=0.7010
data row 468999: value=0.4078
data row 157090: value=0.5436
data row 644738: value=0.8694
data row 956664: value=0.3326
data row 446121: value=0.5247
data row 412731: value=0.1929
data row 945708: value=0.7297
data row 475497: value=0.8153
data row 120186: value=0.8029
data row 677696: value=0.6950
data row 781565: value=0.4032
data row 821133: value=0.7208
data row 664328: value=0.9128
data row 97128: value=0.2105
data row 774708: value=0.4923
data row 322848: value=0.2608
data row 381104: value=0.1432
data row 401231: value=0.8266
data row 970055: value=0.6170
data row 633824: value=0.1766
data row 749007: value=0.6222
data row 977195: value=0.4867
data row 60879: value=0.9618
data row 799058: value=0.0724
data row 891646: value=0.6255
data row 516871: value=0.1959
data row 810442: value=0.7127
data row 546901: value=0.6278
data row 428300: value=0.3930
data row 584440: value=0.2999
data row 233142: value=0.7728
data row 163424: value=0.8470
data row 912312: value=0.4125
data row 220359: value=0.7221
data row 637733: value=0.9884
data row 856749: value=0.1442
data row 450229: value=0.4153
data row 236599: value=0.6832
data row 749353: value=0.2388
data row 630363: value=0.2407
data row 130681: value=0.2527
data row 348365: value=0.3447
data row 563016: value=0.3681
data row 962727: value=0.3567
data row 631654: value=0.2853
data row 977361: value=0.9876
data row 692037: value=0.4799
data row 446156: value=0.3522
data row 969288: value=0.0186
data row 720130: value=0.8507
data row 788398: value=0.8694
data row 918350: value=0.5908
data row 125689: value=0.5070
data row 76954: value=0.7598
data row 443464: value=0.7381
data row 705881: value=0.6505
data row 694760: value=0.0822
data row 99460: value=0.2313
data row 821580: value=0.9781
data row 424553: value=0.2150
data row 948717: value=0.1158
data row 758124: value=0.7548
data row 314258: value=0.1111
data row 719558: value=0.0170
data row 629294: value=0.1572
data row 486982: value=0.4321
data row 53880: value=0.4634
data row 780441: value=0.4446
data row 357189: value=0.7900
data row 817444: value=0.2321
data row 169661: value=0.7694
data row 848582: value=0.0624
data row 929767: value=0.1740
data row 65640: value=0.4256
data row 759726: value=0.0371
data row 64151: value=0.3332
data row 877457: value=0.2490
data row 412901: value=0.3693
data row 34640: value=0.6472
data row 896264: value=0.5681
data row 165062: value=0.1669
data row 82020: value=0.1906
data row 284282: value=0.8249
data row 637595: value=0.9139
data row 176681: value=0.8191
data row 116782: value=0.8772
data row 442990: value=0.4618
data row 448925: value=0.4839
data row 931650: value=0.9302
data row 901624: value=0.5442
data row 367772: value=0.9322
data row 230595: value=0.8432
data row 709468: value=0.1968
data row 425235: value=0.2368
data row 310511: value=0.1582
data row 423474: value=0.7648
data row 100358: value=0.6149
data row 251155: value=0.2123
data row 314289: value=0.2451
data row 667592: value=0.3998
data row 262784: value=0.9960
data row 897031: value=0.9799
data row 277492: value=0.2749
data row 537680: value=0.9911
data row 692843: value=0.3800
data row 172844: value=0.9025
data row 943627: value=0.5765
data row 344356: value=0.8452
data row 673854: value=0.3141
data row 378783: value=0.2900
data row 987976: value=0.5525
data row 604606: value=0.1202
data row 729516: value=0.2904
data row 887195: value=0.2916
data row 806273: value=0.3643
data row 94319: value=0.6043
data row 405538: value=0.2098
data row 817575: value=0.5641
data row 518913: value=0.4201
data row 520907: value=0.5061
data row 623416: value=0.7905
data row 438491: value=0.5379
data row 442508: value=0.9003
data row 245263: value=0.1033
data row 995998: value=0.5247
data row 716404: value=0.3229
data row 98188: value=0.3244
data row 582629: value=0.6561
data row 502548: value=0.4700
data row 679602: value=0.3302
data row 901496: value=0.0601
data row 391195: value=0.5118
data row 119020: value=0.6881
data row 160424: value=0.7583
data row 842631: value=0.6905
data row 457147: value=0.3613
data row 937220: value=0.8623
data row 549604: value=0.8468
data row 816299: value=0.4106
data row 112061: value=0.6960
data row 944272: value=0.2321
data row 288763: value=0.7312
data row 716441: value=0.8489
data row 979077: value=0.6940
data row 689269: value=0.3781
data row 430729: value=0.7739
data row 68560: value=0.6363
data row 595706: value=0.9428
data row 972043: value=0.9589
data row 818545: value=0.4209
data row 210860: value=0.5918
data row 627133: value=0.8385
data row 672068: value=0.6844
data row 216846: value=0.6153
data row 852957: value=0.3984
data row 850674: value=0.4832
data row 527141: value=0.6792
data row 418703: value=0.3066
data row 495974: value=0.6479
data row 564508: value=0.6582
data row 355203: value=0.8491
data row 112345: value=0.3177
data row 182476: value=0.7164
data row 321490: value=0.3293
data row 41663: value=0.3139
data row 876248: value=0.6962
data row 104292: value=0.6836
data row 481179: value=0.8198
data row 489623: value=0.2576
data row 417078: value=0.6951
data row 661648: value=0.4329
data row 450418: value=0.0032
data row 519074: value=0.5967
data row 441831: value=0.4145
data row 876309: value=0.7597
data row 856495: value=0.3065
data row 544110: value=0.9210
data row 632864: value=0.1518
data row 790251: value=0.4007
data row 827875: value=0.3062
data row 659779: value=0.4246
data row 245715: value=0.5947
data row 132503: value=0.1965
data row 502509: value=0.8990
data row 254190: value=0.6087
data row 666322: value=0.2690
data row 648189: value=0.7006
data row 512751: value=0.5553
data row 538585: value=0.8538
data row 997281: value=0.2160
data row 483084: value=0.6060
data row 632801: value=0.4848
data row 462169: value=0.1444
data row 684377: value=0.8484
data row 841067: value=0.3222
data row 642040: value=0.9890
data row 894499: value=0.1806
data row 722926: value=0.6407
data row 32636: value=0.8215
data row 955718: value=0.1152
data row 904622: value=0.1934
data row 863787: value=0.4015
data row 285456: value=0.4924
data row 821280: value=0.7799
data row 815480: value=0.9964
data row 877676: value=0.4137
data row 183034: value=0.7374
data row 605171: value=0.6299
data row 261751: value=0.2238
data row 51595: value=0.2709
data row 547253: value=0.3848
data row 310745: value=0.1602
data row 118048: value=0.8455
data row 174145: value=0.9724
data row 438924: value=0.9686
data row 593932: value=0.8801
data row 851657: value=0.2267
data row 820795: value=0.5497
data row 278102: value=0.1822
data row 612272: value=0.6368
data row 252345: value=0.6743
data row 975429: value=0.5076
data row 351786: value=0.8704
data row 459017: value=0.4499
data row 211924: value=0.1643
data row 229649: value=0.3005
data row 568895: value=0.9539
data row 369874: value=0.2233
data row 441783: value=0.4348
data row 820196: value=0.5546
data row 902991: value=0.0580
data row 542128: value=0.9145
data row 148838: value=0.0438
data row 348086: value=0.8594
data row 411509: value=0.1836
data row 906998: value=0.5252
data row 882023: value=0.9191
data row 587146: value=0.7764
data row 884443: value=0.0385
data row 104520: value=0.8730
data row 589667: value=0.5161
data row 922962: value=0.8553
data row 641419: value=0.6494
data row 701953: value=0.1761
data row 870162: value=0.8974
data row 984429: value=0.8328
data row 683243: value=0.8837
data row 283942: value=0.0834
data row 11414: value=0.4160
data row 253307: value=0.5629
data row 892673: value=0.4653
data row 671495: value=0.7328
data row 498483: value=0.2198
data row 937073: value=0.4605
data row 955067: value=0.0164
data row 105687: value=0.9538
data row 112750: value=0.8686
data row 310074: value=0.3283
data row 134688: value=0.4808
data row 132186: value=0.0241
data row 948136: value=0.3498
data row 634072: value=0.7023
data row 840879: value=0.0058
data row 934820: value=0.0764
data row 452280: value=0.7556
data row 928467: value=0.4566
data row 830159: value=0.1825
data row 267760: value=0.4554
data row 624431: value=0.4045
data row 502248: value=0.7900
data row 766988: value=0.4160
data row 647632: value=0.2412
data row 606615: value=0.6395
data row 824638: value=0.5341
data row 56555: value=0.1667
data row 504664: value=0.8965
data row 225225: value=0.0892
data row 42686: value=0.5715
data row 376265: value=0.5546
data row 948719: value=0.2798
data row 385402: value=0.3353
data row 348390: value=0.8132
data row 280891: value=0.3837
data row 315144: value=0.3193
data row 399708: value=0.9409
data row 434290: value=0.1930
data row 272951: value=0.6383
data row 41671: value=0.1979
data row 407110: value=0.2305
data row 475389: value=0.0381
data row 694889: value=0.1610
data row 90063: value=0.0595
data row 697405: value=0.8673
data row 705027: value=0.4200
data row 458919: value=0.4253
data row 652823: value=0.2902
data row 236259: value=0.8853
data row 181337: value=0.9715
data row 730311: value=0.4783
data row 517587: value=0.0762
data row 763151: value=0.6067
data row 169157: value=0.1042
data row 283948: value=0.7766
data row 316768: value=0.0358
data row 310787: value=0.3956
data row 824280: value=0.4009
data row 188785: value=0.6229
data row 223610: value=0.4203
data row 531213: value=0.2059
data row 960147: value=0.3703
data row 800335: value=0.5580
data row 980851: value=0.6862
data row 160116: value=0.3957
data row 113241: value=0.5076
data row 360099: value=0.7813
data row 832543: value=0.3057
data row 120931: value=0.7799
data row 375515: value=0.1583
data row 863430: value=0.4165
data row 637130: value=0.8842
data row 643856: value=0.7214
data row 621769: value=0.2369
data row 669433: value=0.4007
data row 873782: value=0.2987
data row 988194: value=0.3402
data row 537658: value=0.3002
data row 815306: value=0.0770
data row 981442: value=0.2986
data row 864813: value=0.2863
data row 294793: value=0.0679
data row 527575: value=0.7909
data row 821163: value=0.6404
data row 262596: value=0.6576
data row 13096: value=0.1448
data row 165873: value=0.4125
data row 992214: value=0.9038
data row 416540: value=0.3626
data row 189537: value=0.8561
data row 661586: value=0.5873
data row 381353: value=0.5129
data row 110178: value=0.1913
data row 971147: value=0.9725
data row 285446: value=0.4280
data row 449798: value=0.3650
data row 435063: value=0.4290
data row 361241: value=0.5849
data row 452493: value=0.5713
data row 195293: value=0.9080
data row 774416: value=0.9130
data row 533144: value=0.0048
data row 654656: value=0.1687
data row 742707: value=0.8144
data row 704171: value=0.3803
data row 978350: value=0.7967
data row 973075: value=0.1600
data row 221671: value=0.9171
data row 361544: value=0.7542
data row 864822: value=0.0835
data row 920214: value=0.8019
data row 765987: value=0.6483
data row 865155: value=0.1923
data row 148149: value=0.5983
data row 662416: value=0.6547
data row 853272: value=0.5458
data row 311862: value=0.2405
data row 357954: value=0.6180
data row 443689: value=0.8973
data row 422887: value=0.3825
data row 225511: value=0.5426
data row 720181: value=0.2216
data row 210521: value=0.5400
data row 139197: value=0.5014
data row 264522: value=0.7309
data row 737417: value=0.8080
data row 257725: value=0.8991
data row 640463: value=0.0061
data row 400816: value=0.9787
data row 646605: value=0.8959
data row 992353: value=0.9140
data row 113448: value=0.4239
data row 521418: value=0.8274
data row 598988: value=0.4177
data row 696672: value=0.1500
data row 762634: value=0.0307
data row 45622: value=0.8114
data row 741787: value=0.4775
data row 621084: value=0.5640
data row 709420: value=0.3102
data row 241296: value=0.7879
data row 281705: value=0.5628
data row 401661: value=0.7972
data row 582978: value=0.4289
data row 275445: value=0.1050
data row 505764: value=0.0704
data row 404944: value=0.8174
data row 316298: value=0.5602
data row 238040: value=0.7062
data row 863337: value=0.6006
data row 490213: value=0.9458
data row 437576: value=0.4288
data row 188050: value=0.2236
data row 15966: value=0.3269
data row 296113: value=0.5079
data row 533856: value=0.8528
data row 404693: value=0.5947
data row 781479: value=0.2849
data row 241788: value=0.3079
data row 947793: value=0.8505
data row 499867: value=0.1970
data row 912389: value=0.1945
data row 107081: value=0.0610
data row 335815: value=0.8505
data row 729851: value=0.8115
data row 260524: value=0.6116
data row 805457: value=0.5258
data row 261294: value=0.5600
data row 593706: value=0.8073
data row 334290: value=0.2209
data row 377190: value=0.0890
data row 497525: value=0.9846
data row 392989: value=0.7096
data row 203842: value=0.0471
data row 288525: value=0.6199
data row 855678: value=0.4910
data row 556754: value=0.5831
data row 446418: value=0.0240
data row 537269: value=0.3014
data row 862182: value=0.4070
data row 801488: value=0.5611
data row 337941: value=0.6034
data row 789180: value=0.1458
data row 79845: value=0.3460
data row 871544: value=0.9926
data row 412595: value=0.8315
data row 344658: value=0.4089
data row 96035: value=0.8463
data row 328088: value=0.0549
data row 542310: value=0.1130
data row 742183: value=0.1389
data row 275242: value=0.2668
data row 248352: value=0.9249
data row 385170: value=0.3845
data row 35672: value=0.0614
data row 683203: value=0.6664
data row 373500: value=0.2087
data row 229014: value=0.8755
data row 950428: value=0.8813
data row 786304: value=0.1712
data row 671166: value=0.1210
data row 53282: value=0.6426
data row 784375: value=0.9983
data row 594738: value=0.2083
data row 419889: value=0.8190
data row 697046: value=0.0609
data row 434211: value=0.2119
data row 947655: value=0.4232
data row 203941: value=0.1085
data row 395034: value=0.8951
data row 695793: value=0.4177
data row 818797: value=0.8747
data row 59177: value=0.8145
data row 38938: value=0.9481
data row 560975: value=0.3941
data row 880525: value=0.9157
data row 938877: value=0.6676
data row 414491: value=0.3703
data row 156616: value=0.8085
data row 800159: value=0.9945
data row 248896: value=0.5427
data row 793347: value=0.0421
data row 334630: value=0.3578
data row 259374: value=0.5185
data row 587604: value=0.7146
data row 150078: value=0.9950
data row 223382: value=0.0959
data row 63835: value=0.2483
data row 777336: value=0.8824
data row 402169: value=0.7257
data row 562200: value=0.1897
data row 613494: value=0.4875
data row 186419: value=0.2782
data row 774342: value=0.3732
data row 370134: value=0.8960
data row 593694: value=0.0496
data row 842624: value=0.9907
data row 297889: value=0.3905
data row 423553: value=0.3164
data row 987735: value=0.8423
data row 952556: value=0.7709
data row 591382: value=0.0058
data row 467107: value=0.8051
data row 330712: value=0.7565
data row 81626: value=0.3413
data row 387457: value=0.4500
data row 246076: value=0.9740
data row 538634: value=0.2689
data row 393800: value=0.2222
data row 411177: value=0.2481
data row 463496: value=0.0865
data row 695081: value=0.4578
data row 392972: value=0.3521
data row 651026: value=0.3644
data row 458997: value=0.6024
data row 171391: value=0.2382
data row 711329: value=0.3208
data row 137718: value=0.9734
data row 640760: value=0.2404
data row 525126: value=0.6337
data row 863046: value=0.2319
data row 977015: value=0.8836
data row 193741: value=0.5548
data row 130769: value=0.0236
data row 958780: value=0.2961
data row 370511: value=0.9139
data row 301760: value=0.9760
data row 535228: value=0.3015
data row 812842: value=0.6386
data row 280479: value=0.2049
data row 381016: value=0.2594
data row 168642: value=0.3995
data row 537916: value=0.2895
data row 814217: value=0.7871
data row 869583: value=0.7050
data row 899000: value=0.6757
data row 498442: value=0.0855
data row 958427: value=0.5201
data row 315170: value=0.8779
data row 75283: value=0.4957
data row 438060: value=0.1183
data row 837281: value=0.9220
data row 770886: value=0.1487
data row 113065: value=0.4314
data row 860421: value=0.8939
data row 837555: value=0.7206
data row 491853: value=0.8644
data row 964116: value=0.7903
data row 885620: value=0.2069
data row 116619: value=0.3413
data row 689940: value=0.7432
data row 673213: value=0.9630
data row 615334: value=0.6624
data row 457027: value=0.3361
data row 510578: value=0.9986
data row 848191: value=0.9075
data row 384514: value=0.0633
data row 394022: value=0.5270
data row 253866: value=0.4005
data row 732128: value=0.9709
data row 777940: value=0.0454
data row 265719: value=0.7057
data row 766479: value=0.2915
data row 269517: value=0.4070
data row 474097: value=0.7241
data row 615892: value=0.7892
data row 114090: value=0.1295
data row 248060: value=0.6980
data row 929492: value=0.7142
data row 590738: value=0.7562
data row 403910: value=0.6157
data row 788022: value=0.9126
data row 260790: value=0.4434
data row 983056: value=0.2503
data row 323056: value=0.1942
data row 795927: value=0.3813
data row 500320: value=0.8824
data row 183638: value=0.8017
data row 263039: value=0.6572
data row 409448: value=0.8843
data row 38710: value=0.1590
data row 715469: value=0.0210
data row 605150: value=0.0977
data row 674795: value=0.8171
data row 152106: value=0.2678
data row 838602: value=0.1143
data row 21235: value=0.7561
data row 567821: value=0.2047
data row 684984: value=0.8821
data row 144740: value=0.0668
data row 279447: value=0.2736
data row 921599: value=0.1550
data row 207206: value=0.8611
data row 445254: value=0.0243
data row 764185: value=0.7463
data row 64029: value=0.9540
data row 476818: value=0.3049
data row 909813: value=0.3045
data row 802700: value=0.4589
data row 620389: value=0.1983
data row 943874: value=0.5865
data row 978311: value=0.9598
data row 910700: value=0.6701
data row 33834: value=0.4392
data row 936420: value=0.1350
data row 136896: value=0.9822
data row 616199: value=0.8255
data row 360506: value=0.4962
data row 813415: value=0.8738
data row 122778: value=0.5285
data row 461898: value=0.5686
data row 219817: value=0.8620
data row 134976: value=0.1228
data row 570712: value=0.9580
data row 885046: value=0.6023
data row 944997: value=0.6958
data row 428052: value=0.1832
data row 243744: value=0.6447
data row 452650: value=0.9369
data row 466366: value=0.9050
data row 625333: value=0.0043
data row 382691: value=0.9766
data row 467523: value=0.5352
data row 775135: value=0.3457
data row 313322: value=0.5012
data row 444835: value=0.8584
data row 88357: value=0.9816
data row 321929: value=0.6922
data row 515598: value=0.4840
data row 90519: value=0.1555
data row 890933: value=0.8509
data row 265179: value=0.0402
data row 125395: value=0.2586
data row 881406: value=0.0248
data row 172568: value=0.6392
data row 682197: value=0.1450
data row 735471: value=0.1899
data row 670613: value=0.6160
data row 668320: value=0.1097
data row 662816: value=0.4324
data row 578312: value=0.7398
data row 734707: value=0.8915
data row 484654: value=0.6258
data row 933069: value=0.7736
data row 824093: value=0.7057
data row 920001: value=0.6516
data row 232872: value=0.7630
data row 235290: value=0.5208
data row 647358: value=0.2063
data row 878524: value=0.7919
data row 987405: value=0.5126
data row 861238: value=0.2312
data row 976874: value=0.2154
data row 294072: value=0.8580
data row 652296: value=0.9933
data row 882231: value=0.2460
data row 491769: value=0.4837
data row 921561: value=0.3208
data row 722632: value=0.0927
data row 566468: value=0.3381
data row 268357: value=0.2448
data row 498133: value=0.3074
data row 789844: value=0.3696
data row 212399: value=0.0691
data row 750378: value=0.3363
data row 816782: value=0.3015
data row 201338: value=0.8909
data row 112974: value=0.1037
data row 420471: value=0.2313
data row 501105: value=0.0641
data row 106725: value=0.8154
data row 856506: value=0.1321
data row 382926: value=0.5701
data row 451443: value=0.9474
data row 701342: value=0.9398
data row 951521: value=0.7758
data row 804017: value=0.7503
data row 125064: value=0.9972
data row 934078: value=0.9480
data row 628262: value=0.6773
data row 946812: value=0.6617
data row 311133: value=0.7548
data row 333355: value=0.1511
data row 543098: value=0.3856
data row 904465: value=0.8841
data row 710906: value=0.4768
data row 461522: value=0.0470
data row 943568: value=0.0617
data row 890733: value=0.9745
data row 331679: value=0.7513
data row 635973: value=0.3743
data row 840122: value=0.6776
data row 513623: value=0.8882
data row 194444: value=0.0114
data row 541379: value=0.1138
data row 874434: value=0.9696
data row 242320: value=0.3539
data row 847354: value=0.0064
data row 246042: value=0.1606
data row 839602: value=0.5873
data row 736223: value=0.6931
data row 652093: value=0.9531
data row 845370: value=0.2153
data row 777130: value=0.4017
data row 829407: value=0.7770
data row 200101: value=0.3105
data row 345219: value=0.1430
data row 471941: value=0.6847
data row 477491: value=0.3215
data row 491977: value=0.5417
data row 730061: value=0.4352
data row 939392: value=0.0893
data row 977790: value=0.9889
data row 849437: value=0.6953
data row 750149: value=0.1308
data row 852276: value=0.7778
data row 719623: value=0.1842
data row 618595: value=0.2338
data row 721228: value=0.4163
data row 726835: value=0.8305
data row 727904: value=0.3957
data row 26865: value=0.2066
data row 584351: value=0.5848
data row 965484: value=0.8088
data row 326544: value=0.1711
data row 812870: value=0.8740
data row 849298: value=0.5154
data row 830613: value=0.2001
data row 610843: value=0.5075
data row 289222: value=0.2529
data row 260520: value=0.1840
data row 256468: value=0.0193
data row 626812: value=0.4576
data row 678810: value=0.2258
data row 637586: value=0.4952
data row 523798: value=0.5781
data row 663107: value=0.4781
data row 402512: value=0.1780
data row 337941: value=0.1437
data row 427897: value=0.6778
data row 273957: value=0.1542
data row 23861: value=0.6764
data row 323833: value=0.9009
data row 955834: value=0.9800
data row 641860: value=0.7191
data row 190447: value=0.0727
data row 694761: value=0.4085
data row 122145: value=0.6604
data row 30661: value=0.1526
data row 993608: value=0.0354
data row 424950: value=0.2677
data row 361969: value=0.6661
data row 713362: value=0.7197
data row 173264: value=0.3844
data row 681748: value=0.1335
data row 197583: value=0.8613
data row 470817: value=0.5575
data row 547410: value=0.0221
data row 428245: value=0.4740
data row 281585: value=0.0680
data row 722769: value=0.1623
data row 887382: value=0.5808
data row 399340: value=0.3543
data row 463024: value=0.5770
data row 843259: value=0.7731
data row 466958: value=0.9308
data row 793042: value=0.3113
data row 689841: value=0.3602
data row 776033: value=0.1025
data row 928616: value=0.5163
data row 94497: value=0.8593
data row 708064: value=0.1269
data row 604397: value=0.7890
data row 741738: value=0.4344
data row 844715: value=0.5856
data row 245684: value=0.5305
data row 838116: value=0.2804
data row 769523: value=0.3030
data row 800930: value=0.9762
data row 860747: value=0.8784
data row 802217: value=0.6831
data row 197397: value=0.0475
data row 769687: value=0.7924
data row 965297: value=0.2241
data row 183787: value=0.6075
data row 867356: value=0.0503
data row 64657: value=0.3511
data row 528084: value=0.4674
data row 15237: value=0.7018
data row 132521: value=0.7842
data row 438095: value=0.0004
data row 239089: value=0.2379
data row 104558: value=0.3259
data row 738083: value=0.3677
data row 428066: value=0.1514
data row 89470: value=0.4575
data row 451913: value=0.8969
data row 843618: value=0.5148
data row 339616: value=0.7176
data row 882879: value=0.1418
data row 117331: value=0.7845
data row 560442: value=0.2869
data row 266782: value=0.1305
data row 781908: value=0.5548
data row 318189: value=0.7790
data row 506688: value=0.9052
data row 275674: value=0.5807
data row 340889: value=0.0205
data row 596447: value=0.9173
data row 153354: value=0.7740
data row 305826: value=0.4792
data row 259407: value=0.4756
data row 436789: value=0.2048
data row 325212: value=0.8509
data row 598927: value=0.0205
data row 439154: value=0.5029
data row 636290: value=0.6529
data row 298248: value=0.5410
data row 216424: value=0.1576
data row 976408: value=0.2300
data row 57638: value=0.1984
data row 368832: value=0.2538
data row 629398: value=0.8675
data row 868595: value=0.3505
data row 212408: value=0.7376
data row 86985: value=0.0797
data row 73739: value=0.0502
data row 223657: value=0.5793
data row 767152: value=0.6744
data row 521548: value=0.2918
data row 61889: value=0.9076
data row 152131: value=0.6748
data row 189624: value=0.4948
data row 181949: value=0.9257
data row 944041: value=0.1817
data row 723525: value=0.2180
data row 841030: value=0.0306
data row 614204: value=0.1960
data row 140412: value=0.3297
data row 222413: value=0.5526
data row 447547: value=0.6285
data row 17544: value=0.1473
data row 416989: value=0.6363
data row 346231: value=0.1737
data row 445878: value=0.8056
data row 115359: value=0.3711
data row 313269: value=0.9723
data row 613188: value=0.7905
data row 145504: value=0.4100
data row 621846: value=0.6131
data row 185076: value=0.4971
data row 276432: value=0.2792
data row 715501: value=0.4393
data row 242418: value=0.2042
data row 760250: value=0.6536
data row 695764: value=0.3299
data row 167168: value=0.0473
data row 197122: value=0.7094
data row 401009: value=0.8752
data row 828028: value=0.4322
data row 384618: value=0.6233
data row 387163: value=0.4831
data row 317794: value=0.2984
data row 724951: value=0.5438
data row 463434: value=0.3335
data row 11314: value=0.5279
data row 529272: value=0.0522
data row 332277: value=0.6590
data row 516538: value=0.9370
data row 890359: value=0.0871
data row 749758: value=0.7969
data row 164685: value=0.9625
data row 425797: value=0.1011
data row 661910: value=0.9635
data row 949974: value=0.5635
data row 87894: value=0.8412
data row 376142: value=0.4001
data row 765682: value=0.5118
data row 310533: value=0.0714
data row 326475: value=0.4933
data row 960207: value=0.5581
data row 772102: value=0.2466
data row 667946: value=0.7631
data row 285255: value=0.5431
data row 827116: value=0.2389
data row 937692: value=0.5354
data row 26894: value=0.9338
data row 182058: value=0.6602
data row 45799: value=0.6087
data row 564921: value=0.3250
data row 97756: value=0.9183
data row 257573: value=0.4347
data row 104673: value=0.6698
data row 584850: value=0.7210
data row 175202: value=0.4173
data row 472193: value=0.8408
data row 704406: value=0.4437
data row 421559: value=0.0433
data row 901012: value=0.7988
data row 86186: value=0.2225
data row 379105: value=0.2371
data row 510380: value=0.9448
data row 885407: value=0.3960
data row 853954: value=0.2880
data row 307264: value=0.9462
data row 104105: value=0.7508
data row 495544: value=0.2129
data row 66396: value=0.4547
data row 108672: value=0.4303
data row 282558: value=0.3427
data row 281703: value=0.2418
data row 89722: value=0.1146
data row 757843: value=0.2208
data row 375024: value=0.7535
data row 875974: value=0.7445
data row 257784: value=0.4963
data row 54373: value=0.8249
data row 911515: value=0.7114
data row 680414: value=0.0222
data row 941679: value=0.3551
data row 168678: value=0.4357
data row 646763: value=0.5620
data row 540196: value=0.0219
data row 748719: value=0.4181
data row 969993: value=0.8044
data row 983717: value=0.3389
data row 895068: value=0.4867
data row 117905: value=0.5615
data row 870222: value=0.0798
data row 654733: value=0.6332
data row 432546: value=0.3236
data row 689103: value=0.7833
data row 471874: value=0.2091
data row 794745: value=0.9817
data row 66773: value=0.0052
data row 469673: value=0.4672
data row 80985: value=0.3197
data row 471714: value=0.9879
data row 352171: value=0.0421
data row 555340: value=0.4184
data row 471208: value=0.7020
data row 329062: value=0.9165
data row 68991: value=0.7536
data row 464485: value=0.1579
data row 725454: value=0.8404
data row 576844: value=0.6735
data row 600857: value=0.9690
data row 394923: value=0.8476
data row 560261: value=0.2952
data row 381566: value=0.5251
data row 466943: value=0.7538
data row 966022: value=0.0079
data row 730523: value=0.2070
data row 56192: value=0.6489
data row 793594: value=0.8708
data row 686777: value=0.1550
data row 263080: value=0.7623
data row 885910: value=0.7453
data row 506431: value=0.3725
data row 95815: value=0.2095
data row 420203: value=0.2722
data row 737712: value=0.7828
data row 321192: value=0.1535
data row 346286: value=0.9379
data row 618824: value=0.8610
data row 224331: value=0.2238
data row 719496: value=0.2668
data row 757477: value=0.8659
data row 355964: value=0.3900
data row 302931: value=0.2232
data row 78470: value=0.6133
data row 527753: value=0.6753
data row 217613: value=0.3103
data row 359079: value=0.0311
data row 937845: value=0.2908
data row 429726: value=0.7974
data row 170161: value=0.4676
data row 836456: value=0.5437
data row 450747: value=0.0044
data row 62316: value=0.2519
data row 999751: value=0.4452
data row 788180: value=0.3127
data row 696661: value=0.1014
data row 993214: value=0.6147
data row 75884: value=0.0139
data row 579197: value=0.9766
data row 834059: value=0.1026
data row 700916: value=0.6029
data row 801639: value=0.9497
data row 832377: value=0.0168
data row 630823: value=0.1798
data row 481301: value=0.8879
data row 775590: value=0.9586
data row 376396: value=0.7645
data row 684054: value=0.6862
data row 686301: value=0.0972
data row 585576: value=0.0953
data row 573845: value=0.8621
data row 269866: value=0.7615
data row 857956: value=0.1317
data row 704045: value=0.7598
data row 789033: value=0.7553
data row 579349: value=0.0187
data row 394630: value=0.8792
data row 843316: value=0.5654
data row 604512: value=0.9450
data row 770986: value=0.8644
data row 845421: value=0.3679
data row 669017: value=0.8641
data row 875271: value=0.2432
data row 974242: value=0.9795
data row 980320: value=0.9313
data row 444732: value=0.8533
data row 478441: value=0.8239
data row 710236: value=0.1509
data row 249454: value=0.6043
data row 327728: value=0.5704
data row 312265: value=0.8046
data row 257335: value=0.6602
data row 190496: value=0.6737
data row 237868: value=0.5615
data row 752131: value=0.4950
data row 665135: value=0.1830
data row 225139: value=0.7920
data row 566517: value=0.3603
data row 294097: value=0.6485
data row 656773: value=0.1664
data row 689153: value=0.9131
data row 913865: value=0.9692
data row 621699: value=0.0647
data row 992643: value=0.6449
data row 152727: value=0.7211
data row 267773: value=0.7616
data row 794528: value=0.3304
data row 226590: value=0.8393
data row 718129: value=0.6327
data row 52405: value=0.1158
data row 982968: value=0.7299
data row 920056: value=0.4568
data row 979531: value=0.8326
data row 104512: value=0.4197
data row 775980: value=0.8995
data row 879253: value=0.1192
data row 276238: value=0.6616
data row 243229: value=0.0320
data row 265708: value=0.4339
data row 883569: value=0.0989
data row 455002: value=0.1499
data row 48132: value=0.4366
data row 818565: value=0.3086
data row 199649: value=0.7788
data row 90676: value=0.0319
data row 960684: value=0.5795
data row 496488: value=0.9608
data row 659033: value=0.6259
data row 407080: value=0.7280
data row 906245: value=0.8249
data row 874045: value=0.3081
data row 35511: value=0.1036
data row 634743: value=0.9362
data row 972953: value=0.9948
data row 856688: value=0.8666
data row 274981: value=0.5000
data row 982938: value=0.6159
data row 556979: value=0.8467
data row 220275: value=0.7950
data row 744047: value=0.4648
data row 892403: value=0.0843
data row 844143: value=0.2435
data row 505015: value=0.8071
data row 787810: value=0.2583
data row 608564: value=0.9178
data row 911208: value=0.8359
data row 896441: value=0.5685
data row 138159: value=0.1251
data row 530180: value=0.0535
data row 158449: value=0.8574
data row 599615: value=0.7869
data row 706559: value=0.8280
data row 430726: value=0.2217
data row 628897: value=0.6479
data row 141127: value=0.8473
data row 481486: value=0.4397
data row 784114: value=0.2476
data row 281839: value=0.6175
data row 710797: value=0.4460
data row 80415: value=0.4745
data row 11800: value=0.0099
data row 714524: value=0.6721
data row 292101: value=0.5725
data row 333336: value=0.1755
data row 614334: value=0.3017
data row 22504: value=0.3315
data row 823515: value=0.6879
data row 851070: value=0.0435
data row 75427: value=0.9781
data row 951062: value=0.0611
data row 996056: value=0.3539
data row 108504: value=0.3254
data row 857996: value=0.7986
data row 163146: value=0.1878
data row 121283: value=0.3789
data row 902454: value=0.5177
data row 483363: value=0.3114
data row 382761: value=0.2686
data row 853050: value=0.5483
data row 424846: value=0.4272
data row 37745: value=0.0660
data row 150656: value=0.1277
data row 951388: value=0.8299
data row 138414: value=0.5999
data row 54819: value=0.7094
data row 219965: value=0.8579
data row 640470: value=0.1279
data row 465944: value=0.8594
data row 617790: value=0.3326
data row 336109: value=0.0079
data row 397056: value=0.8163
data row 503529: value=0.2776
data row 921980: value=0.1838
data row 495023: value=0.8142
data row 117862: value=0.2260
data row 105115: value=0.9288
data row 680762: value=0.1886
data row 151888: value=0.3802
data row 11577: value=0.8627
data row 349155: value=0.9349
data row 905840: value=0.3031
data row 172020: value=0.1576
data row 870010: value=0.1225
data row 292373: value=0.2901
data row 738857: value=0.8112
data row 162786: value=0.3556
data row 898203: value=0.1370
data row 336227: value=0.4171
data row 260348: value=0.3382
data row 222197: value=0.8902
data row 446269: value=0.7804
data row 802986: value=0.4729
data row 286903: value=0.8147
data row 392484: value=0.5642
data row 127654: value=0.6558
data row 846806: value=0.7917
data row 303618: value=0.6000
data row 468117: value=0.1389
data row 621985: value=0.0125
data row 819993: value=0.5861
data row 94669: value=0.2993
data row 582732: value=0.5947
data row 583285: value=0.1142
data row 593451: value=0.7549
data row 176002: value=0.2931
data row 265933: value=0.9084
data row 646873: value=0.7311
data row 101801: value=0.7026
data row 274780: value=0.5777
data row 422047: value=0.7563
data row 936208: value=0.5177
data row 811176: value=0.4487
data row 997687: value=0.9887
data row 105549: value=0.1876
data row 889812: value=0.2411
data row 644450: value=0.0363
data row 429274: value=0.6206
data row 373093: value=0.9916
data row 31835: value=0.5414
data row 619226: value=0.7503
data row 276439: value=0.0742
data row 286594: value=0.9026
data row 266467: value=0.5957
data row 97237: value=0.6627
data row 792116: value=0.1143
data row 274295: value=0.3943
data row 469112: value=0.0491
data row 226665: value=0.5221
data row 572946: value=0.4707
data row 118477: value=0.6635
data row 162302: value=0.4678
data row 152921: value=0.6421
data row 930191: value=0.9429
data row 454099: value=0.2973
data row 486040: value=0.6153
data row 14086: value=0.0679
data row 285453: value=0.9158
data row 355216: value=0.7914
data row 500091: value=0.9534
data row 19305: value=0.6974
data row 630927: value=0.9108
data row 545077: value=0.5221
data row 224507: value=0.1802
data row 921230: value=0.0931
data row 804668: value=0.4358
data row 20278: value=0.8870
data row 802487: value=0.2237
data row 463438: value=0.4536
data row 326824: value=0.4202
data row 542138: value=0.1457
data row 99671: value=0.7310
data row 998075: value=0.6051
data row 341500: value=0.4050
data row 638069: value=0.3423
data row 243893: value=0.7895
data row 916877: value=0.2208
data row 576246: value=0.9821
data row 157062: value=0.2729
data row 501429: value=0.7984
data row 24966: value=0.3438
data row 969354: value=0.9785
data row 403111: value=0.2710
data row 465072: value=0.6111
data row 405295: value=0.8690
data row 837594: value=0.4508
data row 280116: value=0.5452
data row 648777: value=0.3292
data row 507855: value=0.6095
data row 266212: value=0.2700
data row 320021: value=0.1675
data row 350543: value=0.7670
data row 109353: value=0.1755
data row 549301: value=0.8329
data row 656966: value=0.2111
data row 312403: value=0.0566
data row 944166: value=0.5738
data row 818487: value=0.4009
data row 655532: value=0.1667
data row 20484: value=0.9261
data row 250272: value=0.9684
data row 446375: value=0.2639
data row 196652: value=0.7142
data row 320441: value=0.1246
data row 372588: value=0.7999
data row 524203: value=0.9508
data row 39545: value=0.8680
data row 594522: value=0.3967
data row 917439: value=0.3761
data row 708809: value=0.0700
data row 565558: value=0.3957
data row 299825: value=0.0899
data row 662632: value=0.8930
data row 31084: value=0.2854
data row 560709: value=0.9713
data row 648735: value=0.0778
data row 670688: value=0.0209
data row 972830: value=0.3703
data row 766466: value=0.1446
data row 937094: value=0.8211
data row 88282: value=0.2425
data row 834667: value=0.5192
data row 427272: value=0.2677
data row 529868: value=0.0143
data row 640736: value=0.9573
data row 171835: value=0.8253
data row 658283: value=0.5523
data row 269026: value=0.2240
data row 319070: value=0.2158
data row 497475: value=0.0981
data row 69062: value=0.2592
data row 272062: value=0.9984
data row 26584: value=0.3964
data row 956054: value=0.7585
data row 151979: value=0.8244
data row 164388: value=0.9587
data row 69337: value=0.9564
data row 415028: value=0.7504
data row 876224: value=0.7791
data row 330141: value=0.0480
data row 697923: value=0.0463
data row 384659: value=0.3665
data row 64474: value=0.0927
data row 237128: value=0.9437
data row 84957: value=0.6738
data row 949089: value=0.6098
data row 834463: value=0.2395
data row 592266: value=0.5866
data row 717773: value=0.8695
data row 742708: value=0.0580
data row 69431: value=0.2205
data row 662695: value=0.1290
data row 596399: value=0.2785
data row 388192: value=0.7520
data row 935823: value=0.2033
data row 860996: value=0.7365
data row 189566: value=0.2518
data row 340589: value=0.9302
data row 178167: value=0.4260
data row 602803: value=0.2187
data row 434577: value=0.0384
data row 730259: value=0.2110
data row 369443: value=0.2974
data row 534372: value=0.1710
data row 130425: value=0.2043
data row 543780: value=0.3837
data row 677131: value=0.1003
data row 149520: value=0.3966
data row 783535: value=0.7460
data row 463308: value=0.1404
data row 304010: value=0.5895
data row 842809: value=0.1634
data row 131021: value=0.3340
data row 760878: value=0.2735
data row 843233: value=0.6682
data row 534986: value=0.0365
data row 763917: value=0.6029
data row 359533: value=0.3226
data row 212172: value=0.3812
data row 476532: value=0.5501
data row 204389: value=0.1321
data row 162891: value=0.3068
data row 193111: value=0.4151
data row 938596: value=0.0629
data row 33246: value=0.8471
data row 340593: value=0.2191
data row 613449: value=0.9001
data row 412508: value=0.1114
data row 65291: value=0.2047
data row 283556: value=0.1099
data row 97703: value=0.2031
data row 663115: value=0.3553
data row 901950: value=0.7821
data row 242511: value=0.6938
data row 505127: value=0.3056
data row 377027: value=0.8608
data row 258431: value=0.7032
data row 492296: value=0.1523
data row 665670: value=0.2572
data row 220930: value=0.9834
data row 259784: value=0.5119
data row 935962: value=0.2857
data row 128447: value=0.4861
data row 340912: value=0.9776
data row 588057: value=0.5926
data row 60210: value=0.0531
data row 722616: value=0.6398
data row 230274: value=0.7622
data row 515586: value=0.6517
data row 70728: value=0.7674
data row 616660: value=0.1865
data row 828578: value=0.5414
data row 223329: value=0.6547
data row 756039: value=0.6797
data row 683217: value=0.1592
data row 167567: value=0.7092
data row 286399: value=0.9005
data row 165914: value=0.0571
data row 870905: value=0.3085
data row 73685: value=0.8722
data row 578594: value=0.3978
data row 981884: value=0.9266
data row 281407: value=0.9639
data row 828018: value=0.8842
data row 857260: value=0.5559
data row 77705: value=0.5595
data row 420966: value=0.5443
data row 240694: value=0.9943
data row 774165: value=0.2323
data row 27893: value=0.2094
data row 792079: value=0.3633
data row 996022: value=0.0670
data row 519343: value=0.8922
data row 744211: value=0.3763
data row 819760: value=0.0420
data row 739598: value=0.6842
data row 418794: value=0.7255
data row 784123: value=0.3925
data row 459220: value=0.1537
data row 941652: value=0.7886
data row 768222: value=0.6258
data row 805357: value=0.2330
data row 709703: value=0.8278
data row 659593: value=0.4937
data row 898510: value=0.5710
data row 53398: value=0.4733
data row 785642: value=0.9129
data row 746404: value=0.7331
data row 109310: value=0.7811
data row 672251: value=0.0208
data row 506822: value=0.0385
data row 97492: value=0.1208
data row 55379: value=0.0789
data row 396408: value=0.5798
data row 900462: value=0.3233
data row 141266: value=0.6085
data row 741820: value=0.6934
data row 257653: value=0.1382
data row 555176: value=0.7263
data row 548199: value=0.5673
data row 505777: value=0.9899
data row 286888: value=0.3554
data row 641457: value=0.7115
data row 656735: value=0.7390
data row 255857: value=0.9498
data row 570811: value=0.6794
data row 421988: value=0.5919
data row 82646: value=0.3923
data row 584651: value=0.1822
data row 702561: value=0.6052
data row 975004: value=0.3467
data row 602262: value=0.4136
data row 715731: value=0.9897
data row 110325: value=0.1995
data row 908635: value=0.1584
data row 403748: value=0.6637
data row 287363: value=0.7672
data row 10125: value=0.3996
data row 969353: value=0.9613
data row 910088: value=0.7133
data row 202942: value=0.1514
data row 442705: value=0.9922
data row 300763: value=0.4005
data row 620519: value=0.2246
data row 969537: value=0.4489
data row 255289: value=0.0759
data row 51012: value=0.1016
data row 871259: value=0.1654
data row 885733: value=0.1180
data row 542784: value=0.1793
data row 764708: value=0.2841
data row 108574: value=0.9882
data row 769448: value=0.4228
data row 541732: value=0.5376
data row 59747: value=0.8574
data row 626432: value=0.6136
data row 889368: value=0.4237
data row 798577: value=0.3643
data row 823258: value=0.8513
data row 431338: value=0.4309
data row 465398: value=0.8985
data row 49570: value=0.0776
data row 339773: value=0.7181
data row 91249: value=0.3593
data row 773537: value=0.2201
data row 730784: value=0.5097
data row 55838: value=0.6652
data row 696217: value=0.8063
data row 201225: value=0.9336
data row 906211: value=0.9675
data row 859872: value=0.7058
data row 334507: value=0.3212
data row 139019: value=0.7507
data row 428053: value=0.5438
data row 222347: value=0.4177
data row 836794: value=0.7125
data row 311820: value=0.5607
data row 186664: value=0.4614
data row 635762: value=0.7271
data row 660707: value=0.4303
data row 337935: value=0.3118
data row 98020: value=0.3847
data row 823540: value=0.0571
data row 969487: value=0.8573
data row 743983: value=0.9839
data row 158895: value=0.0948
data row 154636: value=0.4667
data row 973891: value=0.4443
data row 951973: value=0.8430
data row 111286: value=0.9493
data row 17212: value=0.0263
data row 53152: value=0.7156
data row 351092: value=0.3376
data row 921873: value=0.1834
data row 877011: value=0.6940
data row 920983: value=0.4838
data row 936255: value=0.1086
data row 882399: value=0.9286
data row 772434: value=0.2861
data row 739963: value=0.3809
data row 450937: value=0.8816
data row 22328: value=0.3281
data row 445527: value=0.6063
data row 548031: value=0.9506
data row 65140: value=0.4977
data row 758499: value=0.2699
data row 513132: value=0.9954
data row 358978: value=0.2115
data row 173262: value=0.0522
data row 894106: value=0.5303
data row 53852: value=0.2581
data row 48845: value=0.8327
data row 395649: value=0.0924
data row 119030: value=0.8398
data row 754551: value=0.7356
data row 241587: value=0.8187
data row 659307: value=0.1223
data row 239233: value=0.6886
data row 13921: value=0.2112
data row 838518: value=0.4406
data row 800197: value=0.6842
data row 721748: value=0.3824
data row 124709: value=0.1916
data row 268944: value=0.5942
data row 444678: value=0.5145
data row 608982: value=0.0730
data row 72128: value=0.8803
data row 852652: value=0.1762
data row 365803: value=0.2050
data row 589708: value=0.8386
data row 19840: value=0.6762
data row 587485: value=0.0790
data row 705108: value=0.7150
data row 590020: value=0.1299
data row 246600: value=0.8121
data row 503385: value=0.0122
data row 109223: value=0.0225
data row 779971: value=0.0488
data row 130126: value=0.2721
data row 973657: value=0.4297
data row 364453: value=0.9569
data row 323814: value=0.6089
data row 271023: value=0.3341
data row 714225: value=0.9067
data row 81542: value=0.8139
data row 773086: value=0.0893
data row 227896: value=0.0296
data row 614021: value=0.1488
data row 130287: value=0.6335
data row 330412: value=0.9302
data row 853553: value=0.4309
data row 22002: value=0.2520
data row 267637: value=0.9629
data row 435298: value=0.5076
data row 874720: value=0.4480
data row 578399: value=0.0240
data row 578602: value=0.7868
data row 351485: value=0.3306
data row 229906: value=0.9346
data row 817938: value=0.4205
data row 725141: value=0.1406
data row 539170: value=0.3165
data row 386220: value=0.9281
data row 235338: value=0.7739
data row 679709: value=0.8511
data row 119836: value=0.2670
data row 797879: value=0.9013
data row 302456: value=0.5056
data row 56256: value=0.1203
data row 148423: value=0.4828
data row 561485: value=0.4516
data row 298511: value=0.0388
data row 872066: value=0.0213
data row 530282: value=0.0729
data row 290562: value=0.8946
data row 358240: value=0.0552
data row 678358: value=0.7558
data row 70742: value=0.8014
data row 513863: value=0.9744
data row 107797: value=0.0935
data row 643311: value=0.3101
data row 815505: value=0.0830
data row 760076: value=0.2324
data row 769876: value=0.2436
data row 364846: value=0.8694
data row 48812: value=0.2608
data row 931666: value=0.2924
data row 625519: value=0.3306
data row 619144: value=0.1577
data row 469292: value=0.5317
data row 885571: value=0.2278
data row 690852: value=0.3040
data row 489582: value=0.8439
data row 731605: value=0.3390
data row 409534: value=0.0316
data row 930607: value=0.0484
data row 861700: value=0.6731
data row 549768: value=0.7423
data row 882324: value=0.4996
data row 541152: value=0.8251
data row 826469: value=0.7632
data row 588295: value=0.6516
data row 522142: value=0.5782
data row 972887: value=0.1967
data row 866128: value=0.6312
data row 577334: value=0.7119
data row 110021: value=0.0586
data row 484353: value=0.1721
data row 127245: value=0.4661
data row 257892: value=0.1775
data row 720352: value=0.0300
data row 477606: value=0.7100
data row 281403: value=0.7872
data row 685283: value=0.4304
data row 188429: value=0.8370
data row 11870: value=0.7894
data row 833214: value=0.9611
data row 596879: value=0.6811
data row 58530: value=0.3649
data row 114348: value=0.2142
data row 348745: value=0.8673
data row 650153: value=0.9401
data row 490504: value=0.1733
data row 827103: value=0.4606
data row 452395: value=0.7500
data row 585834: value=0.5082
data row 411764: value=0.7016
data row 538577: value=0.5431
data row 665006: value=0.9098
data row 973643: value=0.2314
data row 637172: value=0.3740
data row 942908: value=0.7455
data row 701407: value=0.1600
data row 484187: value=0.9914
data row 379806: value=0.6608
data row 433983: value=0.6680
data row 638054: value=0.2595
data row 125652: value=0.1015
data row 547363: value=0.3200
data row 387791: value=0.7497
data row 39138: value=0.3122
data row 644479: value=0.5015
data row 434461: value=0.9281
data row 910706: value=0.0124
data row 233855: value=0.1472
data row 839793: value=0.5333
data row 813900: value=0.3460
data row 786579: value=0.1298
data row 85892: value=0.6027
data row 44880: value=0.8904
data row 423225: value=0.7942
data row 918242: value=0.6083
data row 409785: value=0.7791
data row 986609: value=0.1395
data row 145820: value=0.2631
data row 708983: value=0.0408
data row 659692: value=0.0504
data row 161369: value=0.4633
data row 808746: value=0.4395
data row 102236: value=0.0690
data row 488679: value=0.6903
data row 863722: value=0.4945
data row 582978: value=0.6477
data row 122952: value=0.2535
data row 355771: value=0.2783
data row 52171: value=0.2176
data row 528177: value=0.5421
data row 461418: value=0.2141
data row 608026: value=0.8272
data row 221551: value=0.4819
data row 420105: value=0.7004
data row 385722: value=0.6580
data row 899734: value=0.6159
data row 897800: value=0.2806
data row 291371: value=0.1011
data row 495132: value=0.0454
data row 752838: value=0.4492
data row 756110: value=0.0536
data row 884393: value=0.5646
data row 835165: value=0.2102
data row 284107: value=0.3710
data row 252942: value=0.5591
data row 333252: value=0.8769
data row 225061: value=0.8274
data row 396426: value=0.8675
data row 695411: value=0.2881
data row 670731: value=0.8566
data row 221863: value=0.3020
data row 482648: value=0.1869
data row 18547: value=0.4248
data row 949229: value=0.8199
data row 877008: value=0.3247
data row 759698: value=0.3712
data row 888417: value=0.0412
data row 714369: value=0.3835
data row 445675: value=0.3602
data row 370063: value=0.4227
data row 704591: value=0.7904
data row 307850: value=0.0791
data row 731034: value=0.4303
data row 930753: value=0.8057
data row 959854: value=0.8417
data row 459635: value=0.7033
data row 594136: value=0.4065
data row 497298: value=0.0385
data row 603882: value=0.2607
data row 562135: value=0.6948
data row 342910: value=0.6556
data row 656244: value=0.6843
data row 109861: value=0.0781
data row 484725: value=0.2285
data row 90037: value=0.7554
data row 835390: value=0.5683
data row 691783: value=0.4398
data row 13772: value=0.2952
data row 393486: value=0.7489
data row 727420: value=0.0460
data row 658444: value=0.8645
data row 146652: value=0.6962
data row 241730: value=0.1272
data row 643596: value=0.8882
data row 296048: value=0.9967
data row 518142: value=0.9645
data row 110335: value=0.0594
data row 275178: value=0.1617
data row 409746: value=0.3812
data row 881300: value=0.9277
data row 350334: value=0.0915
data row 877714: value=0.4454
data row 145805: value=0.6851
data row 547247: value=0.7919
data row 391172: value=0.7892
data row 834830: value=0.2023
data row 94399: value=0.7353
data row 22766: value=0.1837
data row 828543: value=0.1543
data row 715501: value=0.9400
data row 326914: value=0.5832
data row 883767: value=0.8243
data row 359641: value=0.5135
data row 530444: value=0.4309
data row 750876: value=0.3455
data row 189713: value=0.7627
data row 641752: value=0.8253
data row 581778: value=0.2982
data row 699382: value=0.7326
data row 379331: value=0.3908
data row 901453: value=0.0362
data row 589899: value=0.6981
data row 496322: value=0.2683
data row 365212: value=0.3004
data row 40318: value=0.3402
data row 703236: value=0.5611
data row 126911: value=0.0920
data row 661515: value=0.9633
data row 461022: value=0.1797
data row 798938: value=0.9951
data row 91936: value=0.9189
data row 751018: value=0.8673
data row 455335: value=0.8044
data row 231849: value=0.1927
data row 574531: value=0.3561
data row 785572: value=0.5554
data row 798264: value=0.2613
data row 488755: value=0.0292
data row 236784: value=0.3129
data row 96157: value=0.9394
data row 688693: value=0.8613
data row 499977: value=0.1095
data row 659923: value=0.5321
data row 535527: value=0.7807
data row 707299: value=0.5921
data row 103354: value=0.5859
data row 892016: value=0.4482
data row 809335: value=0.9064
data row 364596: value=0.2700
data row 384305: value=0.0253
data row 160958: value=0.7392
data row 478359: value=0.5942
data row 869867: value=0.9346
data row 832846: value=0.6800
data row 362665: value=0.9367
data row 327762: value=0.2590
data row 337902: value=0.0127
data row 777513: value=0.1206
data row 870379: value=0.3348
data row 772609: value=0.1926
data row 341322: value=0.4404
data row 930221: value=0.0853
data row 52102: value=0.0354
data row 954605: value=0.9312
data row 966309: value=0.2549
data row 137347: value=0.8721
data row 421805: value=0.1378
data row 720493: value=0.2156
data row 485000: value=0.6681
data row 742558: value=0.0397
data row 258526: value=0.2758
data row 712602: value=0.6618
data row 876676: value=0.1713
data row 882362: value=0.7141
data row 81396: value=0.0316
data row 310056: value=0.2419
data row 924548: value=0.6037
data row 356705: value=0.1105
data row 509609: value=0.7690
data row 479321: value=0.0565
data row 144276: value=0.1082
data row 520449: value=0.2416
data row 79700: value=0.4161
data row 843792: value=0.7826
data row 475563: value=0.7715
data row 778920: value=0.0731
data row 467688: value=0.6453
data row 141275: value=0.2277
data row 387817: value=0.8150
data row 848794: value=0.5132
data row 857093: value=0.8647
data row 165733: value=0.2330
data row 550639: value=0.7727
data row 226318: value=0.4682
data row 493060: value=0.8186
data row 274827: value=0.8120
data row 802764: value=0.7303
data row 76870: value=0.8760
data row 358414: value=0.0859
data row 606451: value=0.7926
data row 616190: value=0.0906
data row 928763: value=0.0221
data row 94191: value=0.5423
data row 596543: value=0.7260
data row 334797: value=0.4836
data row 997922: value=0.4855
data row 107471: value=0.0566
data row 468177: value=0.9173
data row 740672: value=0.2310
data row 401775: value=0.0170
data row 158771: value=0.7397
data row 959224: value=0.6869
data row 150781: value=0.7606
data row 88729: value=0.6264
data row 580117: value=0.7108
data row 862502: value=0.4608
data row 984925: value=0.3798
data row 683465: value=0.4218
data row 365692: value=0.5782
data row 165967: value=0.3587
data row 69844: value=0.8717
data row 312403: value=0.4122
data row 168836: value=0.7692
data row 263064: value=0.8512
data row 499196: value=0.5440
data row 608965: value=0.4331
data row 313314: value=0.5009
data row 557104: value=0.8921
data row 556194: value=0.0015
data row 139080: value=0.1369
data row 691878: value=0.2771
data row 874855: value=0.6952
data row 906669: value=0.8596
data row 279279: value=0.8402
data row 316283: value=0.9922
data row 752621: value=0.0697
data row 492580: value=0.2701
data row 236886: value=0.5964
data row 771034: value=0.8139
data row 693276: value=0.5823
data row 779780: value=0.8685
data row 296352: value=0.1922
data row 464527: value=0.4467
data row 701525: value=0.1374
data row 126299: value=0.3609
data row 759478: value=0.8237
data row 472802: value=0.7089
data row 456762: value=0.1606
data row 231752: value=0.5839
data row 33571: value=0.9024
data row 811122: value=0.6088
data row 801186: value=0.9720
data row 246032: value=0.6007
data row 651321: value=0.3147
data row 82408: value=0.0653
data row 649649: value=0.6822
data row 961403: value=0.3398
data row 581260: value=0.6110
data row 993706: value=0.1678
data row 445700: value=0.4965
data row 365492: value=0.1623
data row 216413: value=0.7483
data row 300582: value=0.7873
data row 325851: value=0.3156
data row 754449: value=0.8702
data row 703079: value=0.4703
data row 887035: value=0.0202
data row 38186: value=0.2116
data row 801300: value=0.3886
data row 624860: value=0.6150
data row 176278: value=0.5840
data row 428351: value=0.9151
data row 746175: value=0.1308
data row 142641: value=0.8578
data row 545653: value=0.3407
data row 338583: value=0.3061
data row 150742: value=0.6750
data row 479056: value=0.1751
data row 488375: value=0.3594
data row 598371: value=0.7730
data row 726409: value=0.6162
data row 459311: value=0.6187
data row 147791: value=0.8130
data row 800861: value=0.4400
data row 420012: value=0.3261
data row 133720: value=0.5338
data row 935280: value=0.9643
data row 207829: value=0.7482
data row 825002: value=0.7446
data row 309132: value=0.1178
data row 758519: value=0.9699
data row 892956: value=0.9460
data row 10345: value=0.1884
data row 197319: value=0.1878
data row 473667: value=0.8143
data row 736374: value=0.2639
data row 414103: value=0.6184
data row 727769: value=0.6609
data row 568357: value=0.8141
data row 650161: value=0.7723
data row 66001: value=0.2318
data row 852172: value=0.8971
data row 318307: value=0.3044
data row 381088: value=0.8699
data row 92625: value=0.7151
data row 404887: value=0.0080
data row 478830: value=0.0026
data row 439791: value=0.4857
data row 192012: value=0.1306
data row 737199: value=0.9242
data row 52360: value=0.9292
data row 427691: value=0.6140
data row 96880: value=0.8925
data row 260891: value=0.4010
data row 286433: value=0.0417
data row 269345: value=0.5908
data row 622748: value=0.8170
data row 338091: value=0.2195
data row 722367: value=0.9086
data row 223423: value=0.5824
data row 863822: value=0.6989
data row 719694: value=0.3480
data row 904978: value=0.1147
data row 444649: value=0.0075
data row 797189: value=0.0331
data row 561921: value=0.8718
data row 487421: value=0.2838
data row 660712: value=0.2947
data row 380709: value=0.8134
data row 341741: value=0.9833
data row 317378: value=0.9381
data row 929474: value=0.6810
data row 842027: value=0.6697
data row 719948: value=0.4913
data row 806185: value=0.1926
data row 202095: value=0.4626
data row 999945: value=0.3120
data row 889245: value=0.6034
data row 494614: value=0.6404
data row 679239: value=0.1596
data row 634566: value=0.2199
data row 678234: value=0.0128
data row 971714: value=0.9631
data row 230047: value=0.8324
data row 422570: value=0.3390
data row 734822: value=0.5970
data row 159429: value=0.5513
data row 502033: value=0.4109
data row 451685: value=0.7419
data row 728245: value=0.7093
data row 156803: value=0.6739
data row 444725: value=0.5791
data row 323407: value=0.6083
data row 310972: value=0.3344
data row 419756: value=0.7967
data row 384482: value=0.0787
data row 706388: value=0.4547
data row 400441: value=0.2122
data row 685118: value=0.2383
data row 423050: value=0.7712
data row 174213: value=0.7654
data row 537594: value=0.0912
data row 218783: value=0.9206
data row 841269: value=0.9102
data row 669950: value=0.0396
data row 689198: value=0.5455
data row 655486: value=0.3908
data row 909062: value=0.4237
data row 489835: value=0.8099
data row 711083: value=0.7576
data row 394653: value=0.6475
data row 897657: value=0.9067
data row 926812: value=0.6087
data row 230267: value=0.5984
data row 142428: value=0.6254
data row 794437: value=0.7452
data row 120181: value=0.4701
data row 303128: value=0.7600
data row 919709: value=0.7296
data row 495227: value=0.3209
data row 975708: value=0.2624
data row 17051: value=0.5697
data row 112475: value=0.6305
data row 343632: value=0.5512
data row 159372: value=0.3375
data row 136707: value=0.9062
data row 351430: value=0.3793
data row 299119: value=0.2796
data row 491111: value=0.3501
data row 143550: value=0.9304
data row 651793: value=0.8121
data row 796240: value=0.2312
data row 363333: value=0.5531
data row 248716: value=0.6231
data row 352991: value=0.8646
data row 151669: value=0.3326
data row 77222: value=0.9906
data row 696906: value=0.4243
data row 988434: value=0.6167
data row 757157: value=0.1674
data row 420282: value=0.2988
data row 426417: value=0.7256
data row 41903: value=0.0643
data row 56355: value=0.9620
data row 165051: value=0.9228
data row 80639: value=0.2950
data row 881670: value=0.4461
data row 986469: value=0.8330
data row 670005: value=0.8442
data row 961864: value=0.4829
data row 974005: value=0.5231
data row 178648: value=0.8056
data row 612548: value=0.1273
data row 58487: value=0.3877
data row 256038: value=0.0946
data row 622294: value=0.1078
data row 279021: value=0.8251
data row 237082: value=0.8471
data row 134190: value=0.5097
data row 661957: value=0.4442
data row 695413: value=0.9664
data row 909572: value=0.8710
data row 856808: value=0.0732
data row 562638: value=0.7804
data row 729426: value=0.1474
data row 67502: value=0.0873
data row 626639: value=0.8130
data row 218333: value=0.9425
data row 969342: value=0.5946
data row 160399: value=0.8353
data row 109950: value=0.5184
data row 60168: value=0.8783
data row 669636: value=0.4813
data row 176597: value=0.6001
data row 158540: value=0.3579
data row 434282: value=0.1207
data row 416303: value=0.5463
data row 576238: value=0.2716
data row 91049: value=0.1439
data row 963775: value=0.1906
data row 382541: value=0.2850
data row 505991: value=0.6944
data row 617989: value=0.4035
data row 395515: value=0.3484
data row 644411: value=0.4020
data row 154395: value=0.4426
data row 248821: value=0.0687
data row 398888: value=0.6882
data row 915828: value=0.1684
data row 545910: value=0.3062
data row 673699: value=0.5926
data row 818965: value=0.5540
data row 127809: value=0.0196
data row 936087: value=0.4537
data row 912956: value=0.7958
data row 980937: value=0.3993
data row 250300: value=0.2818
data row 364697: value=0.4485
data row 403925: value=0.2807
data row 32397: value=0.2296
data row 220533: value=0.9223
data row 709508: value=0.8581
data row 29531: value=0.8701
data row 671128: value=0.4923
data row 698779: value=0.3069
data row 618879: value=0.2152
data row 577134: value=0.2685
data row 212754: value=0.3760
data row 274770: value=0.3726
data row 350487: value=0.0935
data row 156875: value=0.0074
data row 558807: value=0.0743
data row 733186: value=0.8822
data row 320736: value=0.0185
data row 544742: value=0.9923
data row 722878: value=0.3673
data row 865504: value=0.4837
data row 314719: value=0.4337
data row 731455: value=0.3401
data row 581820: value=0.6936
data row 698691: value=0.7476
data row 536612: value=0.7779
data row 607164: value=0.0927
data row 628137: value=0.4949
data row 274194: value=0.8077
data row 456608: value=0.0961
data row 897072: value=0.2788
data row 801292: value=0.9945
data row 911627: value=0.4240
data row 162423: value=0.2018
data row 706118: value=0.5312
data row 785041: value=0.7800
data row 700325: value=0.2062
data row 840492: value=0.5502
data row 772367: value=0.7894
data row 266719: value=0.0857
data row 592020: value=0.7841
data row 810130: value=0.0460
data row 58861: value=0.3909
data row 67238: value=0.0714
data row 790173: value=0.1872
data row 992005: value=0.7229
data row 765702: value=0.9643
data row 963731: value=0.7557
data row 174413: value=0.4829
data row 963773: value=0.0581
data row 588911: value=0.3848
data row 296002: value=0.4908
data row 17819: value=0.9880
data row 735257: value=0.5169
data row 29322: value=0.9783
data row 783125: value=0.0526
data row 37044: value=0.1507
data row 726590: value=0.5809
data row 990249: value=0.4420
data row 390303: value=0.6150
data row 910463: value=0.9730
data row 471639: value=0.0268
data row 702981: value=0.1561
data row 406088: value=0.9961
data row 504756: value=0.0791
data row 758122: value=0.1926
data row 360844: value=0.7997
data row 492143: value=0.9237
data row 325656: value=0.2236
data row 511646: value=0.9838
data row 466253: value=0.4204
data row 292622: value=0.4399
data row 331177: value=0.6009
data row 11500: value=0.0851
