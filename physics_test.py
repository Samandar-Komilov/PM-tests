import random

#.....


# ---| [9] Turli muhitlarda elektr toki \---

metallar = ["Metallarda asosiy tok tashuvchilar nima?","Metallarda qarshilikning temperaturaga bog'liqligi?","O'ta-o'tkazuvchanlik?","Volt-Amper xarakteristikasi nima?","Qarshilikning termik koeffitsiyenti nima?","Metallarda elektr tokining tarqalish tezligi nima bilan aniqlanadi?","Metallarda Volt-Amper xarakteristikasi qanday?"]

elektrolitlar = ["Elektroliz nima?","Rekombinatsiya nima?","Elektrolitlar nima?","Dissotsiatsiya nima?","Dissotsiyatsiyalanish darajasi nima?","Dissotsiatsiyalanish darajasining eng katta qiymati nima?","Elektrolitlarda dissotsiatsiya darajasi temperaturaga qanday bog'liq?","Faradeyning 1-qonuni","Elektrokimyoviy ekvivalent nima?","Faradey 2-qonuni","Faradey doimiysi","Faradeyning birlashgan qonuni","Elektrolitlarda ionlar qanday vujudga keladi?","Qanday o'tkazgichlar ionli o'tkazuvchanlikka ega?","Elektrolitlarda elektr toki qanday hosil qilinadi?","Temperatura ortishi bilan elektrolitning o'tkazuvchanligi qanday o'zgaradi","Elektroliz hodisasining texnikada qo'llanilishi qanday?","Elektrolitlarda kuchlanish o'zgarmasdan vanna elektrodlari orasidagi masofa o'zgarsa, tok kuchi qanday o'zgaradi?","Elektrolit orqali tok o'tganda ko'chish mumkin bo'lgan eng kichik zaryad qiymati nimaga teng?","Anion nima?","Kation nima?","Ion nima?","Qanday moddalarda qarshilikning termik koeffitsiyenti musbat bo'ladi?","Qanday moddalarda qarshilikning termik koeffitsiyenti manfiy bo'ladi?","Elektrolitdan o'tayotgan umumiy tok qabday topiladi?","Kimyoviy ekvivalent nima?","Elektrokimyoviy ekvivalent birligini XBS dagi asosiy birliklar orqali ifodalang.","Sulfat kislotasi eritilgan suvda elektr tokining qanday ta'siri mavjud?","Elektrolitlarning Volt-Amper xarakteristikasi qanday?","Elektrolitlar uchun Om qonuni o'rinlimi?"]

gazlar = ["Gaz razryadi nima?", "Gazlarda asosiy elektr tashuvchilari nima?","Mustaqil razryad nima?","Nomustaqil razryad nima?","Toj razryadi nima?","Uchqunli razryad nima?","Yoy razryadi nima?","Yolqin razryad nima?","Plazma nima?","Qanday o'tkazgichlar ionli va elektronli o'tkazuvchanlikka ega?","Elektr yoyi yongan daqiqada elektrodlar orasidagi kuchlanish qanday o'zgaradi?","Gazlarda qarshilikning temperaturaga bog'liqligi qanday?","Gazlarning Volt-Amper xarakteristikasi qanday?","Gazlarda elektr tokining o'tishi Om qonuniga bo'ysunadimi?","Gaz razryadida anod kuchlanishi kamaytirilsa uning o'tkazuvchanligi qanday o'zgaradi?","Chaqmoq qaysi razryad turiga kiradi?"]

vakuum = ["Termoelektron emissiya nima?","Diod nima?","To'yinish toki nima?","Vakuumda asosiy tok tashuvchilari nima?","Triod nima?","Elektron nur trubka nima?","Chiqish ishini topish formulasida (A = e*delta_fi) delta_fi nima?","Qanday shart bajarilganda elektron metallni tark etadi?","Vakuumli diod uchun Om qonuni bajariladimi?","Vakuumda tok kuchi temperaturaga qanday bog'liq?","Triodda to'r qayerga qo'yiladi","Qanday shart bajarilganda triod diod vazifasini bajaradi?","Trioddan o'tadigan tok to'r potensialiga qanday bog'liq?","Triodda yopish kuchlanish deb nimaga aytiladi?","Qanday muhitlarda elektr tokining issiqlik ta'siri kuzatilmaydi","Katod nurlari nima?","Anod potensiali ta'sirida elektron olgan tezlanish qanday topiladi?","Diodning Volt-Amper xarakteristikasi qanday?","Volframli, molibdenli va oksidli uch katod bir xil temperaturagacha qizdirilgan. Qaysi katod eng ko'p elektron chiqaradi?"]

yarimotkazgich = ["Yarimotkazgichlarda asosiy tok tashuvchilari nima?","Yarimotkazgichlar nima?","Donor aralashmali yarimotkazgichlar nima?","Akseptor aralashmali yarimotkazgichlar nima?","Tranzistor vazifasi nima?","Tranzistorning asosiy qismlari nima?","Yarimotkazgichlarda qarshilikning temperaturaga bogliqligi","Temperatura ortishi bilan yarimotkazgichning solishtirma qarshiligi qanday ozgaradi?","O'ta o'tkazuvchanlik hodisasini 1-kim aniqlagan?","Davriy jadvalning 3-guruh elementlari qanday otkazuvchanlik beradi?","Fotorezistor nima?","Fotoelement nima?","Termistorlar nima?","Kovaklar qanday zaryadga ega?","Yarimotkazgichlar kristallmi yoki amorfmi?","Bolometr yordamida qaysi kattalik o'lchanadi?","Yarimotkazgichlarda elektron va kovak uchrashganda energiya ajraladimi?","Teng miqdorda teshikli va elektronli yarimotkazgichlar mavjudmi?","Qo'shilmasiz, yaxshi tozalangan yarimotkazgichlardagi elektr toki qaysi zarralar hisobiga hosil boladi?","Ota toza kremniyga akseptor qoshilma kiritilsa, yarimotkazgichning otkazuvchanligi qanday ozgaradi?"]

turli_muhitlarda_elektr_toki = metallar + elektrolitlar + vakuum + yarimotkazgich


# ---| [10] Elekromagnit hodisalar \---

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

#.....

#***********************************************
#***********************************************
#***********************************************

savollar = turli_muhitlarda_elektr_toki + elektromagnit_hodisalar
true_count,false_count = 0,0

for i in range(len(savollar)-1):
    x = random.randint(0,len(savollar)-1)
    print("")
    print(savollar[x])
    print("")
    javob = input("Topsangiz 1, aks holda 0 ni bosing: ")
    if javob == 1:
        true_count+=1
        continue
    else:
        false_count+=1
        continue

print("To'g'ri javoblar:",true_count,'\n', "Noto'g'ri javoblar:",false_count)