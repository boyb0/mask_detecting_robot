# Мобилен робот способен да детектира дали луѓето носат маски или не
##### Проект по предметите Вовед во Роботика и Машинска Визија
## Содржина
- [Опис на идејата](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%BE%D0%BF%D0%B8%D1%81-%D0%BD%D0%B0-%D0%B8%D0%B4%D0%B5%D1%98%D0%B0%D1%82%D0%B0)
- [Опис на системот](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%BE%D0%BF%D0%B8%D1%81-%D0%BD%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BE%D1%82)
- [Програмирање и интеграција на јазлите](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8%D1%80%D0%B0%D1%9A%D0%B5-%D0%B8-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%98%D0%B0-%D0%BD%D0%B0-%D1%98%D0%B0%D0%B7%D0%BB%D0%B8%D1%82%D0%B5)
- [Опис на детекторот за маски](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%BE%D0%BF%D0%B8%D1%81-%D0%BD%D0%B0-%D0%B4%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D1%82-%D0%BD%D0%B0-%D0%BC%D0%B0%D1%81%D0%BA%D0%B8)
- [Инсталација, конфигурирање и стартување](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BB%D0%B0%D1%86%D0%B8%D1%98%D0%B0-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B8%D1%80%D0%B0%D1%9A%D0%B5-%D0%B8-%D1%81%D1%82%D0%B0%D1%80%D1%82%D1%83%D0%B2%D0%B0%D1%9A%D0%B5)
- [Тест возење на роботот](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D1%82%D0%B5%D1%81%D1%82-%D0%B2%D0%BE%D0%B7%D0%B5%D1%9A%D0%B5-%D0%BD%D0%B0-%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%BE%D1%82)
- [Помошни материјали, пакети, библиотеки и модели](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%BF%D0%BE%D0%BC%D0%BE%D1%88%D0%BD%D0%B8-%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D1%98%D0%B0%D0%BB%D0%B8-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B8-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8-%D0%B8-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8)
- [Изработиле](https://github.com/boyb0/mask_detecting_robot/blob/master/README.md#%D0%B8%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B8%D0%BB%D0%B5)
## Опис на идејата

Идејата за креирањето на овој проект потекнува од моменталната ситуација во која се наоѓа целиот свет поради пандемијата предизвикана од COVID-19 вирусот. Како една од најзначајните превентивни мерки за спречување на ширењето на вирусот е носењето на маска. За жал, луѓето не толку често го почитуваат тоа. Целта на овој проект е да се направи еден вид на мобилен робот кој ќе препознава дали луѓето носат или не носат заштитни маски. Воедно роботот автономно се движи и избегнува препреки. За реализација на таа цел користен е возилниот робот Pioneer P3-DX од Mobile Robots. Кога се стартува роботот тој почнува да се движи по патека дефинирана со различни видови на пречки и во исто време, преку камера препознава дали лицата кои ги детектирал на камерата носат или не носат заштитна маска. Секогаш кога детектира едно или повеќе лица роботот го обележува лицето со соодветна лабела и квадрат и испишува под него дали носи или не носи маска, а воедно праќа и известување за тоа колку лица со маска и колку лица без маска забележал во даден момент.

## Опис на системот

Системот се остои од два хардверски дела, возилниот робот Pioneer P3-DX и лаптоп. Роботот користи 8 сонари, преку кои може да ја мери оддалеченоста од препреките околу него, исто така има и два серво мотори кои ги користи за да ги придвижи тркалата. Од лаптопот се користи камерата преку која се врши снимањето на околината.
Од аспект на логички дизајн, системот се состои од 8 процеси/јазли кои се извршуваат истовремено и се постојано во меѓусебна интеракција. Овие јазли се делат во три групи. Едната група е задолжена за движење на роботот, другата група е задолжена за процесирање на рамките и еден јазол е задолжен за примање и прикажување на пораки. На сликата е прикажан дијаграмот на системот:


 ![Дијаграм на системот](diagram.png)

## Програмирање и интеграција на јазлите

Следи краток опис на функционалностите и поврзаноста на секој од јазлите. Дополнително сите сегменти од кодот на јазлите се објаснети со коментари во самите скрипти.

**I. Main Node:**
Овој јазол е главниот и контролниот јазол на ситемот. Јазолот комуницира со три други јазли и тоа на следниов начин: 
- *sensors_node* -  Комуникацијата со овој јазол се одвива преку топикот *sensor_data* со тоа што контролниот јазол прима сензорски податоци од овој топик кои се пратени од јазолот *sensor_node* и преку нив се донесуваат одлуки за тоа дали и како треба да се придвижи роботот.  - *actuators_node* - Комуникацијата со овој јазол се одвива преку топикот *actuators_cmd* со тоа што контролниот јазол испраќа податоци за придвижување на роботот на  *actuators_cmd*.
- *video_proccessing_node* - Комуникацијата со овој јазол се одвива преку топикот *mask_detection* со тоа што контролниот јазол прима податоци од овој топик за тоа колку лица се детектирани со/без маска во моментот и ја печати таа порака.

**II. Sensors Node:** 
Овој јазол служи за отчитување и процесирање на податоците од сензорите. Јазолот комуницира со два други јазли и тоа на следиов начин:
- *RosAria* - Комуникацијата со овој јазол се одвива преку топикот */RosAria/sonar* со тоа што сензорскиот јазол ги добива сензорските отчитувања од роботот и преку овие информации се пресметува оддалеченоста до препреките на патот.
- *main_node* - Комуникацијата со овој јазол се одвива преку топикот *sensor_data* со тоа што сензорскиот јазол му ја испраќа пресметаната оддалеченост до препреките на патот на контролниот јазол.

**III. Actuators Node:** 
Овој јазол служи за придвижување на роботот. Јазолот комуницира со два други јазли и тоа на следниов начин:
- *main_node* - Комуникацијата со овој јазол се одвива преку топикот *actuators_cmd* со тоа што главниот јазол му испраќа податоци за тоа на каде треба роботот да се придвижи.
- *RosAria* - Комуникацијата со овој јазол се одвива преку топикот */RosAria/cmd_vel* со тоа што  се ипраќаат добиените податоци за движење на роботот до *RosAria*

**IV. RosAria:** 
Овој јазол е екстерен јазол кој треба дополнително да се инсталира, служи за комуникација со сензорите и со актуаторите, т.е за читање на податоците од сензорите и за праќање на команди до актуаторите.

**V. Camera Node:** 
Овој јазол е директно поврзан со камерата и преку неа ги чита рамките, па потоа на јазлите *video_display_node* и *video_proccessing_node* преку топикот *frame* им ги испраќа отчитаните рамки.

**VI. Video Display Node:**
Овој јазол служи за прикажување на рамките кои ги зима од јазолот *camera_node* преку топикот *frame*.

**VII. Video Processing Node:**
Во овој јазол се извршува целата логика на машинската визија. Рамките кои пристигнуваат од *camera_node*  се претпроцесираат и служат како влез на однапред истренирани детектори за лица и маски. Доколку се детектира барем едно лице, преку топикот *mask detection*  се испраќа информација до главниот јазол за тоа колку од детектираните лица носат/ не носат маска. Покрај оваа информација се испраќа и информацијата во колку час е извршена детекцијата. Во овој јазол се користи **детектор на лица** кој е превземен како готов модел и **детектор на маски** кој е креиран, моделиран и трениран од наша страна. Главната логика лежи во тоа што при секој фрејм добиен од камерата, преку детекторот на лица се детектираат човчки лица на дадениот фрејм (доколку постојат) и истите се екстрактираат како региони на интерес (ROI). Во една листа се сочувуваат лицата, а во друга локациите каде се наоѓаат. Лицата се конвертираат во RGB простор на бои и како такви се претпроцесираат. Потоа се итерира низ сите откриени лица и се детектира за секое дали носи маска или не. Околу оние лица што носат маска се прикажува зелен квадрат со лабела *Nosi maska*, додека пак околу оние што не носат се прикажува црвен квадрат со лабела *Ne nosi maska*.

**VIII. Message Sending Node:**
Претставува сервисен јазол кој што се користи за испраќање на пораката до одреден надзорен орган и печатење на истата. Сервисот кој го нуди е со име message_sending_service.

## Опис на детекторот за маски
Овој детектор беше креиран и трениран од наша страна преку посебна .ipynb скрипта и потоа сочуван во **h5 формат** со цел негово понатамошно дистрибуирано користење.
#### Податочно множество
Податочното множество кое се користеше при тренирање и тестирање на моделот се состои од две категории на слики: лица со маска и лица без маска. Поточно, податочното множество се состои од 1916 слики од лица со маска и 1930 слики од лица без маска. Со цел да се добие модел со што повисока точност и рата на погодок, се користи метод **Image Augmentation** кој преку различни техники како ротација, скалирање, поместување на веќе постоечките слики генерира нови, дополнителни слики за тренирање. Сликите од множеството подлежат на *претпроцесирање* т.е. нормализација на вредностите на нивните пиксели. 

Бидејќи невронските мрежи работат исклучиво со бројки, целниот атрибут (лабелите на сликите:mask\no_mask) е енкодиран со помош на кодирачката шема **One Hot Encoding** каде што во колоната на која припаѓа сликата стои 1, додека во другата спротивна колона стои 0. 

#### Делење на податочното множество
Податочното множество беше поделено во следниов сооднос: **75%** од податоците беа искористени за *тренирање* на моделот, додека пак останатите **25%** за *валидација* на истиот.

#### Креирање на моделот
За креирање на нашата CNN се користи техниката наречена **transfer learning** каде се користи основата на веќе истренирана конволуциска невронска мрежа на огромно податочно множество - **MobileNetV2**, додека последниот слој го дефинираме самите и го тренираме на нашето податочно множество со што се специфицира знаењето на моделот. Кога се тренира додадениот слој на мрежата, останатите слоеви се *„замрзнуваат"*  за да не се менуваат веќе утврдените тежини на основниот модел.  Нашиот дел од мрежата се состои од:
- еден *pooling* слој со јадро (7 x 7) кој ја намалува димензионалноста на сликата без да се изгубат значајни карактеристики или шеми од истата.
- еден *flatten* слој кој ја трансформира 2Д матрица од карактеристики во вектор спремен да се предаде на класификаторот
- два *dense* слоја со по 128 и 2 неврони и *dropout* со веројатност од 0.5 да не се зема во предвид пропагацијата од одреден неврон

#### Тренирање на моделот
Моделот беше трениран во **20 епохи** со големина на еден **batch** еднаква на **32**. За валидација на моделот беше користено тестирачкото множество.

#### Евалуација на моделот
| | precision | recall | f1-score | support |
|:----------:|:----------:|:-----:|:-----------:|:--------:|
|mask    | 0.99   | 0.89   | 0.94   |   479|
| no_mask|       0.90   |   0.99 |     0.94 |      483|
|  |
|accuracy|                |        |   0.94 |      962|
|macro avg|       0.94 |     0.94|      0.94|       962|
|weighted avg    |   0.94    |  0.94    |  0.94    |   962|


## Инсталација, конфигурирање и стартување
Информации околу работната околина во која е правен проектот:
- Оперативен систем: Ubuntu 18.04
- Верзија на Python:  2.7.18
- Работна околина: Anaconda 4.8.4
- ROS околина: ROS Melodic

#### Чекори:
1. Отворете го терминалот.

2. Клонирајте го проектот во *src* директориумот од вашата работна околина:

```
cd ~/catkin_ws/src
git clone https://github.com/boyb0/mask_detecting_robot.git
```

3. Клонирајте го [ROSARIA](http://wiki.ros.org/ROSARIA) пакетот во *src* директориумот од вашата ROS работна околина:

```
cd ~/catkin_ws/src
git clone https://github.com/amor-ros-pkg/rosaria.git
```

4. Инсталирајте ја ARIA библиотеката. Истата можете да ја спуштите од [ТУКА](https://web.archive.org/web/20180213095203/http:/robots.mobilerobots.com/wiki/ARIA).

5. Искомпајлирајте ги проектите:

```
cd ~/catkin_ws
catkin_make
```

7. Инсталирајте ги потребните Python пакети:

	- opencv-python
	- imutils
	- tensorflow v.2.1.0

8. Подесете ги патеките до FaceDetectionModel и MaskDetectionModel. Промената треба да се изврши во скриптата *video_processing_node.py* која се наоѓа во *src* директориумот на проектот, на линија 30 и 33.

**ЗАБЕЛЕШКА:** FaceDecetionModel детекторот е зачуван во *model* директориумот на проектот, додека пак MaskDetectionModel е зачуван во домашниот директориум на проектот под името MaskDetectionModel.model. Потребно е да се обезбедат АПСОЛУТНИ ПАТЕКИ за двата детектори да можат да бидат точно вчитани. Исто така MaskDetectionModel е креиран користејќи Tensorflow 2.1.0, па доколку во работната околина е инсталирана друга верзија на овој модул може да настане проблем.

9. Вклучете го роботот и поврзете се со него преку сериска врска. 

10. Доколку не ви е автоматски подесено, source-нете ја catkin setup скриптата во работниот простор:
```
cd ~/catkin_ws
. devel/setup.bash
```

11. Стартувајте ги јазлите:

```
sudo chmod 777 -R /dev/ttyUSB0
roslaunch mask_detecting_robot system.launch
```

## Тест возење на роботот
Тест возењето беше извршено во домашна околина каде што роботот беше поставен на импровизирана патека која поседува пречки кои тој треба да ги одбегне. Помеѓу пречките беа поставени луѓе (ние) со или без маска, со цел да се утврди успешноста на детекциите. Поради лошиот квалитет на камерата, детекцијата не беше совршена, но со подобра камера истата би се постигнала без проблем. Роботот успешно се справи со пречките кои му беа поставени, пронаоѓајќи го својот пат до другиот крај од собата, вршејќи точни детекции во меѓувреме.

#### Видео од извршеното тест возење:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=xebaMDvIfbA" 
target="_blank"><img src="http://img.youtube.com/vi/xebaMDvIfbA/0.jpg" 
alt="Video" width="640" height="480" border="10" /></a>
## Помошни материјали, пакети, библиотеки и модели

- [Pioneer 3 Operations Manual](https://www.inf.ufrgs.br/~prestes/Courses/Robotics/manual_pioneer.pdf)
- [ROSARIA](http://wiki.ros.org/ROSARIA)
- [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [ARIA](https://web.archive.org/web/20180213095203/http:/robots.mobilerobots.com/wiki/ARIA)
- [Realtime Face Detection](https://github.com/simplesaad/FaceDetection_Realtime)
- [MobileNetV2](https://keras.io/api/applications/mobilenet/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)

## Изработиле
- Ана Трајковска
- Бојан Богдановиќ 
- Филип Јорданов 

ФИНКИ - Факултет за информатички науки и компјутерско инженерство, 2020
