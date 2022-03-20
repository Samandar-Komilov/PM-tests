import random

# ---| [7] Elektrostatika \---


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

elektrostatika = elektr_zaryadi


# ---| [8] O'zgarmas elektr toki \---


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
true_count = 0
false_count = 0

for i in range(30):
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

print("To'g'ri javoblar:",true_count,'\n', "Noto'g'ri javoblar:",false_count)