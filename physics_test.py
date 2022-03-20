import random

#.....


# ---| [9] Turli muhitlarda elektr toki \---

metallar = ["Metallarda asosiy tok tashuvchilar nima?","Metallarda qarshilikning temperaturaga bog'liqligi?","O'ta-o'tkazuvchanlik?","Volt-Amper xarakteristikasi nima?","Qarshilikning termik koeffitsiyenti nima?","Metallarda elektr tokining tarqalish tezligi nima bilan aniqlanadi?","Metallarda Volt-Amper xarakteristikasi qanday?"]

elektrolitlar = ["Elektroliz nima?","Rekombinatsiya nima?","Elektrolitlar nima?","Dissotsiatsiya nima?","Dissotsiyatsiyalanish darajasi nima?","Dissotsiatsiyalanish darajasining eng katta qiymati nima?","Elektrolitlarda dissotsiatsiya darajasi temperaturaga qanday bog'liq?","Faradeyning 1-qonuni","Elektrokimyoviy ekvivalent nima?","Faradey 2-qonuni","Faradey doimiysi","Faradeyning birlashgan qonuni","Elektrolitlarda ionlar qanday vujudga keladi?","Qanday o'tkazgichlar ionli o'tkazuvchanlikka ega?","Elektrolitlarda elektr toki qanday hosil qilinadi?","Temperatura ortishi bilan elektrolitning o'tkazuvchanligi qanday o'zgaradi","Elektroliz hodisasining texnikada qo'llanilishi qanday?","Elektrolitlarda kuchlanish o'zgarmasdan vanna elektrodlari orasidagi masofa o'zgarsa, tok kuchi qanday o'zgaradi?","Elektrolit orqali tok o'tganda ko'chish mumkin bo'lgan eng kichik zaryad qiymati nimaga teng?","Anion nima?","Kation nima?","Ion nima?","Qanday moddalarda qarshilikning termik koeffitsiyenti musbat bo'ladi?","Qanday moddalarda qarshilikning termik koeffitsiyenti manfiy bo'ladi?","Elektrolitdan o'tayotgan umumiy tok qabday topiladi?","Kimyoviy ekvivalent nima?","Elektrokimyoviy ekvivalent birligini XBS dagi asosiy birliklar orqali ifodalang.","Sulfat kislotasi eritilgan suvda elektr tokining qanday ta'siri mavjud?","Elektrolitlarning Volt-Amper xarakteristikasi qanday?","Elektrolitlar uchun Om qonuni o'rinlimi?"]

gazlar = ["Gaz razryadi nima?", "Gazlarda asosiy elektr tashuvchilari nima?","Mustaqil razryad nima?","Nomustaqil razryad nima?","Toj razryadi nima?","Uchqunli razryad nima?","Yoy razryadi nima?","Yolqin razryad nima?","Plazma nima?","Qanday o'tkazgichlar ionli va elektronli o'tkazuvchanlikka ega?","Elektr yoyi yongan daqiqada elektrodlar orasidagi kuchlanish qanday o'zgaradi?","Gazlarda qarshilikning temperaturaga bog'liqligi qanday?","Gazlarning Volt-Amper xarakteristikasi qanday?","Gazlarda elektr tokining o'tishi Om qonuniga bo'ysunadimi?","Gaz razryadida anod kuchlanishi kamaytirilsa uning o'tkazuvchanligi qanday o'zgaradi?","Chaqmoq qaysi razryad turiga kiradi?"]

vakuum = []

yarimotkazgich = ["Yarimotkazgichlarda asosiy tok tashuvchilari nima?","Yarimotkazgichlar nima?","Donor aralashmali yarimotkazgichlar nima?","Akseptor aralashmali yarimotkazgichlar nima?","Tranzistor vazifasi nima?","Tranzistorning asosiy qismlari nima?","Yarimotkazgichlarda qarshilikning temperaturaga bogliqligi","Temperatura ortishi bilan yarimotkazgichning solishtirma qarshiligi qanday ozgaradi?","O'ta o'tkazuvchanlik hodisasini 1-kim aniqlagan?","Davriy jadvalning 3-guruh elementlari qanday otkazuvchanlik beradi?","Fotorezistor nima?","Fotoelement nima?","Termistorlar nima?","Kovaklar qanday zaryadga ega?","Yarimotkazgichlar kristallmi yoki amorfmi?","Bolometr yordamida qaysi kattalik o'lchanadi?","Yarimotkazgichlarda elektron va kovak uchrashganda energiya ajraladimi?","Teng miqdorda teshikli va elektronli yarimotkazgichlar mavjudmi?","Qo'shilmasiz, yaxshi tozalangan yarimotkazgichlardagi elektr toki qaysi zarralar hisobiga hosil boladi?","Ota toza kremniyga akseptor qoshilma kiritilsa, yarimotkazgichning otkazuvchanligi qanday ozgaradi?"]

turli_muhitlarda_elektr_toki = metallar + elektrolitlar + vakuum


# ---| [10] Elekromagnit hodisalar \---

#.....

#***********************************************
#***********************************************
#***********************************************

savollar = turli_muhitlarda_elektr_toki

for i in range(10):
    x = random.randint(0,len(savollar)-1)
    print("")
    print(savollar[x])
    print("")
    javob = input("Topsangiz 1, aks holda 0 ni bosing: ")
    if javob == 1:
        continue
