#!/usr/bin/python
"""

إضافة تسميات عناصر ويكي بيانات

بناءاً على خاصية سبقه أو تبعه


"""
#
# (C) Ibrahem Qasim, 2022
#
#
# ---
from make.lists import Sport_key
# from make.Sport_key import Sports_Keys_For_Label #Sports_Keys_For_Team#Sports_Keys_For_Jobs#Sports_Keys_For_Label
# ---
Sports_Keys_Lab = Sport_key.Sports_Keys_For_Label
Sports_Keys_Team = Sport_key.Sports_Keys_For_Team
# ---
cccccups = {
    "FIS Alpine Ski World Cup": "كأس العالم للتزلج على المنحدرات الثلجية",
    "alpine skiing world cup": "كأس العالم للتزلج على المنحدرات الثلجية",
}
# ---
Mako_keys_4 = {
    "ice dance": "الرقص على الجليد",
    "freestyle pursuit": "مطاردة حرة",
    "female": "إناث",
    "male": "ذكور",
    "team": "فريق",
    "pairs": "مزدوج",
    "normal hill individual": "تل عادي فردي",
    "Two-man": "رجلين",
    "Two-woman": "سيدتين",
    "four-man": "4 رجال",
    "four-woman": "4 سيدات",
    "Cross-country skiing": "التزلج الريفي",
    "Cross country": "التزلج الريفي",
    "team race": "سباق الفريق",
}
# ---
Mako_keys2 = {
    "free skating": "تزلج حر",
    # "pair skating" : "التزلج الفني على الجليد" ,
    "pair skating": "تزلج مزدوج",
    "bantamweight": "وزن بانتام",
    "featherweight": "وزن الريشة",
    "lightweight": "وزن خفيف",
    "light heavyweight": "وزن ثقيل خفيف",
    "light-heavyweight": "وزن ثقيل خفيف",
    "light middleweight": "وزن خفيف متوسط",
    "middleweight": "وزن متوسط",
    "super heavyweight": "وزن ثقيل سوبر",
    " slalom ": "متعرج",
    "heavyweight": "وزن ثقيل",
    "welterweight": "وزن الويلتر",
    "classical": "كلاسيكي",
    "butterfly": "فراشة",
    "flyweight": "وزن الذبابة",
    "super middleweight": "وزن متوسط سوبر",
    "Pinweight": "وزن الذرة",
    "super flyweight": "وزن الذبابة سوبر",
    "super featherweight": "وزن الريشة سوبر",
    "super bantamweight": "وزن البانتام سوبر",
    "light flyweight": "وزن ذبابة خفيف",
    "light welterweight": "وزن والتر خفيف",
    "cruiserweight": "وزن الطراد",
    "Atomweight": "وزن الذرة",
    "super cruiserweight": "وزن الطراد سوبر",
    # ---
}
# ---
Mako_keys = {
    "tennis at the summer olympics": "كرة المضرب في الألعاب الأولمبية الصيفية",
    "tennis at the winter olympics": "كرة المضرب في الألعاب الأولمبية الشتوية",
    "team jumping": "القفز للفرق",
    "team eventing": "أحداث الفرق",
    "ice dancing": "الرقص على الجليد",
    "– qualification": "– تصفيات",
    "ice dancing": "الرقص على الجليد",
    "World Figure Skating Championships - ice dancing": "بطولة العالم للتزلج الفني - الرقص على الجليد",
    "World Figure Skating Championships": "بطولة العالم للتزلج الفني",
    "ladies' singles free skating": "تزلج حر فردي للسيدات",
    "men's singles free skating": "تزلج حر فردي للرجال",
}
# ---
International_Federation = {

    "FIL World Luge Championships": "كأس العالم للزحف الثلجي",
    "FIL under 23 World Luge Championships": "كأس العالم للزحف الثلجي تحت 23 سنة",


    "NCAA": "الرابطة الوطنية لرياضة الجامعات",
    "NCAA Men's Water Polo Championships": "بطولة كرة الماء للرجال للجامعات",
    "NCAA women's Water Polo Championships": "بطولة كرة الماء للسيدات للجامعات",
    "National Collegiate Athletic Association": "الرابطة الوطنية لرياضة الجامعات",
    "BWF World Championships": "بطولة العالم لكرة الريشة",
    "BWF World Junior Championships": "بطولة العالم لكرة الريشة للناشئين",

    "ConIFA World Football Cup": "كأس العالم لاتحاد الجمعيات المستقلة لكرة القدم",

    "ATP World Tour": "بطولات العالم لرابطة محترفي التنس",
    "ATP Challenger Tour": "بطولات تشالنجر لرابطة محترفي التنس",
    "ATP Tour": "رابطة محترفي التنس",
    "ATP Tour tournaments": "بطولات رابطة محترفي التنس",
    "ATP Tour tournaments": "بطولات رابطة محترفي التنس",
    "ATP World Tour": "بطولات العالم لرابطة محترفات التنس",
    "ATP Challenger Tour": "بطولات تشالنجر لرابطة محترفات التنس",

    "WTA Auckland Open": "أوكلاند المفتوحة للسيدات",
    "WTA Madrid Open (tennis)": "مدريد المفتوحة للسيدات (تنس)",
    "WTA Tour tournaments": "بطولات رابطة محترفات التنس",
    "WTA Tour tournaments": "بطولات رابطة محترفات التنس",
    "WTA Tour": "رابطة محترفات التنس",

    "UCI Continental Teams": "الفرق القارية للاتحاد الدولي للدراجات",
    "UCI Continental Teams (Asia)": "الفرق القارية للاتحاد الدولي للدراجات (آسيا)",
    "UCI Continental Teams (Africa)": "الفرق القارية للاتحاد الدولي للدراجات (أفريقيا)",
    "UCI Continental Teams (America)": "الفرق القارية للاتحاد الدولي للدراجات (أمريكا)",
    "UCI Continental Teams (Europe)": "الفرق القارية للاتحاد الدولي للدراجات (أوروبا)",
    "UCI Continental Teams (Oceania)": "الفرق القارية للاتحاد الدولي للدراجات (أوقيانوسيا)",
    "UCI Under 23 Nations' Cup": "كؤوس وطنية لسباقات الدراجات",
    "UCI World Championships": "بطولات العالم للدراجات",
    "UCI World Tour": "طواف العالم للدراجات",
    "UCI America Tour": "طواف أمريكا للدراجات",
    "UCI Asia Tour": "طواف آسيا للدراجات",
    "UCI Europe Tour": "طواف أوروبا للدراجات",
    "UCI Africa Tour": "طواف أفريقيا للدراجات",
    "UCI Oceania Tour": "طواف أوقيانوسيا للدراجات",
    "UCI Women's World Tour": "طواف العالم للدراجات للسيدات",
    "UCI America Tour": "طواف أمريكا للدراجات",
    "UCI Asia Tour": "طواف آسيا للدراجات",
    "UCI Europe Tour": "طواف أوروبا للدراجات",
    "UCI Africa Tour": "طواف أفريقيا للدراجات",
    "UCI Oceania Tour": "طواف أوقيانوسيا للدراجات",
    "Former UCI WorldTeams": "فرق دراجات هوائية عالمية سابقة",
    "UCI WorldTeam riders": "دراجو فرق دراجات هوائية عالمية",
    "UCI WorldTeams": "فرق دراجات هوائية عالمية",
    "UCI Track Cycling World Championships": "بطولة العالم للدراجات على المضمار",
    "UCI Mountain Bike World Cup": "كأس العالم للدراجات الجبلية",
    "UCI Road World Championships": "بطولة العالم لسباق الدراجات على الطريق",
    "UCI Road World Cup": "كأس العالم لسباق الدراجات على الطريق",
    "UCI Women's Road World Cup": "كأس العالم لسباق الدراجات على الطريق للسيدات",
    "UCI Track Cycling World Cup": "كأس العالم لسباق الدراجات على المضمار",
    "UCI Track Cycling World Cup Classics": "كأس العالم لسباق الدراجات على المضمار",
    "UCI Road World Championships – Men's road race": "سباق الطريق في بطولة العالم لسباق الدراجات على الطريق",
    "UCI Road World Championships – Men's team time trial": "سباق الطريق ضد الساعة للفرق في بطولة العالم لسباق الدراجات على الطريق",
    "UCI Track Cycling World Championships – Men's 1 km time trial": "سباق الكيلو متر ضد الساعة في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's individual pursuit": "سباق المطاردة الفردية في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's keirin": "سباق الكيرين في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's madison": "سباق ماديسون في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's omnium": "سباق الأومنيوم في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's points race": "سباق النقاط في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's scratch": "سباق الخدش - السكراتش في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's sprint": "سباق السرعة الفردية في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's team pursuit": "سباق المطاردة الفرقية في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Men's team sprint": "سباق السرعة الفردية للفرق في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's 500 m time trial": "سباق 500 متر ضد الساعة للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's individual pursuit": "سباق المطاردة الفردية للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's keirin": "سباق الكيرين للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's madison": "سباق ماديسون للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's omnium": "سباق الأومنيوم للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's points race": "سباق النقاط للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's scratch": "سباق الخدش للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's sprint": "سباق السرعة الفردية للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's team pursuit": "سباق المطاردة الفرقية للنساء في بطولة الدراجات على المضمار",
    "UCI Track Cycling World Championships – Women's team sprint": "سباق السرعة الفردية لفرق النساء في بطولة الدراجات على المضمار",

    "OFC U-17 Championships": "كأس أوقيانوسيا للأمم تحت 17 سنة",
    "OFC Nations Cup": "كأس أوقيانوسيا للأمم",
    "OFC U-20 Championships": "كأس أوقيانوسيا للأمم تحت 20 سنة",
    "OFC Nations Cup": "كأس أوقيانوسيا للأمم",
    "OFC U-17 Championships": "كأس أوقيانوسيا للأمم تحت 17 سنة",
    "OFC U-20 Championships": "كأس أوقيانوسيا للأمم تحت 20 سنة",
    "OFC Champions League": "دوري أبطال أوقيانوسيا",

    "AFC Asian Cup Finals": "نهائيات كأس آسيا",
    "AFC Futsal Championships": "بطولة آسيا لكرة القدم الخماسية",
    "AFC U-16 Women's Championships": "بطولة آسيا تحت 16 سنة لكرة القدم للسيدات",
    "AFC Futsal Championships": "بطولة آسيا لكرة القدم الخماسية",
    "AFC President's Cup": "كأس رئيس الاتحاد الآسيوي",
    "AFC Solidarity Cup": "كأس التضامن الآسيوي",
    "AFC Women's Asian Cup": "كأس الأمم الآسيوية لكرة القدم للسيدات",
    "AFC U-16 Championships": "بطولة آسيا للناشئين تحت 16 سنة",
    "AFC Asian Cup": "كأس آسيا",
    "AFC Futsal Club Championships": "بطولة آسيا لكرة القدم الخماسية للأندية",

    "CONCACAF Championships": "بطولة أمريكا الشمالية",
    "CONCACAF Gold Cup": "كأس الكونكاكاف الذهبية",
    "CONCACAF U17 Championships": "الكأس الذهبية تحت 17 سنة لكرة القدم",
    "CONCACAF Under-20 Championships": "الكأس الذهبية تحت 20 سنة لكرة القدم",
    "CONCACAF Women's Championships": "بطولة أمريكا الشمالية للسيدات",
    "CONCACAF Women's U-10 Championships": "بطولة أمريكا الشمالية للسيدات تحت 10 سنة",
    "CONCACAF Women's U-17 Championships": "بطولة أمريكا الشمالية للسيدات تحت 17 سنة",
    "CONCACAF U17 Championships": "الكأس الذهبية تحت 17 سنة لكرة القدم",
    "CONCACAF Champions League": "دوري أبطال الكونكاكاف",
    "CONCACAF Under-20 Championships": "الكأس الذهبية تحت 20 سنة لكرة القدم",

    "AFF U-23 Youth Championships": "بطولة اتحاد آسيان لكرة القدم",
    "AFF U-23 Championships": "بطولة اتحاد آسيان تحت 23 سنة",
    "AFF U-23 Youth Championships": "بطولة اتحاد آسيان تحت 23 سنة للشباب",
    "AFF Championships": "بطولة اتحاد آسيان لكرة القدم",

    "EHF Champions League": "دوري أبطال أوروبا لكرة اليد",
    "Women's EHF Champions League": "دوري أبطال أوروبا لكرة اليد للسيدات",
    "EHF Cup": "كأس أوروبا لكرة اليد",
    "Women's EHF Cup": "كأس أوروبا لكرة اليد للسيدات",
    "Women's EHF Challenge Cup": "كأس التحدي الأوروبية لكرة اليد للسيدات",
    "EHF Champions League": "دوري أبطال أوروبا لكرة اليد",
    "EHF Cup": "كأس أوروبا لكرة اليد",
    "Women's EHF Cup Winners' Cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "EHF Women's Cup Winners' Cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "EHF Women's Champions League": "دوري أبطال أوروبا لكرة اليد للسيدات",

    "AFC Champions League": "دوري أبطال آسيا",

    "ASEAN Football Championships": "بطولة اتحاد آسيان لكرة القدم",

    "FIBA EuroBasket": "بطولة أمم أوروبا لكرة السلة",
    "FIBA Basketball World Cup": "كأس العالم لكرة السلة",
    "FIBA Women's Basketball World Cup": "كأس العالم لكرة السلة للسيدات",

    "FIBA European Champions Cup": "كأس أبطال أوروبا لكرة السلة",
    "FIBA Women's European Champions Cup": "كأس أبطال أوروبا لكرة السلة للسيدات",
    "FIBA Women's World Cup": "كأس العالم لكرة السلة للسيدات",
    "FIBA World Cup": "كأس العالم لكرة السلة",

    "FIBA Asia Under-18 Championships": "بطولة فيبا آسيا تحت 18 سنة لكرة السلة",
    "FIBA Under-20 World Championships": "بطولة العالم تحت 20 سنة لكرة السلة",
    "FIBA Under-19 World Championships": "بطولة العالم تحت 19 سنة لكرة السلة",
    "FIBA Under-18 World Championships": "بطولة العالم تحت 18 سنة لكرة السلة",
    "FIBA Under-17 World Championships": "بطولة العالم تحت 17 سنة لكرة السلة",
    "FIBA Under-16 World Championships": "بطولة العالم تحت 16 سنة لكرة السلة",
    "FIBA competitions": "منافسات الاتحاد الدولي لكرة السلة",
    "FIBA Korać Cup": "كأس كوراتش لكرة السلة",
    "FIBA Saporta Cup": "كأس سابورتا",
    "FIBA Asia Cup": "كأس أمم آسيا لكرة السلة",
    "FIBA Basketball World Cup": "كأس العالم لكرة السلة",
    "FIBA Americas League": "دوري الأمريكتين لكرة السلة",
    "FIBA Americas Championships": "بطولة أمم الأمريكتين لكرة السلة",
    "FIBA": "الاتحاد الدولي لكرة السلة",
    "FIBA AmeriCup": "بطولة أمم الأمريكتين لكرة السلة",
    "FIBA Africa Championships": "بطولة أمم أفريقيا لكرة السلة",
    "FIBA EuroBasket": "بطولة أمم أوروبا لكرة السلة",
    "FIBA Asia Championships": "بطولة أمم آسيا لكرة السلة",
    "FIBA Basketball World Cup": "بطولة كأس العالم لكرة السلة",
    "FIBA World Championships": "بطولة كأس العالم لكرة السلة",
    "FIBA World Championship for Women": "بطولة كأس العالم لكرة السلة للسيدات",
    "FIBA Korać Cup": "كأس كوراتش لكرة السلة",

    "FIFA World Cup": "كأس العالم لكرة القدم",
    # "FIFA World Cup":"كأس العالم",
    # "FIFA Women's World Cup":"كأس العالم للسيدات",
    "FIFA Women's World Cup": "كأس العالم لكرة القدم للسيدات",
    "FIFA U-17 World Cup": "كأس العالم تحت 17 سنة لكرة القدم",
    "FIFA U-17 Women's World Cup": "كأس العالم تحت 17 سنة لكرة القدم للسيدات",
    "FIFA U-20 World Cup": "كأس العالم تحت 20 سنة لكرة القدم",
    "FIFA U-20 Women's World Cup": "كأس العالم تحت 20 سنة لكرة القدم للسيدات",
    "the FIFA World Cup": "كأس العالم لكرة القدم",
    "FIFA Club World Cup": "كأس العالم للأندية",
    "FIFA Beach Soccer World Cup": "كأس العالم الشاطئية",
    "FIFA World Cup qualification (CAF)": "تصفيات كأس العالم لكرة القدم (أفريقيا)",
    "FIFA World Cup qualification (AFC)": "تصفيات كأس العالم لكرة القدم (آسيا)",
    "FIFA Women's World Cup qualification": "تصفيات كأس العالم لكرة القدم للسيدات",
    "FIFA Futsal World Cup Ney": "بطولة كأس العالم داخل الصالات",
    "FIFA World Cup players": "لاعبو كأس العالم لكرة القدم",
    "The Best FIFA Football Awards": "جوائز الفيفا للأفضل كرويا",

    "IAAF Continental Cup": "كأس العالم لألعاب القوى",
    "IAAF World U20 Championships": "بطولة العالم للناشئين لألعاب القوى",
    "IAAF Diamond League": "دوري ماسي",
    "IAAF World Indoor Championships in Athletics": "بطولة العالم لألعاب القوى داخل الصالات",
    "IAAF World Cross Country Championships": "بطولة العالم للعدو الريفي",
    "IAAF World Indoor Championships in Athletics": "بطولة العالم لألعاب القوى داخل الصالات",
    "IAAF World Indoor Championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "IAAF World Indoor Games": "بطولة العالم لألعاب القوى داخل الصالات",
    "IAAF World Junior Championships in Athletics": "بطولة العالم للناشئين لألعاب القوى",
    "IAAF World Cross Country Championships": "بطولة العالم للعدو الريفي",
    "IAAF World Indoor Championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "IAAF World Indoor Games": "بطولة العالم لألعاب القوى داخل الصالات",

    "SAFF Championships": "بطولة اتحاد جنوب آسيا لكرة القدم",
    "SAFF Championships": "بطولة اتحاد جنوب آسيا لكرة القدم",

    "FIS Nordic World Ski Championships": "بطولة العالم للتزلج النوردي على الثلج",
    "FIS Nordic World Ski Championships": "بطولة العالم للتزلج النوردي على الثلج",

    "FIVB Women's Volleyball World Championships": "بطولة العالم لكرة الطائرة للسيدات",
    "FIVB Volleyball World Cup": "كأس العالم لكرة الطائرة",
    "FIVB Volleyball Women's World Cup": "كأس العالم لكرة الطائرة للسيدات",
    "FIVB Volleyball Men's World Championships": "بطولة العالم للكرة الطائرة",
    "FIVB Volleyball World Championships": "بطولة العالم لكرة الطائرة",
    "FIVB Volleyball World League": "الدوري العالمي للكرة الطائرة",

    "IIHF World Championships": "بطولة العالم للهوكي على الجليد",
    "IIHF World Championships": "بطولة العالم لهوكي الجليد",
    "IIHF Challenge Cup of Asia": "كأس التحدي الآسيوي لهوكي الجليد",

    # "UEFA Euro":"بطولة أمم أوروبا لكرة القدم",
    "UEFA Futsal Championships": "بطولة أمم أوروبا لكرة الصالات",
    "UEFA Women's Euro": "بطولة أمم أوروبا لكرة القدم للسيدات",
    "UEFA Champions League": "دوري أبطال أوروبا",
    "UEFA Euro 2004 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم 2004",
    "UEFA European Championship video games": "ألعاب فيديو بطولة أمم أوروبا لكرة القدم",
    "UEFA Futsal Euro 2012": "بطولة أوروبا لكرة الصالات 2012",
    "UEFA Women's Euro 1993": "بطولة أمم أوروبا لكرة القدم للسيدات 1993",
    "UEFA Women's Euro 1995": "بطولة أمم أوروبا لكرة القدم للسيدات 1995",
    "UEFA Women's Euro 1997": "بطولة أمم أوروبا لكرة القدم للسيدات 1997",
    "UEFA Women's Euro 2009": "بطولة أمم أوروبا لكرة القدم للسيدات 2009",
    "UEFA Women's Euro 2013": "بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "UEFA Women's Euro 2013 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "UEFA Women's Euro 2017": "بطولة أمم أوروبا لكرة القدم للسيدات 2017",
    "UEFA Women's Under-17 Championships": "بطولة أوروبا تحت 17 سنة لكرة القدم للسيدات",
    "UEFA Europa League": "الدوري الأوروبي",
    "UEFA Women's Championships": "بطولة أمم أوروبا للسيدات",
    "UEFA Futsal Euro": "بطولة أوروبا لكرة الصالات",
    "UEFA Euro": "بطولة أمم أوروبا",
    "UEFA Champions League": "دوري أبطال أوروبا",
    "2017–18 UEFA Champions League": "دوري أبطال أوروبا 2017–18",
    # "UEFA European Championships":"بطولة أمم أوروبا لكرة القدم",
    "UEFA Nations League": "دوري الأمم الأوروبية",
    "UEFA European Championship qualifying": "تصفيات بطولة أمم أوروبا",
    "UEFA Super Cup": "كأس السوبر الأوروبي",
    "UEFA Cup": "كأس الاتحاد الأوروبي",
    "UEFA Intertonto": "كأس إنترتوتو",
    "UEFA Cup Winners' Cup": "كأس الكؤوس الأوروبية",
    "UEFA Regions' Cup": "كأس المقاطعات الأوروبية",
    "UEFA European Championships": "بطولة أمم أوروبا",
    "UEFA European Football Championships": "بطولة أمم أوروبا",
    "UEFA European Under-10 Championships": "بطولة أمم أوروبا تحت 10 سنة",
    "UEFA Europa League": "الدوري الأوروبي",
    "UEFA Youth League": "الدوري الأوروبي للشباب",
    "UEFA Futsal Championships": "بطولة أمم أوروبا داخل الصالات",
    "UEFA European Under-16 Football Championships": "بطولة أوروبا تحت 16 سنة لكرة القدم",
    "UEFA European Under-17 Football Championships": "بطولة أوروبا تحت 17 سنة لكرة القدم",
    "UEFA Women's Under-17 Championships": "بطولة أوروبا تحت 17 سنة لكرة القدم للسيدات",
    "UEFA European Under-19 Football Championships": "بطولة أوروبا تحت 19 سنة لكرة القدم",
    "UEFA Women's Under-19 Championships": "بطولة أوروبا تحت 19 سنة لكرة القدم للسيدات",
    "UEFA European Under-21 Championships": "بطولة أوروبا تحت 21 سنة لكرة القدم",
    "UEFA European Under-21 Football Championships": "بطولة أوروبا تحت 21 سنة لكرة القدم",

    "CAF Confederation Cup": "كأس الكونفيدرالية الأفريقية",
    "CAF Champions League": "دوري أبطال أفريقيا",

    "UNAF U-17 Tournament": "بطولة أمم شمال أفريقيا تحت 17 سنة",
    "UNAF U-20 Tournament": "بطولة أمم شمال أفريقيا تحت 20 سنة",
    "UNAF Club Cup": "كأس اتحاد شمال أفريقيا",
    "UNAF U-17 Tournament": "بطولة أمم شمال أفريقيا تحت 17 سنة",
    "UNAF Club Cup": "كأس اتحاد شمال أفريقيا",
    "UNAF U-20 Tournament": "بطولة أمم شمال أفريقيا تحت 20 سنة",
    "UNAF U-23 Tournament": "بطولة أمم شمال أفريقيا تحت 23 سنة",

    "FINA World Aquatics Championships": "بطولة العالم للألعاب المائية",
    "FINA Water Polo World League": "الدوري العالمي لكرة الماء",
    "FINA": "الاتحاد الدولي للسباحة",
    "FINA World Swimming Championships (25 m)": "بطولة العالم للسباحة (25 متر)",
    "FINA World Swimming Championships": "بطولة العالم للسباحة",
    "FINA World Aquatics Championships": "بطولة العالم للألعاب المائية",

}
# ---
olympics = {
    "Women's 500 m time trial": "سباق 500 متر ضد الساعة للسيدات",
    "Women's individual pursuit": "سباق المطاردة الفردية للسيدات",
    "Women's keirin": "سباق الكيرين للسيدات",
    "Women's madison": "سباق ماديسون للسيدات",
    "Women's omnium": "سباق الأومنيوم للسيدات",
    "Women's points race": "سباق النقاط للسيدات",
    "Women's scratch": "سباق الخدش للسيدات",
    "Women's sprint": "سباق السرعة الفردية للسيدات",
    "Women's team pursuit": "سباق المطاردة الفرقية للسيدات",
    "Women's team sprint": "سباق السرعة الفردية لفرق السيدات",
    # ---
    "Women's road race": "سباق الطريق للسيدات",
    "Women's time trial": "سباق الطريق ضد الساعة للسيدات",
    "Women's road race": "سباق الطريق للسيدات",
    "Women's time trial": "سباق الطريق ضد الساعة للسيدات",
    # ---

    "Men's road race": "سباق الطريق",
    "Men's team time trial": "سباق الطريق ضد الساعة للفرق",
    "Men's 1 km time trial": "سباق الكيلو متر ضد الساعة",
    "Men's individual pursuit": "سباق المطاردة الفردية",
    "Men's keirin": "سباق الكيرين",
    "Men's madison": "سباق ماديسون",
    "Men's omnium": "سباق الأومنيوم",
    "Men's points race": "سباق النقاط",
    "Men's scratch": "سباق الخدش - السكراتش",
    "Men's sprint": "سباق السرعة الفردية",
    "Men's team pursuit": "سباق المطاردة الفرقية",
    "Men's team sprint": "سباق السرعة الفردية للفرق",
}
# ---
for fff, ffflab in Sports_Keys_Team.items():  # – winter youth olympics
    # cccccups["%s world Championships" %  fff.lower() ] = "بطولة العالم %s"  % ffflab
    cccccups[f"{fff.lower()} world championships"] = f"بطولة العالم {ffflab}"
    cccccups[f"world team {fff.lower()} championships"] = f"بطولة العالم {ffflab} للفرق"
    cccccups[f"{fff.lower()} world team championships"] = f"بطولة العالم {ffflab} للفرق"
    cccccups[f"world men's {fff.lower()} championships"] = f"بطولة العالم {ffflab} للرجال"
    cccccups[f"{fff.lower()} world men's championships"] = f"بطولة العالم {ffflab} للرجال"
    cccccups[f"world women's {fff.lower()} championships"] = f"بطولة العالم {ffflab} للسيدات"
    cccccups[f"{fff.lower()} world women's championships"] = f"بطولة العالم {ffflab} للسيدات"
# ---
for fff, ffflab in Sports_Keys_Lab.items():  # – winter youth olympics
    olympics[f"{fff.lower()} at the summer olympics"] = f"{ffflab} في الألعاب الأولمبية الصيفية"
    olympics[f"{fff.lower()} at the winter youth olympics"] = f"{ffflab} في الألعاب الأولمبية الشبابية الشتوية"
    olympics[f"{fff.lower()} at the winter olympics"] = f"{ffflab} في الألعاب الأولمبية الشتوية"
    Mako_keys_4[f" mens's {fff.lower()}"] = f"{ffflab} للرجال"
    Mako_keys_4[f" womens's {fff.lower()}"] = f"{ffflab} للسيدات"
    # Mako_keys_4[ fff.lower() ] = ffflab
# ---
# individual
# jumping
keys_1 = {
    "individual": "فردي",
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "women's": "سيدات",
    "womens": "سيدات",
    "ladies": "سيدات",
    "ladies": "سيدات",
    "mens": "رجال",
    "men's": "رجال",
    # ---
}  # men's individual road race
# ---
keys_2 = {
    "tournament": "مسابقة",
    # "single" : "فردي",
    "individual": "فردي",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team pursuit": "مطاردة الفرق",
    "large hill": "تل كبير",
    "normal hill": "تل عادي",
    "team": "فريق",
    "decathlon": "ديكاتلون",
    # "double" : "زوجي",
    "doubles": "زوجي",
    # "single sculls" : "تجديف فردي",
    # "double sculls" : "تجديف زوجي",
    # "quadruple sculls" : "تجديف رباعي",
    # "coxless pair" : "رباعي مزدوج",
    "quadruple": "رباعي",
    "coxless": "رباعي",
    "jumping": "قفز",
}
# ---
keys_3 = {
    "road race": "سباق الطريق",
    "pursuit": "مطاردة",
    "team": "فريق",
    "decathlon": "ديكاتلون",
    "individual": "فردي",
    "sculls": "تجديف",
    "pair": "مزدوج",
}
# ---
for start in keys_1:  # –
    for suff in keys_2:  # –
        lab_ke = f"{keys_2[suff]} {keys_1[start]}"
        # ---
        ke = f"{start} {suff}"
        Mako_keys2[ke.lower()] = lab_ke
        # ---
        ke44 = f"{suff} {start}"
        Mako_keys2[ke44.lower()] = lab_ke
        for su3 in keys_3:
            lab_ke3 = f"{keys_2[suff]} {keys_1[start]} {keys_3[su3]}"
            # ---
            ke3 = f"{start} {suff} {su3}"
            Mako_keys2[ke3.lower()] = lab_ke3
            # ---
            lab_ke2 = f"{keys_2[suff]} {keys_3[su3]}"
            # ---
            ke2 = f"{suff} {su3}"
            Mako_keys2[ke2.lower()] = lab_ke2
# ---
