#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
CategoryTableNew = { 
    #"A.ADM1" : {   "item" : "Q10864048" ,  "ar" : "المستوى الأول من التقسيم الإداري" , "en" : "first-level administrative country subdivision" }
    #, "A.ADM2" : { "item" : "Q13220204" ,  "ar" : "المستوى الثاني من التقسيم الإداري" ,    "en" : "second-level administrative country subdivision" }
    #, "A.ADM3" : { "item" : "Q13221722" ,  "ar" : "المستوى الثالث من التقسيم الإداري" ,    "en" : "third-level administrative country subdivision" }
    #, "A.ADM4" : { "item" : "Q14757767" ,  "ar" : "المستوى الرابع من التقسيم الإداري" ,    "en" : "fourth-level administrative country subdivision" }
    #, "A.ADM5" : { "item" : "Q15640612" ,  "ar" : "المستوى الخامس من التقسيم الإداري" ,    "en" : "fifth-level administrative country subdivision" }
    #, "A.ADMD" : { "item" : "Q56061" , "ar" : "تقسيم إداري" ,  "en" : "administrative territorial entity" }
    #, "A.null" : { "item" : "Q22927291" ,  "ar" : "المستوى السادس من التقسيم الإداري" ,    "en" : "sixth-level administrative country subdivision" }
    "A.PRSH" : {    "item" : "Q102496" ,    "ar" : "رعية" , "en" : "parish" }
    , "A.ZNB" : {   "item" : "Q1054581" ,   "ar" : "منطقة عازلة" ,  "en" : "Buffer zone" }
    , "GLCR" : {    "item" : "Q35666" , "ar" : "مثلجة" ,    "en" : "glacier" }
    , "H.BAY" : {   "item" : "Q39594" , "ar" : "خليج" , "en" : "bay" }
    , "H.BAYS" : {  "item" : "Q39594" , "ar" : "خليج" , "en" : "bay" }
    , "H.BNK" : {   "item" : "Q468756" ,    "ar" : "ضفة" ,  "en" : "bank" }
    , "H.BOG" : {   "item" : "Q30198" , "ar" : "هور" ,  "en" : "marsh" }
    , "H.CAPG" : {  "item" : "Q878077" ,    "ar" : "غطاء جليدي" ,   "en" : "ice cap" }
    , "H.CHN" : {   "item" : "Q1210950" ,   "ar" : "قناة بحرية" ,   "en" : "channel" }
    , "H.CHNM" : {  "item" : "Q1210950" ,   "ar" : "قناة بحرية" ,   "en" : "channel" }
    , "H.CHNN" : {  "item" : "Q1210950" ,   "ar" : "قناة بحرية" ,   "en" : "channel" }
    , "H.CNL" : {   "item" : "Q12284" , "ar" : "قناة" , "en" : "canal" }
    , "H.CNLA" : {  "item" : "Q474" ,   "ar" : "قناة" , "en" : "aqueduct" }
    , "H.CNLN" : {  "item" : "Q12284" , "ar" : "قناة" , "en" : "canal" }
    , "H.CNLX" : {  "item" : "Q12284" , "ar" : "قناة" , "en" : "canal" }
    , "H.COVE" : {  "item" : "Q31615" , "ar" : "جون" ,  "en" : "cove" }
    , "H.ESTY" : {  "item" : "Q47053" , "ar" : "خور" ,  "en" : "estuary" }
    , "H.FJD" : {   "item" : "Q45776" , "ar" : "خلل" ,  "en" : "fjord" }
    , "H.FJDS" : {  "item" : "Q45776" , "ar" : "خلل" ,  "en" : "fjord" }
    , "H.FLLS" : {  "item" : "Q34038" , "ar" : "شلال" , "en" : "waterfall" }
    , "H.FLLSX" : { "item" : "Q34038" , "ar" : "شلال" , "en" : "waterfall" }
    , "H.GLCR" : {  "item" : "Q35666" , "ar" : "مثلجة" ,    "en" : "glacier" }
    , "H.GYSR" : {  "item" : "Q83471" , "ar" : "سخان" , "en" : "geyser" }
    , "H.HBR" : {   "item" : "Q283202" ,    "ar" : "مرفأ" , "en" : "harbor" }
    , "H.INLT" : {  "item" : "Q1172599" ,   "ar" : "بوغاز" ,    "en" : "inlet" }
    , "H.LGN" : {   "item" : "Q187223" ,    "ar" : "بحيرة شاطئة" ,  "en" : "lagoon" }
    , "H.LGNS" : {  "item" : "Q187223" ,    "ar" : "بحيرة شاطئة" ,  "en" : "lagoon" }
    , "H.LGNX" : {  "item" : "Q187223" ,    "ar" : "بحيرة شاطئة" ,  "en" : "lagoon" }
    , "H.LK" : {    "item" : "Q23397" , "ar" : "بحيرة" ,    "en" : "lake" }
    , "H.LKS" : {   "item" : "Q23397" , "ar" : "بحيرة" ,    "en" : "lake" }
    , "H.MFGN" : {  "item" : "Q244326" ,    "ar" : "ملاحات" ,   "en" : "salt evaporation pond" }
    , "H.MRSH" : {  "item" : "Q30198" , "ar" : "هور" ,  "en" : "marsh" }
    , "H.OCN" : {   "item" : "Q9430" ,  "ar" : "محيط" , "en" : "ocean" }
    , "H.PND" : {   "item" : "Q3253281" ,   "ar" : "بركة" , "en" : "pond" }
    , "H.PNDSF" : { "item" : "Q1265665" ,   "ar" : "بركة سمك" , "en" : "fish pond" }
    , "H.RF" : {    "item" : "Q184358" ,    "ar" : "منطقة شعاب" ,   "en" : "reef" }
    , "H.RFX" : {   "item" : "Q184358" ,    "ar" : "منطقة شعاب" ,   "en" : "reef" }
    , "H.RSV" : {   "item" : "Q131681" ,    "ar" : "خزان مائي" ,    "en" : "reservoir" }
    , "H.RVN" : {   "item" : "Q2042028" ,   "ar" : "إفجيج" ,    "en" : "ravine" }
    , "H.SHOL" : {  "item" : "Q28337" , "ar" : "مياه ضحلة" ,    "en" : "shoal" }
    , "H.SPNG" : {  "item" : "Q124714" ,    "ar" : "ينبوع" ,    "en" : "spring" }
    , "H.STM" : {   "item" : "Q47521" , "ar" : "جدول مائي" ,    "en" : "stream" }
    #, "H.STM" : {   "item" : "Q4022" ,  "ar" : "نهر" ,  "en" : "river" }
    , "H.SWMP" : {  "item" : "Q166735" ,    "ar" : "مستنقع" ,   "en" : "swamp" }
    , "H.WAD" : {   "item" : "Q187971" ,    "ar" : "وادي" , "en" : "wadi" }
    , "H.WADS" : {  "item" : "Q187971" ,    "ar" : "وادي" , "en" : "wadi" }
    , "H.WTRC" : {  "item" : "Q355304" ,    "ar" : "مجرى مائي" ,    "en" : "watercourse" }
    , "L.BSND" : {  "item" : "Q166620" ,    "ar" : "مستجمع مائي" ,  "en" : "drainage basin" }
    , "L.CONT" : {  "item" : "Q5107" ,  "ar" : "قارة" , "en" : "continent" }
    , "L.CST" : {   "item" : "Q93352" , "ar" : "ساحل" , "en" : "coast" }
    , "L.INDS" : {  "item" : "Q329683" ,    "ar" : "منطقة صناعية" , "en" : "industrial park" }
    , "L.MILB" : {  "item" : "Q245016" ,    "ar" : "قاعدة عسكرية" , "en" : "military base" }
    , "L.NVB" : {   "item" : "Q1324633" ,   "ar" : "قاعدة بحرية" ,  "en" : "naval base" }
    , "L.RESN" : {  "item" : "Q179049" ,    "ar" : "محمية طبيعية" , "en" : "nature reserve" }
    , "L.RGN" : {   "item" : "Q82794" , "ar" : "منطقة" ,    "en" : "geographic region" }
    , "L.RGNH" : {  "item" : "Q1620908" ,   "ar" : "منطقة تاريخية" ,    "en" : "historical region" }
    , "P.PPL" : {   "item" : "Q486972" ,    "ar" : "مستوطنة" ,  "en" : "human settlement" }
    , "R.ST" : {    "item" : "Q79007" , "ar" : "شارع" , "en" : "street" }
    , "R.TNL" : {   "item" : "Q44377" , "ar" : "نفق" ,  "en" : "tunnel" }
    , "S.AIRH" : {  "item" : "Q502074" ,    "ar" : "مطار مروحيات" , "en" : "heliport" }
    , "S.AQC" : {   "item" : "Q188989" ,    "ar" : "زراعة مائية" ,  "en" : "aquaculture" }
    , "S.ATM" : {   "item" : "Q81235" , "ar" : "آلة صراف آلي" , "en" : "automated teller machine" }
    , "S.BANK" : {  "item" : "Q22687" , "ar" : "بَنْك" ,    "en" : "bank" }
    , "S.BLDG" : {  "item" : "Q41176" , "ar" : "مبنى" , "en" : "building" }
    , "S.BTYD" : {  "item" : "Q190928" ,    "ar" : "حوض بناء سفن" , "en" : "shipyard" }
    , "S.BUSTN" : { "item" : "Q494829" ,    "ar" : "موقف حافلات" ,  "en" : "bus station" }
    , "S.CAVE" : {  "item" : "Q35509" , "ar" : "كهف" ,  "en" : "cave" }
    , "S.CH" : {    "item" : "Q16970" , "ar" : "كنيسة" ,    "en" : "church" }
    , "S.CSNO" : {  "item" : "Q133215" ,    "ar" : "كازينو" ,   "en" : "casino" }
    , "S.CSTL" : {  "item" : "Q23413" , "ar" : "قلعة" , "en" : "castle" }
    , "S.DCKY" : {  "item" : "Q190928" ,    "ar" : "حوض بناء سفن" , "en" : "shipyard" }
    , "S.GOSP" : {  "item" : "Q3011536" ,   "ar" : "فاصل" , "en" : "Separator" }
    , "S.INSM" : {  "item" : "Q245016" ,    "ar" : "قاعدة عسكرية" , "en" : "military base" }
    , "S.LTHSE" : { "item" : "Q39715" , "ar" : "منارة" ,    "en" : "lighthouse" }
    , "S.MLWTR" : { "item" : "Q185187" ,    "ar" : "طاحونة مائية" , "en" : "watermill" }
    , "S.MUS" : {   "item" : "Q33506" , "ar" : "متحف" , "en" : "museum" }
    , "S.OBS" : {   "item" : "Q62832" , "ar" : "مرصد" , "en" : "observatory" }
    , "S.OBSR" : {  "item" : "Q184356" ,    "ar" : "مقراب راديوي" , "en" : "radio telescope" }
    , "S.OILW" : {  "item" : "Q587682" ,    "ar" : "بئر نفط" ,  "en" : "oil well" }
    , "S.PAL" : {   "item" : "Q16560" , "ar" : "قصر" ,  "en" : "palace" }
    , "S.PKLT" : {  "item" : "Q6501349" ,   "ar" : "موقف سيارات" ,  "en" : "parking lot" }
    , "S.PSH" : {   "item" : "Q159719" ,    "ar" : "محطة طاقة" ,    "en" : "power station" }
    , "S.PYR" : {   "item" : "Q12516" , "ar" : "هرم" ,  "en" : "pyramid" }
    , "S.RECG" : {  "item" : "Q1048525" ,   "ar" : "ملعب غولف" ,    "en" : "golf course" }
    , "S.RSTN" : {  "item" : "Q55488" , "ar" : "محطة قطار" ,    "en" : "train station" }
    , "S.SCHC" : {  "item" : "Q189004" ,    "ar" : "كلية" , "en" : "college" }
    , "S.SHRN" : {  "item" : "Q697295" ,    "ar" : "مزار" , "en" : "shrine" }
    , "S.SNTR" : {  "item" : "Q46124" , "ar" : "مصحة" , "en" : "sanatorium" }
    , "S.STBL" : {  "item" : "Q214252" ,    "ar" : "إسطبل" ,    "en" : "stable" }
    , "S.STNM" : {  "item" : "Q190107" ,    "ar" : "محطة رصد جوي" , "en" : "weather station" }
    , "S.UNIV" : {  "item" : "Q3918" ,  "ar" : "جامعة" ,    "en" : "university" }
    , "T.BCH" : {   "item" : "Q40080" , "ar" : "شاطئ" , "en" : "beach" }
    , "T.CAPE" : {  "item" : "Q185113" ,    "ar" : "رأس" ,  "en" : "cape" }
    , "T.CLDA" : {  "item" : "Q159954" ,    "ar" : "كالديرا" ,  "en" : "caldera" }
    , "T.CONE" : {  "item" : "Q1368970" ,   "ar" : "مخروط بركاني" , "en" : "volcanic cone" }
    , "T.DVD" : {   "item" : "Q152005" ,    "ar" : "حاجز مائي" ,    "en" : "drainage divide" }
    , "T.ISL" : {   "item" : "Q23442" , "ar" : "جزيرة" ,    "en" : "island" }
    , "T.ISLT" : {  "item" : "Q1226252" ,   "ar" : "جزيرة متصلة" ,  "en" : "tied island" }
    , "T.NTK" : {   "item" : "Q194408" ,    "ar" : "نوناتاك" ,  "en" : "nunatak" }
    , "T.NTKS" : {  "item" : "Q194408" ,    "ar" : "نوناتاك" ,  "en" : "nunatak" }
    , "T.PT" : {    "item" : "Q24529780" ,  "ar" : "نقطة" , "en" : "point" }
    , "T.SAND" : {  "item" : "Q34379419" ,  "ar" : "منطقة رملية" ,  "en" : "sand area" }
    , "T.VAL" : {   "item" : "Q39816" , "ar" : "واد" ,  "en" : "valley" }
    , "T.VLC" : {   "item" : "Q8072" ,  "ar" : "بركان" ,    "en" : "volcano" }
    , "U.CNYU" : {  "item" : "Q963729" ,    "ar" : "أخدود غائص" ,   "en" : "submarine canyon" }
    , "U.ESCU" : {  "item" : "Q1174791" ,   "ar" : "جرف" ,  "en" : "escarpment" }
    , "U.KNSU" : {  "item" : "Q3294251" ,   "ar" : "أكمة أوراسية" , "en" : "hillock" }
    , "U.MESU" : {  "item" : "Q623319" ,    "ar" : "مائدة صحراوية" ,    "en" : "mesa" }
    , "U.PKU" : {   "item" : "Q207326" ,    "ar" : "قمة جبل" ,  "en" : "summit" }
    , "U.RDGU" : {  "item" : "Q740445" ,    "ar" : "نتوء جبلي" ,    "en" : "ridge" }
    , "U.SHFU" : {  "item" : "Q134851" ,    "ar" : "منحدر قاري" ,   "en" : "continental shelf" }
    , "U.SMSU" : {  "item" : "Q503269" ,    "ar" : "جبل بحري" , "en" : "seamount" }
    , "U.SMU" : {   "item" : "Q503269" ,    "ar" : "جبل بحري" , "en" : "seamount" }
    , "U.TMSU" : {  "item" : "Q151957" ,    "ar" : "جيوت" , "en" : "guyot" }
    , "V.FRST" : {  "item" : "Q4421" ,  "ar" : "غابة" , "en" : "forest" }
    , "V.MDW" : {   "item" : "Q7777019" ,   "ar" : "مرج" ,  "en" : "meadow" }
    , "V.SCRB" : {  "item" : "Q879641" ,    "ar" : "أراضي أشجار قمئية" ,    "en" : "shrubland" }
    , "V.TUND" : {  "item" : "Q43262" , "ar" : "تندرا" ,    "en" : "tundra" }
    , "V.VIN" : {   "item" : "Q22715" , "ar" : "كرم" ,  "en" : "vineyard" }
    , "V.VINS" : {  "item" : "Q22715" , "ar" : "كرم" ,  "en" : "vineyard" }
}
#---
CategoryTableNew["S.DAM"]= {"item" : "Q12323" , "ar" : "سد" , "en" : "dam" }
CategoryTableNew["T.MT"]= {"item" : "Q8502" , "ar" : "جبل" , "en" : "mountain" }

CategoryTableNew["T.ISLET"]= {"item" : "Q207524" , "ar" : "جزيرة صغيرة" , "en" : "islet" }
CategoryTableNew["L.PRK"]= {"item" : "Q22698" , "ar" : "متنزه" , "en" : "park" }
CategoryTableNew["H.MOOR"]= {"item" : "Q34795826" , "ar" : "" , "en" : "moor" }
CategoryTableNew["L.OILF"]= {"item" : "Q211748" , "ar" : "حقل نفط" , "en" : "oilfield" }

CategoryTableNew["T.HLL"]= {"item" : "Q54050" , "ar" : "تل" , "en" : "hill" }
CategoryTableNew["T.HLLS"] = CategoryTableNew["T.HLL"]

CategoryTableNew["S.AIRP"]= {"item" : "Q1248784" , "ar" : "مطار" , "en" : "airport" }
CategoryTableNew["H.STMD"]= {"item" : "Q591942" , "ar" : "فرع" , "en" : "distributary" }
CategoryTableNew["T.LEV"]= {"item" : "Q105190" , "ar" : "سد مائي" , "en" : "levee" }
CategoryTableNew["T.PLN"]= {"item" : "Q160091" , "ar" : "سهل" , "en" : "plain" }
CategoryTableNew["T.PLNX"]= CategoryTableNew["T.PLN"]
CategoryTableNew["T.PLNX"]= CategoryTableNew["T.PLN"]
CategoryTableNew["H.STMI"]= CategoryTableNew["H.STM"]

CategoryTableNew["P.PPLF"]= {"item" : "Q532" , "ar" : "قرية" , "en" : "farm village" }
CategoryTableNew["T.RDGE"]= {"item" : "Q740445" , "ar" : "نتوء جبلي" , "en" : "ridge" }
CategoryTableNew["S.MN"]= {"item" : "Q820477" , "ar" : "منجم" , "en" : "mine" }

CategoryTableNew["T.MTS"]= {"item" : "Q46831" , "ar" : "سلسلة جبلية" , "en" : "mountains" }
CategoryTableNew["canyon"]= {"item" : "Q150784" , "ar" : "أخدود" , "en" : "canyon" }
CategoryTableNew["T.ISLX"]=  CategoryTableNew['T.ISL']
CategoryTableNew["V.HTH"]= {"item" : "Q27590" , "ar" : "براح" , "en" : "heath" }
CategoryTableNew["H.STRT"]= {"item" : "Q37901" , "ar" : "مضيق" , "en" : "strait" }
CategoryTableNew["T.CLF"]= {"item" : "Q107679" , "ar" : "جرف" , "en" : "cliff" }
CategoryTableNew["H.WTLD"]= {"item" : "Q170321" , "ar" : "منطقة رطبة" , "en" : "wetland" }
CategoryTableNew["T.PLAT"]= {"item" : "Q75520" , "ar" : "هضبة" , "en" : "plateau" }
CategoryTableNew["H.CNLI"]= {"item" : "Q2935978" , "ar" : "قناة ري" , "en" : "irrigation canal" }
CategoryTableNew["T.DPR"]= {"item" : "Q190429" , "ar" : "منخفض" , "en" : "depression" }
CategoryTableNew["L.PRT"]= {"item" : "Q44782" , "ar" : "ميناء" , "en" : "port" }
CategoryTableNew[""]= {"item" : "" , "ar" : "" , "en" : "" }
CategoryTableNew[""]= {"item" : "" , "ar" : "" , "en" : "" }
CategoryTableNew[""]= {"item" : "" , "ar" : "" , "en" : "" }
CategoryTableNew[""]= {"item" : "" , "ar" : "" , "en" : "" }

CategoryTableNew["H.CHNL"]=  CategoryTableNew['H.LK']#H.LK#H.CHN

#---
CategoryTable_New = { 
    #"A.ADM1" : "10864048",  #   المستوى الأول من التقسيم الإداري    #   first-level administrative country subdivision
    #"A.ADM2" : "13220204",  #   المستوى الثاني من التقسيم الإداري   #   second-level administrative country subdivision
    #"A.ADM3" : "13221722",  #   المستوى الثالث من التقسيم الإداري   #   third-level administrative country subdivision
    #"A.ADM4" : "14757767",  #   المستوى الرابع من التقسيم الإداري   #   fourth-level administrative country subdivision
    #"A.ADM5" : "15640612",  #   المستوى الخامس من التقسيم الإداري   #   fifth-level administrative country subdivision
    #"A.ADMD" : "56061", #   تقسيم إداري #   administrative territorial entity
    "A.ADMDH" : "19832712", #       #   historical administrative division
    "A.null" : "22927291",  #   المستوى السادس من التقسيم الإداري   #   sixth-level administrative country subdivision
    "A.PCL" : "7225121",    #       #   Political structure
    "A.PRSH" : "102496",    #   رعية    #   parish
    "A.ZNB" : "1054581",    #   منطقة عازلة #   Buffer zone
    "GLCR" : "35666",   #   مثلجة   #   glacier
    "H.ANCH" : "6908406",   #       #   anchorage
    "H.BAY" : "39594",  #   خليج    #   bay
    "H.BAYS" : "39594", #   خليج    #   bay
    "H.BGHT" : "17018380",  #       #   bight
    "H.BNK" : "468756", #   ضفة #   bank
    "H.BNKR" : "3706062",   #       #   Stream bank
    "H.BOG" : "30198",  #   هور #   marsh
    "H.CAPG" : "878077",    #   غطاء جليدي  #   ice cap
    "H.CHN" : "1210950",    #   قناة بحرية  #   channel
    "H.CHNM" : "1210950",   #   قناة بحرية  #   channel
    "H.CHNN" : "1210950",   #   قناة بحرية  #   channel
    "H.CNL" : "12284",  #   قناة    #   canal
    "H.CNLA" : "474",   #   القناة  #   aqueduct
    "H.CNLD" : "28109789",  #       #   drainage canal
    "H.CNLI" : "2935978",   #       #   irrigation canal
    "H.CNLN" : "12284", #   قناة    #   canal
    "H.CNLX" : "12284", #   قناة    #   canal
    "H.COVE" : "31615", #   جون #   cove
    "H.DCK" : "124282", #       #   dock
    "H.DTCH" : "2048319",   #       #   ditch
    "H.DTCHD" : "2048319",  #       #   ditch
    "H.ESTY" : "47053", #   خور #   estuary
    "H.FJD" : "45776",  #   خلل #   fjord
    "H.FJDS" : "45776", #   خلل #   fjord
    "H.FLLS" : "34038", #   شلال    #   waterfall
    "H.FLLSX" : "34038",    #   شلال    #   waterfall
    "H.FLTM" : "31796", #       #   mudflat
    "H.FLTT" : "31796", #       #   mudflat
    "H.GLCR" : "35666", #   مثلجة   #   glacier
    "H.GULF" : "1322134",   #       #   gulf
    "H.GYSR" : "83471", #   سخان    #   geyser
    "H.HBR" : "283202", #   مرفأ    #   harbor
    "H.INLT" : "1172599",   #   بوغاز   #   inlet
    "H.LGN" : "187223", #   بحيرة شاطئة #   lagoon
    "H.LGNS" : "187223",    #   بحيرة شاطئة #   lagoon
    "H.LGNX" : "187223",    #   بحيرة شاطئة #   lagoon
    "H.LK" : "23397", #   بركة سمك    #   fish pond
    "H.LKS" : "23397",  #   بحيرة   #   lake
    "H.LKSB" : "1048337",   #       #   underground lake
    "H.MFGN" : "244326",    #   ملاحات  #   salt evaporation pond
    "H.MRSH" : "30198", #   هور #   marsh
    "H.OCN" : "9430",   #   محيط    #   ocean
    "H.PND" : "3253281",    #   بركة    #   pond
    "H.PNDSF" : "1265665",  #   بركة سمك    #   fish pond
    "H.RDST" : "913035",    #       #   roadstead
    "H.RF" : "184358",  #   الشعاب  #   reef
    "H.RFX" : "184358", #   الشعاب  #   reef
    "H.RSV" : "131681", #   خزان مائي   #   reservoir
    "H.RVN" : "2042028",    #   إفجيج   #   ravine
    "H.SD" : "491713",  #       #   sound
    "H.SHOL" : "28337", #   مياه ضحلة   #   shoal
    "H.SPNG" : "124714",    #   ينبوع   #   spring
    "H.STM" : "4022",   #   نهر #   river
    "H.STM" : "47521",  #   جدول مائي   #   stream
    "H.SWMP" : "166735",    #   مستنقع  #   swamp
    "H.SYSI" : "6129871",   #       #   irrigation system
    "H.TNLC" : "5031071",   #       #   canal tunnel
    "H.WAD" : "187971", #   شعيب    #   wadi
    "H.WADS" : "187971",    #   شعيب    #   wadi
    "H.WTRC" : "355304",    #   مجرى مائي   #   watercourse
    "L.BSND" : "166620",    #   مستجمع مائي #   drainage basin
    "L.CLG" : "4358873",    #       #   glade
    "L.CMN" : "2259176",    #       #   common land
    "L.CONT" : "5107",  #   قارة    #   continent
    "L.CST" : "93352",  #   ساحل    #   coast
    "L.DEVH" : "5916199",   #       #   housing development
    "L.INDS" : "329683",    #   المنطقة الصناعية    #   industrial park
    "L.MILB" : "245016",    #   قاعدة عسكرية    #   military base
    "L.NVB" : "1324633",    #   قاعدة بحرية #   naval base
    "L.RESN" : "179049",    #   محمية طبيعية    #   nature reserve
    "L.RESW" : "20268591",  #       #   wildlife reserve
    "L.RGN" : "82794",  #   منطقة   #   geographic region
    "L.RGNE" : "1973901",   #       #   economic region
    "L.RGNH" : "1620908",   #   منطقة تاريخية   #   historical region
    "P.PPL" : "486972", #   مستوطنة #   human settlement
    "R.OILP" : "1262090",   #       #   oil pipeline
    "R.RDJCT" : "1788454",  #       #   road junction
    "R.ST" : "79007",   #   شارع    #   street
    "R.STKR" : "7617917",   #       #   Stock route
    "R.TNL" : "44377",  #   نفق #   tunnel
    "R.TNLRD" : "2354973",  #       #   road tunnel
    "S.AIRH" : "502074",    #   مطار مروحيات    #   heliport
    "S.AQC" : "188989", #   زراعة مائية #   aquaculture
    "S.ATM" : "81235",  #   آلة صراف آلي    #   automated teller machine
    "S.BANK" : "22687", #   بَنْك   #   bank
    "S.BCN" : "17484395",   #       #   beacon
    "S.BLDG" : "41176", #   مبنى    #   building
    "S.BLDO" : "1021645",   #       #   office building
    "S.BRKW" : "153084",    #       #   groyne
    "S.BTYD" : "190928",    #   حوض بناء سفن    #   shipyard
    "S.BUSTN" : "494829",   #   موقف حافلات #   bus station
    "S.CAVE" : "35509", #   كهف #   cave
    "S.CH" : "16970",   #   كنيسة   #   church
    "S.CMPMN" : "820254",   #       #   mining community
    "S.CSNO" : "133215",    #   كازينو  #   casino
    "S.CSTL" : "23413", #   قلعة    #   castle
    "S.CTHSE" : "1137809",  #       #   courthouse
    "S.DCKY" : "190928",    #   حوض بناء سفن    #   shipyard
    "S.FRMQ" : "16423630",  #       #   abandoned farm
    "S.GOSP" : "3011536",   #   فاصل    #   Separator
    "S.HSPL" : "1406569",   #       #   leper colony
    "S.HSTS" : "10296418",  #       #   historical site
    "S.INSM" : "245016",    #   قاعدة عسكرية    #   military base
    "S.LTHSE" : "39715",    #   منارة   #   lighthouse
    "S.MFGSG" : "227857",   #       #   sugar refinery
    "S.MLWTR" : "185187",   #   طاحونة مائية    #   watermill
    "S.MUS" : "33506",  #   متحف    #   museum
    "S.OBS" : "62832",  #   مرصد    #   observatory
    "S.OBSR" : "184356",    #   مقراب راديوي    #   radio telescope
    "S.OILW" : "587682",    #   بئر نفط #   oil well
    "S.PAL" : "16560",  #   قصر #   palace
    "S.PKLT" : "6501349",   #   موقف سيارات #   parking lot
    "S.PRNJ" : "7307453",   #       #   reformatory
    "S.PSH" : "159719", #   محطة طاقة   #   power station
    "S.PYR" : "12516",  #   هرم #   pyramid
    "S.RECG" : "1048525",   #   ملعب غولف   #   golf course
    "S.RSD" : "21683257",   #       #   Siding
    "S.RSTN" : "55488", #   محطة قطار   #   train station
    "S.SCHA" : "3345348",   #       #   Agricultural education
    "S.SCHC" : "189004",    #   كلية    #   college
    "S.SCHL" : "897403",    #       #   language school
    "S.SHRN" : "697295",    #   مزار    #   shrine
    "S.SNTR" : "46124", #   مصحة    #   sanatorium
    "S.STBL" : "214252",    #   إسطبل   #   stable
    "S.STNB" : "195339",    #       #   research station
    "S.STNM" : "190107",    #   محطة رصد جوي    #   weather station
    "S.STNS" : "357742",    #       #   broadcast relay station
    "S.STNW" : "3497366",   #       #   whaling station
    "S.SWT" : "15242449",   #       #   wastewater treatment plant
    "S.TRIG" : "131862",    #       #   triangulation station
    "S.UNIV" : "3918",  #   جامعة   #   university
    "S.WTRW" : "11849395",  #       #   waterworks
    "T.BCH" : "40080",  #   شاطئ    #   beach
    "T.CAPE" : "185113",    #   رأس #   cape
    "T.CLDA" : "159954",    #   كالديرا #   caldera
    "T.CONE" : "1368970",   #   مخروط بركاني    #   volcanic cone
    "T.DVD" : "152005", #   حاجز مائي   #   drainage divide
    "T.ISL" : "23442",  #   جزيرة   #   island
    "T.ISLT" : "1226252",   #   جزيرة متصلة #   tied island
    "T.NTK" : "194408", #   نوناتاك #   nunatak
    "T.NTKS" : "194408",    #   نوناتاك #   nunatak
    "T.PT" : "24529780",    #   نقطة    #   point
    "T.RKS" : "24576816",   #       #   group of rocks
    "T.VAL" : "39816",  #   واد #   valley
    "T.VALG" : "25424443",  #       #   hanging valley
    "T.VLC" : "8072",   #   بركان   #   volcano
    "U.CNYU" : "963729",    #   أخدود غائص  #   submarine canyon
    "U.ESCU" : "1174791",   #   جرف #   escarpment
    "U.FRZU" : "5477586",   #       #   fracture zone
    "U.FURU" : "1474839",   #       #   furrow
    "U.GAPU" : "16887036",  #       #   gap
    "U.KNSU" : "3294251",   #   أكمة أوراسية    #   hillock
    "U.MESU" : "623319",    #   مائدة صحراوية   #   mesa
    "U.PKU" : "207326", #   قمة جبل #   summit
    "U.RDGU" : "740445",    #   نتوء جبلي   #   ridge
    "U.SHFU" : "134851",    #   منحدر قاري  #   continental shelf
    "U.SMSU" : "503269",    #   جبل بحري    #   seamount
    "U.SMU" : "503269", #   جبل بحري    #   seamount
    "U.SPRU" : "1400565",   #       #   spur
    "U.TMSU" : "151957",    #   جيوت    #   guyot
    "V.FRST" : "4421",  #   غابة    #   forest
    "V.MDW" : "7777019",    #   مرج #   meadow
    "V.SCRB" : "879641",    #   أراضي الأشجار القمئية   #   shrubland
    "V.TUND" : "43262", #   تندرا   #   tundra
    "V.VIN" : "22715",  #   كرم #   vineyard
    "V.VINS" : "22715", #   كرم #   vineyard
    "H.WAD" : "34207295", #  وادي يمني
    }
#---