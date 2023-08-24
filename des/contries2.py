#!/usr/bin/python
#  python pwb.py wd/wikinews
#
#
ContriesTable2 = {
    "Q27": {
        "ar": "جمهورية أيرلندا",
        "en": "the Republic of Ireland",
    },
    "Q851": {
        "ar": "السعودية",
        "en": "Saudi Arabia",
    },
    "Q928": {
        "ar": "الفلبين",
        "en": "the Philippines",
    },
    "Q1410": {
        "ar": "جبل طارق",
        "en": "Gibraltar",
    },
    "Q804": {
        "ar": "بنما",
        "en": "Panama",
    },
    "Q800": {
        "ar": "كوستاريكا",
        "en": "Costa Rica",
    },
    "Q419": {
        "ar": "بيرو",
        "en": "Peru",
    },
    "Q668": {
        "ar": "الهند",
        "en": "India",
    },
    "Q1019": {
        "ar": "مدغشقر",
        "en": "Madagascar",
    },
    "Q664": {
        "ar": "نيوزيلندا",
        "en": "New Zealand",
    },
    "Q414": {
        "ar": "الأرجنتين",
        "en": "Argentina",
    },
    "Q142": {
        "ar": "فرنسا",
        "en": "France",
    },
    "Q55": {
        "ar": "هولندا",
        "en": "the Netherlands",
    },
    "Q13353": {
        "ar": "مونتسرات",
        "en": "Montserrat",
    },
    "Q32": {
        "ar": "لوكسمبورغ",
        "en": "Luxembourg",
    },
    "Q781": {
        "ar": "أنتيغوا وباربودا",
        "en": "Antigua and Barbuda",
    },
    "Q25279": {
        "ar": "كوراساو",
        "en": "Curaçao",
    },
    "Q783": {
        "ar": "هندوراس",
        "en": "Honduras",
    },
    "Q784": {
        "ar": "دومينيكا",
        "en": "Dominica",
    },
    "Q785": {
        "ar": "جيرزي",
        "en": "Jersey",
    },
    "Q786": {
        "ar": "جمهورية الدومينيكان",
        "en": "the Dominican Republic",
    },
    "Q37": {
        "ar": "ليتوانيا",
        "en": "Lithuania",
    },
    "Q1011": {
        "ar": "الرأس الأخضر",
        "en": "Cape Verde",
    },
    "Q833": {
        "ar": "ماليزيا",
        "en": "Malaysia",
    },
    "Q711": {
        "ar": "منغوليا",
        "en": "Mongolia",
    },
    "Q710": {
        "ar": "كيريباتي",
        "en": "Kiribati",
    },
    "Q717": {
        "ar": "فنزويلا",
        "en": "Venezuela",
    },
    "Q837": {
        "ar": "نيبال",
        "en": "Nepal",
    },
    "Q34": {
        "ar": "السويد",
        "en": "Sweden",
    },
    "Q183": {
        "ar": "ألمانيا",
        "en": "Germany",
    },
    "Q35555": {
        "ar": "واليس وفوتونا",
        "en": "Wallis and Futuna",
    },
    "Q408": {
        "ar": "أستراليا",
        "en": "Australia",
    },
    "Q252": {
        "ar": "إندونيسيا",
        "en": "Indonesia",
    },
    "Q399": {
        "ar": "أرمينيا",
        "en": "Armenia",
    },
    "Q398": {
        "ar": "البحرين",
        "en": "Bahrain",
    },
    "Q403": {
        "ar": "صربيا",
        "en": "Serbia",
    },
    "Q657": {
        "ar": "تشاد",
        "en": "Chad",
    },
    "Q258": {
        "ar": "جنوب أفريقيا",
        "en": "South Africa",
    },
    "Q21203": {
        "ar": "أروبا",
        "en": "Aruba",
    },
    "Q805": {
        "ar": "اليمن",
        "en": "Yemen",
    },
    "Q45": {
        "ar": "البرتغال",
        "en": "Portugal",
    },
    "Q159": {
        "ar": "روسيا",
        "en": "Russia",
    },
    "Q43": {
        "ar": "تركيا",
        "en": "Turkey",
    },
    "Q40": {
        "ar": "النمسا",
        "en": "Austria",
    },
    "Q41": {
        "ar": "اليونان",
        "en": "Greece",
    },
    "Q155": {
        "ar": "البرازيل",
        "en": "Brazil",
    },
    "Q792": {
        "ar": "السلفادور",
        "en": "El Salvador",
    },
    "Q790": {
        "ar": "هايتي",
        "en": "Haiti",
    },
    "Q796": {
        "ar": "العراق",
        "en": "Iraq",
    },
    "Q794": {
        "ar": "إيران",
        "en": "Iran",
    },
    "Q23635": {
        "ar": "جزر برمودا",
        "en": "Bermuda",
    },
    "Q954": {
        "ar": "زيمبابوي",
        "en": "Zimbabwe",
    },
    "Q889": {
        "ar": "أفغانستان",
        "en": "Afghanistan",
    },
    "Q884": {
        "ar": "كوريا الجنوبية",
        "en": "South Korea",
    },
    "Q958": {
        "ar": "جنوب السودان",
        "en": "South Sudan",
    },
    "Q881": {
        "ar": "فيتنام",
        "en": "Vietnam",
    },
    "Q986": {
        "ar": "إريتريا",
        "en": "Eritrea",
    },
    "Q14773": {
        "ar": "ماكاو",
        "en": "Macau",
    },
    "Q822": {
        "ar": "لبنان",
        "en": "Lebanon",
    },
    "Q241": {
        "ar": "كوبا",
        "en": "Cuba",
    },
    "Q242": {
        "ar": "بليز",
        "en": "Belize",
    },
    "Q244": {
        "ar": "باربادوس",
        "en": "Barbados",
    },
    "Q424": {
        "ar": "كمبوديا",
        "en": "Cambodia",
    },
    "Q33": {
        "ar": "فنلندا",
        "en": "Finland",
    },
    "Q921": {
        "ar": "بروناي",
        "en": "Brunei",
    },
    "Q31": {
        "ar": "بلجيكا",
        "en": "Belgium",
    },
    "Q30": {
        "ar": "الولايات المتحدة الأمريكية",
        "en": "the United States of America",
    },
    "Q924": {
        "ar": "تنزانيا",
        "en": "Tanzania",
    },
    "Q36": {
        "ar": "بولندا",
        "en": "Poland",
    },
    "Q35": {
        "ar": "الدنمارك",
        "en": "Denmark",
    },
    "Q730": {
        "ar": "سورينام",
        "en": "Suriname",
    },
    "Q929": {
        "ar": "جمهورية أفريقيا الوسطى",
        "en": "the Central African Republic",
    },
    "Q39": {
        "ar": "سويسرا",
        "en": "Switzerland",
    },
    "Q38": {
        "ar": "إيطاليا",
        "en": "Italy",
    },
    "Q858": {
        "ar": "سوريا",
        "en": "Syria",
    },
    "Q423": {
        "ar": "كوريا الشمالية",
        "en": "North Korea",
    },
    "Q983": {
        "ar": "غينيا الاستوائية",
        "en": "Equatorial Guinea",
    },
    "Q733": {
        "ar": "باراغواي",
        "en": "Paraguay",
    },
    "Q854": {
        "ar": "سريلانكا",
        "en": "Sri Lanka",
    },
    "Q734": {
        "ar": "غيانا",
        "en": "Guyana",
    },
    "Q736": {
        "ar": "الإكوادور",
        "en": "Ecuador",
    },
    "Q1013": {
        "ar": "ليسوتو",
        "en": "Lesotho",
    },
    "Q235": {
        "ar": "موناكو",
        "en": "Monaco",
    },
    "Q236": {
        "ar": "الجبل الأسود",
        "en": "Montenegro",
    },
    "Q230": {
        "ar": "جورجيا",
        "en": "Georgia",
    },
    "Q232": {
        "ar": "كازاخستان",
        "en": "Kazakhstan",
    },
    "Q233": {
        "ar": "مالطا",
        "en": "Malta",
    },
    "Q334": {
        "ar": "سنغافورة",
        "en": "Singapore",
    },
    "Q145": {
        "ar": "المملكة المتحدة",
        "en": "the United Kingdom",
    },
    "Q20": {
        "ar": "النرويج",
        "en": "Norway",
    },
    "Q1045": {
        "ar": "الصومال",
        "en": "Somalia",
    },
    "Q1044": {
        "ar": "سيراليون",
        "en": "Sierra Leone",
    },
    "Q1042": {
        "ar": "سيشل",
        "en": "Seychelles",
    },
    "Q1041": {
        "ar": "السنغال",
        "en": "Senegal",
    },
    "Q262": {
        "ar": "الجزائر",
        "en": "Algeria",
    },
    "Q28": {
        "ar": "المجر",
        "en": "Hungary",
    },
    "Q29": {
        "ar": "إسبانيا",
        "en": "Spain",
    },
    "Q819": {
        "ar": "لاوس",
        "en": "Laos",
    },
    "Q148": {
        "ar": "الصين",
        "en": "People's Republic of China",
    },
    "Q1049": {
        "ar": "السودان",
        "en": "Sudan",
    },
    "Q1025": {
        "ar": "موريتانيا",
        "en": "Mauritania",
    },
    "Q1027": {
        "ar": "موريشيوس",
        "en": "Mauritius",
    },
    "Q1020": {
        "ar": "مالاوي",
        "en": "Malawi",
    },
    "Q189": {
        "ar": "آيسلندا",
        "en": "Iceland",
    },
    "Q843": {
        "ar": "باكستان",
        "en": "Pakistan",
    },
    "Q842": {
        "ar": "سلطنة عمان",
        "en": "Oman",
    },
    "Q184": {
        "ar": "روسيا البيضاء",
        "en": "Belarus",
    },
    "Q1029": {
        "ar": "موزمبيق",
        "en": "Mozambique",
    },
    "Q846": {
        "ar": "قطر",
        "en": "Qatar",
    },
    "Q265": {
        "ar": "أوزبكستان",
        "en": "Uzbekistan",
    },
    "Q228": {
        "ar": "أندورا",
        "en": "Andorra",
    },
    "Q227": {
        "ar": "أذربيجان",
        "en": "Azerbaijan",
    },
    "Q225": {
        "ar": "البوسنة والهرسك",
        "en": "Bosnia and Herzegovina",
    },
    "Q224": {
        "ar": "كرواتيا",
        "en": "Croatia",
    },
    "Q223": {
        "ar": "غرينلاند",
        "en": "Greenland",
    },
    "Q222": {
        "ar": "ألبانيا",
        "en": "Albania",
    },
    "Q221": {
        "ar": "جمهورية مقدونيا",
        "en": "the Republic of Macedonia",
    },
    "Q96": {
        "ar": "المكسيك",
        "en": "Mexico",
    },
    "Q229": {
        "ar": "قبرص",
        "en": "Cyprus",
    },
    "Q347": {
        "ar": "ليختنشتاين",
        "en": "Liechtenstein",
    },
    "Q1050": {
        "ar": "سوازيلاند",
        "en": "Swaziland",
    },
    "Q17": {
        "ar": "اليابان",
        "en": "Japan",
    },
    "Q16": {
        "ar": "كندا",
        "en": "Canada",
    },
    "Q1028": {
        "ar": "المغرب",
        "en": "Morocco",
    },
    "Q902": {
        "ar": "بنغلاديش",
        "en": "Bangladesh",
    },
    "Q25230": {
        "ar": "غيرنزي",
        "en": "Guernsey",
    },
    "Q1036": {
        "ar": "أوغندا",
        "en": "Uganda",
    },
    "Q1008": {
        "ar": "ساحل العاج",
        "en": "Ivory Coast",
    },
    "Q1032": {
        "ar": "النيجر",
        "en": "Niger",
    },
    "Q1033": {
        "ar": "نيجيريا",
        "en": "Nigeria",
    },
    "Q1030": {
        "ar": "ناميبيا",
        "en": "Namibia",
    },
    "Q191": {
        "ar": "إستونيا",
        "en": "Estonia",
    },
    "Q965": {
        "ar": "بوركينا فاسو",
        "en": "Burkina Faso",
    },
    "Q967": {
        "ar": "بوروندي",
        "en": "Burundi",
    },
    "Q962": {
        "ar": "بنين",
        "en": "Benin",
    },
    "Q963": {
        "ar": "بوتسوانا",
        "en": "Botswana",
    },
    "Q697": {
        "ar": "ناورو",
        "en": "Nauru",
    },
    "Q298": {
        "ar": "تشيلي",
        "en": "Chile",
    },
    "Q695": {
        "ar": "بالاو",
        "en": "Palau",
    },
    "Q115": {
        "ar": "إثيوبيا",
        "en": "Ethiopia",
    },
    "Q114": {
        "ar": "كينيا",
        "en": "Kenya",
    },
    "Q117": {
        "ar": "غانا",
        "en": "Ghana",
    },
    "Q754": {
        "ar": "ترينيداد وتوباغو",
        "en": "Trinidad and Tobago",
    },
    "Q750": {
        "ar": "بوليفيا",
        "en": "Bolivia",
    },
    "Q212": {
        "ar": "أوكرانيا",
        "en": "Ukraine",
    },
    "Q213": {
        "ar": "التشيك",
        "en": "the Czech Republic",
    },
    "Q211": {
        "ar": "لاتفيا",
        "en": "Latvia",
    },
    "Q217": {
        "ar": "مولدافيا",
        "en": "Moldova",
    },
    "Q214": {
        "ar": "سلوفاكيا",
        "en": "Slovakia",
    },
    "Q215": {
        "ar": "سلوفينيا",
        "en": "Slovenia",
    },
    "Q218": {
        "ar": "رومانيا",
        "en": "Romania",
    },
    "Q219": {
        "ar": "بلغاريا",
        "en": "Bulgaria",
    },
    "Q912": {
        "ar": "مالي",
        "en": "Mali",
    },
    "Q917": {
        "ar": "بوتان",
        "en": "Bhutan",
    },
    "Q916": {
        "ar": "أنغولا",
        "en": "Angola",
    },
    "Q1000": {
        "ar": "الغابون",
        "en": "Gabon",
    },
    "Q1007": {
        "ar": "غينيا بيساو",
        "en": "Guinea-Bissau",
    },
    "Q1006": {
        "ar": "غينيا",
        "en": "Guinea",
    },
    "Q1005": {
        "ar": "غامبيا",
        "en": "the Gambia",
    },
    "Q712": {
        "ar": "فيجي",
        "en": "Fiji",
    },
    "Q977": {
        "ar": "جيبوتي",
        "en": "Djibouti",
    },
    "Q1009": {
        "ar": "الكاميرون",
        "en": "Cameroon",
    },
    "Q974": {
        "ar": "جمهورية الكونغو الديمقراطية",
        "en": "the Democratic Republic of the Congo",
    },
    "Q971": {
        "ar": "جمهورية الكونغو",
        "en": "the Republic of the Congo",
    },
    "Q970": {
        "ar": "جزر القمر",
        "en": "the Comoros",
    },
    "Q683": {
        "ar": "ساموا",
        "en": "Samoa",
    },
    "Q769": {
        "ar": "غرينادا",
        "en": "Grenada",
    },
    "Q685": {
        "ar": "جزر سليمان",
        "en": "the Solomon Islands",
    },
    "Q686": {
        "ar": "فانواتو",
        "en": "Vanuatu",
    },
    "Q836": {
        "ar": "ميانمار",
        "en": "Myanmar",
    },
    "Q766": {
        "ar": "جامايكا",
        "en": "Jamaica",
    },
    "Q574": {
        "ar": "تيمور الشرقية",
        "en": "East Timor",
    },
    "Q874": {
        "ar": "تركمانستان",
        "en": "Turkmenistan",
    },
    "Q6250": {
        "ar": "الصحراء الغربية",
        "en": "Western Sahara",
    },
    "Q79": {
        "ar": "مصر",
        "en": "Egypt",
    },
    "Q77": {
        "ar": "الأوروغواي",
        "en": "Uruguay",
    },
    "Q878": {
        "ar": "الإمارات العربية المتحدة",
        "en": "the United Arab Emirates",
    },
    "Q774": {
        "ar": "غواتيمالا",
        "en": "Guatemala",
    },
    "Q948": {
        "ar": "تونس",
        "en": "Tunisia",
    },
    "Q817": {
        "ar": "الكويت",
        "en": "Kuwait",
    },
    "Q810": {
        "ar": "الأردن",
        "en": "Jordan",
    },
    "Q811": {
        "ar": "نيكاراغوا",
        "en": "Nicaragua",
    },
    "Q813": {
        "ar": "قيرغيزستان",
        "en": "Kyrgyzstan",
    },
    "Q1014": {
        "ar": "ليبيريا",
        "en": "Liberia",
    },
    "Q1016": {
        "ar": "ليبيا",
        "en": "Libya",
    },
    "Q1246": {
        "ar": "كوسوفو",
        "en": "Kosovo",
    },
    "Q739": {
        "ar": "كولومبيا",
        "en": "Colombia",
    },
    "Q778": {
        "ar": "باهاماس",
        "en": "the Bahamas",
    },
    "Q945": {
        "ar": "توغو",
        "en": "Togo",
    },
    "Q25228": {
        "ar": "أنغويلا",
        "en": "Anguilla",
    },
    "Q678": {
        "ar": "تونغا",
        "en": "Tonga",
    },
    "Q26273": {
        "ar": "سينت مارتن",
        "en": "Sint Maarten",
    },
    "Q863": {
        "ar": "طاجيكستان",
        "en": "Tajikistan",
    },
    "Q865": {
        "ar": "تايوان",
        "en": "Taiwan",
    },
    "Q869": {
        "ar": "تايلاند",
        "en": "Thailand",
    },
    "Q953": {
        "ar": "زامبيا",
        "en": "Zambia",
    },

}
