#!/usr/bin/env python3
#
#
#

import pywikibot
# ---
# start of newdesc.py file
from wd_API import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
taop = {
    "Q2680952": {"ar": "روتردام", "en": "Rotterdam"},  # 5191
    "Q9899": {"ar": "أمستردام", "en": "Amsterdam"},  # 4513
    "Q803": {"ar": "أوترخت", "en": "Utrecht"},  # 3057
    "Q36600": {"ar": "لاهاي", "en": "The Hague"},  # 2958
    "Q9832": {"ar": "آيندهوفن", "en": "Eindhoven"},  # 2610
    "Q26430": {"ar": "تلبرغ", "en": "Tilburg"},  # 2260
    "Q9822": {"ar": "بريدا", "en": "Breda"},  # 2068
    "Q83178": {"ar": "ألميرا", "en": "Almere"},  # 2006
    "Q992": {"ar": "آمرسفورت", "en": "Amersfoort"},  # 1943
    # "Q9807": {"ar":"'s-Hertogenbosch", "en":"'s-Hertogenbosch"},#1926
    "Q1473276": {"ar": "سودفيست- فريسلان", "en": "Súdwest-Fryslân"},  # 1858
    "Q1310": {"ar": "أرنهيم", "en": "Arnhem"},  # 1776
    "Q10002": {"ar": "أنسخديه", "en": "Enschede"},  # 1666
    "Q101918": {"ar": "آبلدورن", "en": "Apeldoorn"},  # 1654
    "Q9978": {"ar": "زانستاد", "en": "Zaanstad"},  # 1651
    "Q9920": {"ar": "هارلم", "en": "Haarlem"},  # 1566
    "Q1309": {"ar": "ماستريخت", "en": "Maastricht"},  # 1558
    "Q9781": {"ar": "سيتارد- خيلين", "en": "Sittard-Geleen"},  # 1532
    "Q43631": {"ar": "لايدن", "en": "Leiden"},  # 1530
    "Q793": {"ar": "زفوله", "en": "Zwolle"},  # 1474
    "Q892526": {"ar": "خرونينغن", "en": "Groningen"},  # 1473
    "Q26556": {"ar": "فيستلاند", "en": "Westland"},  # 1473
}

xsxsxsx = {
    "Q10001": {"ar": "ديفينتر", "en": "Deventer"},  # 1444
    "Q9777": {"ar": "فينلو", "en": "Venlo"},  # 1441
    "Q26555": {"ar": "إيده", "en": "Ede"},  # 1404
    "Q47887": {"ar": "نايميخن", "en": "Nijmegen"},  # 1402
    "Q972": {"ar": "ألكمار", "en": "Alkmaar"},  # 1356
    "Q9859": {"ar": "أوس", "en": "Oss"},  # 1353
    "Q14853527": {"ar": "نيسافارد", "en": "Nissewaard"},  # 1326
    "Q14641": {"ar": "إيمين", "en": "Emmen"},  # 1312
    "Q2311189": {"ar": "ليوواردن", "en": "Leeuwarden"},  # 1283
    "Q9924": {"ar": "هارلمرمير", "en": "Haarlemmermeer"},  # 1269
    "Q9844": {"ar": "هيلموند", "en": "Helmond"},  # 1258
    "Q10081": {"ar": "تيرنوزن", "en": "Terneuzen"},  # 1237
    "Q26432": {"ar": "زوترمير", "en": "Zoetermeer"},  # 1205
    "Q9799": {"ar": "هيلرن", "en": "Heerlen"},  # 1135
    "Q10006": {"ar": "هينجيلو", "en": "Hengelo"},  # 1099
    "Q988": {"ar": "الميلو", "en": "Almelo"},  # 1079
    "Q26421": {"ar": "دوردريخت", "en": "Dordrecht"},  # 1068
    "Q47104": {"ar": "بيركيلاند", "en": "Berkelland"},  # 1066
    "Q3916626": {"ar": "هاردنبيرخ", "en": "Hardenberg"},  # 1047
    "Q933459": {"ar": "خوريه- أوفرفلاكيه", "en": "Goeree-Overflakkee"},  # 1045
    "Q10079": {"ar": "سخاون- داوفللاند", "en": "Schouwen-Duiveland"},  # 1018
    "Q690": {"ar": "دلفت", "en": "Delft"},  # 1012
    "Q9814": {"ar": "بيرخن أوب زووم", "en": "Bergen op Zoom"},  # 1005
    "Q166065": {"ar": "ليليستاد", "en": "Lelystad"},  # 970
    "Q10050": {"ar": "نيواخاين", "en": "Nieuwegein"},  # 946
    "Q84125": {"ar": "خاودا", "en": "Gouda"},  # 917
    "Q747999": {"ar": "برونكهورست", "en": "Bronckhorst"},  # 905
    "Q9774": {"ar": "فيرت", "en": "Weert"},  # 905
    "Q69262": {"ar": "نوردأوست بولدر", "en": "Noordoostpolder"},  # 891
    "Q10080": {"ar": "سلاوس", "en": "Sluis"},  # 877
    "Q9793": {"ar": "لودال", "en": "Leudal"},  # 870
    "Q9861": {"ar": "روسيندال", "en": "Roosendaal"},  # 866
    "Q9785": {"ar": "بيل آن ماس", "en": "Peel en Maas"},  # 852
    "Q8167972": {"ar": "رورموند", "en": "Roermond"},  # 839
    "Q15991891": {"ar": "كرمبنيرفارد", "en": "Krimpenerwaard"},  # 833
    "Q9797": {"ar": "هورست آن دي ماس", "en": "Horst aan de Maas"},  # 832
    "Q9936": {"ar": "هولاندز كرون", "en": "Hollands Kroon"},  # 829
    "Q10022": {"ar": "ستينفايكرلاند", "en": "Steenwijkerland"},  # 824
    "Q9775": {"ar": "فينراي", "en": "Venray"},  # 822
    "Q9970": {"ar": "فيلسن", "en": "Velsen"},  # 818
    "Q213246": {"ar": "ألفن آن دن راين", "en": "Alphen aan den Rijn"},  # 817
    "Q1144739": {"ar": "لانسينجيرلاند", "en": "Lansingerland"},  # 805
    "Q798": {"ar": "أسن", "en": "Assen"},  # 801
    "Q145845": {"ar": "دوتينخيم", "en": "Doetinchem"},  # 800
    "Q10076": {"ar": "ميديلبورخ", "en": "Middelburg"},  # 800
    "Q60453": {"ar": "كوفردن", "en": "Coevorden"},  # 784
    "Q9996": {"ar": "هوف فان تفنته", "en": "Hof van Twente"},  # 783
    "Q600871": {"ar": "أوفربيتوا", "en": "Overbetuwe"},  # 782
    "Q208012": {"ar": "هوخيفين", "en": "Hoogeveen"},  # 777
    "Q9955": {"ar": "سخاخن", "en": "Schagen"},  # 768
    "Q932031": {"ar": "آودا آيسلستريك", "en": "Oude IJsselstreek"},  # 767
    "Q574558": {"ar": "هيرينفين", "en": "Heerenveen"},  # 762
    "Q9858": {"ar": "أوسترهاوت", "en": "Oosterhout"},  # 761
    "Q204709": {"ar": "سخيدام", "en": "Schiedam"},  # 754
    "Q10043": {"ar": "أوترختسه هوفلروخ", "en": "Utrechtse Heuvelrug"},  # 754
    "Q9845": {"ar": "هوسدن", "en": "Heusden"},  # 753
    "Q745038": {"ar": "فالفايك", "en": "Waalwijk"},  # 745
    "Q932058": {"ar": "لوخيم", "en": "Lochem"},  # 740
    "Q851299": {"ar": "دونجراديل", "en": "Dongeradeel"},  # 730
    "Q9898": {"ar": "أمستلفين", "en": "Amstelveen"},  # 723
    "Q9854": {"ar": "موردايك", "en": "Moerdijk"},  # 722
    "Q164098": {"ar": "بارنيفيلد", "en": "Barneveld"},  # 717
    "Q9954": {"ar": "بورميراند", "en": "Purmerend"},  # 713
    "Q10072": {"ar": "خوس", "en": "Goes"},  # 710
    "Q1347872": {"ar": "أولدامبت", "en": "Oldambt"},  # 706
    "Q9999": {"ar": "دينكللاند", "en": "Dinkelland"},  # 705
    "Q835083": {"ar": "نوردنفيلد", "en": "Noordenveld"},  # 704
    "Q952939": {"ar": "لينجافارد", "en": "Lingewaard"},  # 701
    "Q10073": {"ar": "هولست", "en": "Hulst"},  # 701
    "Q5128": {"ar": "فوردن", "en": "Woerden"},  # 698
    "Q952963": {"ar": "مونتفيرلاند", "en": "Montferland"},  # 696
    "Q9934": {"ar": "هيلفرسوم", "en": "Hilversum"},  # 691
    "Q208764": {"ar": "كاتفايك", "en": "Katwijk"},  # 690
    "Q10019": {"ar": "رالته", "en": "Raalte"},  # 683
    "Q23814173": {"ar": "كامبن", "en": "Kampen"},  # 682
    "Q10083": {"ar": "فيراه", "en": "Veere"},  # 680
    "Q507065": {"ar": "سمولينجالاند", "en": "Smallingerland"},  # 665
    "Q281768": {"ar": "باين آكر- نوتدورب", "en": "Pijnacker-Nootdorp"},  # 664
    "Q1840": {"ar": "فينندال", "en": "Veenendaal"},  # 663
    "Q18335889": {"ar": "خويسه ميرين", "en": "Gooise Meren"},  # 655
    "Q9947": {"ar": "ميديمبليك", "en": "Medemblik"},  # 654
    "Q9828": {"ar": "دورنه", "en": "Deurne"},  # 651
    "Q9930": {"ar": "هيرهوخوفارد", "en": "Heerhugowaard"},  # 649
    "Q9874": {"ar": "فيخل", "en": "Veghel"},  # 647
    "Q835125": {"ar": "ميدن-درنته", "en": "Midden-Drenthe"},  # 644
    "Q210007": {"ar": "فلاردينجن", "en": "Vlaardingen"},  # 638
    "Q840457": {"ar": "تينالو", "en": "Tynaarlo"},  # 638
    "Q1147580": {"ar": "أوست خيلره", "en": "Oost Gelre"},  # 636
    "Q238396": {"ar": "إيبه", "en": "Epe"},  # 636
    "Q112675": {"ar": "لايتسيندام- فوربورخ", "en": "Leidschendam-Voorburg"},  # 635
    "Q10044": {"ar": "هاوتن", "en": "Houten"},  # 633
    "Q10071": {"ar": "بورسله", "en": "Borsele"},  # 632
    "Q73221": {"ar": "تيل", "en": "Tiel"},  # 630
    "Q10084": {"ar": "فلسنكن", "en": "Vlissingen"},  # 624
    "Q10082": {"ar": "تولين", "en": "Tholen"},  # 621
    "Q244692": {"ar": "زويندريخت", "en": "Zwijndrecht"},  # 620
    "Q9875": {"ar": "فيلدهوفن", "en": "Veldhoven"},  # 612
    "Q9836": {"ar": "خيميرت- باكل", "en": "Gemert-Bakel"},  # 611
    "Q15858232": {"ar": "زوتفن", "en": "Zutphen"},  # 607
    "Q328087": {"ar": "درونتن", "en": "Dronten"},  # 607
    "Q58931": {"ar": "هاردرفايك", "en": "Harderwijk"},  # 605
    "Q9815": {"ar": "بيرنهيزه", "en": "Bernheze"},  # 600
    "Q10023": {"ar": "توبيرخن", "en": "Tubbergen"},  # 599
    "Q73074": {"ar": "ستادسكانال", "en": "Stadskanaal"},  # 596
    "Q9802": {"ar": "إيخت- سوسترين", "en": "Echt-Susteren"},  # 594
    "Q9819": {"ar": "بوكسمير", "en": "Boxmeer"},  # 594
    "Q843899": {"ar": "ريدن", "en": "Rheden"},  # 589
    "Q73226": {"ar": "نايكيرك", "en": "Nijkerk"},  # 587
    "Q10042": {"ar": "ستيختسه فيخت", "en": "Stichtse Vecht"},  # 587
    "Q9938": {"ar": "هورن", "en": "Hoorn"},  # 583
    "Q9796": {"ar": "كيركراده", "en": "Kerkrade"},  # 578
    "Q204239": {"ar": "باريندريخت", "en": "Barendrecht"},  # 573
    "Q73061": {"ar": "بورين", "en": "Buren"},  # 572
    "Q9833": {"ar": "إيتن- لور", "en": "Etten-Leur"},  # 568
    "Q9872": {"ar": "أودن", "en": "Uden"},  # 561
    "Q18088965": {"ar": "بيرخ آن دال", "en": "Berg en Dal"},  # 558
    "Q9901": {"ar": "بيرخن", "en": "Bergen"},  # 555
    "Q300665": {"ar": "آ أن هونزه", "en": "Aa en Hunze"},  # 547
    "Q341024": {"ar": "أختكارسبيلن", "en": "Achtkarspelen"},  # 547
    "Q10036": {"ar": "دي رونده فينن", "en": "De Ronde Venen"},  # 547
    "Q9939": {"ar": "هاوزن", "en": "Huizen"},  # 546
    "Q9866": {"ar": "سينت ميخيليسخيستل", "en": "Sint-Michielsgestel"},  # 545
    "Q734860": {"ar": "كابيلا آن دن آيسل", "en": "Capelle aan den IJssel"},  # 544
    "Q10005": {"ar": "هيليندورن", "en": "Hellendoorn"},  # 544
    "Q826130": {"ar": "هيليفوتسلاوس", "en": "Hellevoetsluis"},  # 540
    "Q244327": {"ar": "خوريكوم", "en": "Gorinchem"},  # 539
    "Q10020": {"ar": "رايسن- هولتن", "en": "Rijssen-Holten"},  # 536
    "Q9841": {"ar": "هالدربيرخه", "en": "Halderberge"},  # 536
    "Q72974": {"ar": "فينترسفايك", "en": "Winterswijk"},  # 535
    "Q9910": {"ar": "كاستركوم", "en": "Castricum"},  # 535
    "Q9873": {"ar": "فالكنسفارد", "en": "Valkenswaard"},  # 533
    "Q9911": {"ar": "دن هيلدر", "en": "Den Helder"},  # 532
    "Q9792": {"ar": "ماسخاو", "en": "Maasgouw"},  # 531
    "Q9835": {"ar": "خيلدروب- ميرلو", "en": "Geldrop-Mierlo"},  # 531
    "Q1532373": {"ar": "زالتبومل", "en": "Zaltbommel"},  # 529
    "Q197050": {"ar": "زيفينار", "en": "Zevenaar"},  # 528
    "Q1368003": {"ar": "تايلنجن", "en": "Teylingen"},  # 526
    "Q9870": {"ar": "ستينبيرخن", "en": "Steenbergen"},  # 524
    "Q10056": {"ar": "زايست", "en": "Zeist"},  # 523
    "Q747920": {"ar": "فيسترفيلد", "en": "Westerveld"},  # 516
    "Q9795": {"ar": "لاندخراف", "en": "Landgraaf"},  # 514
    "Q9816": {"ar": "بيست، هولندا", "en": "Best"},  # 514
    "Q683658": {"ar": "فرانيكراديل", "en": "Franekeradeel"},  # 513
    "Q228673": {"ar": "زاودبلاس", "en": "Zuidplas"},  # 511
    "Q9998": {"ar": "دالفسن", "en": "Dalfsen"},  # 511
    # "Q225521": {"ar":"Skarsterlân", "en":"Skarsterlân"},#510
    "Q840632": {"ar": "أوبسترلاند", "en": "Opsterland"},  # 508
    # "Q840641": {"ar":"Boarnsterhim", "en":"Boarnsterhim"},#503
    "Q840636": {"ar": "تيتسياركستيراديل", "en": "Tytsjerksteradiel"},  # 500
    "Q10035": {"ar": "دي بيلت", "en": "De Bilt"},  # 499
    "Q863961": {"ar": "بيننيماس", "en": "Binnenmaas"},  # 498
    "Q322986": {"ar": "دلفزايل", "en": "Delfzijl"},  # 495
    "Q9821": {"ar": "بوكستل", "en": "Boxtel"},  # 491
    "Q904544": {"ar": "ماسدريل", "en": "Maasdriel"},  # 490
    "Q10016": {"ar": "أولدنزال", "en": "Oldenzaal"},  # 489
    "Q384772": {"ar": "فورست", "en": "Voorst"},  # 486
    "Q10045": {"ar": "آيسلستاين", "en": "IJsselstein"},  # 485
    "Q60425": {"ar": "ميبل", "en": "Meppel"},  # 482
    "Q835108": {"ar": "دي فولدن", "en": "De Wolden"},  # 473
    "Q9766": {"ar": "آيسدن- مارخراتن", "en": "Eijsden-Margraten"},  # 473
    "Q753913": {"ar": "فيستستيلينجفيرف", "en": "Weststellingwerf"},  # 469
    "Q275909": {"ar": "آلتن", "en": "Aalten"},  # 466
    "Q10078": {"ar": "رايميرسفال", "en": "Reimerswaal"},  # 464
    "Q9830": {"ar": "دريميلين", "en": "Drimmelen"},  # 463
    "Q889423": {"ar": "بوديخرافن-ريودايك", "en": "Bodegraven-Reeuwijk"},  # 462
    "Q10024": {"ar": "تفنتاراند", "en": "Twenterand"},  # 461
    "Q816699": {"ar": "كولمبورخ", "en": "Culemborg"},  # 460
    "Q1943433": {"ar": "مولنفارد", "en": "Molenwaard"},  # 457
    "Q9857": {"ar": "أويسترفايك", "en": "Oisterwijk"},  # 455
    "Q9880": {"ar": "فيركندام", "en": "Werkendam"},  # 455
    "Q9905": {"ar": "بيفيرفايك", "en": "Beverwijk"},  # 455
    "Q691725": {"ar": "رينكوم", "en": "Renkum"},  # 453
    "Q9784": {"ar": "روردالن", "en": "Roerdalen"},  # 451
    "Q9780": {"ar": "ستاين", "en": "Stein"},  # 448
    "Q10046": {"ar": "لوسدن", "en": "Leusden"},  # 446
    "Q171536": {"ar": "خيلدرمالسن", "en": "Geldermalsen"},  # 444
    "Q9823": {"ar": "كرانندونك", "en": "Cranendonck"},  # 444
    "Q259205": {"ar": "أوستستالينجفيرف", "en": "Ooststellingwerf"},  # 442
    "Q9829": {"ar": "دونجن", "en": "Dongen"},  # 441
    "Q9917": {"ar": "إدام- فولندام", "en": "Edam-Volendam"},  # 435
    "Q9944": {"ar": "لانجادايك", "en": "Langedijk"},  # 435
    "Q72981": {"ar": "فايخن", "en": "Wijchen"},  # 432
    "Q10018": {"ar": "أومين", "en": "Ommen"},  # 426
    "Q9827": {"ar": "كاوك", "en": "Cuijk"},  # 425
    "Q835118": {"ar": "بورخر- أودورن", "en": "Borger-Odoorn"},  # 424
    "Q948866": {"ar": "نيوكوب", "en": "Nieuwkoop"},  # 423
    "Q10003": {"ar": "هاكسبيرخن", "en": "Haaksbergen"},  # 422
    "Q613989": {"ar": "داوفن", "en": "Duiven"},  # 421
    "Q9855": {"ar": "نونن، خيرفن آن نيدرفيتن", "en": "Nuenen, Gerwen en Nederwetten"},  # 421
    "Q9848": {"ar": "لاربيك", "en": "Laarbeek"},  # 419
    "Q210234": {"ar": "زاودهورن", "en": "Zuidhorn"},  # 413
    "Q9856": {"ar": "أويرشخوت", "en": "Oirschot"},  # 412
    "Q9881": {"ar": "فونسدريخت", "en": "Woensdrecht"},  # 410
    "Q1348471": {"ar": "كاخ آن براسم", "en": "Kaag en Braassem"},  # 408
    "Q10041": {"ar": "سوست", "en": "Soest"},  # 408
    "Q10027": {"ar": "بارن", "en": "Baarn"},  # 407
    "Q9926": {"ar": "هيمسكيرك", "en": "Heemskerk"},  # 407
    "Q9868": {"ar": "سومرين", "en": "Someren"},  # 404
    "Q222220": {"ar": "ريدركيرك", "en": "Ridderkerk"},  # 402
    "Q10025": {"ar": "فيردن", "en": "Wierden"},  # 401
    "Q10026": {"ar": "زفارتافاترلاند", "en": "Zwartewaterland"},  # 401
    "Q658081": {"ar": "فيست ماس آن فال", "en": "West Maas en Waal"},  # 400
    "Q9862": {"ar": "روكفن", "en": "Rucphen"},  # 399
    "Q9837": {"ar": "خيلزه آن راين", "en": "Gilze en Rijen"},  # 391
    "Q9997": {"ar": "بورنه، أوفرآيسل", "en": "Borne"},  # 391
    "Q934511": {"ar": "بابندريخت", "en": "Papendrecht"},  # 389
    "Q10015": {"ar": "لوسر", "en": "Losser"},  # 389
    "Q9876": {"ar": "فوخت", "en": "Vught"},  # 385
    "Q73069": {"ar": "هوخازاند-سابامير", "en": "Hoogezand-Sappemeer"},  # 384
    "Q952997": {"ar": "نيدر- بيتواه", "en": "Neder-Betuwe"},  # 384
    "Q1305": {"ar": "فاخينينجن", "en": "Wageningen"},  # 383
    "Q9817": {"ar": "بلادل", "en": "Bladel"},  # 382
    "Q9883": {"ar": "زونديرت", "en": "Zundert"},  # 382
    "Q455464": {"ar": "نوردفايك", "en": "Noordwijk"},  # 381
    "Q9789": {"ar": "نيدرفيرت", "en": "Nederweert"},  # 381
    "Q255972": {"ar": "إيمسموند", "en": "Eemsmond"},  # 380
    "Q843895": {"ar": "برومن", "en": "Brummen"},  # 379
    "Q9803": {"ar": "برونسوم", "en": "Brunssum"},  # 379
    "Q9834": {"ar": "خيرتراودنبيرخ", "en": "Geertruidenberg"},  # 377
    "Q9850": {"ar": "لوب أوب زند", "en": "Loon op Zand"},  # 377
    "Q9864": {"ar": "سخايندل", "en": "Schijndel"},  # 377
    "Q795623": {"ar": "آود- بايرلاند", "en": "Oud-Beijerland"},  # 375
    "Q506745": {"ar": "رايسفايك", "en": "Rijswijk"},  # 373
    "Q9867": {"ar": "سينت أوداروده", "en": "Sint-Oedenrode"},  # 373
    "Q73065": {"ar": "فيندام", "en": "Veendam"},  # 371
    "Q10017": {"ar": "أولست- فايه", "en": "Olst-Wijhe"},  # 371
    "Q851310": {"ar": "ليتينسيراديل", "en": "Littenseradiel"},  # 370
    "Q9812": {"ar": "بيرخ آيك", "en": "Bergeijk"},  # 369
    "Q9831": {"ar": "إيرسل", "en": "Eersel"},  # 362
    "Q934525": {"ar": "ألبراندزفارد", "en": "Albrandswaard"},  # 360
    "Q497130": {"ar": "ماسلاوس", "en": "Maassluis"},  # 358
    "Q851244": {"ar": "بونينجن", "en": "Beuningen"},  # 358
    "Q184454": {"ar": "زيفولده", "en": "Zeewolde"},  # 357
    "Q9846": {"ar": "هيلفارينبيك", "en": "Hilvarenbeek"},  # 357
    "Q165662": {"ar": "إلبورخ", "en": "Elburg"},  # 356
    "Q931997": {"ar": "نونسبيت", "en": "Nunspeet"},  # 355
    "Q9838": {"ar": "خورلا", "en": "Goirle"},  # 355
    "Q739449": {"ar": "كريمبن آن دن آيسل", "en": "Krimpen aan den IJssel"},  # 354
    "Q1000817": {"ar": "لايدردورب", "en": "Leiderdorp"},  # 342
    "Q935657": {"ar": "فيستفورنه", "en": "Westvoorne"},  # 340
    "Q939948": {"ar": "بوتن", "en": "Putten"},  # 339
    "Q9928": {"ar": "هيمستيده", "en": "Heemstede"},  # 338
    "Q9869": {"ar": "سون آن بروخل", "en": "Son en Breugel"},  # 337
    "Q840460": {"ar": "فلاختفيده", "en": "Vlagtwedde"},  # 335
    "Q389213": {"ar": "دانتوماديل", "en": "Dantumadiel"},  # 334
    "Q505601": {"ar": "فاسينار", "en": "Wassenaar"},  # 333
    "Q9969": {"ar": "آوتهورن", "en": "Uithoorn"},  # 332
    "Q2536628": {"ar": "هارلينغن", "en": "Harlingen"},  # 331
    "Q1025079": {"ar": "فينسوم", "en": "Winsum"},  # 329
    "Q9767": {"ar": "خولبن- فيتيم", "en": "Gulpen-Wittem"},  # 329
    "Q9800": {"ar": "خنيب", "en": "Gennep"},  # 328
    "Q615491": {"ar": "هيرده", "en": "Heerde"},  # 327
    "Q932042": {"ar": "أولدابروك", "en": "Oldebroek"},  # 327
    "Q9918": {"ar": "إنكهاوزن", "en": "Enkhuizen"},  # 326
    "Q10077": {"ar": "نورد- بيفيلاند", "en": "Noord-Beveland"},  # 324
    "Q9843": {"ar": "هيزه- لينده", "en": "Heeze-Leende"},  # 324
    "Q9940": {"ar": "كوخينلاند", "en": "Koggenland"},  # 324
    "Q10053": {"ar": "فايك باي ديورستيده", "en": "Wijk bij Duurstede"},  # 322
    "Q9908": {"ar": "بلوميندال", "en": "Bloemendaal"},  # 321
    "Q475366": {"ar": "ميناميراديل", "en": "Menameradiel"},  # 320
    "Q753920": {"ar": "إيرميلو", "en": "Ermelo"},  # 318
    "Q840663": {"ar": "دي مارنه", "en": "De Marne"},  # 317
    "Q9966": {"ar": "تيكسل", "en": "Texel"},  # 317
    "Q691754": {"ar": "هارين", "en": "Haren"},  # 316
    "Q9810": {"ar": "أستن", "en": "Asten"},  # 315
    "Q9882": {"ar": "فاودريخيم", "en": "Woudrichem"},  # 314
    "Q9772": {"ar": "ميرسن", "en": "Meerssen"},  # 312
    "Q9877": {"ar": "فالره", "en": "Waalre"},  # 311
    "Q835096": {"ar": "ليك", "en": "Leek"},  # 309
    "Q9853": {"ar": "مل آن سينت هوبرت", "en": "Mill en Sint Hubert"},  # 308
    "Q571198": {"ar": "كوليميلاند أن نيوكراوزلاند", "en": "Kollumerland en Nieuwkruisland"},  # 306
    "Q848324": {"ar": "فورسخوتن", "en": "Voorschoten"},  # 303
    "Q9787": {"ar": "نوت", "en": "Nuth"},  # 303
    "Q952206": {"ar": "ميدن- دلفلاند", "en": "Midden-Delfland"},  # 302
    "Q9840": {"ar": "هارن", "en": "Haaren"},  # 299
    "Q538725": {"ar": "هندريك- إيدو- أمباخت", "en": "Hendrik-Ido-Ambacht"},  # 298
    "Q9849": {"ar": "لانديرد", "en": "Landerd"},  # 296
    "Q849574": {"ar": "لوبيرسوم", "en": "Loppersum"},  # 295
    "Q462663": {"ar": "بريله", "en": "Brielle"},  # 294
    "Q10034": {"ar": "بونسخوتن", "en": "Bunschoten"},  # 291
    "Q9897": {"ar": "ألسمير", "en": "Aalsmeer"},  # 288
    "Q388575": {"ar": "ليردام", "en": "Leerdam"},  # 286
    "Q850211": {"ar": "سلوخترن", "en": "Slochteren"},  # 286
    "Q94747": {"ar": "أوخستخيست", "en": "Oegstgeest"},  # 283
    "Q9771": {"ar": "فالكنبورخ آن دي خول", "en": "Valkenburg aan de Geul"},  # 283
    "Q9839": {"ar": "خرافه", "en": "Grave"},  # 283
    "Q826048": {"ar": "فادينكسفين", "en": "Waddinxveen"},  # 279
    "Q10052": {"ar": "فيانن", "en": "Vianen"},  # 279
    "Q9975": {"ar": "فايديميرين", "en": "Wijdemeren"},  # 278
    "Q9860": {"ar": "روسل- دي ميردن", "en": "Reusel-De Mierden"},  # 277
    "Q9865": {"ar": "سينت أنطونيس", "en": "Sint Anthonis"},  # 277
    "Q932142": {"ar": "دروتن", "en": "Druten"},  # 276
    "Q9915": {"ar": "دريخترلاند", "en": "Drechterland"},  # 274
    "Q932089": {"ar": "نيراينن", "en": "Neerijnen"},  # 271
    # "Q850707": {"ar":"Gaasterlân-Sleat", "en":"Gaasterlân-Sleat"},#267
    "Q932155": {"ar": "هومين", "en": "Heumen"},  # 267
    "Q10021": {"ar": "ستابهورست", "en": "Staphorst"},  # 267
    "Q750772": {"ar": "فيرفيرديراديل", "en": "Ferwerderadiel"},  # 263
    "Q9804": {"ar": "بيرخن", "en": "Bergen"},  # 261
    "Q9971": {"ar": "فاترلاند", "en": "Waterland"},  # 260
    "Q9932": {"ar": "هي لو", "en": "Heiloo"},  # 250
    "Q332730": {"ar": "ليسه", "en": "Lisse"},  # 246
    "Q10040": {"ar": "رينن", "en": "Rhenen"},  # 246
    "Q736131": {"ar": "ألبلاسردام", "en": "Alblasserdam"},  # 243
    "Q10032": {"ar": "بونيك", "en": "Bunnik"},  # 241
    "Q10074": {"ar": "كابيله", "en": "Kapelle"},  # 241
    "Q750760": {"ar": "سليدريخت", "en": "Sliedrecht"},  # 239
    "Q9770": {"ar": "فوريندال", "en": "Voerendaal"},  # 239
    "Q9806": {"ar": "بييك", "en": "Beek"},  # 239
    "Q840628": {"ar": "ليميسترلاند", "en": "Lemsterland"},  # 238
    "Q841525": {"ar": "ماروم", "en": "Marum"},  # 235
    "Q932066": {"ar": "مينترفولده", "en": "Menterwolde"},  # 235
    "Q932116": {"ar": "هيليخوم", "en": "Hillegom"},  # 233
    "Q9809": {"ar": "ألفن- كام", "en": "Alphen-Chaam"},  # 231
    "Q208259": {"ar": "أمالاند", "en": "Ameland"},  # 228
    "Q58797": {"ar": "هاتيم", "en": "Hattem"},  # 228
    "Q1124998": {"ar": "خيسينلاندن", "en": "Giessenlanden"},  # 227
    "Q952948": {"ar": "لينجيفال", "en": "Lingewaal"},  # 227
    "Q518739": {"ar": "راينفاردن", "en": "Rijnwaarden"},  # 226
    "Q9805": {"ar": "بيسل", "en": "Beesel"},  # 224
    "Q9974": {"ar": "فيسب", "en": "Weesp"},  # 223
    "Q9980": {"ar": "زانتفورت", "en": "Zandvoort"},  # 223
    "Q605986": {"ar": "خروتاخاست", "en": "Grootegast"},  # 222
    "Q778989": {"ar": "ليووراديراديل", "en": "Leeuwarderadeel"},  # 222
    "Q290475": {"ar": "كرومستراين", "en": "Cromstrijen"},  # 219
    "Q952194": {"ar": "كوريندايك", "en": "Korendijk"},  # 219
    "Q995": {"ar": "أبنجيدام", "en": "Appingedam"},  # 218
    "Q848988": {"ar": "تصنيف:نوردفايكرهاوت", "en": "Noordwijkerhout"},  # 217
    "Q273746": {"ar": "أورك", "en": "Urk"},  # 214
    "Q184288": {"ar": "زيدريك", "en": "Zederik"},  # 212
    "Q9906": {"ar": "بلاريكوم", "en": "Blaricum"},  # 211
    "Q9782": {"ar": "سخينن", "en": "Schinnen"},  # 210
    "Q953012": {"ar": "هاردينكسفيلد- خيسيندام", "en": "Hardinxveld-Giessendam"},  # 209
    "Q850722": {"ar": "هت بيلدت", "en": "het Bildt"},  # 208
    "Q747965": {"ar": "بيلينجفيده", "en": "Bellingwedde"},  # 207
    "Q10047": {"ar": "لوبيك", "en": "Lopik"},  # 207
    "Q9962": {"ar": "ستيده بروك", "en": "Stede Broec"},  # 205
    "Q9913": {"ar": "ديمين", "en": "Diemen"},  # 204
    "Q10048": {"ar": "مونتفورت", "en": "Montfoort"},  # 203
    "Q9945": {"ar": "لارين", "en": "Laren"},  # 202
    "Q932077": {"ar": "باكالا", "en": "Pekela"},  # 194
    "Q9976": {"ar": "فورمرلاند", "en": "Wormerland"},  # 193
    "Q9769": {"ar": "سيمبلفيلد", "en": "Simpelveld"},  # 192
    "Q9953": {"ar": "آودر- أمستل", "en": "Ouder-Amstel"},  # 192
    # "Q952183": {"ar":"Rijnwoude", "en":"Rijnwoude"},#189
    "Q9808": {"ar": "آلبورخ", "en": "Aalburg"},  # 189
    "Q461142": {"ar": "بيدوم", "en": "Bedum"},  # 184
    "Q10055": {"ar": "فاودنبيرخ", "en": "Woudenberg"},  # 179
    "Q9967": {"ar": "آوتخيست", "en": "Uitgeest"},  # 176
    "Q9811": {"ar": "بارل نوسو", "en": "Baarle-Nassau"},  # 174
    "Q165736": {"ar": "دوسبورخ", "en": "Doesburg"},  # 170
    "Q9818": {"ar": "بوكل", "en": "Boekel"},  # 169
    "Q9952": {"ar": "أوبمير", "en": "Opmeer"},  # 167
    "Q9786": {"ar": "أوندربانكن", "en": "Onderbanken"},  # 166
    "Q9900": {"ar": "بيمستر", "en": "Beemster"},  # 165
    "Q10051": {"ar": "آودافاتر", "en": "Oudewater"},  # 162
    "Q524808": {"ar": "فيسترفورت", "en": "Westervoort"},  # 158
    "Q849566": {"ar": "تن بور", "en": "Ten Boer"},  # 157
    "Q858607": {"ar": "ستراين", "en": "Strijen"},  # 157
    "Q204412": {"ar": "تيرشخيلينج", "en": "Terschelling"},  # 154
}
# ---
pokn = {
    "Q204412": {"ar": "تيرشخيلينج", "en": "Terschelling"},  # 154
}
# ---
Format = {
    'ar': '1 في 2، هولندا', 'nl': '1 in 2', 'en': '1 in 2, the Netherlands'
}
# ---
topics = {}
topics['Q79007'] = {'ar': 'شارع', 'nl': 'straat', 'en': 'street'}
# topics['Q174782'] = {'ar' : 'ميدان' , 'nl' : 'plein', 'en' : 'square' }
# ---
iop = ['Q79007', 'Q523166', 'Q174782', 'Q1484611']
# ---
translations = {}
for topic in topics:
    for city in taop:
        translations[topic] = {}
        quarry = 'SELECT ?item WHERE { ' + f'?item wdt:P31 wd:{topic}. ?item wdt:P17 wd:Q55. ?item wdt:P131 wd:{city}.'

        for prop in iop:
            if prop != topic:
                quarry += '\nFILTER NOT EXISTS {' + f'?item wdt:P31 wd:{prop}.' + '}'

        quarry += '\nOPTIONAL { ?item schema:description ?des. FILTER((LANG(?des)) = "ar")  } FILTER(!BOUND(?des))\n}'
        for lang in topics[topic]:
            descraption = Format[lang]
            lang2 = lang
            if lang == 'nl':
                lang2 = 'en'
            wal = descraption.replace('1', str(topics[topic][lang]))
            wal = wal.replace('2', str(taop[city][lang2]))
            # re.sub(r'2' , taop[city][lang2] ,topics[topic][lang] )
            translations[topic][lang] = wal
        pywikibot.output(translations)
        newdesc.mainfromQuarry2(topic, quarry, translations)
# ---
