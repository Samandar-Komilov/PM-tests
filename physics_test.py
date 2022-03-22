import random

# ---| [1] KINEMATIKA \---


moddiy_nuqta_vektorlar = ["Fizika qanday qismlardan iborat?","Mexanika nima?","Kinematika/Dinamika/Statika nima?","Mexanik harakat nima?","Moddiy nuqta nima?","Ilgarilanma harakat nima?","Sanoq jismi nima?","Sanoq sistemasi nima?","Koordinata sistemasi va turlari qanday?","Trayektoriya nima?","Yo'l nima?","Ko'chish nima?","Kesma nima?","vektor nima? Vektorlarni qo'shish qoidalari qanday?","Bir xil yo'nalishli vektorlar qanday qo'shiladi?","Qarama-qarshi yo'nalishli vektorlar qanday qo'shiladi?","Vektorni songa ko'paytirish qanday?","Jismning mexanik harakatini o'rganishda koordinatalar sistemasi nima maqsadda beriladi?","Sanoq sistemasi nima uchun kerak?"]

tch_tekis_harakat = ["Trayektoriya shakliga qarab harakatlar qanday turlarga bo'linadi?","Qanday harakat turida ko'chish yo'lga teng?","T/ch li tekis harakat nima?","Tezlik ta'rifi formulasi va birligi qanday?","T/ch li tekis harakatda tezlik moduli va yo'nalishi qanday o'zgaradi?","Spidometr nima?","Harakat qonuni nima?","Umumiy holda tenglamasi qanday?","t/ch li tekis harakat tenglamasi qanday?","t/ch li tekis harakatda tezlikning vaqtga/yo'lning vaqtga bog'liqligi grafigi qanday?","Tezlikning vaqtga bog'liqligidan hosil bo'lgan yuza son jihatidan qanday kattalikka teng?","T/ch li tekis harakatning yo'l grafigi qanday chiziq?","Tezliklari turlicha bo'lgan t/ch li tekis harakatda yo'l grafiklari qaysi biri tikroq bo'ladi?","T/ch li tekis harakat tezlik grafigidan moddiy nuqta bosib o'tgan yo'li qanday aniqlanadi?"]

harakat_nisbiyligi = ["Harakat nisbiyligi nima?","Turli hollar uchun tezliklar qo'shilishi qanday?","Ikkitadan ortiq tezliklar qanday qo'shiladi?","Bir-biriga tik yo'nalgan tezliklar qanday qo'shiladi?","Vektorlarni kosinuslar teoremasi bo'yicha qanday qo'shiladi?","Gayka boltga gayka kaliti yordamida burab kiritilmoqda, gayka belgilangan nuqtaning gayka kalitiga nisbatan harakat trayektoriyasi qanday bo'ladi?"]

notekis_harakat = ["Notekis harakat va uning turlari qanday?","O'rtacha tezlik va oniy tezlik ta'rifi va formulasi qanday?","Jism yo'lning/vaqtning turli qismlarida turli tezliklar bilan harakatlanganda, o'rtacha tezlik qanday topiladi?","Tekis tezlanuvchan/sekinlanuvchan harakatda tezlikning vaqtga/yo'lning vaqtga/tezlanishning vaqtga bog'liqlik grafigi","Tekis tezlanuvchan/sekinlanuvchan harakat tenglamasi qanday?"]

erkin_tushish = ["Erkin tushish nima? Uning tezlanishi va qiymatlari - ?","Boshlang'ich tezliksiz/bilan erkin tushayotgan jismning oniy tezligi/balandligi/vaqti qanday?","Tekis o'zgaruvchan harakatda n sekundda bosib o'tilgan yo'l formulasi nima?","Yuqoriga tik otilgan jismning oniy tezligi/maximal balandligi/ko'tarilish vaqti/uchish vaqti qanday?","Yuqoriga tik otilgan jismning ixtiyoriy vaqtdagi ko'tarilish balandligi - ?","Erkin tushayotgan jism oxirgi sekunddagi yo'lini topish formulasi qanday?","Erkin tushayotgan jism qanday harakatlanadi?","Erkin tushayotgan/Yuqoriga otilgan jism tezlanishi qanday yo'nalgan? Tezligichi?","Erkin tushish tezlanishining qiymati nimalarga bog'liq?","Yuqoriga tik otilgan jismning eng yuqori balandlikdagi tezligi/tezlanishi nimaga teng?"]

aylanma_harakat = ["Aylana bo'ylab tekis harakat nima?","Davr ta'rifi va formulasi - ?","Chastota ta'rifi va formulasi nima?","Burchak tezlik ta'rifi va formulasi nima?","Burchak tezlikning aylanish davriga/chastotasiga bog'liqlik formulalari - ?","Davr va chastota orasidagi bog'liqlik formulasi - ?","Chiziqli tezlik ta'rifi va formulasi qanday?","Chiziqli tezlikning aylanish davriga/chastotasiga/burchak tezlikka bog'liqlik formulasi qanday?","Aylana uzunligini topish formulasi qanday?","Aylana bo'ylab tekis harakatlanayotgan jismning chiziqli tezligining/burchak tezligining/markazga intilma tezlanishining qiymati o'zgaradimi? Yo'nalishichi?","Chiziqli tezlik qayerga yo'nalgan?","Markazga intilma tezlanishning aylanish chastotasiga/burchak tezlikka/chiziqli tezlikka/davrga bog'liqlik formulalari qanday?"]

aylana_boylab_uzatish = ["Tasmali uzatma nima?","Harakat tasmali/zanjirli uzatma yordamida bir shkivdan ikkinchisiga uzatilayotganda shkivlarning aylanish davrlari, chastotalari va chiziqli tezliklari qanday munosabatda bo'ladi?","Zanjirli uzatma nima?","Ikkita shkiv bitta o'qga mahkamlanganda, shkivlarning aylanish davrlari, chastotalari va chiziqli tezliklari qanday munosabatda bo'ladi?","Friksion bog'lanish nima?","Friksion bog'langan ikki shkivning chiziqli tezliklari va burchak tezliklari qanday munosabatda bo'ladi?"]

tch_tekis_ozgaruvchan_harakat = ["Tekis tezlanuvchan harakat nima?","Tekis sekinlanuvchan harakat nima?","Tezlanish tarifi va formulasi qanday?","Tekis o'zgaruvchan harakat nima?","Tekis tezlanuvchan/sekinlanuvchan harakatda oniy tezlik/yo'l/o'rtacha tezlik formulalari - ?","Qaysi harakat turida tezlanish noldan katta/kichik/teng bo'ladi?","Musbat va manfiy tezlanishlar qaysi harakat turlarida qo'llaniladi?","To'g'ri chiziqli tekis tezlanuvchan/sekinlanuvchan harakatda tezlik/tezlanish moduli va yo'nalishi qanday?"]

aylana_notekis_harakat = ["Markazga intilma tezlanish qayerga yo'nalgan?","Urinma tezlanish ta'rifi va formulasi qanday?","Aylana bo'ylab harakatda umumiy tezlanish nimaga teng?","Aylana bo'ylab tekis harakatlanayotgan jismning urinma tezlanish qiymati o'zgaradimi? Yo'nalishichi?","Burchak tezlanish nima?","Aylana bo'ylab notekis harakatda ixtiyoriy vaqt momentida burilish burchagi qanday topiladi?","Oniy burchak tezlik nima?"]

gorizontal_otilgan_jism = ["Gorizontal otilgan jism trayektoriyasi/uchish vaqti/uzoqligi qanday?","Gorizontal otilgan jism ixtiyoriy vaqtdagi gorizont bilan tashkil etgan burchagini topish formulasi qanday?","Gorizontal otilgan jism vertikal tezligini/gorizontal tezligini/natijaviy tezligini/tangensial tezlanishini/normal tezlanishini topish formulalari qanday?","Gorizontal otilgan jism natijaviy tezlanishini yo'nalishi va son qiymati qanday?"]

gorizontga_qiya_otilgan_jism = ["Gorizontga qiya otilgan jism trayektoriyasi qanday?","Gorizontga qiya otilgan jism vertikal/gorizontal tezligini, ko'tarilish balandligi/uchish uzoqligi/uchish vaqtini/ko'tarilish vaqtini topish formulasi - ?","Gorizontga qiya otilgan jism trayektoriyasining egrilik radiusini topish formulasi - ?","Gorizontga qiya otilgan jism ixtiyoriy vaqt momentidagi gorizont bilan tashkil qilgan burchagini topish formulasi qanday?","Gorizontga qiya otilgan jism umumiy tezligini topish formulasi - ?","Gorizontga qiya otilgan jism minimal va maximal tezliklari nimaga teng?","Gorizontga qiya otilgan jismda root_2h/R qanday kattalik?","Gorizontga qiya otilgan jism tezlanishi nimaga teng va qayerga yo'nalgan?","Gorizontga nisbatan burchak ostida otilgan jismning harakati davomida qaysi kattalik doimiysi emas?"]

kinematika = moddiy_nuqta_vektorlar + tch_tekis_harakat + harakat_nisbiyligi + notekis_harakat + erkin_tushish + aylanma_harakat + aylana_boylab_uzatish + tch_tekis_ozgaruvchan_harakat + aylana_notekis_harakat + gorizontal_otilgan_jism + gorizontga_qiya_otilgan_jism


# ---| [2] DINAMIKA \---


zichlik_massa_nyuton_qonunlari = ["Massa nima?","Inertlik nima?","Kuch nima?","Zichlik nima?","Dinamometr nima?","Gravitatsion massa nima?","Inert massa nima?","1 N ta'rifi qanday?","Areometr nima?","Galileyning nisbiylik prinsipi qanday?","Inersial sanoq sistemasi nima?","Solishtirma hajm nima?","Nyutonning 1 va 2 qonunlari - ?","Kuch qanday kattalik? Birligini XBS orqali ifodalang.","Kuch yo'nalishi qanday aniqlanadi?","Kuchlar qanday qo'shiladi?","Teng ta'sir etuvchi kuch nima?","To'g'ri chiziqli tekis/tezlanuvchan harakat qilayotgan jismga ta'sir etuvchi natijaviy kuch qanday yo'nalgan?","Nyutonning 3-qonuni qanday?","Nyutonning 2 va 3 qonunlari birlashmasi qanday?","Nyutonning 3 ta qonuni doim o'rinlimi?"]

aylanma_kuch_b_o_tortishish = ["Markazga intilma va markazdan qochma kuchlari formulalari va ta'riflari qanday?","Aylana bo'ylab tekis harakatda markazdan qochma kuch aylanish davriga/chiziqli tezlikka/burchak tezlikka qanday bog'liq?","Butun olam tortishish qonuni nima?","Gravitatsion doimiysi va uning ta'rifi qiymati birligi - ?","Erkin tushish tezlanishini topish formulasi qanday?","Erkin tushish tezlanishi qiymati nima uchun Yerning turli qismlarida turlicha?","Yerdan biror balandlikdagi erkin tushish tezlanishi nimaga teng?","Oydagi erkin tushish tezlanishi nimaga teng?","Planetadagi erkin tushish tezlanishi berilgan holda zichlikni topish formulasi qanday?"]

ogirlik_kuchi = ["Og'irlik kuchi formulasi va ta'rifi qanday?","Og'irlik va og'irlik kuchi farqi nimada?","Vaznsizlik nima?","Yuklanish nima?","Yuklanishni topish formulasi qanday?","O'lik sirtmoq yoki botiq ko'prikda jism og'irligini topish formulalari qanday?","Qavariq ko'prikda jism og'irligini topish formulalari qanday?","Qavariq ko'prikda harakatlanayotgan jism qachon vaznsizlik holatida bo'ladi?","Yuqoriga tekis tezlanuvchan/sekinlanuvchan harakat qilayotgan jismning og'irligi qanday o'zgaradi? Uning og'irligi qanday topiladi?","Pastga tekis tezlanuvchan/sekinlanuvchan harakat qilayotgan jismning og'irligi qanday o'zgaradi? Uning og'irligi qanday topiladi?","Yuqoriga/Pastga tekis harakat qilayotgan jismning og'irligi qanday o'zgaradi? Uning og'irligi qanday topiladi?","Nesterov sirtmog'i nima?","Massasi ma'lum bo'lgan shar havoda muallaq holda turgan bo'lsa, uning vazni qanday topiladi?","Agar jismni chuqur shaxtaning ichiga joylashtirilsa, uning vazni qanday o'zgaradi?","Zargar o'z tillasini pallali torozi yordamida Yerning qaysi nuqtasida sotsa ko'proq foyda ko'radi?"]

kosmik_tezliklar = ["I,II,III,IV kosmik tezliklar ta'riflari qanday?","I kosmik tezlikni topish formulasi qanday? Yerdan h balandlikda bo'lsachi?","Sun'iy yo'ldoshning aylanish davri qanday topiladi?","II kosmik tezlikni topish formulasini keltirib chiqaring.","Sun'iy yo'ldosh qanday tezlikda harakatlanganda uning trayektoriyasi giperbola/parabola/ellips dan iborat bo'ladi?","Oy - Yerning tabiiy yo'ldoshi. Agar Yer bilan Oy o'rtasidagi o'zaro tortishish kuchi birdan yo'qolsa, Oyning keyingi harakati qanday bo'ladi?"]

elastiklik_kuchi = ["Elastiklik kuchida reaksiya kuchi nima?"] #Qolgan savollar qattiq jism mexanikasida berilgan ekan

prujinalar = ["Prujinalar ketma-ket/parallel ulanganda umumiy bikrlik qanday topiladi?","Bikrligi bir xil bo'lgan n ta prujinalar parallel/ketma-ket ulanganda umumiy bikrlik qanday topiladi?"]

ishqalanish_kuchi = ["Ishqalanish kuchlari nima?","Ishqalanish kuchlarining vujudga kelishiga asosiy sabablar nima?","Ishqalanish kuchining yo'nalishi qanday?","Tashqi ishqalanish nima?","Ichki ishqalanish nima?","Ishqalanish kuchi qanday topiladi?","Ishqalanish koeffitsiyenti nima, qanday topiladi, birligi - ?","Sirpanish ishqalanish kuchi nima?","Ishqalanish koeffitsiyenti bir-biriga tegib turgan jismlar sirtining kattaligiga bog'liqmi?","Gorizontal sirtda odam ketmoqda. Odam chap oyog'i bilan sirtdan itarilayotganda sirt tomonidan odamga ta'sir etuvchi ishqalanish kuchi qaysi tomonga yo'nalgan?","Avtomobil oldinga harakatlanmoqda, uning g'ildiragi va sirt orasidagi ishqalanish kuchi qayerga yo'nalgan?","Vertikal sirtga magnit yopishib turibdi. Magnit va sirt orasidagi ishqalanish kuchi qanday topiladi?","To'g'ri chiziqli tekis/tekis tezlanuvchan/sekinlashuvchan harakatlanayotgan avtomobil kuzovidagi yashikka pol tomonidan ta'sir etuvchi ishqalanish kuchining yo'nalishi qanday?"]

gorizontal_vertikal_qiya_tekisliklar = ["Qiya tekislikda ishqalanish kuchi qanday topiladi?","Pastga harakatlantiruvchi kuch nima?","Qiya tekislikda normal bosim kuchi qanday topiladi?","Qiya tekislikda reaksiya kuchi qanday topiladi?","Qiya tekislikda ishqalanish koef berilgan holda tezlanish qanday topiladi?","Qiya tekislikda jism tinch/tekis tezlanuvchan/sekinlanuvchan turishi uchun qanday shart bajarilishi kerak?","Gorizontal tekislikda jism tinch/tekis tezlanuvchan/sekinlanuvchan harakat qilishi uchun qanday shart bajarilishi kerak?","Gorizontal tekislikda faqat ishqalanish kuchi ta'siridagi harakatda tezlanish qanday topiladi?","Harakatning dinamik tenglamasi qanday?","Gorizontal tekislikda bir necha kuch ta'siridagi harakatda tezlanish qanday topiladi?","Vertikal tekislikda jism tinch/tekis sekinlanuvchan/tezlanuvchan harakat qilishi uchun qanday shart bajarilishi kerak?","Vertikal tekislikga faqat ishqalanish kuchi ta'siridagi harakatda tezlanish qanday topiladi?","Vertikal tekislikda bir necha kuch ta'siridagi harakatda tezlanish qanday topiladi?","Shamol havo sharini sharqqa olib ketyapti. Sharning yuqori nuqtasiga o'rnatilgan bayroq qaysi tomonga hilpillaydi?","Qiya tekislikda bir necha kuch ta'siridagi harakatda tezlanish qanday topiladi?","Qiya tekislikda jismni qiyalik bo'ylab tekis/tezlanish bilan tortish uchun qanday kuch kerak bo'ladi?","Qiya tekislikda sirpanib tushayotgan jismning tezlanishi qanday topiladi?"]

kochmas_blok = ["Qo'zg'almas blokda tezlanish/ipning taranglik kuchi qanday topiladi?","Silliq stoldan arqon sirpanib tushmoqda (ishqalanish yo'q), arqon harakatining xarakteri qanday?"]

impuls = ["Jism impulsi ta'rifi, formulasi va birligi - ?","Kuch impulsi ta'rifi, formulasi va birligi - ?","Jism va kuch impulslari orasidagi bog'liqlik formulasini keltirib chiqaring.","Jismlar sistemasi nima?","Yopiq sistema nima?","Impulsda ichki/tashqi kuchlar nima?","Impulsning saqlanish qonuni ta'rifi va formulasi qanday?","Reaktiv harakat nima?","Raketa tezligi qanday topiladi?","To'qnashishlar necha turga bo'linadi?","To'qnashishlar qanday parametrlarga qarab bo'linadi?","Mutlaq elastik/noelastik to'qnashish nima?","Mutlaq to'qnashishda sistemaning tezligi qanday aniqlanadi?","Bir-biriga/Bir tomonga qarab harakatlanayotgan jismlar noelastik to'qnashgandan keyingi tezligi qanday topiladi?","Ikki jism qanday to'qnashgandan keyin yagona bitta jism sifatida harakatlanadi?"]

mexanik_ish = ["Mexanik ish nima? Uning birligi (XBS da), formulasi qanday?","Mexanik ish qachon musbat/manfiy/nol bo'ladi?","Kuchning ko'chishga bog'liqlik grafigidan hosil bo'lgan yuza son jihatidan nimaga teng?","O'zgarmas kuchning bajargan ishi nimaga teng?"]

energiya = ["Energiya nima?","Kinetik energiya nima?","Potensial energiya nima?","Potensial energiya nima sababdan vujudga keladi?","Deformatsiyalangan jismning potensial energiyasi qanday?","Energiya birligi nima? XBS orqali ifodalang.","Kaloriya nimaning birligi?","Kinetik energiyaning tezlikka bog'liq grafigi qanday?"]

energiya_mexanik_ish_bogliqlik = ["Kinetik energiya bilan mexanik ish orasida qanday bog'liqlik bor?","Potensial energiya bilan mexanik ish orasida qanday bog'liqlik bor?","Og'irlik kuchining bajargan ishi nimaga teng?","Qiya tekislikda og'irlik kuchining bajargan ishi nimaga teng?","Og'irlik kuchining bajargan ishi trayektoriyaning shakliga qanday bog'liq?","Konservativ kuch nima?","Potensial maydon nima?","Nokonservativ kuch nima?","Og'irlik kuchi, ishqalanish kuchi, elastiklik kuchi, elektrostatik va havoning qarshilik kuchlaridan qaysilari konservativ?","Konservativ kuchlarning yopiq trayektoriya bo'ylab bajargan ishi nimaga teng?","Nokonservativ kuchlarning yopiq trayektoriya bo'ylab bajargan ishi nimaga teng?","Elastiklik kuchining bajargan ishi nimaga teng?","Ishqalanish kuchining bajargan ishi nimaga teng?","Kuchning siljishga bog'liqlik grafigidan hosil bo'lgan yuza son jihatidan nimaga teng?"]

energiya_saqlanish_qonuni = ["To'la mexanik energiya nima?","Mexanik energiyaning saqlanish qonuni nima?","Og'irlik kuchi ta'siri ostida harakatlanayotgan jism uchun to'la mexanik energiyani topish formulasi qanday?","Elastiklik kuchi ta'siri ostida harakatlanayotgan jism uchun to'la mexanik energiyani topish formulasi qanday?","Absolyut elastik to'qnashuv nima? Unda kinetik energiya o'zgaradimi?","Noelastik to'qnashuvda kinetik energiya o'zgaradimi?","Havo qarshiligini hisobga olganda, vertikal yuqoriga tepilgan koptokni to'la mexanik energiyasi qanday o'zgaradi?","Turli shakldagi harakatlar va o'zaro ta'sirlarning universal o'lchoviga nima deyiladi?","Jism va jismlar sistemasining energiyasi deb nimaga aytiladi?","Havoning qarshiligini hisobga olganda, gorizontga burchak ostida otilgan jismning to'la mexanik energiyasi trayektoriyaning qaysi nuqtasida maximal/minimal bo'ladi?"]

quvvat_fik = ["Quvvat ta'rifi, formulasi va birligi qanday? XBS orqali ifodalang.","Bir Watt ta'rifi qanday?","Bir ot kuchi nima?","T/ch li tekis harakatda quvvat qanday aniqlanadi?","1 kv*soat nimaga teng?","FIK nima?","Qiya tekislikning FIKsi qanday topiladi?"]

dinamika = zichlik_massa_nyuton_qonunlari + aylanma_kuch_b_o_tortishish + ogirlik_kuchi + kosmik_tezliklar + elastiklik_kuchi + prujinalar + ishqalanish_kuchi + gorizontal_vertikal_qiya_tekisliklar + kochmas_blok + impuls + mexanik_ish + energiya + energiya_mexanik_ish_bogliqlik + energiya_saqlanish_qonuni + quvvat_fik


# ---| [3] STATIKA \---


kuch_momenti = ["Muvozanat nima?","Jism muvozanat holatini saqlashi uchun qanday shartlar bajarilishi kerak?","Jism ilgarilanma harakat qilishi uchun qanday shartlar bajarilishi kerak?","Teng ta'sir etuvchi kuch nima?","Qarama-qarshi/Bir xil/O'zaro tik/O'zaro burchak ostida yo'nalgan kuchlarning teng ta'sir etuvchisi qanday topiladi?","Kuch momenti nima? U qanday kattalik? Birligini XBS dagi birliklar orqali ifodalang","Kuch yelkasi nima?","Momentlar qoidasi qanday?","Aylanish o'qiga ega bo'lgan jism muvozanatda bo'lishi uchun qanday shart bajarilishi kerak?","Richag nima?","Richagning muvozanat sharti qanday?","Mexanikaning oltin qoidasi qanday?","Turg'un/Farqsiz/Noturg'un muvozanat nima?","Massa markazi nima?","Massasi M va uzunligi l bo'lgan richagning yelkalariga F1 va F2 kuchlar qo'yilganda muvozanat sharti qanday?","Agar M massali richagning faqat 1 tomoniga F kuch qo'yilgan bo'lsa muvozanat sharti qanday?","Agar M massali richagning yelkalariga/faqat bir tomoniga yuk osilgan bo'lsa, muvozanat sharti qanday?","Yerda yotgan m massali xodaning bir uchidan bir uchidan bir oz ko'tarish uchun kerak bo'ladigan kuch qanday topiladi?","Ko'ndalang kesim yuzalari bir xil bo'lgan har xil jismlar tutashgan joyida tayanchga o'rnatilgan muvozanat sharti qanday?","Ikki tayanchga o'rnatilgan jismni tayanchga berayotgan bosim kuchlari yoki tayanchlarning reaksiya kuchlari qanday topiladi?","Bir jinsli sterjenning massa markazini delta_x ga surish uchun uning bir uchidan qanday uzunlikdagi qismini kesib tashlash kerak?","Qachon kuch jismni buradi?","To'rtburchak/Doira/Shar/Aylana/Uchburchak shaklidagi jismning massa markazi uning qayerida joylashgan?","Jismlar sistemasining massa markazi qanday topiladi?","Qavariq/Botiq sirtda turgan jism muvozanatda bo'lish sharti qanday?","Jism doimo turg'un muvozanatda bo'lishi uchun u qanday shaklda yoki holatda bo'lishi kerak?","Aylanma harakat dinamikasining formulasi qanday?","Mutlaq silliq gorizontal tekislik ustida jism tinch turibdi. Agar jismga boshlang'ich tezlik berilsa, u qanday muvozanatda bo'ladi?"]

statika = kuch_momenti


# ---| [4] SUYUQLIK VA GAZLAR MEXANIKASI \---

bosim = ["Bosim nima? birligi va formulasini yozing.","Bosim qanday kattalik?","Qattiq jismlarda bosim qanday yo'nalishda uzatiladi?"]

paskal_qonuni = ["Suyuqlik va gazlarda bosimning uzatilish mexanizmini qaysi qonun xarakterlaydi?","Paskal qonuni ta'rifi qanday?","Gidravlik press nima? formulasi qanday?","Gidravlik press ishlash prinsipi qaysi qonunga asoslangan?","Porshenlarning siljish masofasi nisbati ularning kuchlar/yuzalar nisbatiga qanday bog'liq?","Real gidravlik pressning ideal gidravlik pressdan farqi qanday?"]

gidrostatik_bosim = ["Gidrostatik bosim nima? U idish shakliga bog'liqmi? U qanday kattaliklarga bog'liq? Formulasini yozing.","Gidrostatik paradoks nima?","Idish qanday shaklda bo'lganda suyuqlikning idish tubiga ta'sir etadigan bosim kuchi shu idishdagi suyuqlikning og'irligiga teng/katta/kichik bo'ladi?","Manometr nima?","Tutash idish nima?","Tutash idishlar qonuni va formulasi - ?"]

atmosfera_bosimi = ["Atmosfera nima?","Atmosfera tarkibining qancha qismini kislorod tashkil qiladi?","Nima sababdan atmosfera bosimi yuzaga keladi?","Atmosfera bosimining mavjudligini kim aniqlagan?","Torichelli tajribasini tushuntirib bering.","Torichelli tajribasi qaysi qonunga asoslangan?","Normal atmosfera bosimi nima?","1 mm simob ustuni necha Pa?","1 atmosfera bosimi nima?","Dengiz sathidan har 12 metrda atmosfera bosimi qanchaga kamayadi?","760 mm sim ust nima?","Barometr nima?","Aneroid nima?","Altmetr nima?","Suyuqlik quyilgan idishning usti ochiq bo'lsa idish tubiga beradigan bosimi qanday topiladi?","1 kg/sm^2 necha Pa?","130 mm.sim.ust necha Pa?","Atmosfera bosimining balandlikka bog'liqlik grafigi qanday?"]

arximed_kuchi = ["Arximed kuchi nima? Arximed qonuni ta'rifi - ?","Jismning cho'kish sharti - ?","Jismning qalqib chiqish sharti qanday?","Jismning to'la botgan holda suzish sharti qanday?","Ko'taruvchi kuch nima? U qachon manfiy/musbat/0 bo'ladi?","Jismning suyuqlikka botgan qismini topish formulasi qanday?","Suyuqlikda Arximed va og'irlik kuchi ta'sirida harakatlanayotgan jismning tezlanishi qanday topiladi?","Kemalarning vater chizig'i nima?","Areometr chizig'i nima?","Kema daryodan dengizga chiqqanda uning suvga botishi qanday o'zgaradi?","Suv sirtida suzayotgan yog'och bo'lakchasi suvga botirilsa, yog'och - Yer tizimining potensial energiyasi qanday o'zgaradi?"]

bernulli = ["Suyuqlik oqimining uzluksizlik tenglamasi nima?","Suyuqlikning naydagi harakati qonunini kim kashf etgan?","Bernulli qonuni formulasi va ta'rifi - ?","Gorizontal bo'lmagan quvur uchun Bernulli tenglamasi qanday?","Nayning qaysi qismida bosim katta bo'ladi?","Torichelli tenglamasi - ?","Quvurdan oqib chiqqan suyuqlik hajmi va massasini topish formulalari qanday?","XBS dagi asosiy birliklar - ?","Samalyotning uchishi qaysi qonunga asoslangan?","Yerdan ko'tarilishda samalyotning shamol yo'nalishi bo'yicha uchishi afzalroqmi yoki unga qarshi?"]

suyuqlik_gazlar_mexanikasi = bosim + paskal_qonuni + gidrostatik_bosim + atmosfera_bosimi + arximed_kuchi + bernulli


# ---| [5] MOLEKULYAR FIZIKA \---


mkn_asoslari = ["MKN ning asosiy 3 qoidasi - ?","Massa atom birligi - ?","Modda miqdori nima?","Avogadro soni qanday son?","Molyar massa nima?","Bitta molekula massasi - ?","Molekulalar sonini topish formulalari - ?","Modda miqdorini topish formulalari - ?","Molekula o'lchami qanday topiladi?","Molekulalar konsentratsiyasi - ?","Gazlarni ideal deb hisoblash uchun nimalarni hisobga olmaslik kerak?"]

molekulalar_harakati = ["Gazlarda/Suyuqliklarda/Qattiq jismlarda molekulalar o'zaro ta'sir potensial va kinetik energiyasi qanday munosabatda bo'ladi?","Gaz molekulalari orasidagi masofa qanday topiladi?","Broun harakati. U temperaturaga qanday bog'liq?","Diffuziya hodisasi nima?","Gazlarda/Suyuqliklarda/Qattiq jismlarda diffuziya","Erkin yugurishning o'rtacha masofasi qancha?","Nima uchun temperatura ko'tarilishi bilan broun harakatining jadalligi ortadi?","Nima uchun ancha mayda zarralarda broun harakati juda tez, yirik zarralarda esa zo'rg'a seziladi?"]

mkn_asosiy_tenglamasi = ["Ideal gaz bosimi uchun MKN ning asosiy tenglamasini tushuntiring.","Dalton qonuni - ?","Parsial bosim nima?","Ideal gaz zichligini topish - ?",'Molyar hajm nima?',"Agar gazli idish ichidagi molekulalarning o'zaro tortishish kuchi birdan yo'qolsa, idishdagi bosim qanday o'zgargan bo'ladi?"]

temperatura = ["Temperatura nima?","Temperaturaning Selsiy va Kelvin shkalalari - ?","Termodinamik muvozanat nima?","Absolyut nol temperatura nima?","Temperatura va molekulalarning o'rtacha kinetik energiyasi o'zaro bog'liqligi qanday?","Gaz molekulalarining o'rtacha kvadratik tezligi - ?","Gaz molekulalari o'rtacha kvadratik tezlik temperaturaga bog'liq grafigi qanday?"]

klapeyron_izoxorabaraterma = ["Klapeyron tenglamasi nima?","Bolsman doimiysi nima?","Boyl-Marriot qonuni nima?","Izotermik jarayon va izoterma - ?","Izotermik jarayonda bosimning zichlikka bog'liqligi","Gey-Lyussak qonuni nima?","Izobarik jarayon va izobara - ?","Termik koeffitsiyent bosim uchun - ?","Sharl qonuni - ?","Izoxorik jarayon va izoterma - ?","Termik koeffitsient hajm uchun - ?","Mendeleyev-Klapeyron tenglamasi nima?","Universal gaz doimiysi + birlig - ?","Ideal gaz holat tenglamasi nima?","Gazning asosiy parametrlari - ?","Normal sharoitda bosim va temperatura nima?","Avogadro qonuni nima?","Ideal gaz holat tenglamasidan zichlik/modda miqdori qanday topiladi?","Bir xil bosim va temperaturada quruq havoning zichligi kattami yoki nam havonikimi?"]

molekulyar_fizika = mkn_asoslari + molekulalar_harakati + mkn_asosiy_tenglamasi + temperatura + klapeyron_izoxorabaraterma


# ---| [6] TERMODINAMIKA \---


ichki_energiya = ["Termodinamik sistema nima?","Termodinamik jarayon nima?","Molekulalarning erkinlik darajasi nima?","Bir/Ikki/Uch atomli gazlarning erkinlik darajasi", "Ichki energiya va birligi nima?","Ichki energiya o'zgarishi nima?"]

issiqlik_miqdori = ["Quyoshdan Yerga qanday yo'l bilan energiya uzatiladi?","Konveksiya nima? (Issiqlik miqdori mavzusida)","Issiqlik o'tkazuvchanlik nima?","Issiqlik uzatish yoki almashinish nima?","Issiqlik miqdorini tushuntiring.","Solishtirma issiqlik sig'imi va birligi nima?","Solishtirma issiqlik sig'imi va birligi qanday? XBS orqali ifodalang.","Kalorometrning vazifasi nima?"]

yoqilgining_yonish_issiqligi = ["Yoqilg'i vositasida ishlovchi dvigatelning FIK si qanday topiladi?","Yoqilg'ining yonishi natijasida ajralib chiqqan issiqlik miqdori qanday?","Yoqilg'ining solishtirma yonish issiqligi nima?","Yoqilg'ining solishtirma yonish issiqligi birligini XBS dagi birliklar orqali ifodalang."]

issiqlik_balansi_tenglamasi = ["Issiqlik balansi tenglamasi nima?","Suyuqlik aralashmasining temperaturasi nima?","Issiqlik balansi tenglamasi qaysi qonunga asoslangan?"]

termodinamika_Iqonuni_ish = ["Gaz hajmining o'zgarishida bajarilgan ish qanday?","Mendeleyev-Klapeyron tenglamasi yordamida bajarilgan ish qanday?","Universal gaz doimiysining ta'rifi qanday?","Yopiq sistema nima?","Termodinamikaning I qonuni nima?","Termodinamikaning I qonuni qaysi qonunga asoslangan?","Birinchi tur abadiy dvigatel nima?","Izotermik jarayon uchun termodinamikaning I qonuni qanday?","Izotermik jarayonda solishtirma issiqlik sig'imi nimaga teng?","Yengil harakatlanadigan porshendagi ish va ichki energiya nima?","Izobarik jarayon uchun Termodinamika I qonuni","Izobarik jarayonda sistemaga berilgan issiqlik miqdorining qancha qismi ichki energiyaning o'zgarishiga sarf bo'ladi?","Izobarik jarayon uchun solishtirma issiqlik sig'imi nimaga teng?","Izoxorik jarayon uchun termodinamikaning birinchi qonuni/solishtirma issiqlik sig'imi nimaga teng?","Adiabatik jarayon nima?","Adiabatik jarayon uchun termodinamikaning I qonuni qanday?","Puasson tenglamasi yoki adiabata tenglamasi nima?","O'zgarmas hajmdagi solishtirma issiqlik sig'imi nima uchun o'zgarmas bosimdagi solishtirma issiqlik sig'imidan kichik?","Gaz adiabatik siqilganda temperaturasi qanday o'zgaradi?","Agar ideal gaz tez siqilsa uning temperaturasi nima sababdan ortadi?","Adiabatik jarayon qaysi idishlarda amalga oshiriladi: kolbadami yoki kallorometrdami?","Gaz PV^2=const tenglamaga muvofiq siqilmoqda, uning temperaturasi qanday o'zgaradi?","Gaz V/T^2 = const tenglamaga muvofiq sovitilmoqda, uning bosimi qanday o'zgaradi?","Gazning bosimi root_P/T = const tenglamaga muvofiq pasaymoqda. Bunda uning hajmi qanday o'zgaradi?"]

issiqlik_dvigatellari = ["Qaytar va qaytmas jarayonlar nima?","Issiq jismdan sovuq jismga issiqlik uzatilishi bilan ro'y beradigan jarayon qanday jarayonga kiradi?","Issiqlik mashina yoki issiqlik dvigateli nima?","Issiqlik dvigatelining asosiy qismlari nima?","Real/Ideal issiqlik mashinasining FIKsi qanday?","Karno sikli. Karno formulasi - ?","Real issiqlik mashinasining max FIKsi - ?","Issiqlik mashinasining ishlash prinsipi qanday?","Sovitkich mashinasining sovitish koeffitsiyenti qanday topiladi?"]

termodinamika = ichki_energiya + issiqlik_miqdori + yoqilgining_yonish_issiqligi + issiqlik_balansi_tenglamasi + termodinamika_Iqonuni_ish + issiqlik_dvigatellari


# ---| [7] QATTIQ VA SUYUQ JISMLAR MEXANIKASI \---


qaynash = ["Qaynash nima?","Qaynash temperaturasi va qaynash nuqtasi nima?","Qaynash sodir bo'lishiga sabab nima?","Qaynash bosim bilan qanday bog'langan?"]

buglanish = ["Bug' hosil bo'lishi va bug'lanish nima?","Kondensatsiya va sublimatsiya nima?","Solishtirma bug'lanish issiqligi nima?","Bug'lanish intensivligi (tezligi) nimaga bog'liq?","Uzun va tor bo'g'izli sferik kolbaga to'ldirib issiq suv qo'yilgan. Suv soviganda uning kolba tubiga bosimi qanday o'zgaradi?"]

toyingan_bug = ["To'yingan bug' nima?","To'yinmagan bug' nima?","Dinamik muvozanat nima?","To'yingan bug' Mendeleyev-Klapeyron tenglamasiga bo'ysunadimi?","Kritik temperatura nima?","Gazlarni qachon suyuqlikka aylantirish mumkin?","Silindrda porshen ostida o'z suyuqligi bilan muvozanatda turgan to'yingan bug'ni siqsak qanday hodisa ro'y beradi?","Moddaga tegishli bo'lgan kritik temperaturadan yuqori temperaturada u qanday agregat holatda bo'ladi?","O'zgarmas temperaturada to'yingan bug'ning bosimi hajmga qanday bog'liq?"]

havo_namligi = ["Namlik nima?","Absolyut namlik va uning birligi nima?","Nisbiy namlik va uning birligi nima?","Shudring nuqtasi nima?","Lambrext gigrometri va uning ishlash prinsipi","Inson o'zini yaxshi his qiladigan nisbiy namlik qanday?","Psixometr va uning ishlash prinsipi qanday?","Psixometrda quruq va nam termometrlar ko'rsatishlari farqi ortsa nisbiy namlik qanday o'zgaradi?","Temperatura ortishi bilan havoning absolyut va nisbiy namligi qanday o'zgaradi?"]

sirt_taranglik_xollash_kapillarlar = ["Sirt taranglik kuchi nima?","Sirt taranglik koeffitsiyentining ikki ta'rifi va birligi - ?","Tomchilar soni qanday topiladi?","Sovun pufagidagi qo'shimcha bosim qanday topiladi?","Sovun pufagi sirtining yuzi o'zgarishi natijasida bajarilgan ish qanday topiladi?","Xo'llash nima?","Xo'llamaslik nima?","Xo'llash burchagi nima?","Kapillar hodisalar - ?","Laplas formulasi nima?","Qo'shimcha bosim qachon manfiy bo'ladi?","Kapillarlarda suyuqlikning ko'tarilish balandligi qanday?","Kapillarlik hodisasining qo'llanilish sohasi qanday?","Ikki parallel plastinkada suyuqlikning ko'tarilish balandligi qanday?","Qattiq jismlarning qanday turlari mavjud?","Kristall/Amorf jismlarning xususiyati qanday?","Polikristall jismlar nima?","Kristallarning 2 turi","Qattiq holatdan suyuq holatga [Suyuqdan qattiqqa o'tsachi?] o'tishi jarayonida amorf jismning temperaturasi qanday o'zgaradi?"]

erish_qotish = ["Erish deb nimaga aytiladi?","Solishtirma erish issiqligi nima?","Modda eriganda hajmi o'zgaradimi?","Erish temperaturasining bosimga bog'liqligi qanday?","Modda qattiq/suyuq holatdan suyuq/qattiq holatga o'tmoqda, bunda uning ichki energiyasi va temperaturasi qanday o'zgaradi?","Suv temperaturasi 0 C dan 4 C gacha isitilsa, uning hajmi va zichligi qanday o'zgaradi?","Suv muzlashi davomida energiya yutiladimi yoki ajraladimi?"]

qattiq_jism_mexanikasi = ["Qattiq jism mexanikasida reaksiya kuchi nima?","Deformatsiya nima?","Absolyut deformatsiya nima?","Nisbiy deformatsiya nima?","Elastik deformatsiya nima?","Plastik deformatsiya nima?","Siljish deformatsiyasi nima?","Buralish deformatsiyasi nima?","Mexanik kuchlanish nima?","Yung moduli nima?","Oquvchanlik chegarasi nima?","Proporsionallik darajasi nima?","Elastik deformatsiya darajasi nima?","Namunaning uzilishi nima?","Mo'rt jismlar - ?","Elastiklik kuchi va uning yo'nalishi - ?","Guk qonuni va uning ta'rifi qanday?","Guk qonunidagi '-' ishora ma'nosi nima?","Bikirlik nima?","Yung moduli orqali bikirlikni topish formulasi qanday?","Elastiklik kuchining absolyut uzayishiga bog'liqlik grafigi qanday? Undan bikrlik qanday topiladi?","Yung moduli birligini XBS dagi asosiy birliklar orqali ifodalang.","Qattiq jismlarning chiziqli/hajmiy kengayish koeffitsiyenti nima?","Tirqishi bor metall halqa isitilmoqda, bunda tirqish kengligi qanday o'zgaradi?"]

qattiq_suyuq_jism_mexanikasi = qaynash + buglanish + toyingan_bug + havo_namligi + sirt_taranglik_xollash_kapillarlar + erish_qotish + qattiq_jism_mexanikasi


# ---| [8] TEBRANISHLAR \---

mexanik_tebranishlar = ["Tebranish nima?","Tebranish davri nima?","Tebranish chastotasi nima?","Davr va chastota bog'liqligi qanday?","SIklik chastota nima?","1 HZ ta'rifi - ?","Tebranish amplitudasi nima?","Siljish nima?","Garmonik tebranishlar nima?","Matematik mayatnik nima?","Prujinali mayatnik nima?","Bir davr ichidagi yo'l nima deyiladi?"]

matematik_mayatnik = ["Matematik mayatnik nima?","Matematik mayatnikda to'la tebranish nima?","Matematik mayatnik qanday kuch ta'sirida tebranadi?","Matematik tebranish davri, chastotasi va siklik chastotasi formulalari qanday?","Mat.mayatnikda siljish nima?","Mat.mayatnikda amplituda nima?","Mat.Mayatnik to'la energiyasi nimalarga bog'liq?","Vaznsizlik holatida mat.mayatnik davri, chastotasi, siklik chastotasi qanday bo'ladi?","Vaznsizlik nima?","Erkin tushish tezlanishi qanday topiladi?","Mat.mayatnikda l,m,A berilgan holatida tezlik amplituda qiymati, tezlanish amplituda qiymati, maksimal kinetik energiyalari qanday topiladi?","Matematik mayatnikda og'irlik kuchining tashkil etuvchilari nima?","Agar matematik mayatnikni Oydan Yerga ko'chirilsa uning tebranish davri qanday o'zgaradi?","Tubida teshigi bor chelak suvga to'ldirilgan va cho'zilmas arqonga bog'langan holda tebranmoqda. Chelakdagi suv tomib tamom bo'lguncha uning tebranish davri qanday o'zgaradi?"]

prujinali_mayatnik = ["Prujinali mayatnikda siljish nima?","Prujinali mayatnikda amplituda nima?","Prujinali mayatnik nima?","Prujinali mayatnikda to'la tebranish nima?","Prujinali mayatnik qaysi kuch yordamida tebranadi?","Prujinali mayatnik davri va chastotasi qanday kattaliklarga bog'liq?","Prujinali mayatnik to'la energiyasi qanday topiladi?","Guk qonuni ta'rifi - ?","Bikirlik nima?","Parallel va ketma-ket ulanganda prujina bikrliklari qanday topiladi?","Yung moduli nima?","Bikrlik Yung moduliga qanday bog'liq?","Prujinali mayatnikda potensial va kinetik energiya qanday topiladi?","Prujinali mayatnik qachon W_kinetik_max ga ega bo'ladi?","Potensial energiya qachon eng katta qiymatni qabul qiladi?","Vaznsizlik holatida qumli/prujinali/mayatnikli soatdan foydalanib bo'ladimi?"]

garmonik_tebranishlar = ["Garmonik tebranishlarda siljish nima?","Garmonik tebranishlarda amplituda nima?","Garmonik tebranishlar nima?","Garmonik tebranish tenglamasini yozing.","Boshlang'ich faza nima?","Tebranish fazasi nima?","Garmonik tebranishlarda tezlik qanday topiladi? Tezlikning amplituda qiymati nimaga teng?","Garmonik tebranishlarda tezlanish qanday topiladi? Tezlanishning maximum qiymati nimaga teng?","Tebranuvchi jismning xususiy xossasi nima?","Garmonik tebranishda nuqta tezligi qaysi qonun asosida o'zgaradi?","Matematik mayatnikda tezlanish o'zgarish qonunini (a=(-g/l)*x keltirib chiqaring.","Garmonik teblanishlarda Nyutonning ikkinchi qonuni - ?","a = (-k/m)*x = -(w_0)^2*x formulani tushuntiring va isbotlang.","Jismni tebranma harakatga keltiruvchi kuch moduli va yo'nalishi qanday o'zgaradi?","Tebranayotgan jismning kinetik energiyasi qachon eng katta qiymatga erishadi?","Garmonik tebranishlarda to'la mexanik energiya qanday topiladi?","Jism garmonik tebransa, uning tezlanishi/kinetik energiyasi qanday o'zgaradi?","Tebranayotgan jismning potensial/kinetik energiyasi qanday vaziyatda eng katta bo'ladi?"]

erkin_va_majburiy_tebranishlar = ["Erkin tebranishlar nima?","Erkin tebranishlar garmonik tebranishlar qonuniyatlariga bo'ysunadimi?","Majburiy tebranish nima?","Rezonans nima?","Rezonans chiziqlari nima?","Rezonans ishqalanishga qanday bog'liq?","Rezonans texnikada qanday qo'llaniladi? (4 tagacha misol)","Ichki va tashqi kuchlar nima?","Ideal tebranish sistemasi nima?","Jism qiya tekislikdan sirpanib tushayotganda tezlanish massaga qanday bog'liq?"]

tolqinlar = ["To'lqinlar nima?","Bo'ylama to'lqin nima? Misollar keltiring.","Ko'ndalang to'lqin nima? Misollar keltiring.","Bir davr ichidagi yo'l deb nimaga aytiladi?","To'lqin uzunligi uning davriga qanday bog'liq?","To'lqin tezligini topish formulasi qanday?","Bir-biridan har xil masofada tebranayotgan to'lqinlarning fazalar farqi qanday topiladi?","Qattiq jismlarda qanday mexanik to'lqinlar tarqaladi?","Ko'ndalang mexanik to'lqinlar qanday muhitlar ichida tarqala oladi?","Musiqa asboblari torlarida/suv sirtida hosil bo'lgan to'lqinlar bo'ylamami yoki ko'ndalang?"]

tovush_tolqinlari = ["Tovush to'lqinlariga misollar keltiring.","Akustika fizikaning qanday bo'limi?","Tovush to'lqinlari chastotasi qanday oraliqda joylashgan?","Tovush nimadan paydo bo'ladi?","Gazlardan qanday to'lqinlar tarqaladi?","Havodagi tovush to'lqinlari qanday to'lqin?","Tovush to'lqinlarining tezligi qanday moddalarda eng katta?","Tovush intensivligi yoki tovush kuchi nima?","Tovush bosimi nima?","Tovush bosimi o'rtacha hisobda necha Pa?","Tovush qattiqligi nimaga bog'liq?","Aks sado nima?","Tovush lokatsiyasi nima?","Tovush tembri nima?","Dopler effekti nima?","Radiolokatordan obyektgacha masofa qanday aniqlanadi?","Tovush bir muhitdan boshqasiga o'tganida qanday kattalik o'zgarmaydi?","Tovush balandligi nimaga bog'liq?","Vakuumda tovush yuzaga keladimi?","Tovushni yuzaga keltirib, uni sezishni qanday shartlari mavjud?","Gazlarda tovush tezligi temperaturaga qanday bog'liq?","G'ovak jismlarda tovush qanday tarqaladi?","Musiqiy ton nima?","Tovushning asosiy toni nima?","Oberton nima?","Shovqin nima?","Tovush energiyasi amplituda va chastotaga qanday bog'liq?","Tovush balandligi nima?","Tovush intensivligi birligi nima?","Inson qulog'i seza oladigan intensivlik qancha?","Intensivlik masofaga qanday bog'liq?","Ultratovush/Infratovush to'lqinlari diapazoni qanday?","Suyuqlik/Gazlardagi ultratovush to'lqinlari bo'ylamami yoki ko'ndalang?","Yerdan 100 000 km uzoqlikdagi sun'iy yo'ldosh portladi. Uning ovozi Yerga eshitiladimi?","Marsda portlash sodir bo'ldi. Uning ovozi Yerga eshitiladimi?"]

tebranishlar = mexanik_tebranishlar + matematik_mayatnik + prujinali_mayatnik + garmonik_tebranishlar + erkin_va_majburiy_tebranishlar + tolqinlar + tovush_tolqinlari


# ---| [9] ELEKTROSTATIKA \---


elektr_zaryadi = ["Elektrostatika nimani o'rganadi?","Junga ishqalangan qahrabo/shisha tayoqchasi qanday zaryadlanadi?","Shisha tayoqchani shoyiga ishqalaganda shoyi qanday zaryadlanadi?","Elektromagnit o'zaro ta'sir nima?","Bir xil ishorali zaryadlar bir-biriga qanday ta'sir qiladi?","Atom qanday zarralardan tashkil topgan?","Atom yadrosi tarkibi qanday?","Elektron/Proton/Neytron zaryadi/massasi nimaga teng?","Zaryadning karralilik qonuni nima?","Yopiq sistema nima?","Zaryadning saqlanish qonuni nima?","Ebonit/Shisha tayoqchasi musbat zaryadlanganda uning massasi qanday o'zgaradi?"]

kulon_qonuni = ["Kulon qonunini ta'riflang.","Kulon qonunidagi koeffitsiyent qiymati va birligi","Elektr doimiysi nimaga teng?","1 C ta'rifi - ?","Elektrostatik maydon nima?","Elektromagnit maydon nima?","Zaryad sirt zichligi - ?","Zaryad sirt zichligi/Elektr doimiysi/Kulon qonunidagi koeffitsiyent birligini XBS dagi asosiy birliklar orqali ifodalang."]

elektr_maydon = ["Elektr maydon kuchlanganligi nima?","Nuqtaviy zaryad elektr maydon kuchlanganligi nima?","Kuchlanganlik chiziqlari - ?","Musbat/Manfiy nuqtaviy zaryadning kuchlanganlik chiziqlari","Kuchlanganlik chiziqlari kesishadimi?","Maydon kuchlanganligi birligi - ?","Maydon superpozitsiya prinsipi qanday?","Maydon kuchlanganliklari qanday qo'shiladi?","Ikkita bir xil ishorali nuqtaviy zaryadlar orasidagi maydon kuchlanganligi nolga teng bo'lgan nuqta - ?","Elektr maydon kuchlanganligi birligini XBS dagi asosiy birliklar orqali ifodalang.","Zaryadlangan parallel platinka orasidagi kuch chiziqlari qanday?","Cheksiz tekislik va tekisliklar orasidagi elektr maydon kuchlanganligi","Bir jinsli maydon nima?","Vertikal yo'nalishdagi elektr maydonida zaryadning harakat tenglamasi nima?","Zaryadlangan shar sirtidagi/ichidagi elektr maydon kuchlanganligi qanday?","Zaryadlangan shardan H masofa uzoqlikdagi maydon kuchlanganligi qanday?","Musbat zaryad maydoniga musbat zaryad kiritsak, maydon qanday o'zgaradi?"]

elektr_maydonda_otkazgichlar_dielektriklar = ["Bir jinsli elektr maydonga kiritilgan otkazgichning ichida elektr maydon kuchlanganligi qanday topiladi?","Elektr zaryadlari otkazgich bo'ylab qanday taqsimlanadi?","Elektrostatik induksiya hodisasi nima?","Oval/Kub/Shar,Silindr shaklidagi bir butun metall jismga zaryad berilganda zaryad qayerda va qanday taqsimlanadi?","Dielektriklar nima?","Dielektrik singdiruvchanlik nima?","Qutblanish nima?","Qutbli va qutbsiz dielektrik nima?","Elektr dipoli nima?","Dipol momenti nima?","Debay - qanday kattalik belgisi?","Politilien/Osh tuzi/Distillangan suv qanday dielektrik turiga kiradi?"]

potensial = ["Elektr maydonida nuqtaviy zaryadni ko'chirishda bajarilgan ish nima?","Elektrostatik maydonda zaryadni yopiq kontur bo'ylab ko'chirishda bajarilgan ish qanday topiladi?","Konservativ kuch nima?","Ikki nuqtaviy zaryad potensial energiyasi - ?","Potensial energiya va ish orasidagi bog'liqlik qanday?","Potensial va potensiallar ayirmasi nima? Birligi qanday?","Potensial qanday kattalik?","Qaysi kattalik elektr maydonni energiya tomonidan xarakterlaydi?","Nuqtaviy zaryad potensiali","Ikkita har xil ishorali nuqtaviy zaryadlar orasidagi maydon potensiali nolga teng bo'lgan nuqta - ?","Potensiallar qanday qo'shiladi?","Maydon superpozitsiya prinsipi natijasi - ?","Potensiallar ayirmasi birligini XBS dagi asosiy birliklar orqali ifodalang.","Zaryadlangan shar ichidagi/sirtidagi/tashqarisidagi potensial qanday?","Qaysi shart berilganda sharlardan zaryad bir-birga o'tadi?","Zaryadlangan sharlar tutashtirilganda biridan ikkinchisiga o'tgan zaryad miqdori qanday topiladi?","Bir xil potensialga ega bo'lgan bir nechta shar qo'shilishidan hosil bo'lgan potensial qanday topiladi?","Bir xil potensialga ega bo'lgan bir nechta shar qo'shilishidan hosil bo'lgan katta sharni potensiali qanday topiladi?"]

potensiallar_ayirmasi = ["Potensiallar ayirmasi va maydon kuchlanganligi orasidagi bog'liqlik qanday?","Ekvipotensial sirt nima?","Ekvipotensial sirt bo'ylab zaryadni ko'chirishda bajarilgan ish qanday topiladi?","Kuchlanganlik chiziqlari ekvipotensial sirt bilan qanday burchak tashkil qiladi?","Nuqtaviy zaryadning ekvipotensial sirti - ?","Zaryadlangan tekislikning ekvipotensial sirti"]

otkazgichning_elektr_sigimi = ["Elektr sig'imi va uning birligi - ?","Yakkalangan o'tkazgich - ?","Shar elektr sig'imi - ?","Elektr sig'imi birligini XBS dagi asosiy birliklar orqali ifodalang."]

kondensator_elektr_sigimi = ["Kondensator nima?","Yassi/Silindrik/Sferik kondensator elektr sigimi qanday?","Yassi kondensator qoplamalari orasidagi potensiallar farqi/elektr maydon kuchlanganligi qanday?","Yassi kondensatorning plastinkalariga doimiy kuchlanish berilganda shu plastinkalar orasidan uchib o'tayotgan elektron qanday trayektoriya chizadi?"]

kondensator_ketma_ket_parallel = ["Kondensator parallel/ketma-ket ulash sxemasi qanday?","Kondensatorlar parallel/ketma-ket ulanganda umumiy sig'im/kuchlanish/zaryad qanday?","Ikki zaryadlangan kondensator bir-biri bilan tutashtirilganda umumiy kuchlanish qanday topiladi?","Kondensatorlarning teskari qutblari bilan ulaganda natijaviy zaryad qanday o'zgaradi?","Sig'imlari va kuchlanishlari berilgan kondensatorlar, teskari qutblari bilan ulansa natijaviy kuchlanish qanday topiladi?"]

kondensator_elektr_maydon_energiyasi = ["Kondensatorning asosiy xossalari nima?","Kondensator elektr maydon energiyasi nima?","Kondensator elektr maydon energiya zichligi nima?","Kondensatorning elektr maydoni uning qayerida joylashadi?","Sig'imlari va kuchlanishlari berilgan kondensatorlar teskari/tog'ri qutblari bilan ulansa, umumiy energiyasining o'zgarishi qanday topiladi?","Sig'imlari va zaryadlari berilgan kondensatorlar teskari qutblari bilan ulansa, umumiy energiyasining o'zgarishi qanday topiladi?"]

elektrostatika = elektr_zaryadi + kulon_qonuni + elektr_maydon + elektr_maydonda_otkazgichlar_dielektriklar + potensial + potensiallar_ayirmasi + otkazgichning_elektr_sigimi + kondensator_elektr_sigimi + kondensator_ketma_ket_parallel + kondensator_elektr_maydon_energiyasi


# ---| [10] O'ZGARMAS ELEKTR TOKI \---


tok_kuchi = ["Elektrodinamika nima?","O'zgarmas tok nima?","Tok kuchi nima?","Tok zichligi nima?","Elektr toki ta'sirlari qanday?","Elektr tokini mavjud bo'lish shartlari","Tok kuchi qanday kattalik?","Tok zichligi qanday kattalik?","Zaryad konsentratsiyasi berilgan holda tok zichligini topish formulasi qanday?","Metall o'tkazgich ko'ndalang kesim yuzidan o'tgan elektronlar sonini topish formulasi qanday?","Metallarda zaryadning tartibli harakat tezligini topish formulasi qanday?"]

zbq_om_qonuni = ["Tok kuchining kuchlanishga bog'liqlik grafigidan qarshilik qanday topiladi?","Zanjirning bir qismi uchun Om qonuni qanday?","Elektr qarshilik birligini XBS dagi asosiy birliklar orqali ifodalang."]

qarshilik = ["Bir Om ta'rifi - ?","O'ta-o'tkazuvchanlik hodisasi nima?","Qarshilik termometrlari nima?","Elektr qarshilik nima sababdan vujudga keladi?","Elektr qarshilik qaysi kattalikka bog'liq?","Solishtirma qarshilik nima?","Reostat nima?","Rezistor nima?","Solishtirma qarshilik birligini XBS dagi asosiy birliklar orqali ifodalang."]

ketma_ket_va_parallel_ulash = ["O'tkazgichlarni ketma-ket ulash sxemasi qanday?","Otkazgichlar ketma-ket ulansa, umumiy tok kuchi/kuchlanish/qarshilik/zaryad nimaga teng?","O'tkazgichlarni parallel ulash sxemasi qanday?","O'tkazgichlarni parallel ulaganda umumiy tok kuchi/qarshilik/kuchlanish/zaryad nimaga teng?","Simni cho'zib uzaytirsak qarshiligi qanday o'zgaradi?"]

shunt_ulash = ["Ampermetr zanjirga qanday ulanadi?","Voltmetr nima va u zanjirga qanday ulanadi?","Ommetr nima va u zanjirga qanday ulanadi?","Vattmetr nima va u zanjirga qanday ulanadi?","Ampermetrga shunt nima maqsadda ulanadi?","Voltmetrga shunt nima maqsadda ulanadi?","Shunt nima?"]

zbq_joul_lens = ["Joul-Lens qonunini tushuntiring!","O'zgarmas tokning ishi (zanjirning 1 qismi uchun) qanday topiladi?","O'zgarmas tokning quvvati (zanjirning bir qismi uchun) qanday topiladi?"]

ketma_ket_va_parallel_ish_quvvat = ["O'tkazgichlar ketma-ket/parallel ulanganda qaysi birida ko'p issiqlik ajraladi?","Spirallar ketma-ket/parallel ulanganda suvni qaynash vaqtini topish formulasi qanday?","n ta bir xil cho'lg'am ketma-ket ulanganda suvning qaynash vaqti, ular parallel ulangandagidan qancha farq qiladi?","Ketma-ket/Parallel ulangan iste'molchilarning umumiy quvvat qanday topiladi?","Quvvatlari P1 va P2 bo'lgan lampalar manbaga parallel/ketma-ket ulanganda ularning alohida quvvatlari qanday topiladi?"]

toliq_om_qonuni = ["EYuK nima?","Berk zanjir uchun Om qonuni qanday?","Qisqa tutashuv nima?"]

tok_manbalarini_kk_pll_ulash = ["Manbalarni ketma-ket/parallel ulash sxemasi qanday?","Elementlar ketma-ket/parallel ulanganda berk zanjir uchun Om qonuni qanday?","Akkumulyatorni zaryadlashdagi/razryadlashdagi kuchlanish","Tok manbalarining FIK qanday topiladi?","Kirxgofning I qonuni - ?","Kirxgofning II qonuni","Tarmoqlanish tugunida uchrashuvchi toklarning algebraik yig'indisi qanday topiladi?"]

toliq_joul_lens = ["O'zgarmas tokning quvvati (butun zanjir uchun) qanday topiladi?","Tok manbaining foydali/samarasiz quvvati qanday topiladi?","Tok manbaini FIK sini topish formulasini isbotlang.","Tok manbaining FIK qarshiliklar/kuchlanish orqali qanday topiladi?"]

ozgarmas_elektr_toki = tok_kuchi + zbq_om_qonuni + qarshilik + ketma_ket_va_parallel_ulash + shunt_ulash + zbq_joul_lens + ketma_ket_va_parallel_ish_quvvat + toliq_om_qonuni + tok_manbalarini_kk_pll_ulash + toliq_joul_lens


# ---| [11] TURLI MUHITLARDA ELEKTR TOKI \---


metallar = ["Metallarda asosiy tok tashuvchilar nima?","Metallarda qarshilikning temperaturaga bog'liqligi?","O'ta-o'tkazuvchanlik?","Volt-Amper xarakteristikasi nima?","Qarshilikning termik koeffitsiyenti nima?","Metallarda elektr tokining tarqalish tezligi nima bilan aniqlanadi?","Metallarda Volt-Amper xarakteristikasi qanday?"]

elektrolitlar = ["Elektroliz nima?","Rekombinatsiya nima?","Elektrolitlar nima?","Dissotsiatsiya nima?","Dissotsiyatsiyalanish darajasi nima?","Dissotsiatsiyalanish darajasining eng katta qiymati nima?","Elektrolitlarda dissotsiatsiya darajasi temperaturaga qanday bog'liq?","Faradeyning 1-qonuni","Elektrokimyoviy ekvivalent nima?","Faradey 2-qonuni","Faradey doimiysi","Faradeyning birlashgan qonuni","Elektrolitlarda ionlar qanday vujudga keladi?","Qanday o'tkazgichlar ionli o'tkazuvchanlikka ega?","Elektrolitlarda elektr toki qanday hosil qilinadi?","Temperatura ortishi bilan elektrolitning o'tkazuvchanligi qanday o'zgaradi","Elektroliz hodisasining texnikada qo'llanilishi qanday?","Elektrolitlarda kuchlanish o'zgarmasdan vanna elektrodlari orasidagi masofa o'zgarsa, tok kuchi qanday o'zgaradi?","Elektrolit orqali tok o'tganda ko'chish mumkin bo'lgan eng kichik zaryad qiymati nimaga teng?","Anion nima?","Kation nima?","Ion nima?","Qanday moddalarda qarshilikning termik koeffitsiyenti musbat bo'ladi?","Qanday moddalarda qarshilikning termik koeffitsiyenti manfiy bo'ladi?","Elektrolitdan o'tayotgan umumiy tok qabday topiladi?","Kimyoviy ekvivalent nima?","Elektrokimyoviy ekvivalent birligini XBS dagi asosiy birliklar orqali ifodalang.","Sulfat kislotasi eritilgan suvda elektr tokining qanday ta'siri mavjud?","Elektrolitlarning Volt-Amper xarakteristikasi qanday?","Elektrolitlar uchun Om qonuni o'rinlimi?"]

gazlar = ["Gaz razryadi nima?", "Gazlarda asosiy elektr tashuvchilari nima?","Mustaqil razryad nima?","Nomustaqil razryad nima?","Toj razryadi nima?","Uchqunli razryad nima?","Yoy razryadi nima?","Yolqin razryad nima?","Plazma nima?","Qanday o'tkazgichlar ionli va elektronli o'tkazuvchanlikka ega?","Elektr yoyi yongan daqiqada elektrodlar orasidagi kuchlanish qanday o'zgaradi?","Gazlarda qarshilikning temperaturaga bog'liqligi qanday?","Gazlarning Volt-Amper xarakteristikasi qanday?","Gazlarda elektr tokining o'tishi Om qonuniga bo'ysunadimi?","Gaz razryadida anod kuchlanishi kamaytirilsa uning o'tkazuvchanligi qanday o'zgaradi?","Chaqmoq qaysi razryad turiga kiradi?"]

vakuum = ["Termoelektron emissiya nima?","Diod nima?","To'yinish toki nima?","Vakuumda asosiy tok tashuvchilari nima?","Triod nima?","Elektron nur trubka nima?","Chiqish ishini topish formulasida (A = e*delta_fi) delta_fi nima?","Qanday shart bajarilganda elektron metallni tark etadi?","Vakuumli diod uchun Om qonuni bajariladimi?","Vakuumda tok kuchi temperaturaga qanday bog'liq?","Triodda to'r qayerga qo'yiladi","Qanday shart bajarilganda triod diod vazifasini bajaradi?","Trioddan o'tadigan tok to'r potensialiga qanday bog'liq?","Triodda yopish kuchlanish deb nimaga aytiladi?","Qanday muhitlarda elektr tokining issiqlik ta'siri kuzatilmaydi","Katod nurlari nima?","Anod potensiali ta'sirida elektron olgan tezlanish qanday topiladi?","Diodning Volt-Amper xarakteristikasi qanday?","Volframli, molibdenli va oksidli uch katod bir xil temperaturagacha qizdirilgan. Qaysi katod eng ko'p elektron chiqaradi?"]

yarimotkazgich = ["Yarimotkazgichlarda asosiy tok tashuvchilari nima?","Yarimotkazgichlar nima?","Donor aralashmali yarimotkazgichlar nima?","Akseptor aralashmali yarimotkazgichlar nima?","Tranzistor vazifasi nima?","Tranzistorning asosiy qismlari nima?","Yarimotkazgichlarda qarshilikning temperaturaga bogliqligi","Temperatura ortishi bilan yarimotkazgichning solishtirma qarshiligi qanday ozgaradi?","O'ta o'tkazuvchanlik hodisasini 1-kim aniqlagan?","Davriy jadvalning 3-guruh elementlari qanday otkazuvchanlik beradi?","Fotorezistor nima?","Fotoelement nima?","Termistorlar nima?","Kovaklar qanday zaryadga ega?","Yarimotkazgichlar kristallmi yoki amorfmi?","Bolometr yordamida qaysi kattalik o'lchanadi?","Yarimotkazgichlarda elektron va kovak uchrashganda energiya ajraladimi?","Teng miqdorda teshikli va elektronli yarimotkazgichlar mavjudmi?","Qo'shilmasiz, yaxshi tozalangan yarimotkazgichlardagi elektr toki qaysi zarralar hisobiga hosil boladi?","Ota toza kremniyga akseptor qoshilma kiritilsa, yarimotkazgichning otkazuvchanligi qanday ozgaradi?"]

turli_muhitlarda_elektr_toki = metallar + elektrolitlar + vakuum + yarimotkazgich


# ---| [12] ELEKTROMAGNIT HODISALAR \---


magnit_maydon = ["Doimiy magnit nima?","Magnit qutblari nima?","Yerning magnit maydoni qanday yo'nalgan?","Kompas nima?","Har xil magnit qutblari bir-biriga qanday ta'sir ko'rsatadi?","Qanday magnit qutblari bir-biridan qochadi?","Elektr toki atrofida qanday maydon mavjud?","Magnit maydonni aniqlagan odam kim?","Qachon parallel toklar bir-biridan qochadi va qachon bir-biriga tortiladi?","Amper tajribasi qanday edi?","Sinov konturi nima?","Parma qoidasi nima?","Magnit momenti nima?","Magnit maydon induksiyasi nima?","Tokli ramkaga ta'sir etuvchi kuch momenti qanday topiladi?","M = BISsin@ da @ qanday burchak?","Induksiya chiziqlari nima?","Induksiya chiziqlari yopiqmi yoki ochiqmi?","Magnit maydon kuchlanganligi nima?","Magnit maydon kuchlanganligi birligi va formulasi qanday?","Magnit maydon kuchlanganligi va induksiya orasida qanday bog'liqlik mavjud?","Tabiatda magnit zaryadlari mavjudmi?","Konturning magnit momenti nimani ko'rsatadi?","Konturning magnit momentining yo'nalishi qanday aniqlanadi?","Harakatsiz zaryad atrofida magnit maydon hosil bo'ladimi?","Magnit induksiya chiziqlari magnit ichida qanday yo'nalishga ega?","Magnit induksiya chiziqlari magnit tashqarisida qanday yo'nalishga ega?","Quyosh shamoli nima?","Qutb yog'dusi qanday vujudga keladi?","Magnitosfera deb nimaga aytiladi?","Parallel toklarning o'zaro ta'siri kuchi formulasi nima?","Parallel toklarning o'zaro ta'sir kuchi nimalarga bog'liq?","Magnit doimiysi nima?","Nisbiy magnit singdiruvchanlik nima?","1 Amper ni ta'riflang.","Ersted tajribada nimani aniqlagan?","Magnit doimiysi birligini XBS dagi asosiy birliklar orqali ifodalang.","Magnit maydon induksiya birligini XBS dagi asosiy birliklar orqali ifodalang.","Magnit maydon kuchlanganligi birligini XBS dagi asosiy birliklar orqali ifodalang","Magnit maydonning elektr maydoni bilan bog'liqligini tajribada birinchi bo'lib kim aniqlagan?","Gorizontal o'q atrofida erkin aylana oladigan magnit strelka deyarli tik turib qoldi, bunda uning shimoliy uchi tepada joylashdi. Strelka Yerning qaysi joyida joylashgan?","Kompasning magnit strelkasining o'qi magnit meridianiga tik ravishda gorizontal o'rnatildi. Bunda strelka aniq gorizontal vaziyatni oldi. Kompas qayerda joylashgan?"]

magnit_maydonda_tokli_otkazgichga_tasir_qiluvchi_kuch = ["Amper kuchi nima?","Amper kuchi formulasi qanday?","Amper qonuni ta'rifi","Amper kuchi yo'nalishi qanday?","Chap qo'l qoidasi","Agar o'tkazgich magnit induksiya chiziqlari bo'ylab joylashgan bo'lsa, ta'sir kuchi nimaga teng bo'ladi?"]

bio_salvar_laplas_qonuni = ["Bio Salvar-Laplas qonuni nima?","Bio Salvar-Laplas qonunida induksiya yo'nalishi qanday aniqlanadi?","Ikkita bir xil kuchli (I1=I2), o'zaro || va sirtdan tik chiquvchi (bizga yo'nalgan) t/chli toklarning o'rtasidagi nuqtada hosil bo'lgan magnit maydon induksiyasi qanday yo'nalgan?","Ikkita bir xil kuchli (I1=I2), o'zaro || va sirtga tik kiruvchi (bizdan yo'nalgan) t/chli toklarning o'rtasidagi nuqtada hosil bo'lgan magnit maydon induksiyasi qanday yo'nalgan?","Ikkita bir xil kuchli (I1=I2), o'zaro ||, bizdan chap tomondagisi sirtga tik kiruvchi (bizga yo'nalgan) va bizdan o'ng tomondagisi sirtdan tik chiquvchi t/chli toklarning o'rtasidagi nuqtada hosil bo'lgan magnit maydon induksiyasi qanday yo'nalgan?","Ikkita bir xil kuchli (I1=I2), o'zaro ||, bizdan chap tomondagisi sirtdan tik chiquvchi (bizga yo'nalgan) va bizdan o'ng tomondagisi sirtga tik kiruvchi t/chli toklarning o'rtasidagi nuqtada hosil bo'lgan magnit maydon induksiyasi qanday yo'nalgan?","Cheksiz to'g'ri tokning magnit maydon induksiyasi qanday?","Aylanma tokning magnit maydon induksiyasi","Tokli selenoid o'zagidagi magnit maydon induksiyasi nima?","Tokli toroid magnit maydon induksiyasi","Magnit maydon uchun superpozitsiya prinsipi","Ikkita tokli to'g'ri va juda uzun o'tkazgichlar o'zaro tik joylashgan. Ular qanday ta'sirlashadi?"]

lorens_kuchi = ["Lorens kuchi nima?","Lorens qonuni nima?","Lorens kuchi yo'nalishi qanday aniqlanadi?","Lorens kuchi bajargan ishs qanday topiladi?","Lrens kuchi tasirida zarra qanday harakat qiladi?","Lorens kuchi ta'sirida harakatlanayotgan zaryadli zarra trayektoriya radiusi, aylanish davri, harakat tezligi formulasi qanday?","Zaryadlangan zarra magnit maydonga o'tkir/to'g'ri burchak ostida [maydon yo'nalishidachi?] kirsa qanday trayektoriya bo'ylab harakatlanadi?","Elektr tokini hosil qilgan va faqat harakatlanuvchi zaryadlarga ta'sir etuvchi maydon qanday nomlanadi?"]

magnit_oqimi = ["Magnit oqimi ta'rifi va birligi?","Yopiq sirt orqali magnit oqimi nimaga teng?","Magnit oqimi vektor kattalikmi?","Bir jinsli magnit maydonda joylashgan ramkaning normali bilan induksiya chiziqlari orasidagi burchak ortsa, magnit oqimi qanday o'zgaradi?"]

muhit_magnit_singdiruvchanligi = ["Nisbiy magnit singdiruvchanlik nima?","Diamagnetiklar nima?","Paramagnetiklar nima?","Ferromagnetiklar","Diamagnetiklar xususiyati temperaturaga qanday bog'liq?","Paramagnetiklar xususiyati temperaturaga qanday bog'liq?", "Magnit lentalari va disklarga axborot yozish nimaga asoslangan?","Magnit lentalari va disklari qanday tuzilgan?","Oltin va kumush magnit maydonni zaiflashtiradimi yoki kuchaytiradimi?","Kobalt va nikel magnit maydonni zaiflashtiradimi yoki kuchaytiradimi?","Aluminiy va qalay magnit maydonni zaiflashtiradimi yoki kuchaytiradimi?","Kyuri temperaturasi nima?","Ferromagnit moddalar Kyuri temperaturasidan past temperaturada qanday moddaga aylanadi?","Ferromagnit moddalar Kyuri temperaturasidan yuqori temperaturada qanday moddaga aylanadi?","Temir uchun Kyuri nuqtasi nimaga teng?"]

elektromagnit_induksiya = []

lens_qoidasi_ozinduksiya = []

induktivlik = []

magnit_maydon_energiyasi = []

elektromagnit_hodisalar = magnit_maydon + magnit_maydonda_tokli_otkazgichga_tasir_qiluvchi_kuch + bio_salvar_laplas_qonuni + lorens_kuchi + magnit_oqimi + muhit_magnit_singdiruvchanligi + elektromagnit_induksiya + lens_qoidasi_ozinduksiya + induktivlik + magnit_maydon_energiyasi


# ---| [13] ELEKTROMAGNIT TEBRANISHLAR \---


#


# ---| [14] GEOMETRIK OPTIKA \---


#


# ---| [15] TO'LQIN OPTIKASI \---


#


# ---| [16] NISBIYLIK NAZARIYASI \---


#


# ---| [17] YORUG'LIK KVANTI \---


#


# ---| [18] ATOM VA YADRO FIZIKASI \---


#




#***********************************************
#***********************************************
#***********************************************

savollar = turli_muhitlarda_elektr_toki + elektromagnit_hodisalar + elektrostatika + ozgarmas_elektr_toki + tebranishlar + qattiq_jism_mexanikasi + termodinamika + molekulyar_fizika + suyuqlik_gazlar_mexanikasi + statika + dinamika + kinematika
true_count = 0
false_count = 0
test = 3

for i in range(test):
    x = random.randint(0,len(savollar)-1)
    print("")
    print(savollar[x])
    print("")
    javob = input("Topsangiz 1, aks holda 0 ni bosing: ")
    if javob == "1":
        true_count+=1
        continue
    if javob == "0":
        false_count+=1
        continue

print("Jami savollar soni:",len(savollar))
print("Test savollari soni:",test)
print("To'g'ri javoblar:",true_count)
print("Noto'g'ri javoblar:",false_count)