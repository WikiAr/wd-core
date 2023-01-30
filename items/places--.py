#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#

placesTable={ 
    "Q124714":{    
        "ar": "ينبوع"
        ,"en": "spring"
        },
    "Q39816":{        
        "ar": "واد"
        #,"de": "Siedlung"
        #,"el": "οικισμός"
        ,"en": "valley"
        #,"eo": "setlejo"
        #,"es": "asentamiento"
        #,"et": "asula"
        #,"fa": "سکونتگاه انسانی"
        #,"fr": "établissement humain"
        #,"it": "insediamento umano"
        #,"nb": "bosetning"
        ,"nl": "dal"
        #,"ru": "населённый пункт"
        #,"sco": "human settlement"
        },
    "Q29701762":{        
        "ar": "مستوطنة"
        ,"de": "Siedlung"
        ,"el": "οικισμός"
        ,"en": "human settlement"
        ,"eo": "setlejo"
        ,"es": "asentamiento"
        ,"et": "asula"
        ,"fa": "سکونتگاه انسانی"
        ,"fr": "établissement humain"
        ,"it": "insediamento umano"
        ,"nb": "bosetning"
        ,"nl": "nederzetting"
        ,"ru": "населённый пункт"
        ,"sco": "human settlement"
        },
    "Q8072":{        
        "ar": "بركان"
        ,"de": "Vulkan"
        #,"el": ""
        ,"en": "volcano"
        #,"eo": ""
        ,"es": "volcán"
        #,"et": ""
        #,"fa": ""
        #,"fr": ""
        #,"it": ""
        #,"nb": ""
        ,"nl": "vulkaan"
        #,"ru": ""
        #,"sco": ""
        },
    "Q184358":{        
        "ar": "شعاب"
        ,"de": "Riff"
        ,"el": "Ύφαλος"
        ,"en": "reef"
        ,"eo": "Rifo"
        ,"es": "arrecife"
        ,"et": "Kari"
        ,"fa": "آب‌سنگ"
        ,"fr": "récif"
        ,"it": "scogliera"
        ,"nb": "rev"
        ,"nl": "rif"
        ,"ru": "Риф"
        },
    "Q166735":{        
        "ar": "مستنقع"
        ,"de": "Sumpf"
        ,"el": "Έλος"
        ,"en": "swamp"
        ,"eo": "marĉo"
        ,"es": "pantano"
        ,"fa": "باتلاق"
        ,"fr": "marais"
        ,"it": "palude"
        ,"nb": "sump"
        ,"nl": "moeras"
        ,"ru": "болото"
        },
    "Q12323":{        
        "ar": "سد"
        ,"de": "Talsperre"
        ,"el": "Φράγμα"
        ,"en": "dam"
        ,"eo": "Akvobaraĵo"
        ,"es": "represa"
        ,"et": "Pais"
        ,"fa": "سد"
        ,"fr": "barrage"
        ,"it": "diga"
        ,"nb": "demning"
        ,"nl": "dam"
        ,"ru": "плотина"
        ,"sco": "dam"
        },
    "Q24529780":{        
        "ar": "نقطة"
        ,"en": "point"
        ,"es": "punta"
        },
    "Q637600":{        
        "ar": "سبخة"
        ,"de": "Sabcha"
        ,"en": "sabkha"
        ,"es": "Sebkha"
        ,"fr": "Sebkha"
        ,"it": "Sabkhah"
        },
    "Q54050":{        
        "ar": "تل"
        ,"de": "Hügel"
        ,"el": "λόφος"
        ,"en": "hill"
        ,"es": "colina"
        ,"et": "Küngas"
        ,"fa": "تپه"
        ,"fr": "colline"
        ,"it": "collina"
        ,"nb": "ås"
        ,"nl": "heuvel"
        ,"ru": "холм"
        },
    "Q165":{        
        "ar": "بحر"
        ,"de": "Meer"
        ,"el": "θάλασσα"
        ,"en": "sea"
        ,"eo": "maro"
        ,"es": "mar"
        ,"et": "Meri"
        ,"fa": "دریا"
        ,"fr": "mer"
        ,"it": "mare"
        ,"nb": "hav"
        ,"nl": "zee"
        ,"ru": "море"
        ,"sco": "sea"
        },      
    "Q25391":{        
        "ar": "كثيب"
        ,"de": "Düne"
        ,"el": "αμμόλοφος"
        ,"en": "dune"
        ,"eo": "Duno"
        ,"es": "Duna"
        ,"et": "Luide"
        ,"fa": "ریگ‌روان"
        ,"fr": "dune"
        ,"it": "Duna"
        ,"nb": "sanddyne"
        ,"nl": "duin"
        ,"ru": "Дюна"
        ,"sco": "dune"
        },
    "Q491713":{        
        "de": "Sund"
        ,"en": "sound"
        ,"es": "seno"
        ,"fa": "دریاراه"
        ,"fr": "bras de mer"
        ,"it": "sound"
        ,"nb": "sund"
        ,"nl": "sound"
        ,"ru": "зунд"
        },
    "Q23397":{        
        "ar": "بحيرة"
        ,"de": "See"
        ,"el": "λίμνη"
        ,"en": "lake"
        ,"eo": "lago"
        ,"es": "lago"
        ,"et": "Järv"
        ,"fa": "دریاچه"
        ,"fr": "lac"
        ,"it": "lago"
        ,"nb": "innsjø"
        ,"nl": "meer"
        ,"ru": "озеро"
        ,"sco": "loch"
        },
    "Q1174791":{        
        "ar": "جرف"
        ,"de": "Hang"
        ,"en": "escarpment"
        ,"es": "Escarpe"
        ,"fa": "دیواره"
        ,"fr": "escarpement"
        ,"it": "Scarpata"
        ,"ru": "вертикальное обнажение породы"
        },
    "Q17018380":{        
        "en": "bight"
        ,"es": "Ancón"
        },
    "Q131681":{        
        "ar": "خزان مائي"
        ,"de": "Stausee"
        ,"el": "Τεχνητή λίμνη"
        ,"en": "reservoir"
        ,"eo": "Baraĵlago"
        ,"es": "embalse"
        ,"et": "Veehoidla"
        ,"fa": "مخزن سد"
        ,"fr": "lac de barrage"
        ,"it": "bacino artificiale"
        ,"nb": "vannmagasin"
        ,"nl": "stuwmeer"
        ,"ru": "водохранилище"
        ,"sco": "reservoir"
        },
    "Q187223":{        
        "ar": "بحيرة شاطئة"
        ,"de": "Lagune"
        ,"el": "Λιμνοθάλασσα"
        ,"en": "lagoon"
        ,"eo": "Laguno"
        ,"es": "lagoon"
        ,"et": "Laguun"
        ,"fa": "مرداب"
        ,"fr": "lagune"
        ,"it": "laguna"
        ,"nb": "lagune"
        ,"nl": "lagune"
        ,"ru": "лагуна"
        ,"sco": "lagoon"
        },
    "Q16887036":{        
        "en": "gap"
        ,"fa": "گپ (زمین‌چهره)"
        },
    "Q4022":{        
        "ar": "نهر"
        ,"de": "Fluss"
        ,"el": "ποταμός"
        ,"en": "river"
        ,"eo": "rivero"
        ,"es": "río"
        ,"et": "Jõgi"
        ,"fa": "رود"
        ,"fr": "rivière"
        ,"it": "fiume"
        ,"nb": "elv"
        ,"nl": "rivier"
        ,"ru": "река"
        ,"sco": "river"
        },
    "Q179049":{        
        "ar": "محمية طبيعية"
        ,"de": "Naturschutzgebiet"
        ,"en": "nature reserve"
        ,"eo": "Naturrezervejo"
        ,"es": "reserva natural"
        ,"et": "Looduskaitseala"
        ,"fa": "ذخیره‌گاه طبیعی"
        ,"fr": "réserve naturelle"
        ,"it": "area naturale protetta"
        ,"nb": "naturreservat"
        ,"nl": "natuurreservaat"
        ,"ru": "заповедник"
        ,"sco": "naitur reserve"
        },
    "Q486972":{        
        "ar": "مستوطنة"
        ,"de": "Siedlung"
        ,"el": "οικισμός"
        ,"en": "human settlement"
        ,"eo": "setlejo"
        ,"es": "asentamiento"
        ,"et": "asula"
        ,"fa": "سکونتگاه انسانی"
        ,"fr": "établissement humain"
        ,"it": "insediamento umano"
        ,"nb": "bosetning"
        ,"nl": "nederzetting"
        ,"ru": "населённый пункт"
        ,"sco": "human settlement"
        },
    "Q740445":{        
        "ar": "نتوء جبلي"
        ,"de": "Gebirgskamm"
        ,"el": "οροσειρά"
        ,"en": "ridge"
        ,"eo": "Kresto"
        ,"es": "cresta"
        ,"fa": "خط‌الرأس"
        ,"fr": "crête"
        ,"nl": "bergkam"
        ,"ru": "Кряж"
        },
    "Q8502":{        
        "ar": "جبل"
        ,"de": "Berg"
        ,"el": "βουνό"
        ,"en": "mountain"
        ,"eo": "monto"
        ,"es": "montaña"
        ,"et": "Mägi"
        ,"fa": "کوه"
        ,"fr": "montagne"
        ,"it": "montagna"
        ,"nb": "fjell"
        ,"nl": "berg"
        ,"ru": "гора"
        ,"sco": "muntain"
        },
    "Q207326":{        
        "ar": "قمة جبل"
        ,"de": "Berggipfel"
        ,"el": "κορυφή"
        ,"en": "summit"
        ,"eo": "montopinto"
        ,"es": "cima"
        ,"et": "mäetipp"
        ,"fa": "قله"
        ,"fr": "sommet"
        ,"it": "vetta"
        ,"nb": "topp"
        ,"nl": "top"
        ,"ru": "вершина местности"
        ,"sco": "summit"
        },
    "Q23442":{        
        "ar": "جزيرة"
        ,"de": "Insel"
        ,"el": "νησί"
        ,"en": "island"
        ,"eo": "insulo"
        ,"es": "isla"
        ,"et": "saar"
        ,"fa": "جزیره"
        ,"fr": "île"
        ,"it": "isola"
        ,"nb": "øy"
        ,"nl": "eiland"
        ,"ru": "остров"
        ,"sco": "Island"
        },

    }
#---
'''placesTable["Q34679"] = {        
        "ar": "رمل"
        ,"de": "Sand"
        ,"el": "Άμμος"
        ,"en": "sand"
        ,"eo": "Sablo"
        ,"es": "arena"
        ,"et": "Liiv"
        ,"fa": "ماسه"
        ,"fr": "sable"
        ,"it": "sabbia"
        ,"nb": "sand"
        ,"nl": "zand"
        ,"ru": "Песок"
        ,"sco": "saund"
        }'''
#---
placesTable["Q12323"] = { "ar" : "سد" , "en" : "dam" }
placesTable["Q8502"] = { "ar" : "جبل" , "en" : "mountain" }

placesTable["Q207524"] = { "ar" : "جزيرة صغيرة" , "en" : "islet" }
placesTable["Q22698"] = { "ar" : "متنزه" , "en" : "park" }
placesTable["Q34795826"] = { "ar" : "" , "en" : "moor" }
placesTable["Q211748"] = { "ar" : "حقل نفط" , "en" : "oilfield" }

placesTable["Q54050"] = { "ar" : "تل" , "en" : "hill" }

placesTable["Q1248784"] = { "ar" : "مطار" , "en" : "airport" }
placesTable["Q591942"] = { "ar" : "فرع" , "en" : "distributary" }
placesTable["Q105190"] = { "ar" : "سد مائي" , "en" : "levee" }
placesTable["Q160091"] = { "ar" : "سهل" , "en" : "plain" }

placesTable["Q532"] = { "ar" : "قرية" , "en" : "village" }
placesTable["Q740445"] = { "ar" : "نتوء جبلي" , "en" : "ridge" }
placesTable["Q820477"] = { "ar" : "منجم" , "en" : "mine" }

placesTable["Q46831"] = { "ar" : "سلسلة جبلية" , "en" : "mountains" }
placesTable["Q150784"] = { "ar" : "أخدود" , "en" : "canyon" }
placesTable["Q27590"] = { "ar" : "براح" , "en" : "heath" }
placesTable["Q37901"] = { "ar" : "مضيق" , "en" : "strait" }
placesTable["Q107679"] = { "ar" : "جرف" , "en" : "cliff" }
placesTable["Q170321"] = { "ar" : "منطقة رطبة" , "en" : "wetland" }
placesTable["Q75520"] = { "ar" : "هضبة" , "en" : "plateau" }
placesTable["Q2935978"] = { "ar" : "قناة ري" , "en" : "irrigation canal" }
placesTable["Q190429"] = { "ar" : "منخفض" , "en" : "depression" }
placesTable["Q44782"] = { "ar" : "ميناء" , "en" : "port" }
#placesTable[""] = { "ar" : "" , "en" : "" }
#placesTable[""] = { "ar" : "" , "en" : "" }
#placesTable[""] = { "ar" : "" , "en" : "" }
#placesTable[""] = { "ar" : "" , "en" : "" }

placesTable["Q34379419"] = {        
        "ar": "منطقة رملية"
        ,"de": "Sandgebiet"
        ,"en": "sand area"
        }
        
        
        