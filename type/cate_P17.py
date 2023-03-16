#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update


"""
#
# (C) Ibrahem Qasim, 2022
#
#
#---
USA_P17 = {
    "Alabama": { "ar" : "ألاباما" , "Q" : "Q173" } ,
    "Alaska": { "ar" : "ألاسكا" , "Q" : "Q797" } ,
    "Arizona": { "ar" : "أريزونا" , "Q" : "Q816" } ,
    "Arkansas": { "ar" : "أركنساس" , "Q" : "Q1612" } ,
    "California": { "ar" : "كاليفورنيا" , "Q" : "Q99" } ,
    "Colorado": { "ar" : "كولورادو" , "Q" : "Q1261" } ,
    "Connecticut": { "ar" : "كونيتيكت" , "Q" : "Q779" } ,
    "Delaware": { "ar" : "ديلاوير" , "Q" : "Q1393" } ,
    "Florida": { "ar" : "فلوريدا" , "Q" : "Q812" } ,
    "Georgia (U.S. state)": { "ar" : "ولاية جورجيا" , "Q" : "Q1428" } ,
    "Hawaii": { "ar" : "هاواي" , "Q" : "Q782" } ,
    "Idaho": { "ar" : "أيداهو" , "Q" : "Q1221" } ,
    "Illinois": { "ar" : "إلينوي" , "Q" : "Q1204" } ,
    "Indiana": { "ar" : "إنديانا" , "Q" : "Q1415" } ,
    "Iowa": { "ar" : "آيوا" , "Q" : "Q1546" } ,
    "Kansas": { "ar" : "كانساس" , "Q" : "Q1558" } ,
    "Kentucky": { "ar" : "كنتاكي" , "Q" : "Q1603" } ,
    "Louisiana": { "ar" : "لويزيانا" , "Q" : "Q1588" } ,
    "Maine": { "ar" : "مين" , "Q" : "Q724" } ,
    "Maryland": { "ar" : "ماريلند" , "Q" : "Q1391" } ,
    "Massachusetts": { "ar" : "ماساتشوستس" , "Q" : "Q771" } ,
    "Michigan": { "ar" : "ميشيغان" , "Q" : "Q1166" } ,
    "Minnesota": { "ar" : "مينيسوتا" , "Q" : "Q1527" } ,
    "Mississippi": { "ar" : "مسيسيبي" , "Q" : "Q1494" } ,
    "Missouri": { "ar" : "ميزوري" , "Q" : "Q1581" } ,
    "Montana": { "ar" : "مونتانا" , "Q" : "Q1212" } ,
    "Nebraska": { "ar" : "نبراسكا" , "Q" : "Q1553" } ,
    "Nevada": { "ar" : "نيفادا" , "Q" : "Q1227" } ,
    "New Hampshire": { "ar" : "نيوهامبشير" , "Q" : "Q759" } ,
    "New Jersey": { "ar" : "نيوجيرسي" , "Q" : "Q1408" } ,
    "New Mexico": { "ar" : "نيومكسيكو" , "Q" : "Q1522" } ,
    "New York (state)": { "ar" : "ولاية نيويورك" , "Q" : "Q1384" } ,
    "North Carolina": { "ar" : "كارولاينا الشمالية" , "Q" : "Q1454" } ,
    "North Dakota": { "ar" : "داكوتا الشمالية" , "Q" : "Q1207" } ,
    "Ohio": { "ar" : "أوهايو" , "Q" : "Q1397" } ,
    "Oklahoma": { "ar" : "أوكلاهوما" , "Q" : "Q1649" } ,
    "Oregon": { "ar" : "أوريغون" , "Q" : "Q824" } ,
    "Pennsylvania": { "ar" : "بنسيلفانيا" , "Q" : "Q1400" } ,
    "Rhode Island": { "ar" : "رود آيلاند" , "Q" : "Q1387" } ,
    "South Carolina": { "ar" : "كارولاينا الجنوبية" , "Q" : "Q1456" } ,
    "South Dakota": { "ar" : "داكوتا الجنوبية" , "Q" : "Q1211" } ,
    "Tennessee": { "ar" : "تينيسي" , "Q" : "Q1509" } ,
    "Texas": { "ar" : "تكساس" , "Q" : "Q1439" } ,
    "Utah": { "ar" : "يوتا" , "Q" : "Q829" } ,
    "Vermont": { "ar" : "فيرمونت" , "Q" : "Q16551" } ,
    "Virginia": { "ar" : "فرجينيا" , "Q" : "Q1370" } ,
    "Washington (state)": { "ar" : "ولاية واشنطن" , "Q" : "Q1223" } ,
    "West Virginia": { "ar" : "فيرجينيا الغربية" , "Q" : "Q1371" } ,
    "Wisconsin": { "ar" : "ويسكونسن" , "Q" : "Q1537" } ,
    "Wyoming": { "ar" : "وايومنغ" , "Q" : "Q1214" } ,
    }
#---
ALL_P17 = {
    "the Atlantic Ocean" : { "ar" : "المحيط الأطلسي" , "Q" : "Q97" } ,
    "by continent" : { "ar" : "حسب القارة" , "Q" : "Q19360700" } ,
    "by country" : { "ar" : "حسب البلد" , "Q" : "Q19360703" } ,
    "Afghanistan" : {"ar" : "أفغانستان" ,"Q" :"Q889" } ,
    "Albania" : {"ar" : "ألبانيا" ,"Q" :"Q222" } ,
    "Algeria" : {"ar" : "الجزائر" ,"Q" :"Q262" } ,
    "Andorra" : {"ar" : "أندورا" ,"Q" :"Q228" } ,
    "Angola" : {"ar" : "أنغولا" ,"Q" :"Q916" } ,
    "Anguilla" : {"ar" : "أنغويلا" ,"Q" :"Q25228" } ,
    "Antigua and Barbuda" : {"ar" : "أنتيغوا وباربودا" ,"Q" :"Q781" } ,
    "Argentina" : {"ar" : "الأرجنتين" ,"Q" :"Q414" } ,
    "Armenia" : {"ar" : "أرمينيا" ,"Q" :"Q399" } ,
    "Aruba" : {"ar" : "أروبا" ,"Q" :"Q21203" } ,
    "Australia" : {"ar" : "أستراليا" ,"Q" :"Q408" } ,
    "Austria" : {"ar" : "النمسا" ,"Q" :"Q40" } ,
    "Azerbaijan" : {"ar" : "أذربيجان" ,"Q" :"Q227" } ,
    "Bahrain" : {"ar" : "البحرين" ,"Q" :"Q398" } ,
    "Bangladesh" : {"ar" : "بنغلاديش" ,"Q" :"Q902" } ,
    "Barbados" : {"ar" : "باربادوس" ,"Q" :"Q244" } ,
    "Belarus" : {"ar" : "روسيا البيضاء" ,"Q" :"Q184" } ,
    "Belgium" : {"ar" : "بلجيكا" ,"Q" :"Q31" } ,
    "Belize" : {"ar" : "بليز" ,"Q" :"Q242" } ,
    "Benin" : {"ar" : "بنين" ,"Q" :"Q962" } ,
    "Bermuda" : {"ar" : "برمودا" ,"Q" :"Q23635" } ,
    "Bhutan" : {"ar" : "بوتان" ,"Q" :"Q917" } ,
    "Bolivia" : {"ar" : "بوليفيا" ,"Q" :"Q750" } ,
    "Bonaire" : {"ar" : "بونير" ,"Q" :"Q25396" } ,
    "Bosnia and Herzegovina" : {"ar" : "البوسنة والهرسك" ,"Q" :"Q225" } ,
    "Botswana" : {"ar" : "بوتسوانا" ,"Q" :"Q963" } ,
    "Brazil" : {"ar" : "البرازيل" ,"Q" :"Q155" } ,
    "Bulgaria" : {"ar" : "بلغاريا" ,"Q" :"Q219" } ,
    "Burkina Faso" : {"ar" : "بوركينا فاسو" ,"Q" :"Q965" } ,
    "Burundi" : {"ar" : "بوروندي" ,"Q" :"Q967" } ,
    "Cambodia" : {"ar" : "كمبوديا" ,"Q" :"Q424" } ,
    "Cameroon" : {"ar" : "الكاميرون" ,"Q" :"Q1009" } ,
    "Canada" : {"ar" : "كندا" ,"Q" :"Q16" } ,
    "Cape Verde" : {"ar" : "الرأس الأخضر" ,"Q" :"Q1011" } ,
    "Chad" : {"ar" : "تشاد" ,"Q" :"Q657" } ,
    "Chile" : {"ar" : "تشيلي" ,"Q" :"Q298" } ,
    "China" : {"ar" : "الصين" ,"Q" :"Q148" } ,
    "Colombia" : {"ar" : "كولومبيا" ,"Q" :"Q739" } ,
    "Costa Rica" : {"ar" : "كوستاريكا" ,"Q" :"Q800" } ,
    "Croatia" : {"ar" : "كرواتيا" ,"Q" :"Q224" } ,
    "Cuba" : {"ar" : "كوبا" ,"Q" :"Q241" } ,
    "Curaçao" : {"ar" : "كوراساو" ,"Q" :"Q25279" } ,
    "Cyprus" : {"ar" : "قبرص" ,"Q" :"Q229" } ,
    "Denmark" : {"ar" : "الدنمارك" ,"Q" :"Q35" } ,
    "Djibouti" : {"ar" : "جيبوتي" ,"Q" :"Q977" } ,
    "Dominica" : {"ar" : "دومينيكا" ,"Q" :"Q784" } ,
    "Ecuador" : {"ar" : "الإكوادور" ,"Q" :"Q736" } ,
    "Egypt" : {"ar" : "مصر" ,"Q" :"Q79" } ,
    "El Salvador" : {"ar" : "السلفادور" ,"Q" :"Q792" } ,
    "Equatorial Guinea" : {"ar" : "غينيا الاستوائية" ,"Q" :"Q983" } ,
    "Eritrea" : {"ar" : "إريتريا" ,"Q" :"Q986" } ,
    "Estonia" : {"ar" : "إستونيا" ,"Q" :"Q191" } ,
    "Ethiopia" : {"ar" : "إثيوبيا" ,"Q" :"Q115" } ,
    "Fiji" : {"ar" : "فيجي" ,"Q" :"Q712" } ,
    "Finland" : {"ar" : "فنلندا" ,"Q" :"Q33" } ,
    "France" : {"ar" : "فرنسا" ,"Q" :"Q142" } ,
    "Gabon" : {"ar" : "الغابون" ,"Q" :"Q1000" } ,
    "Georgia (country)" : {"ar" : "جورجيا" ,"Q" :"Q230" } ,
    "Germany" : {"ar" : "ألمانيا" ,"Q" :"Q183" } ,
    "Ghana" : {"ar" : "غانا" ,"Q" :"Q117" } ,
    "Gibraltar" : {"ar" : "جبل طارق" ,"Q" :"Q1410" } ,
    "Greece" : {"ar" : "اليونان" ,"Q" :"Q41" } ,
    "Greenland" : {"ar" : "جرينلاند" ,"Q" :"Q223" } ,
    "Grenada" : {"ar" : "غرينادا" ,"Q" :"Q769" } ,
    "Guatemala" : {"ar" : "غواتيمالا" ,"Q" :"Q774" } ,
    "Guinea" : {"ar" : "غينيا" ,"Q" :"Q1006" } ,
    "Guinea-Bissau" : {"ar" : "غينيا بيساو" ,"Q" :"Q1007" } ,
    "Guyana" : {"ar" : "غيانا" ,"Q" :"Q734" } ,
    "Haiti" : {"ar" : "هايتي" ,"Q" :"Q790" } ,
    "Honduras" : {"ar" : "هندوراس" ,"Q" :"Q783" } ,
    "Hungary" : {"ar" : "المجر" ,"Q" :"Q28" } ,
    "Iceland" : {"ar" : "آيسلندا" ,"Q" :"Q189" } ,
    "India" : {"ar" : "الهند" ,"Q" :"Q668" } ,
    "Indonesia" : {"ar" : "إندونيسيا" ,"Q" :"Q252" } ,
    "Iran" : {"ar" : "إيران" ,"Q" :"Q794" } ,
    "Iraq" : {"ar" : "العراق" ,"Q" :"Q796" } ,
    "Israel" : {"ar" : "إسرائيل" ,"Q" :"Q801" } ,
    "Italy" : {"ar" : "إيطاليا" ,"Q" :"Q38" } ,
    "Ivory Coast" : {"ar" : "ساحل العاج" ,"Q" :"Q1008" } ,
    "Jamaica" : {"ar" : "جامايكا" ,"Q" :"Q766" } ,
    "Japan" : {"ar" : "اليابان" ,"Q" :"Q17" } ,
    "Jersey" : {"ar" : "جيرزي" ,"Q" :"Q785" } ,
    "Jordan" : {"ar" : "الأردن" ,"Q" :"Q810" } ,
    "Karelia" : {"ar" : "كاريليا" ,"Q" :"Q192273" } ,
    "Kazakhstan" : {"ar" : "كازاخستان" ,"Q" :"Q232" } ,
    "Kenya" : {"ar" : "كينيا" ,"Q" :"Q114" } ,
    "Kiribati" : {"ar" : "كيريباتي" ,"Q" :"Q710" } ,
    "Kuwait" : {"ar" : "الكويت" ,"Q" :"Q817" } ,
    "Kyrgyzstan" : {"ar" : "قيرغيزستان" ,"Q" :"Q813" } ,
    "Laos" : {"ar" : "لاوس" ,"Q" :"Q819" } ,
    "Latvia" : {"ar" : "لاتفيا" ,"Q" :"Q211" } ,
    "Lebanon" : {"ar" : "لبنان" ,"Q" :"Q822" } ,
    "Lesotho" : {"ar" : "ليسوتو" ,"Q" :"Q1013" } ,
    "Liberia" : {"ar" : "ليبيريا" ,"Q" :"Q1014" } ,
    "Libya" : {"ar" : "ليبيا" ,"Q" :"Q1016" } ,
    "Liechtenstein" : {"ar" : "ليختنشتاين" ,"Q" :"Q347" } ,
    "Lithuania" : {"ar" : "ليتوانيا" ,"Q" :"Q37" } ,
    "Luxembourg" : {"ar" : "لوكسمبورغ" ,"Q" :"Q32" } ,
    "Madagascar" : {"ar" : "مدغشقر" ,"Q" :"Q1019" } ,
    "Malawi" : {"ar" : "ملاوي" ,"Q" :"Q1020" } ,
    "Mali" : {"ar" : "مالي" ,"Q" :"Q912" } ,
    "Malta" : {"ar" : "مالطا" ,"Q" :"Q233" } ,
    "Mauritania" : {"ar" : "موريتانيا" ,"Q" :"Q1025" } ,
    "Mauritius" : {"ar" : "موريشيوس" ,"Q" :"Q1027" } ,
    "Mexico" : {"ar" : "المكسيك" ,"Q" :"Q96" } ,
    "Moldova" : {"ar" : "مولدافيا" ,"Q" :"Q217" } ,
    "Monaco" : {"ar" : "موناكو" ,"Q" :"Q235" } ,
    "Mongolia" : {"ar" : "منغوليا" ,"Q" :"Q711" } ,
    "Montenegro" : {"ar" : "الجبل الأسود" ,"Q" :"Q236" } ,
    "Montserrat" : {"ar" : "مونتسرات" ,"Q" :"Q13353" } ,
    "Morocco" : {"ar" : "المغرب" ,"Q" :"Q1028" } ,
    "Mozambique" : {"ar" : "موزمبيق" ,"Q" :"Q1029" } ,
    "Namibia" : {"ar" : "ناميبيا" ,"Q" :"Q1030" } ,
    "Nauru" : {"ar" : "ناورو" ,"Q" :"Q697" } ,
    "Nepal" : {"ar" : "نيبال" ,"Q" :"Q837" } ,
    "New Zealand" : {"ar" : "نيوزيلندا" ,"Q" :"Q664" } ,
    "Nicaragua" : {"ar" : "نيكاراغوا" ,"Q" :"Q811" } ,
    "Niger" : {"ar" : "النيجر" ,"Q" :"Q1032" } ,
    "Nigeria" : {"ar" : "نيجيريا" ,"Q" :"Q1033" } ,
    "Niue" : {"ar" : "نييوي" ,"Q" :"Q34020" } ,
    "North Korea" : {"ar" : "كوريا الشمالية" ,"Q" :"Q423" } ,
    "Norway" : {"ar" : "النرويج" ,"Q" :"Q20" } ,
    "Oman" : {"ar" : "سلطنة عمان" ,"Q" :"Q842" } ,
    "Pakistan" : {"ar" : "باكستان" ,"Q" :"Q843" } ,
    "Palau" : {"ar" : "بالاو" ,"Q" :"Q695" } ,
    "Panama" : {"ar" : "بنما" ,"Q" :"Q804" } ,
    "Papua New Guinea" : {"ar" : "بابوا غينيا الجديدة" ,"Q" :"Q691" } ,
    "Paraguay" : {"ar" : "باراغواي" ,"Q" :"Q733" } ,
    "Peru" : {"ar" : "بيرو" ,"Q" :"Q419" } ,
    "Poland" : {"ar" : "بولندا" ,"Q" :"Q36" } ,
    "Portugal" : {"ar" : "البرتغال" ,"Q" :"Q45" } ,
    "Puerto Rico" : {"ar" : "بورتوريكو" ,"Q" :"Q1183" } ,
    "Qatar" : {"ar" : "قطر" ,"Q" :"Q846" } ,
    "Romania" : {"ar" : "رومانيا" ,"Q" :"Q218" } ,
    "Russia" : {"ar" : "روسيا" ,"Q" :"Q159" } ,
    "Rwanda" : {"ar" : "رواندا" ,"Q" :"Q1037" } ,
    "Saint Kitts and Nevis" : {"ar" : "سانت كيتس ونيفيس" ,"Q" :"Q763" } ,
    "Saint Lucia" : {"ar" : "سانت لوسيا" ,"Q" :"Q760" } ,
    "Saint Vincent and the Grenadines" : {"ar" : "سانت فينسنت والغرينادين" ,"Q" :"Q757" } ,
    "Samoa" : {"ar" : "ساموا" ,"Q" :"Q683" } ,
    "San Marino" : {"ar" : "سان مارينو" ,"Q" :"Q238" } ,
    "Saudi Arabia" : {"ar" : "السعودية" ,"Q" :"Q851" } ,
    "Senegal" : {"ar" : "السنغال" ,"Q" :"Q1041" } ,
    "Serbia" : {"ar" : "صربيا" ,"Q" :"Q403" } ,
    "Seychelles" : {"ar" : "سيشل" ,"Q" :"Q1042" } ,
    "Sierra Leone" : {"ar" : "سيراليون" ,"Q" :"Q1044" } ,
    "Singapore" : {"ar" : "سنغافورة" ,"Q" :"Q334" } ,
    "Sint Eustatius" : {"ar" : "سينت أوستاتيوس" ,"Q" :"Q26180" } ,
    "Sint Maarten" : {"ar" : "سينت مارتن" ,"Q" :"Q26273" } ,
    "Slovakia" : {"ar" : "سلوفاكيا" ,"Q" :"Q214" } ,
    "Slovenia" : {"ar" : "سلوفينيا" ,"Q" :"Q215" } ,
    "Somalia" : {"ar" : "الصومال" ,"Q" :"Q1045" } ,
    "Somaliland" : {"ar" : "صوماليلاند" ,"Q" :"Q34754" } ,
    "South Africa" : {"ar" : "جنوب أفريقيا" ,"Q" :"Q258" } ,
    "South Georgia and the South Sandwich Islands" : {"ar" : "جورجيا الجنوبية وجزر ساندويتش الجنوبية" ,"Q" :"Q35086" } ,
    "South Korea" : {"ar" : "كوريا الجنوبية" ,"Q" :"Q884" } ,
    "South Sudan" : {"ar" : "جنوب السودان" ,"Q" :"Q958" } ,
    "Spain" : {"ar" : "إسبانيا" ,"Q" :"Q29" } ,
    "Sri Lanka" : {"ar" : "سريلانكا" ,"Q" :"Q854" } ,
    "Sudan" : {"ar" : "السودان" ,"Q" :"Q1049" } ,
    "Suriname" : {"ar" : "سورينام" ,"Q" :"Q730" } ,
    "Swaziland" : {"ar" : "سوازيلاند" ,"Q" :"Q1050" } ,
    "Sweden" : {"ar" : "السويد" ,"Q" :"Q34" } ,
    "Switzerland" : {"ar" : "سويسرا" ,"Q" :"Q39" } ,
    "Syria" : {"ar" : "سوريا" ,"Q" :"Q858" } ,
    "São Tomé and Príncipe" : {"ar" : "ساو تومي وبرينسيب" ,"Q" :"Q1039" } ,
    "Taiwan" : {"ar" : "تايوان" ,"Q" :"Q865" } ,
    "Tajikistan" : {"ar" : "طاجيكستان" ,"Q" :"Q863" } ,
    "Tanzania" : {"ar" : "تنزانيا" ,"Q" :"Q924" } ,
    "Thailand" : {"ar" : "تايلاند" ,"Q" :"Q869" } ,
    "Tibet" : {"ar" : "التبت" ,"Q" :"Q17252" } ,
    "Togo" : {"ar" : "توغو" ,"Q" :"Q945" } ,
    "Tonga" : {"ar" : "تونغا" ,"Q" :"Q678" } ,
    "Trinidad and Tobago" : {"ar" : "ترينيداد وتوباغو" ,"Q" :"Q754" } ,
    "Tunisia" : {"ar" : "تونس" ,"Q" :"Q948" } ,
    "Turkey" : {"ar" : "تركيا" ,"Q" :"Q43" } ,
    "Turkmenistan" : {"ar" : "تركمانستان" ,"Q" :"Q874" } ,
    "Tuvalu" : {"ar" : "توفالو" ,"Q" :"Q672" } ,
    "Uganda" : {"ar" : "أوغندا" ,"Q" :"Q1036" } ,
    "Ukraine" : {"ar" : "أوكرانيا" ,"Q" :"Q212" } ,
    "Uruguay" : {"ar" : "الأوروغواي" ,"Q" :"Q77" } ,
    "Uzbekistan" : {"ar" : "أوزبكستان" ,"Q" :"Q265" } ,
    "Vanuatu" : {"ar" : "فانواتو" ,"Q" :"Q686" } ,
    "Venezuela" : {"ar" : "فنزويلا" ,"Q" :"Q717" } ,
    "Vietnam" : {"ar" : "فيتنام" ,"Q" :"Q881" } ,
    "Western Sahara" : {"ar" : "الصحراء الغربية" ,"Q" :"Q6250" } ,
    "Yemen" : {"ar" : "اليمن" ,"Q" :"Q805" } ,
    "Zambia" : {"ar" : "زامبيا" ,"Q" :"Q953" } ,
    "Zimbabwe" : {"ar" : "زيمبابوي" ,"Q" :"Q954" } ,
    "the Bahamas" : {"ar" : "باهاماس" ,"Q" :"Q778" } ,
    "the British Indian Ocean Territory" : {"ar" : "إقليم المحيط الهندي البريطاني" ,"Q" :"Q43448" } ,
    "the British Virgin Islands" : {"ar" : "جزر العذراء البريطانية" ,"Q" :"Q25305" } ,
    "the Cayman Islands" : {"ar" : "جزر كايمان" ,"Q" :"Q5785" } ,
    "the Central African Republic" : {"ar" : "جمهورية أفريقيا الوسطى" ,"Q" :"Q929" } ,
    "the Comoros" : {"ar" : "جزر القمر" ,"Q" :"Q970" } ,
    "the Cook Islands" : {"ar" : "جزر كوك" ,"Q" :"Q26988" } ,
    "czech republic" : {"ar" : "التشيك" ,"Q" :"Q213" } ,
    "the Czech Republic" : {"ar" : "التشيك" ,"Q" :"Q213" } ,
    "the Democratic Republic of the Congo" : {"ar" : "جمهورية الكونغو الديمقراطية" ,"Q" :"Q974" } ,
    "the Dominican Republic" : {"ar" : "جمهورية الدومينيكان" ,"Q" :"Q786" } ,
    "the Falkland Islands" : {"ar" : "جزر فوكلاند" ,"Q" :"Q9648" } ,
    "the Federated States of Micronesia" : {"ar" : "ولايات ميكرونيسيا المتحدة" ,"Q" :"Q702" } ,
    "the Gambia" : {"ar" : "غامبيا" ,"Q" :"Q1005" } ,
    "the Maldives" : {"ar" : "جزر المالديف" ,"Q" :"Q826" } ,
    "the Marshall Islands" : {"ar" : "جزر مارشال" ,"Q" :"Q709" } ,
    "the Netherlands" : {"ar" : "هولندا" ,"Q" :"Q55" } ,
    "the Palestinian territories" : {"ar" : "الضفة الغربية وقطاع غزة" ,"Q" :"Q407199" } ,
    "the Philippines" : {"ar" : "الفلبين" ,"Q" :"Q928" } ,
    "the Republic of Ireland" : {"ar" : "جمهورية أيرلندا" ,"Q" :"Q27" } ,
    "the Republic of Macedonia" : {"ar" : "جمهورية مقدونيا" ,"Q" :"Q221" } ,
    "Macedonia" : {"ar" : "مقدونيا" ,"Q" :"Q81734" } ,
    "the Republic of the Congo" : {"ar" : "جمهورية الكونغو" ,"Q" :"Q971" } ,
    #"the Congo" : {"ar" : "جمهورية الكونغو" ,"Q" :"Q971" } ,
    "the Solomon Islands" : {"ar" : "جزر سليمان" ,"Q" :"Q685" } ,
    "the United Arab Emirates" : {"ar" : "الإمارات العربية المتحدة" ,"Q" :"Q878" } ,
    "the United Kingdom" : {"ar" : "المملكة المتحدة" ,"Q" :"Q145" } ,
    "the United States" : {"ar" : "الولايات المتحدة" ,"Q" :"Q30" } ,
    "the Kingdom of Great Britain" : {"ar" : "مملكة بريطانيا العظمى" ,"Q" :"Q161885" } ,
    "the United States Virgin Islands" : {"ar" : "جزر العذراء الأمريكية" ,"Q" :"Q11703" } ,
    "Ireland" : {"ar" : "جزيرة أيرلندا" ,"Q" :"Q22890" } ,
    }
#ALL_P17["the Congo"] = ALL_P17["the Republic of the Congo"]

#---
New_P17 = {
    "Africa": { "ar" : "أفريقيا" , "Q" : "Q15" } ,
    "South America": { "ar" : "أمريكا الجنوبية" , "Q" : "Q18" } ,
    "Europe": { "ar" : "أوروبا" , "Q" : "Q46" } ,
    "Asia": { "ar" : "آسيا" , "Q" : "Q48" } ,
    "North America": { "ar" : "أمريكا الشمالية" , "Q" : "Q49" } ,
    "Antarctica": { "ar" : "أنتاركتيكا" , "Q" : "Q51" } ,
    "Oceania": { "ar" : "أوقيانوسيا" , "Q" : "Q538" } ,
    "Australia": { "ar" : "أستراليا" , "Q" : "Q3960" } ,
    "Yugoslavia": { "ar" : "يوغوسلافيا" , "Q" : "Q36704" } ,
    "Wales": { "ar" : "ويلز" , "Q" : "Q25" } ,
    "Wallis and Futuna": { "ar" : "واليس وفوتونا" , "Q" : "Q35555" } ,
    "Hong Kong": { "ar" : "هونغ كونغ" , "Q" : "Q8646" } ,
    "the Golan Heights": { "ar" : "هضبة الجولان" , "Q" : "Q83210" } ,
    "Newfoundland": { "ar" : "نيوفاوندلاند واللابرادور" , "Q" : "Q2003" } ,
    "Nyasaland": { "ar" : "نياسالاند" , "Q" : "Q1649306" } ,
    "Micronesia": { "ar" : "ميكرونيسيا" , "Q" : "Q3359409" } ,
    "Myanmar": { "ar" : "ميانمار" , "Q" : "Q836" } ,
    "the Kingdom of the Netherlands": { "ar" : "مملكة هولندا" , "Q" : "Q29999" } ,
    "the Kingdom of Hanover": { "ar" : "مملكة هانوفر" , "Q" : "Q164079" } ,
    "the Kingdom of Naples": { "ar" : "مملكة نابولي" , "Q" : "Q173065" } ,
    "Lan Xang": { "ar" : "مملكة لان أكسانغ" , "Q" : "Q853477" } ,
    "the Kilwa Sultanate": { "ar" : "مملكة كلوه" , "Q" : "Q3107156" } ,
    "the Kingdom of Sicily": { "ar" : "مملكة صقلية" , "Q" : "Q188586" } ,
    "the Kingdom of Sardinia": { "ar" : "مملكة سردينيا" , "Q" : "Q165154" } ,
    "the Kingdom of Jerusalem": { "ar" : "مملكة بيت المقدس" , "Q" : "Q55502" } ,
    "the Kingdom of Italy (Napoleonic)": { "ar" : "مملكة إيطاليا النابوليونية" , "Q" : "Q223936" } ,
    "the Habsburg Monarchy": { "ar" : "ملكية هابسبورغ" , "Q" : "Q153136" } ,
    "the Viceroyalty of the Río de la Plata": { "ar" : "ملكية ريو دي لا بلاتا البديلة" , "Q" : "Q210551" } ,
    "the Falkland Islands Dependencies": { "ar" : "مقاطعات جزر فوكلاند" , "Q" : "Q5431953" } ,
    "the Syrian Opposition": { "ar" : "المعارضة السورية" , "Q" : "Q3024068" } ,
    "Nagorno-Karabakh": { "ar" : "مرتفعات قرة باغ" , "Q" : "Q44302" } ,
    "Mayotte": { "ar" : "مايوت" , "Q" : "Q17063" } ,
    "the Maya civilization": { "ar" : "مايا" , "Q" : "Q28567" } ,
    "Dutch Mauritius": { "ar" : "ماورتيوس الهولندية" , "Q" : "Q5245668" } ,
    "Malaysia": { "ar" : "ماليزيا" , "Q" : "Q833" } ,
    "Macau": { "ar" : "ماكاو" , "Q" : "Q14773" } ,
    "Martinique": { "ar" : "مارتينيك" , "Q" : "Q17054" } ,
    "Réunion": { "ar" : "لا ريونيون" , "Q" : "Q17070" } ,
    "Gran Colombia": { "ar" : "كولومبيا الكبرى" , "Q" : "Q199821" } ,
    "Kosovo": { "ar" : "كوسوفو" , "Q" : "Q1246" } ,
    "the Republic of Kosovo": { "ar" : "كوسوفو" , "Q" : "Q1246" } ,
    "Korea": { "ar" : "كوريا" , "Q" : "Q18097" } ,
    "Curaçao": { "ar" : "كوراساو" , "Q" : "Q25279" } ,
    "Iraqi Kurdistan": { "ar" : "كردستان العراق" , "Q" : "Q205047" } ,
    "Kurdistan": { "ar" : "كردستان" , "Q" : "Q41470" } ,
    "New Caledonia": { "ar" : "كاليدونيا الجديدة" , "Q" : "Q33788" } ,
    "the Gaza Strip": { "ar" : "قطاع غزة" , "Q" : "Q39760" } ,
    "Northern Cyprus": { "ar" : "قبرص الشمالية" , "Q" : "Q23681" } ,
    "Israeli-occupied territories": { "ar" : "فلسطين المحتلة" , "Q" : "Q575187" } ,
    "Palestine (region)": { "ar" : "فلسطين" , "Q" : "Q23792" } ,
    "New France": { "ar" : "فرنسا الجديدة" , "Q" : "Q170604" } ,
    "German New Guinea": { "ar" : "غينيا الجديدة الألمانية" , "Q" : "Q165008" } ,
    "French Guiana": { "ar" : "غويانا الفرنسية" , "Q" : "Q3769" } ,
    "Guam": { "ar" : "غوام" , "Q" : "Q16635" } ,
    "Guadeloupe": { "ar" : "غوادلوب" , "Q" : "Q17012" } ,
    "French West Africa": { "ar" : "غرب أفريقيا الفرنسي" , "Q" : "Q210682" } ,
    "the Adal Sultanate": { "ar" : "سلطنة عدل" , "Q" : "Q2365048" } ,
    "Tadjikistan": { "ar" : "طاجيكستان" , "Q" : "Q863" } ,
    "Serbia and Montenegro": { "ar" : "صربيا والجبل الأسود" , "Q" : "Q37024" } ,
    #"Sabah": { "ar" : "صباح (ماليزيا)" , "Q" : "Q179029" } ,
    "German East Africa": { "ar" : "شرق أفريقيا الألماني" , "Q" : "Q153963" } ,
    "Sikkim": { "ar" : "سيكيم" , "Q" : "Q1505" } ,
    "Ottoman Syria": { "ar" : "سوريا العثمانية" , "Q" : "Q3076765" } ,
    "the Seleucid Empire": { "ar" : "سلوقيون" , "Q" : "Q93180" } ,
    "Svalbard": { "ar" : "سفالبارد" , "Q" : "Q25231" } ,
    "São Tomé and Príncipe": { "ar" : "ساو تومي وبرينسيب" , "Q" : "Q1039" } ,
    "Saint Helena and Dependencies": { "ar" : "سانت هيلانة وأسينشين وتريستان دا كونا" , "Q" : "Q192184" } ,
    "Saint Helena, Ascension and Tristan da Cunha": { "ar" : "سانت هيلانة وأسينشين وتريستان دا كونا" , "Q" : "Q192184" } ,
    "Saint Helena": { "ar" : "سانت هيلانة" , "Q" : "Q34497" } ,
    "Saint Martin": { "ar" : "سانت مارتن" , "Q" : "Q25596" } ,
    "Saint Pierre and Miquelon": { "ar" : "سان بيير وميكلون" , "Q" : "Q34617" } ,
    "Saint Barthélemy": { "ar" : "سان بارتيلمي" , "Q" : "Q25362" } ,
    "American Samoa": { "ar" : "ساموا الأمريكية" , "Q" : "Q16641" } ,
    "Saxony": { "ar" : "ساكسونيا" , "Q" : "Q1202" } ,
    "Sarawak": { "ar" : "ساراواك" , "Q" : "Q170462" } ,
    "Saba": { "ar" : "جزيرة سابا" , "Q" : "Q25528" } ,
    "Zanzibar": { "ar" : "زنجبار" , "Q" : "Q1774" } ,
    "Northern Rhodesia": { "ar" : "رودسيا الشمالية" , "Q" : "Q953903" } ,
    "Southern Rhodesia": { "ar" : "رودسيا الجنوبية" , "Q" : "Q750583" } ,
    "Rhodesia": { "ar" : "رودسيا" , "Q" : "Q217169" } ,
    "the State of Palestine": { "ar" : "دولة فلسطين" , "Q" : "Q219060" } ,
    "the Orange Free State": { "ar" : "دولة البرتقال الحرة" , "Q" : "Q218023" } ,
    "the Grand Duchy of Hesse": { "ar" : "دوقية هسن الكبرى" , "Q" : "Q20135" } ,
    "the Duchy of Modena and Reggio": { "ar" : "دوقية مودينا وريدجو" , "Q" : "Q252580" } ,
    "the Grand Duchy of Tuscany": { "ar" : "دوقية توسكانا الكبرى" , "Q" : "Q154849" } ,
    "the Zapotec civilization": { "ar" : "حضارة الزابوتيك" , "Q" : "Q844750" } ,
    "German South West Africa": { "ar" : "جنوب غرب أفريقيا الألمانية" , "Q" : "Q153665" } ,
    "South West Africa": { "ar" : "جنوب غرب أفريقيا" , "Q" : "Q953068" } ,
    "the Dutch Republic": { "ar" : "جمهورية هولندا" , "Q" : "Q170072" } ,
    "the Socialist Republic of Macedonia": { "ar" : "جمهورية مقدونيا الاشتراكية" , "Q" : "Q240592" } ,
    "the Nagorno-Karabakh Republic": { "ar" : "جمهورية مرتفعات قرة باغ" , "Q" : "Q244165" } ,
    }
#---
New_P172 = {
    "the Republic of Upper Volta": { "ar" : "جمهورية فولتا العليا" , "Q" : "Q797422" } ,
    "the Republic of Florence": { "ar" : "جمهورية فلورنسا" , "Q" : "Q148540" } ,
    "the Republic of New Granada": { "ar" : "جمهورية غرناطة الجديدة" , "Q" : "Q630882" } ,
    "Donetsk People's Republic": { "ar" : "جمهورية دونيتسك الشعبية" , "Q" : "Q16150196" } ,
    "the Republic of Genoa": { "ar" : "جمهورية جنوة" , "Q" : "Q174306" } ,
    "the Republic of Texas": { "ar" : "جمهورية تكساس" , "Q" : "Q170588" } ,
    "Central African Republic": { "ar" : "جمهورية أفريقيا الوسطى" , "Q" : "Q929" } ,
    "South Yemen": { "ar" : "جمهورية اليمن الديمقراطية الشعبية" , "Q" : "Q199841" } ,
    "the Republic of Venice": { "ar" : "جمهورية البندقية" , "Q" : "Q4948" } ,
    "Norfolk Island": { "ar" : "جزيرة نورفولك" , "Q" : "Q31057" } ,
    "the Isle of Man": { "ar" : "جزيرة مان" , "Q" : "Q9676" } ,
    "Easter Island": { "ar" : "جزيرة القيامة" , "Q" : "Q14452" } ,
    "the Northern Mariana Islands": { "ar" : "جزر ماريانا الشمالية" , "Q" : "Q16644" } ,
    "the Cocos (Keeling) Islands": { "ar" : "جزر كوكوس" , "Q" : "Q36004" } ,
    "the Faroe Islands": { "ar" : "جزر فارو" , "Q" : "Q4628" } ,
    "the Turks and Caicos Islands": { "ar" : "جزر توركس وكايكوس" , "Q" : "Q18221" } ,
    "the Pitcairn Islands": { "ar" : "جزر بيتكيرن" , "Q" : "Q35672" } ,
    "the Channel Islands": { "ar" : "جزر القنال الإنجليزي" , "Q" : "Q42314" } ,
    "the Netherlands Antilles": { "ar" : "جزر الأنتيل الهولندية" , "Q" : "Q25227" } ,
    "East Timor": { "ar" : "تيمور الشرقية" , "Q" : "Q574" } ,
    "Tokelau": { "ar" : "توكيلاو" , "Q" : "Q36823" } ,
    "the Islamic State of Iraq and the Levant": { "ar" : "تنظيم داعش" , "Q" : "Q2429253" } ,
    "Tanganyika": { "ar" : "تنجانيقا" , "Q" : "Q431731" } ,
    "Transnistria": { "ar" : "ترانسنيستريا" , "Q" : "Q907112" } ,
    "the Collectivity of Saint Martin": { "ar" : "تجمع سان مارتين" , "Q" : "Q126125" } ,
    "the Republic of China": { "ar" : "تايوان" , "Q" : "Q865" } ,
    "Tahiti": { "ar" : "تاهيتي" , "Q" : "Q42000" } ,
    "Bohemia": { "ar" : "بوهيميا" , "Q" : "Q39193" } ,
    "French Polynesia": { "ar" : "بولينزيا الفرنسية" , "Q" : "Q30971" } ,
    "Punjab": { "ar" : "منطقة بنجاب" , "Q" : "Q169132" } ,
    "Great Britain": { "ar" : "بريطانيا العظمى" , "Q" : "Q23666" } ,
    "Brunei": { "ar" : "بروناي" , "Q" : "Q921" } ,
    "Prussia": { "ar" : "بروسيا" , "Q" : "Q38872" } ,
    "Alderney": { "ar" : "آلدرني" , "Q" : "Q179313" } ,
    "Assyria": { "ar" : "آشور" , "Q" : "Q41137" } ,
    "Northern Ireland": { "ar" : "أيرلندا الشمالية" , "Q" : "Q26" } ,
    "Okinawa": { "ar" : "محافظة أوكيناوا" , "Q" : "Q766445" } ,
    "South Ossetia": { "ar" : "أوسيتيا الجنوبية" , "Q" : "Q23427" } ,
    "Central America": { "ar" : "أمريكا الوسطى" , "Q" : "Q27611" } ,
    "West Germany": { "ar" : "ألمانيا الغربية" , "Q" : "Q713750" } ,
    "East Germany": { "ar" : "ألمانيا الشرقية" , "Q" : "Q16957" } ,
    "British Overseas Territories": { "ar" : "أقاليم ما وراء البحار البريطانية" , "Q" : "Q46395" } ,
    "French Somaliland": { "ar" : "أرض الصومال الفرنسي" , "Q" : "Q333126" } ,
    "Abkhazia": { "ar" : "أبخازيا" , "Q" : "Q23334" } ,
    "Ingushetia": { "ar" : "إنغوشيتيا" , "Q" : "Q5219" } ,
    "England": { "ar" : "إنجلترا" , "Q" : "Q21" } ,
    "the Maratha Empire": { "ar" : "إمبراطورية ماراثا" , "Q" : "Q83618" } ,
    "the Mongol Empire": { "ar" : "إمبراطورية المغول" , "Q" : "Q12557" } ,
    "the Trucial States": { "ar" : "إمارات الساحل المتصالح" , "Q" : "Q1852345" } ,
    "New Spain": { "ar" : "إسبانيا الجديدة" , "Q" : "Q170603" } ,
    "the Electorate of Hesse": { "ar" : "انتخابية هسن" , "Q" : "Q529605" } ,
    "North Yemen": { "ar" : "اليمن الشمالي" , "Q" : "Q1998401" } ,
    "French India": { "ar" : "الهند الفرنسية" , "Q" : "Q646374" } ,
    "French Indochina": { "ar" : "الهند الصينية الفرنسية" , "Q" : "Q185682" } ,
    "the Dutch East Indies": { "ar" : "الهند الشرقية الهولندية" , "Q" : "Q188161" } ,
    "Portuguese India": { "ar" : "الهند البرتغالية" , "Q" : "Q323904" } ,
    "in Mexico": { "ar" : "المكسيك" , "Q" : "Q96" } ,
    "the Thirteen Colonies": { "ar" : "المستعمرات الثلاث عشرة" , "Q" : "Q179997" } ,
    "the Polish–Lithuanian Commonwealth": { "ar" : "الكومنولث البولندي الليتواني" , "Q" : "Q172107" } ,
    "Vatican City": { "ar" : "الفاتيكان" , "Q" : "Q237" } ,
    "the West Bank": { "ar" : "الضفة الغربية" , "Q" : "Q36678" } ,
    "the People's Republic of China": { "ar" : "الصين" , "Q" : "Q148" } ,  #Q148
    "Spanish Sahara": { "ar" : "الصحراء الإسبانية" , "Q" : "Q689837" } ,   #Q689837
    "Chechnya": { "ar" : "الشيشان" , "Q" : "Q5187" } , #Q5187
    "French Sudan": { "ar" : "السودان الفرنسي" , "Q" : "Q508014" } ,   #Q508014
    "the Palestinian National Authority": { "ar" : "السلطة الوطنية الفلسطينية" , "Q" : "Q42620" } ,
    "the Hasmonean Kingdom": { "ar" : "السلالة الحشمونية" , "Q" : "Q496922" } ,
    "the Mamluk Sultanate (Cairo)": { "ar" : "الدولة المملوكية" , "Q" : "Q282428" } ,
    "the Fatimid Caliphate": { "ar" : "الدولة الفاطمية" , "Q" : "Q160307" } ,  #Q12536
    "the Abbasid Caliphate": { "ar" : "الدولة العباسية" , "Q" : "Q12536" } ,   #Q170174
    "the Papal States": { "ar" : "الدولة البابوية" , "Q" : "Q170174" } ,   #Q12406729
    "the Israeli Military Governorate": { "ar" : "الحكم العسكري الإسرائيلي" , "Q" : "Q12406729" } ,    #Q659312
    "the Ligurian Republic": { "ar" : "الجمهورية الليغورية" , "Q" : "Q659312" } ,  #Q40362
    "the Sahrawi Arab Democratic Republic": { "ar" : "الجمهورية العربية الصحراوية الديمقراطية" , "Q" : "Q40362" } ,    #Q1031430
    "the Habsburg Netherlands": { "ar" : "الأراضي المنخفضة الهابسبورجية" , "Q" : "Q1031430" } ,    #Q28513
    "Austria-Hungary": { "ar" : "الإمبراطورية النمساوية المجرية" , "Q" : "Q28513" } ,  #Q179023
    "the French colonial empire": { "ar" : "الإمبراطورية الفرنسية الاستعمارية" , "Q" : "Q179023" } ,   #Q12548
    "the Holy Roman Empire": { "ar" : "الإمبراطورية الرومانية المقدسة" , "Q" : "Q12548" } ,    #Q2277
    "the Roman Empire": { "ar" : "الإمبراطورية الرومانية" , "Q" : "Q2277" } ,      #Q12544
    "the Byzantine Empire": { "ar" : "الإمبراطورية البيزنطية" , "Q" : "Q12544" } , #Q8680
    "the British Empire": { "ar" : "الإمبراطورية البريطانية" , "Q" : "Q8680" } ,   #Q329618
    "the German colonial empire": { "ar" : "الإمبراطورية الألمانية الاستعمارية" , "Q" : "Q329618" } ,  #Q926295
    "the Italian Empire": { "ar" : "الإمبراطورية الاستعمارية الإيطالية" , "Q" : "Q926295" } ,  #Q6087526
    "the Israeli Civil Administration area": { "ar" : "الإدارة المدنية الإسرائيلية" , "Q" : "Q6087526" } , #Q2893000
    "the West Bank Governorate": { "ar" : "الإدارة الأردنية للضفة الغربية" , "Q" : "Q2893000" } ,  #Q139708
    "Mandatory Syria": { "ar" : "الانتداب الفرنسي على سوريا ولبنان" , "Q" : "Q139708" } ,  #Q193714
    "Mandatory Palestine": { "ar" : "الانتداب البريطاني على فلسطين" , "Q" : "Q193714" } ,  #Q15180
    "the Soviet Union": { "ar" : "الاتحاد السوفيتي" , "Q" : "Q15180" } ,   #Q458
    "the European Union": { "ar" : "الاتحاد الأوروبي" , "Q" : "Q458" } ,   #Q22
    "Scotland": { "ar" : "اسكتلندا" , "Q" : "Q22" } ,      #Q654342
    "Federation of Rhodesia and Nyasaland": { "ar" : "اتحاد رودسيا ونياسلاند" , "Q" : "Q654342" } 
    }
New_P173 = {
    #"Ceylon"    : { "ar" : "سريلانكا" , "Q" : "Q854" } ,   #   156
    "British Columbia"  : { "ar" : "كولومبيا البريطانية" , "Q" : "Q1974" } ,   #   169
    "the Spanish East Indies"   : { "ar" : "جزر الهند الشرقية الإسبانية" , "Q" : "Q910648" } ,   #   155
    "Prince Edward Island"  : { "ar" : "جزيرة الأمير إدوارد" , "Q" : "Q1979" } ,   #   141
    "British India" : { "ar" : "الراج البريطاني" , "Q" : "Q129286" } ,   #   137
    "Bavaria"   : { "ar" : "بافاريا" , "Q" : "Q980" } ,   #   135
    "the Ottoman Empire"    : { "ar" : "الدولة العثمانية" , "Q" : "Q12560" } ,   #   472
    "the Spanish Empire"    : { "ar" : "الإمبراطورية الإسبانية" , "Q" : "Q80702" } ,   #   449
    "the Caribbean" : { "ar" : "الكاريبي" , "Q" : "Q664609" } ,   #   332
    "the Portuguese Empire" : { "ar" : "الإمبراطورية البرتغالية" , "Q" : "Q200464" } ,   #   330
    "Nova Scotia"   : { "ar" : "نوفا سكوشا" , "Q" : "Q1952" } ,   #   254
    "Washington, D.C."  : { "ar" : "واشنطن العاصمة" , "Q" : "Q61" } ,   #   241
    "Southeast Asia"    : { "ar" : "جنوب شرق آسيا" , "Q" : "Q11708" } ,   #   377
    "the Dutch Empire"  : { "ar" : "الإمبراطورية الهولندية" , "Q" : "Q130654" } ,   #   231
    "London"    : { "ar" : "لندن" , "Q" : "Q84" } ,   #   230
    "Manitoba"  : { "ar" : "مانيتوبا" , "Q" : "Q1948" } ,    #   161
    "politics"  : { "ar" : "السياسة" , "Q" : "Q7163" } ,   #   1053
    "religion"  : { "ar" : "الدين" , "Q" : "Q9174" } ,   #   933
    "Christianity"  : { "ar" : "المسيحية" , "Q" : "Q5043" } ,   #   748
    "art"   : { "ar" : "الفن" , "Q" : "Q735" } ,   #   690
    "science"   : { "ar" : "العلم" , "Q" : "Q336" } ,   #   680
    "sports "   : { "ar" : "الرياضة" , "Q" : "Q349" } ,   #   644
    "law"   : { "ar" : "القانون" , "Q" : "Q7748" } ,   #   578
    "military history"  : { "ar" : "التاريخ العسكري" , "Q" : "Q192781" } ,   #   570
    "fiction"   : { "ar" : "الخيال" , "Q" : "Q8253" } ,   #   510
    "music" : { "ar" : "الموسيقى" , "Q" : "Q638" } ,   #   473
    "transport" : { "ar" : "النقل" , "Q" : "Q7590" } ,   #   460
    "the environment"   : { "ar" : "البيئة" , "Q" : "Q2249676" } ,   #   213
    "arts"  : { "ar" : "الفنون" , "Q" : "Q2018526" } ,   #   183
    "international relations"   : { "ar" : "العلاقات الدولية" , "Q" : "Q166542" } ,   #   448
    "economics" : { "ar" : "الاقتصاد" , "Q" : "Q8134" } ,   #   384
    "theatre"   : { "ar" : "المسرح" , "Q" : "Q11635" } ,   #   332
    "cricket"   : { "ar" : "الكريكت" , "Q" : "Q5375" } ,   #   298
    "horse racing"  : { "ar" : "سباق الخيل" , "Q" : "Q187916" } ,   #   272
    "rail transport"    : { "ar" : "السكك الحديدية" , "Q" : "Q3565868" } ,   #   272
    "education" : { "ar" : "التعليم" , "Q" : "Q8434" } ,   #   238
    "chess" : { "ar" : "الشطرنج" , "Q" : "Q718" } ,   #   172
    "association football"  : { "ar" : "كرة القدم" , "Q" : "Q2736" } ,   #   171
    "paleontology"  : { "ar" : "علم الأحياء القديمة" , "Q" : "Q7205" } ,   #   162
    "Gaelic games"  : { "ar" : "" , "Q" : "Q2447366" } ,   #   160
    "technology"    : { "ar" : "التقانة" , "Q" : "Q11016" } ,   #   160
    "Judo"    : { "ar" : "الجودو" , "Q" : "Q11420" } ,   #   160
    "baseball"  : { "ar" : "كرة القاعدة" , "Q" : "Q5369" } ,   #   160
    "rugby union"   : { "ar" : "اتحاد الرجبي" , "Q" : "Q5849" } ,   #   158
    "golfs"  : { "ar" : "الغولف" , "Q" : "Q5377" } ,   #   156
    "golf"  : { "ar" : "الغولف" , "Q" : "Q5377" } ,   #   156
    "film"  : { "ar" : "الأفلام" , "Q" : "Q11424" } ,   #   155
    "films"  : { "ar" : "الأفلام" , "Q" : "Q11424" } ,   #   155
    "literature"    : { "ar" : "الأدب" , "Q" : "Q8242" } ,   #   154
    "women's history"   : { "ar" : "تاريخ المرأة" , "Q" : "Q1279400" } ,   #   144
    "rugby league"  : { "ar" : "دوري الرغبي" , "Q" : "Q10962" } ,   #   143
    "tennis"    : { "ar" : "كرة المضرب" , "Q" : "Q847" } ,   #   143
    "ice hockey"    : { "ar" : "هوكي الجليد" , "Q" : "Q41466" } ,   #   142
    "American football" : { "ar" : "كرة القدم الأمريكية" , "Q" : "Q41323" } ,   #   152
    "Australian rules football" : { "ar" : "كرة القدم الأسترالية" , "Q" : "Q50776" } ,   #   145
    "winter sports" : { "ar" : "رياضة شتوية" , "Q" : "Q204686" } ,   #   145
    "women's sport" : { "ar" : "رياضة نسوية" , "Q" : "Q920057" } ,   #   140
    }
#---
New_P174 = {
    "Alberta": { "ar" : "ألبرتا" , "Q" : "Q1951" } ,
    "Ontario": { "ar" : "أونتاريو" , "Q" : "Q1904" } ,#476
    "Sports": { "ar" : "الرياضة" , "Q" : "Q349" } ,#367
    "Quebec": { "ar" : "كيبك" , "Q" : "Q176" } ,#367
    "New brunswick": { "ar" : "نيو برونزويك" , "Q" : "Q1965" } ,#358
    #"ceylon": { "ar" : "" , "Q" : "" } ,#356
    "British sport": { "ar" : "الرياضة البريطانية" , "Q" : "Q1282250"} ,#294
    "English sport": { "ar" : "الرياضة الإنجليزية" , "Q" : "Q349" } ,#294
    "English cricket": { "ar" : "الكريكت الإنجليزي" , "Q" : "Q5375" } ,#294
    "British law": { "ar" : "القانون البريطاني" , "Q" : ["Q7748", "Q145"]} ,#257
    "Sports by country": { "ar" : "رياضة حسب البلد" , "Q" : ["Q349" , "Q19360703"] } ,#223
    "Women's sport by country": { "ar" : "رياضة نسوية حسب البلد" , "Q" : ["Q920057" , "Q19360703"] } ,#138
    "Rugby union by country": { "ar" : "اتحاد الرجبي حسب البلد" , "Q" : ["Q5849" , "Q19360703"] } ,#131
    "Rugby league by country": { "ar" : "دوري الرجبي حسب البلد" , "Q" :["Q10962" , "Q19360703"] } ,#123
    #"the united states by state": { "ar" : "" , "Q" : "" } ,#277
    "Case law": { "ar" : "السوابق القضائية" , "Q" : "Q11022655" } ,#247
    "Saskatchewan": { "ar" : "" , "Q" : "" } ,#244
    #"Burma": { "ar" : "" , "Q" : "" } ,#244
    #"the united states by city": { "ar" : "" , "Q" : "" } ,#240
    "American politics": { "ar" : "السياسة الأمريكية" , "Q" : ["Q828", "Q7163"] } ,#239
    "American law": { "ar" : "القانون الأمريكي" , "Q" : ["Q828", "Q7748"] } ,#237
    "Enited states case law": { "ar" : "" , "Q" : ["Q11022655","Q828"] } ,#225
    "European sport": { "ar" : "رياضة أوروبية" , "Q" : ["Q349" , "Q46"] } ,#224
    "the spanish west indies": { "ar" : "جزر الهند الغربية الأسبانية" , "Q" : "Q12213222" } ,#218
    "Siam": { "ar" : "سيام" , "Q" : "Q1081620" } ,#193
    "New york": { "ar" : "نيويورك" , "Q" : "Q1384" } ,#191
    "Czechoslovakia": { "ar" : "تشيكوسلوفاكيا" , "Q" : "Q33946" } ,#190
    "British malaya": { "ar" : "ملايا البريطانية" , "Q" : "Q871091" } ,#182
    }
#---
New_P175 = {
    "north american sport": { "ar" : "" , "Q" : "" } ,#177
    "the polish-lithuanian commonwealth": { "ar" : "" , "Q" : "" } ,#173
    "the cape colony": { "ar" : "" , "Q" : "" } ,#172
    "scottish sport": { "ar" : "" , "Q" : "" } ,#159
    "the viceroyalty of peru": { "ar" : "" , "Q" : "" } ,#159
    "irish sport": { "ar" : "" , "Q" : "" } ,#158
    "american sports": { "ar" : "" , "Q" : "" } ,#158
    "south-west africa": { "ar" : "" , "Q" : "" } ,#157
    "labour relations": { "ar" : "" , "Q" : "" } ,#157
    "norwegian music": { "ar" : "" , "Q" : "" } ,#155
    "oceanian sport": { "ar" : "" , "Q" : "" } ,#152
    "australian sport": { "ar" : "" , "Q" : "" } ,#151
    "south american sport": { "ar" : "" , "Q" : "" } ,#143
    "welsh sport": { "ar" : "" , "Q" : "" } ,#143
    "canadian sports": { "ar" : "" , "Q" : "" } ,#139
    "the austrian empire": { "ar" : "" , "Q" : "" } ,#136
    "australian cricket": { "ar" : "" , "Q" : "" } ,#136
    "women's tennis": { "ar" : "" , "Q" : "" } ,#135
    "motorsport": { "ar" : "" , "Q" : "" } ,#134
    "canadian football": { "ar" : "" , "Q" : "" } ,#134
    "american women's sport": { "ar" : "" , "Q" : "" } ,#134
    "gaelic football": { "ar" : "" , "Q" : "" } ,#132
    "basketball": { "ar" : "" , "Q" : "" } ,#132
    "hurling": { "ar" : "" , "Q" : "" } ,#132
    "new mexico territory": { "ar" : "" , "Q" : "" } ,#131
    "danish sport": { "ar" : "" , "Q" : "" } ,#131
    "new zealand sport": { "ar" : "" , "Q" : "" } ,#130
    "los angeles": { "ar" : "" , "Q" : "" } ,#129
    "south american football": { "ar" : "" , "Q" : "" } ,#129
    "the japanese colonial empire": { "ar" : "" , "Q" : "" } ,#128
    "argentine sport": { "ar" : "" , "Q" : "" } ,#127
    "swedish sport": { "ar" : "" , "Q" : "" } ,#127
    "asian sport": { "ar" : "" , "Q" : "" } ,#127
    "newfoundland and labrador": { "ar" : "" , "Q" : "" } ,#127
    "french sport": { "ar" : "" , "Q" : "" } ,#126
    "bandy": { "ar" : "" , "Q" : "" } ,#126
    "canadian law": { "ar" : "" , "Q" : "" } ,#125
    "cycle racing": { "ar" : "" , "Q" : "" } ,#125
    "british women's sport": { "ar" : "" , "Q" : "" } ,#125
    "swiss sport": { "ar" : "" , "Q" : "" } ,#125
    "arizona territory": { "ar" : "" , "Q" : "" } ,#124
    "dutch sport": { "ar" : "" , "Q" : "" } ,#124
    "african sport": { "ar" : "" , "Q" : "" } ,#124
    "italian sport": { "ar" : "" , "Q" : "" } ,#123
    "austrian sport": { "ar" : "" , "Q" : "" } ,#123
    "english rugby league": { "ar" : "" , "Q" : "" } ,#123
    "belgian sport": { "ar" : "" , "Q" : "" } ,#122
    "spanish sport": { "ar" : "" , "Q" : "" } ,#122
    "new york city": { "ar" : "" , "Q" : "" } ,#121
    "hungarian sport": { "ar" : "" , "Q" : "" } ,#121
    "german sport": { "ar" : "" , "Q" : "" } ,#121
    "athletics (track and field)": { "ar" : "" , "Q" : "" } ,#121
    "paris": { "ar" : "" , "Q" : "" } ,#120
    "comics": { "ar" : "" , "Q" : "" } ,#119
    "south african sport": { "ar" : "" , "Q" : "" } ,#119
    "mexican sports": { "ar" : "" , "Q" : "" } ,#118
    "brazilian sport": { "ar" : "" , "Q" : "" } ,#118
    "american tennis": { "ar" : "" , "Q" : "" } ,#118
    "road cycling": { "ar" : "" , "Q" : "" } ,#118
    "aviation": { "ar" : "" , "Q" : "" } ,#118
    "brazilian football": { "ar" : "" , "Q" : "" } ,#117
    "aquatics": { "ar" : "" , "Q" : "" } ,#117
    "uruguayan sport": { "ar" : "" , "Q" : "" } ,#117
    "south american football leagues": { "ar" : "" , "Q" : "" } ,#117
    "indian territory": { "ar" : "" , "Q" : "" } ,#117
    "norwegian sport": { "ar" : "" , "Q" : "" } ,#116
    "track cycling": { "ar" : "" , "Q" : "" } ,#116
    "turkish sport": { "ar" : "" , "Q" : "" } ,#115
    "figure skating": { "ar" : "" , "Q" : "" } ,#115
    "multi-sport events": { "ar" : "" , "Q" : "" } ,#115
    "water polo": { "ar" : "" , "Q" : "" } ,#113
    "animation": { "ar" : "" , "Q" : "" } ,#113
    "norwegian football": { "ar" : "" , "Q" : "" } ,#112
    "australian rugby league": { "ar" : "" , "Q" : "" } ,#111
    "catalonia": { "ar" : "" , "Q" : "" } ,#111
    "irish politics": { "ar" : "" , "Q" :["", "Q7163"]} ,#110
    "american motorsport": { "ar" : "" , "Q" : "" } ,#110
    "utah territory": { "ar" : "" , "Q" : "" } ,#110
    "greek sport": { "ar" : "" , "Q" : "" } ,#109
    "badminton": { "ar" : "" , "Q" : "" } ,#109
    "british guiana": { "ar" : "" , "Q" : "" } ,#109
    "indian cinema": { "ar" : "" , "Q" : "" } ,#109
    "romanian sport": { "ar" : "" , "Q" : "" } ,#108
    "south african rugby union": { "ar" : "" , "Q" : "" } ,#108
    "asian football": { "ar" : "" , "Q" : "" } ,#107
    "luxembourgian sport": { "ar" : "" , "Q" : "" } ,#107
    "television": { "ar" : "" , "Q" : "" } ,#106
    "radio": { "ar" : "" , "Q" : "" } ,#106
    "uruguayan football": { "ar" : "" , "Q" : "" } ,#106
    "new zealand rugby union": { "ar" : "" , "Q" : "" } ,#106
    "new zealand cricket": { "ar" : "" , "Q" : "" } ,#105
    "yukon": { "ar" : "" , "Q" : "" } ,#104
    "finnish sport": { "ar" : "" , "Q" : "" } ,#104
    "australian rugby union": { "ar" : "" , "Q" : "" } ,#104
    "british television": { "ar" : "" , "Q" : "" } ,#104
    "peruvian sport": { "ar" : "" , "Q" : "" } ,#103
    "indian sport": { "ar" : "" , "Q" : "" } ,#103
    "peruvian football": { "ar" : "" , "Q" : "" } ,#102
    "south african law": { "ar" : "" , "Q" : "" } ,#102
    "wrestling": { "ar" : "" , "Q" : "" } ,#102
    "french motorsport": { "ar" : "" , "Q" : "" } ,#101
    "upper canada": { "ar" : "" , "Q" : "" } ,#101
    "portuguese sport": { "ar" : "" , "Q" : "" } ,#101
    "the straits settlements": { "ar" : "" , "Q" : "" } ,#101
    "biology": { "ar" : "" , "Q" : "" } ,#100
    "american cinema": { "ar" : "" , "Q" : "" } ,#100
    "lower canada": { "ar" : "" , "Q" : "" } ,#99
    "australian law": { "ar" : "" , "Q" : "" } ,#98
    "indian cricket": { "ar" : "" , "Q" : "" } ,#98
    "northern ireland sport": { "ar" : "" , "Q" : "" } ,#98
    "polish sport": { "ar" : "" , "Q" : "" } ,#98
    "canadian case law": { "ar" : "" , "Q" : "" } ,#98
    "japanese sport": { "ar" : "" , "Q" : "" } ,#96
    "american television": { "ar" : "" , "Q" : "" } ,#96
    "bulgarian sport": { "ar" : "" , "Q" : "" } ,#96
    "caribbean sport": { "ar" : "" , "Q" : "" } ,#95
    "south african cricket": { "ar" : "" , "Q" : "" } ,#95
    "irish law": { "ar" : "" , "Q" : "" } ,#95
    "new zealand rugby league": { "ar" : "" , "Q" : "" } ,#95
    "boat racing": { "ar" : "" , "Q" : "" } ,#95
    "computer science": { "ar" : "" , "Q" : "" } ,#95
    "american music": { "ar" : "" , "Q" : "" } ,#94
    "australian tennis": { "ar" : "" , "Q" : "" } ,#93
    "australian women's sport": { "ar" : "" , "Q" : "" } ,#93
    "british motorsport": { "ar" : "" , "Q" : "" } ,#92
    "finnish football": { "ar" : "" , "Q" : "" } ,#92
    "weightlifting": { "ar" : "" , "Q" : "" } ,#91
    "british music": { "ar" : "" , "Q" : "" } ,#90
    "gymnastics": { "ar" : "" , "Q" : "" } ,#90
    "sailing": { "ar" : "" , "Q" : "" } ,#90
    "japanese football": { "ar" : "" , "Q" : "" } ,#89
    "squash": { "ar" : "" , "Q" : "" } ,#89
    "italian motorsport": { "ar" : "" , "Q" : "" } ,#89
    "women's golf": { "ar" : "" , "Q" : "" } ,#89
    "the united states virg": { "ar" : "" , "Q" : "" } ,#89
    "boxing": { "ar" : "" , "Q" : "" } ,#89
    "the mughal empire": { "ar" : "" , "Q" : "" } ,#88
    "the northwest territories": { "ar" : "" , "Q" : "" } ,#87
    "rowing": { "ar" : "" , "Q" : "" } ,#87
    "australian motorsport": { "ar" : "" , "Q" : "" } ,#86
    "camogie": { "ar" : "" , "Q" : "" } ,#86
    "west indian cricket": { "ar" : "" , "Q" : "" } ,#86
    "british cinema": { "ar" : "" , "Q" : "" } ,#86
    "yugoslavian sport": { "ar" : "" , "Q" : "" } ,#85
    "argentine football": { "ar" : "" , "Q" : "" } ,#85
    "sport wrestling": { "ar" : "" , "Q" : "" } ,#85
    "professional wrestling": { "ar" : "" , "Q" : "" } ,#85
    "albanian sport": { "ar" : "" , "Q" : "" } ,#85
    "spaceflight": { "ar" : "" , "Q" : "" } ,#85
    "fencing": { "ar" : "" , "Q" : "" } ,#84
    "snooker": { "ar" : "" , "Q" : "" } ,#84
    "cue sports": { "ar" : "" , "Q" : "" } ,#84
    "speedway": { "ar" : "" , "Q" : "" } ,#84
    "bobsleigh": { "ar" : "" , "Q" : "" } ,#83
    "the colony of natal": { "ar" : "" , "Q" : "" } ,#83
    "cypriot sport": { "ar" : "" , "Q" : "" } ,#83
    "table tennis": { "ar" : "" , "Q" : "" } ,#83
    "the british virg": { "ar" : "" , "Q" : "" } ,#82
    "volleyball": { "ar" : "" , "Q" : "" } ,#82
    "venezuelan sport": { "ar" : "" , "Q" : "" } ,#82
    "shooting sports": { "ar" : "" , "Q" : "" } ,#81
    "archery": { "ar" : "" , "Q" : "" } ,#81
    "ski jumping": { "ar" : "" , "Q" : "" } ,#81
    "moldavia": { "ar" : "" , "Q" : "" } ,#81
    "african football": { "ar" : "" , "Q" : "" } ,#80
    "new zealand law": { "ar" : "" , "Q" : "" } ,#79
    "israeli sport": { "ar" : "" , "Q" : "" } ,#79
    "swimming": { "ar" : "" , "Q" : "" } ,#79
    "central american sport": { "ar" : "" , "Q" : "" } ,#79
    "alpine skiing": { "ar" : "" , "Q" : "" } ,#78
    "nascar": { "ar" : "" , "Q" : "" } ,#78
    "german motorsport": { "ar" : "" , "Q" : "" } ,#77
    "cross-country skiing": { "ar" : "" , "Q" : "" } ,#77
    "swedish football": { "ar" : "" , "Q" : "" } ,#77
    "israeli politics": { "ar" : "" , "Q" : ["", "Q7163"] } ,#76
    "canadian television": { "ar" : "" , "Q" : "" } ,#76
    "french women's sport": { "ar" : "" , "Q" : "" } ,#76
    "british politics": { "ar" : "" , "Q" :["", "Q7163"] } ,#76
    "gold coast (british colony)": { "ar" : "" , "Q" : "" } ,#76
    "lgbt history": { "ar" : "" , "Q" : "" } ,#76
    "women's basketball": { "ar" : "" , "Q" : "" } ,#76
    "youth sport": { "ar" : "" , "Q" : "" } ,#75
    "german television": { "ar" : "" , "Q" : "" } ,#75
    "maltese sport": { "ar" : "" , "Q" : "" } ,#75
    "portuguese mozambique": { "ar" : "" , "Q" : "" } ,#75
    "luge": { "ar" : "" , "Q" : "" } ,#75
    "the united nations": { "ar" : "" , "Q" : "" } ,#74
    "philippine cinema": { "ar" : "" , "Q" : "" } ,#74
    "washington territory": { "ar" : "" , "Q" : "" } ,#74
    "canoeing": { "ar" : "" , "Q" : "" } ,#74
    "hong kong sport": { "ar" : "" , "Q" : "" } ,#74
    "chilean sport": { "ar" : "" , "Q" : "" } ,#73
    "belgian television": { "ar" : "" , "Q" : "" } ,#73
    "odisha": { "ar" : "" , "Q" : "" } ,#73
    "algerian sport": { "ar" : "" , "Q" : "" } ,#73
    "diving": { "ar" : "" , "Q" : "" } ,#73
    "comoros": { "ar" : "" , "Q" : "" } ,#73
    "youth association football": { "ar" : "" , "Q" : "" } ,#72
    "french television": { "ar" : "" , "Q" : "" } ,#72
    "czechoslovak sport": { "ar" : "" , "Q" : "" } ,#72
    "handball": { "ar" : "" , "Q" : "" } ,#72
    "nordic combined": { "ar" : "" , "Q" : "" } ,#71
    "danish television": { "ar" : "" , "Q" : "" } ,#71
    "icelandic sport": { "ar" : "" , "Q" : "" } ,#71
    "dutch television": { "ar" : "" , "Q" : "" } ,#71
    "speed skating": { "ar" : "" , "Q" : "" } ,#71
    "philippine sport": { "ar" : "" , "Q" : "" } ,#71
    "australian television": { "ar" : "" , "Q" : "" } ,#71
    "grand prix motorcycle racing": { "ar" : "" , "Q" : "" } ,#70
    "the danish colonial empire": { "ar" : "" , "Q" : "" } ,#70
    "formula one": { "ar" : "" , "Q" : "" } ,#70
    "japanese television": { "ar" : "" , "Q" : "" } ,#70
    "brazilian television": { "ar" : "" , "Q" : "" } ,#70
    "swedish television": { "ar" : "" , "Q" : "" } ,#69
    "south korean sport": { "ar" : "" , "Q" : "" } ,#69
    "curaçao and dependencies": { "ar" : "" , "Q" : "" } ,#69
    "italian music": { "ar" : "" , "Q" : "" } ,#69
    "mexican television": { "ar" : "" , "Q" : "" } ,#69
    "pakistani sport": { "ar" : "" , "Q" : "" } ,#68
    "biathlon": { "ar" : "" , "Q" : "" } ,#68
    "egyptian sport": { "ar" : "" , "Q" : "" } ,#68
    "canadian music": { "ar" : "" , "Q" : "" } ,#68
    "guernsey": { "ar" : "" , "Q" : "" } ,#68
    "biotechnology": { "ar" : "" , "Q" : "" } ,#67
    "irish television": { "ar" : "" , "Q" : "" } ,#67
    "pakistani cricket": { "ar" : "" , "Q" : "" } ,#67
    "portuguese guinea": { "ar" : "" , "Q" : "" } ,#66
    "cannabis": { "ar" : "" , "Q" : "" } ,#66
    "croatian sport": { "ar" : "" , "Q" : "" } ,#66
    "swedish music": { "ar" : "" , "Q" : "" } ,#65
    "norwegian television": { "ar" : "" , "Q" : "" } ,#64
    "women's volleyball": { "ar" : "" , "Q" : "" } ,#64
    "iranian sport": { "ar" : "" , "Q" : "" } ,#64
    "italian television": { "ar" : "" , "Q" : "" } ,#64
    "curling": { "ar" : "" , "Q" : "" } ,#64
    "philippine television": { "ar" : "" , "Q" : "" } ,#64
    "dakota territory": { "ar" : "" , "Q" : "" } ,#64
    "field hockey": { "ar" : "" , "Q" : "" } ,#63
    "the moldavian soviet socialist republic": { "ar" : "" , "Q" : "" } ,#63
    "croatian television": { "ar" : "" , "Q" : "" } ,#63
    "irish music": { "ar" : "" , "Q" : "" } ,#62
    "thai sport": { "ar" : "" , "Q" : "" } ,#61
    "french equatorial africa": { "ar" : "" , "Q" : "" } ,#61
    "czech television": { "ar" : "" , "Q" : "" } ,#61
    "michigan territory": { "ar" : "" , "Q" : "" } ,#61
    "latvian sport": { "ar" : "" , "Q" : "" } ,#60
    "malaya": { "ar" : "" , "Q" : "" } ,#60
    "venezuelan television": { "ar" : "" , "Q" : "" } ,#60
    "japanese music": { "ar" : "" , "Q" : "" } ,#59
    "swedish association football leagues": { "ar" : "" , "Q" : "" } ,#59
    "honduran sport": { "ar" : "" , "Q" : "" } ,#59
    "video gaming": { "ar" : "" , "Q" : "" } ,#59
    "bowling": { "ar" : "" , "Q" : "" } ,#59
    "canadian politics": { "ar" : "" , "Q" : ["", "Q7163"] } ,#59
    "soviet sport": { "ar" : "" , "Q" : "" } ,#58
    "kuwaiti sport": { "ar" : "" , "Q" : "" } ,#58
    "cuban sport": { "ar" : "" , "Q" : "" } ,#58
    "the state of the teutonic order": { "ar" : "" , "Q" : "" } ,#58
    "the kazakh soviet socialist republic": { "ar" : "" , "Q" : "" } ,#58
    "libyan sport": { "ar" : "" , "Q" : "" } ,#57
    "castile": { "ar" : "" , "Q" : "" } ,#57
    "rugby league by club": { "ar" : "" , "Q" : "" } ,#57
    "roller hockey": { "ar" : "" , "Q" : "" } ,#57
    "cameroonian football": { "ar" : "" , "Q" : "" } ,#57
    "cameroonian sport": { "ar" : "" , "Q" : "" } ,#57
    "central american football": { "ar" : "" , "Q" : "" } ,#57
    "lithuanian sport": { "ar" : "" , "Q" : "" } ,#56
    "austrian television": { "ar" : "" , "Q" : "" } ,#56
    "american soccer": { "ar" : "" , "Q" : "" } ,#56
    "american sports by state": { "ar" : "" , "Q" : "" } ,#56
    "aragon": { "ar" : "" , "Q" : "" } ,#56
    "soviet football leagues": { "ar" : "" , "Q" : "" } ,#56
    "alta california": { "ar" : "" , "Q" : "" } ,#56
    "canadian soccer": { "ar" : "" , "Q" : "" } ,#56
    "soviet football": { "ar" : "" , "Q" : "" } ,#56
    "african basketball": { "ar" : "" , "Q" : "" } ,#55
    "spanish motorsport": { "ar" : "" , "Q" : "" } ,#55
    "australian cinema": { "ar" : "" , "Q" : "" } ,#55
    "malaysian sport": { "ar" : "" , "Q" : "" } ,#55
    "indian sports": { "ar" : "" , "Q" : "" } ,#55
    "concacaf football": { "ar" : "" , "Q" : "" } ,#55
    "hong kong television": { "ar" : "" , "Q" : "" } ,#54
    "american soccer leagues": { "ar" : "" , "Q" : "" } ,#54
    "estonian sport": { "ar" : "" , "Q" : "" } ,#54
    "estonian football": { "ar" : "" , "Q" : "" } ,#54
    "san francisco": { "ar" : "" , "Q" : "" } ,#54
    "asian basketball": { "ar" : "" , "Q" : "" } ,#53
    "canadian motorsport": { "ar" : "" , "Q" : "" } ,#53
    "bodybuilding": { "ar" : "" , "Q" : "" } ,#53
    "indonesian sport": { "ar" : "" , "Q" : "" } ,#53
    "french cinema": { "ar" : "" , "Q" : "" } ,#53
    "lacrosse": { "ar" : "" , "Q" : "" } ,#53
    "ugandan sport": { "ar" : "" , "Q" : "" } ,#53
    "british honduras": { "ar" : "" , "Q" : "" } ,#53
    "lithuanian football": { "ar" : "" , "Q" : "" } ,#52
    "latvian football": { "ar" : "" , "Q" : "" } ,#52
    "jamaican sport": { "ar" : "" , "Q" : "" } ,#52
    "montana territory": { "ar" : "" , "Q" : "" } ,#52
    "karate": { "ar" : "" , "Q" : "" } ,#52
    "taiwanese sport": { "ar" : "" , "Q" : "" } ,#51
    "equestrian": { "ar" : "" , "Q" : "" } ,#51
    "the austrian netherlands": { "ar" : "" , "Q" : "" } ,#51
    "the viceroyalty of new granada": { "ar" : "" , "Q" : "" } ,#51
    "florida territory": { "ar" : "" , "Q" : "" } ,#51
    "pakistani sports": { "ar" : "" , "Q" : "" } ,#51
    "tunisian sport": { "ar" : "" , "Q" : "" } ,#51
    "new zealand television": { "ar" : "" , "Q" : "" } ,#51
    "rallying": { "ar" : "" , "Q" : "" } ,#51
    "canadian curling": { "ar" : "" , "Q" : "" } ,#51
    "japanese cinema": { "ar" : "" , "Q" : "" } ,#51
    "turkish politics": { "ar" : "" , "Q" : ["", "Q7163"] } ,#51
    "guatemalan sport": { "ar" : "" , "Q" : "" } ,#50
    "estonian television": { "ar" : "" , "Q" : "" } ,#50
    "saudi arabian sport": { "ar" : "" , "Q" : "" } ,#50
    "moroccan sport": { "ar" : "" , "Q" : "" } ,#50
    "icelandic football": { "ar" : "" , "Q" : "" } ,#49
    "polish television": { "ar" : "" , "Q" : "" } ,#49
    "spanish television": { "ar" : "" , "Q" : "" } ,#49
    "modern pentathlon": { "ar" : "" , "Q" : "" } ,#49
    "israeli television": { "ar" : "" , "Q" : "" } ,#48
    "poker": { "ar" : "" , "Q" : "" } ,#48
    "german south-west africa": { "ar" : "" , "Q" : "" } ,#48
    "oceanian association football leagues": { "ar" : "" , "Q" : "" } ,#48
    "softball": { "ar" : "" , "Q" : "" } ,#48
    "berlin": { "ar" : "" , "Q" : "" } ,#47
    "women's athletics": { "ar" : "" , "Q" : "" } ,#47
    "hamburg": { "ar" : "" , "Q" : "" } ,#47
    "women's association football": { "ar" : "" , "Q" : "" } ,#47
    "the belgian congo": { "ar" : "" , "Q" : "" } ,#47
    "the aztec civilization": { "ar" : "" , "Q" : "" } ,#47
    "the northwest territory": { "ar" : "" , "Q" : "" } ,#47
    "sri lankan sport": { "ar" : "" , "Q" : "" } ,#47
    "women's handball": { "ar" : "" , "Q" : "" } ,#47
    "canadian cinema": { "ar" : "" , "Q" : "" } ,#47
    "the swedish colonial empire": { "ar" : "" , "Q" : "" } ,#47
    "costa rican sport": { "ar" : "" , "Q" : "" } ,#47
    "robotics": { "ar" : "" , "Q" : "" } ,#46
    "chinese sport": { "ar" : "" , "Q" : "" } ,#46
    "emirati sport": { "ar" : "" , "Q" : "" } ,#46
    "fijian sport": { "ar" : "" , "Q" : "" } ,#46
    "women's cricket": { "ar" : "" , "Q" : "" } ,#46
    "australian music": { "ar" : "" , "Q" : "" } ,#46
    "sri lankan cricket": { "ar" : "" , "Q" : "" } ,#46
    "spanish music": { "ar" : "" , "Q" : "" } ,#45
    "paraguayan sport": { "ar" : "" , "Q" : "" } ,#45
    "nunavut": { "ar" : "" , "Q" : "" } ,#45
    "finnish television": { "ar" : "" , "Q" : "" } ,#45
    "north korean sport": { "ar" : "" , "Q" : "" } ,#45
    "ukrainian sport": { "ar" : "" , "Q" : "" } ,#45
    "colombian sport": { "ar" : "" , "Q" : "" } ,#45
    "swedish cinema": { "ar" : "" , "Q" : "" } ,#45
    "paraguayan football": { "ar" : "" , "Q" : "" } ,#45
    "idaho territory": { "ar" : "" , "Q" : "" } ,#44
    "boston": { "ar" : "" , "Q" : "" } ,#44
    "american women's basketball": { "ar" : "" , "Q" : "" } ,#44
    "philippine basketball": { "ar" : "" , "Q" : "" } ,#44
    "esports": { "ar" : "" , "Q" : "" } ,#43
    "taiwanese television": { "ar" : "" , "Q" : "" } ,#43
    "go": { "ar" : "" , "Q" : "" } ,#43
    "australian soccer": { "ar" : "" , "Q" : "" } ,#43
    "east german sport": { "ar" : "" , "Q" : "" } ,#43
    "the kingdom of georgia": { "ar" : "" , "Q" : "" } ,#43
    "zaire": { "ar" : "" , "Q" : "" } ,#43
    "italian cinema": { "ar" : "" , "Q" : "" } ,#42
    "indian television": { "ar" : "" , "Q" : "" } ,#42
    "spanish tennis": { "ar" : "" , "Q" : "" } ,#42
    "french music": { "ar" : "" , "Q" : "" } ,#42
    "darts": { "ar" : "" , "Q" : "" } ,#42
    "baden": { "ar" : "" , "Q" : "" } ,#42
    "chinese television": { "ar" : "" , "Q" : "" } ,#42
    "polish football": { "ar" : "" , "Q" : "" } ,#41
    "oklahoma territory": { "ar" : "" , "Q" : "" } ,#41
    "bangladeshi sport": { "ar" : "" , "Q" : "" } ,#41
    "new zealand basketball": { "ar" : "" , "Q" : "" } ,#41
    "upper volta": { "ar" : "" , "Q" : "" } ,#41
    "canadian rugby union": { "ar" : "" , "Q" : "" } ,#41
    "argentine television": { "ar" : "" , "Q" : "" } ,#41
    "colombian television": { "ar" : "" , "Q" : "" } ,#40
    "west german sport": { "ar" : "" , "Q" : "" } ,#40
    "synchronized swimming": { "ar" : "" , "Q" : "" } ,#40
    "grand prix racing": { "ar" : "" , "Q" : "" } ,#40
    "singaporean sport": { "ar" : "" , "Q" : "" } ,#40
    "bahamian sport": { "ar" : "" , "Q" : "" } ,#40
    "wyoming territory": { "ar" : "" , "Q" : "" } ,#40
    "islam": { "ar" : "" , "Q" : "" } ,#40
    "chinese football": { "ar" : "" , "Q" : "" } ,#40
    "mississippi territory": { "ar" : "" , "Q" : "" } ,#39
    "syrian sport": { "ar" : "" , "Q" : "" } ,#39
    "jordanian sport": { "ar" : "" , "Q" : "" } ,#39
    "women's curling": { "ar" : "" , "Q" : "" } ,#39
    "kickboxing": { "ar" : "" , "Q" : "" } ,#39
    "women's field hockey": { "ar" : "" , "Q" : "" } ,#39
    "west german motorsport": { "ar" : "" , "Q" : "" } ,#39
    "french rugby league": { "ar" : "" , "Q" : "" } ,#39
    "puerto rican sport": { "ar" : "" , "Q" : "" } ,#39
    "vietnamese sport": { "ar" : "" , "Q" : "" } ,#39
    "lebanese sport": { "ar" : "" , "Q" : "" } ,#38

    }
#---
saop = [USA_P17 , ALL_P17,New_P17 , New_P172 , New_P173 , New_P174]
P17_final = {}
P17_final_lower = {}
for sao in saop:
    for sasas in sao.keys():
        P17_final[sasas] = sao[sasas]
        P17_final_lower[sasas.lower()] = sao[sasas]
#---
frf = []
def main():
    
from API import printe
import pywikibot
    for k in P17_final.keys():
        k2 = k.lower()
        if not k2 in frf:
            printe.output('   ,"%s" : "%s"' %   ( k2 , P17_final[k]["ar"])  )
            frf.append(k2)
    printe.output(' len frf "%d" : len P17_final "%d"' %   ( len(frf) , len(P17_final.keys()) )  )
#---
if __name__ == "__main__":
    main()
#---