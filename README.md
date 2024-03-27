# Human-Face-Attendance

## Attendence of person through face recognition


https://github.com/Mukhriddin19980901/Human-Face-Attendance/assets/86052339/1cce1b06-2b19-4ca2-85dd-c7f45a5a183c

Ushbu loyiha ko'plab oliygoh yoki o'quv joylari talabalari yoki kompaniya , ofis yoki ma'lum bir ishxonalarda ishchilarning 
qatnashuvini (keldi-ketdisini) aniqlash uchun ishlatiladi. Bunda ishxona yoki ofis hodimlarining yuzlari orqali aniqlab
uning ismi va ko'ringan vaqtini bazaga yozib qo'yadi.

<img src="https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/images/Scarlet.png" height="700" width="800"/>

Loyihani qilish uchun [PyCharm Community](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)  versiyasi va [Visual Studio 2019](https://my.visualstudio.com/Downloads?q=visual%20studio%202019&wt.mc_id=o~msft~vscom~older-downloads) ning community versiyasi kerak bo'ladi.
Yuklab bo'lgandan keyin Visual Studioda rasmda ko'rsatilgan joyini yuklab olamiz.

<img src="https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/images/installation.png" height="500" width="800"/>

Uni ham yuklab olgandan keyin Pycharmda yangi loyihani **environment** bilan yaratamiz
va bizga kerakli kutubxonalarni qo'shamiz.Buning uchun Loyihani **File** bo'limidan **Settings** ga kiramiz. 
Va quyidagi rasmdagi kutubxonalarni birma bir yuklab olamiz.Kerakli versiyalari [requirements.txt](https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/requirements.txt) faylni ichida mavjud

<img src="https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/images/Settings.png" height="500" width="800"/>



<img src="https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/images/dependencies.png" height="500" width="800"/>

Endi proyektda yangi 2 ta *py* fayl yaratamiz. Birinchisi [**main.py**](https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/main.py) kodni tushunish uchun va ikkinchisi [**Attendanceproject.py**](https://github.com/Mukhriddin19980901/Human-Face-Attendance/blob/main/Attendanceproject.py) asosiy kod yoziladigan fayl.


ma'lumotlar bazasiga kiritilgan insonlarning yuzini tanib oladi va kamera orqali ayni vaqtda ko'rinayotgan 
insonning yuzi bilan solishtirish orqali uning ismi va qayd etilgan vaqtini yozib oladi
