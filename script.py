from openexp.mouse import mouse
from openexp.canvas import canvas
from openexp.keyboard import keyboard
from openexp.sampler import sampler
from random import random, shuffle

# variables

myMouse = mouse(exp, visible=True)
index = 99
myCanvas = self.copy_sketchpad('planche1')
myKeyboard = keyboard(exp, timeout=None)
cases = []
for i in range(30):
    cases.append(0)
startTime = self.time()
totalTime = 0
interval = False
complexity = False  # true = easy
duration = False  # true = quick
Interruption = False
clicks = 0
numberInterruptions2 = 0
clickTrigger = clicks[numberInterruptions2]
goodClicks = 0
isInterruption = False
hasEndInterruption = False
endInterruption = False
currentInterruption = 0
displayResponseTime = 500
displayNumberTime = 1000
printingTime = 1000
numbersTyped = ",,,"
numbersShown = ""
lengthCurrent = 3
resumptionLag1 = 0
resumptionLag12 = 0
interruption0 = 0
typeinterruption = 0
blackNumber = exp.get_file(u'blackNumber.jpg')
crossFull = exp.get_file(u'croix.png')
crossEmpty = exp.get_file(u'vide.png')

# add or withdraw a cross if the participant click on an area where there could be one (a box)
# can't use a fonction there since the area are randomly distributed on the screen

if str(self.get("Image")) == "16.jpg" or str(self.get("Image")) == "17.jpg" or str(self.get("Image")) == "10.jpg":
    Interruption = True
    interval = True
    complexity = True
    duration = True
    self.log("interval simple rapide")

if str(self.get("Image")) == "1.jpg" or str(self.get("Image")) == "7.jpg" or str(self.get("Image")) == "5.jpg":
    Interruption = True
    interval = True
    complexity = True
    self.log("interval simple lent")

if str(self.get("Image")) == "8.jpg" or str(self.get("Image")) == "29.jpg" or str(self.get("Image")) == "2.jpg":
    Interruption = True
    interval = True
    duration = True
    self.log("interval complexe rapide")

if str(self.get("Image")) == "4.jpg" or str(self.get("Image")) == "19.jpg" or str(self.get("Image")) == "28.jpg":
    Interruption = True
    interval = True
    self.log("interval complexe lent")

if str(self.get("Image")) == "20.jpg" or str(self.get("Image")) == "21.jpg" or str(self.get("Image")) == "26.jpg":
    Interruption = True
    complexity = True
    duration = True
    self.log("Pas interval simple rapide")

if str(self.get("Image")) == "14.jpg" or str(self.get("Image")) == "18.jpg" or str(self.get("Image")) == "30.jpg":
    Interruption = True
    complexity = True
    self.log("Pas interval simple lent")

if str(self.get("Image")) == "6.jpg" or str(self.get("Image")) == "9.jpg" or str(self.get("Image")) == "12.jpg":
    Interruption = True
    duration = True
    self.log("Pas interval complexe rapide")

if str(self.get("Image")) == "13.jpg" or str(self.get("Image")) == "24.jpg" or str(self.get("Image")) == "25.jpg":
    Interruption = True
    self.log("Pas interval complexe lent")

if str(self.get("Image")) == "3.jpg" or str(self.get("Image")) == "11.jpg" or str(self.get("Image")) == "15.jpg" or str(self.get("Image")) == "22.jpg" or str(self.get("Image")) == "23.jpg" or str(self.get("Image")) == "27.jpg":
    self.log("Non interrompu")

self.log(self.get("Image"))
self.log("VD,Croix,Temps,Reponse 1,Reponse 2,Reponse 3")


# during the task, participants also had to do a memory task that's here to disturb them
# fonction that defines the parameters of the interruption task

def createInterruption(boardNumber, taskDifficulty):
    global myCanvas, printingTime, myKeyboard, displayResponseTime, displayNumberTime

    numbersGenerated = ""
    x = str(int(9.0*random()))

    myCanvas.rect(26, -290, 200, 100, color="black", fill=True)
    myCanvas.show()
    self.sleep(displayNumberTime)

    for i in range(taskDifficulty):
        while x in numbersGenerated:
            x = str(int(9.0*random()))
        numbersGenerated += x
        chiffre = exp.get_file(u'chiffre'+x+'.jpg')
        myCanvas.image(chiffre, y=-240, x=-460, scale=0.1, center=False)
        myCanvas.show()
        self.sleep(printingTime)
        if interval == True:
            myCanvas.image(blackNumber, y=-240, x=-
                           460, scale=0.1, center=False)
            myCanvas.show()
            self.sleep(1000)

    myCanvas.image(exp.get_file(u'chiffrePi.jpg'), y=-
                   240, x=-460, scale=0.1, center=False)
    myCanvas.show()
    self.sleep(displayResponseTime)
    myCanvas.rect(31, -285, 190, 90, color="white", fill=True)
    myCanvas.show()
    myKeyboard.flush()

    self.log(numbersGenerated)
    return numbersGenerated

# loop that checks the current situation of the task and increment variables so as to follow the procedure of the the experiment


if Interruption == True:
    if complexity == True:
        if duration == True:
            nextInterruption = taskEasy1[nbinterruptionsSR]
            numberInterruptionsSR = len(taskEasy1[nbinterruptionsSR])
            nbinterruptionsSR += 1
            typeinterruption += 1
            tableInterruption = nextInterruption
        else:
            nextInterruption = taskEasy2[nbinterruptionsSL]
            nb_interruptionsSL = len(taskEasy2[nbinterruptionsSL])
            nbinterruptionsSL += 1
            typeinterruption += 2
            tableInterruption = nextInterruption

    else:
        if duration == True:
            nextInterruption = taskComplex1[nbinterruptionsCR]
            nb_interruptionsCR = len(taskComplex1[nbinterruptionsCR])
            nbinterruptionsCR += 1
            typeinterruption += 3
            tableInterruption = nextInterruption
        else:
            nextInterruption = taskComplex2[nbinterruptionsCL]
            nb_interruptionsCL = len(taskComplex2[nbinterruptionsCL])
            nbinterruptionsCL += 1
            typeinterruption += 4
            tableInterruption = nextInterruption

# main loop, that goes on for as long as the participant doesn't click on the bin icon at the top left of the screen

while index != 0:
    en_colonne = False

    button, position, timestamp = myMouse.get_click(timeout=100)
    if position != None:
        x, y = position
    else:
        x = -1
        y = -1

    # if the participant clicks on a certain area, consequences will follow (cross, uncross, interruption, new email page)
    # once again the spatial coordinates are random so no fonction could be used here

    if x >= -641 and x < -557 and y >= -527 and y < -470 and totalTime > 1000:
        index = 0

    if x >= -653 and x < -638 and y >= -442 and y < -426:
        y = -440
        index = 1
        en_colonne = True

    if x >= -653 and x < -638 and y >= -408 and y < -393:
        y = -408
        index = 2
        en_colonne = True

    if x >= -653 and x < -638 and y >= -376 and y < -360:
        y = -374
        index = 3
        en_colonne = True

    if x >= -653 and x < -638 and y >= -343 and y < -326:
        y = -341
        index = 4
        en_colonne = True

    if x >= -653 and x < -638 and y >= -310 and y < -293:
        y = -308
        index = 5
        en_colonne = True

    if x >= -653 and x < -638 and y >= -277 and y < -261:
        y = -275
        index = 6
        en_colonne = True

    if x >= -653 and x < -638 and y >= -244 and y < -227:
        y = -242
        index = 7
        en_colonne = True

    if x >= -653 and x < -638 and y >= -211 and y < -195:
        y = -210
        index = 8
        en_colonne = True

    if x >= -653 and x < -638 and y >= -178 and y < -162:
        y = -177
        index = 9
        en_colonne = True

    if x >= -653 and x < -638 and y >= -145 and y < -128:
        y = -144
        index = 10
        en_colonne = True

    if x >= -653 and x < -638 and y >= -112 and y < -95:
        y = -111
        index = 11
        en_colonne = True

    if x >= -653 and x < -638 and y >= -79 and y < -63:
        y = -79
        index = 12
        en_colonne = True

    if x >= -653 and x < -638 and y >= -46 and y < -30:
        y = -46
        index = 13
        en_colonne = True

    if x >= -653 and x < -638 and y >= -14 and y < 3:
        y = -12
        index = 14
        en_colonne = True

    if x >= -653 and x < -638 and y >= 19 and y < 36:
        y = 21
        index = 15
        en_colonne = True

    if x >= -653 and x < -638 and y >= 52 and y < 69:
        y = 53
        index = 16
        en_colonne = True

    if x >= -653 and x < -638 and y >= 86 and y < 103:
        y = 86
        index = 17
        en_colonne = True

    if x >= -653 and x < -638 and y >= 118 and y < 135:
        y = 119
        index = 18
        en_colonne = True

    if x >= -653 and x < -638 and y >= 151 and y < 168:
        y = 152
        index = 19
        en_colonne = True

    if x >= -653 and x < -638 and y >= 184 and y < 201:
        y = 185
        index = 20
        en_colonne = True

    if x >= -653 and x < -638 and y >= 219 and y < 234:
        y = 219
        index = 21
        en_colonne = True

    if x >= -653 and x < -638 and y >= 250 and y < 268:
        y = 251
        index = 22
        en_colonne = True

    if x >= -653 and x < -638 and y >= 284 and y < 301:
        y = 284
        index = 23
        en_colonne = True

    if x >= -653 and x < -638 and y >= 316 and y < 332:
        y = 317
        index = 24
        en_colonne = True

    if x >= -653 and x < -638 and y >= 350 and y < 365:
        y = 351
        index = 25
        en_colonne = True

    if x >= -653 and x < -638 and y >= 382 and y < 399:
        y = 383
        index = 26
        en_colonne = True

    if x >= -653 and x < -638 and y >= 415 and y < 432:
        y = 416
        index = 27
        en_colonne = True

    if x >= -653 and x < -638 and y >= 448 and y < 465:
        y = 449
        index = 28
        en_colonne = True

    if x >= -653 and x < -638 and y >= 481 and y < 497:
        y = 482
        index = 29
        en_colonne = True

    if x >= -653 and x < -638 and y >= 514 and y < 530:
        y = 515
        index = 30
        en_colonne = True

    # if a certain number of clicks is reached, the interruption task starts with no warning

    if isInterruption:
        key, end_time = myKeyboard.get_key(timeout=3000)
        if key != None:
            if len(numbersTyped) < (2*lengthCurrent + 3):
                numbersShown += key
                numbersTyped += key + ","
                myCanvas.text(numbersShown, x=66, y=-
                              250, color="black", center=False)
                myCanvas.show()
        else:
            self.log(numbersTyped)
            currentInterruption += 1

            if typeinterruption == 1 and currentInterruption < numberInterruptionsSR:
                numbersGenerated = createInterruption(
                    currentInterruption, tableInterruption[currentInterruption])
                interruptionStartTime = self.time()
                numbersTyped = ",,,"
                numbersShown = ""
            elif typeinterruption == 2 and currentInterruption < nb_interruptionsSL:
                numbersGenerated = createInterruption(
                    currentInterruption, tableInterruption[currentInterruption])
                interruptionStartTime = self.time()
                numbersTyped = ",,,"
                numbersShown = ""
            elif typeinterruption == 3 and currentInterruption < nb_interruptionsCR:
                numbersGenerated = createInterruption(
                    currentInterruption, tableInterruption[currentInterruption])
                interruptionStartTime = self.time()
                numbersTyped = ",,,"
                numbersShown = ""
            elif typeinterruption == 4 and currentInterruption < nb_interruptionsCL:
                numbersGenerated = createInterruption(
                    currentInterruption, tableInterruption[currentInterruption])
                interruptionStartTime = self.time()
                numbersTyped = ",,,"
                numbersShown = ""

            else:
                eyetracker.log("Intfin")
                isInterruption = False
                endInterruption = True
                interruption0 = 1
                resumptionLag1 = self.time()
                startTime = self.time()
                resumptionLag1_startTime = self.time()
                myCanvas.image(exp.get_file(self.get("Image")),
                               y=-540, x=-960, center=False)
                myCanvas.show()
                if cases[0] == 1:
                    myCanvas.image(crossFull, y=-440, x=-652, center=False)
                    myCanvas.show()
                if cases[1] == 1:
                    myCanvas.image(crossFull, y=-408, x=-652, center=False)
                    myCanvas.show()
                if cases[2] == 1:
                    myCanvas.image(crossFull, y=-374, x=-652, center=False)
                    myCanvas.show()
                if cases[3] == 1:
                    myCanvas.image(crossFull, y=-341, x=-652, center=False)
                    myCanvas.show()
                if cases[4] == 1:
                    myCanvas.image(crossFull, y=-308, x=-652, center=False)
                    myCanvas.show()
                if cases[5] == 1:
                    myCanvas.image(crossFull, y=-275, x=-652, center=False)
                    myCanvas.show()
                if cases[6] == 1:
                    myCanvas.image(crossFull, y=-242, x=-652, center=False)
                    myCanvas.show()
                if cases[7] == 1:
                    myCanvas.image(crossFull, y=-210, x=-652, center=False)
                    myCanvas.show()
                if cases[8] == 1:
                    myCanvas.image(crossFull, y=-177, x=-652, center=False)
                    myCanvas.show()
                if cases[9] == 1:
                    myCanvas.image(crossFull, y=-144, x=-652, center=False)
                    myCanvas.show()
                if cases[10] == 1:
                    myCanvas.image(crossFull, y=-111, x=-652, center=False)
                    myCanvas.show()
                if cases[11] == 1:
                    myCanvas.image(crossFull, y=-79, x=-652, center=False)
                    myCanvas.show()
                if cases[12] == 1:
                    myCanvas.image(crossFull, y=-46, x=-652, center=False)
                    myCanvas.show()
                if cases[13] == 1:
                    myCanvas.image(crossFull, y=-12, x=-652, center=False)
                    myCanvas.show()
                if cases[14] == 1:
                    myCanvas.image(crossFull, y=21, x=-652, center=False)
                    myCanvas.show()
                if cases[15] == 1:
                    myCanvas.image(crossFull, y=53, x=-652, center=False)
                    myCanvas.show()
                if cases[16] == 1:
                    myCanvas.image(crossFull, y=86, x=-652, center=False)
                    myCanvas.show()
                if cases[17] == 1:
                    myCanvas.image(crossFull, y=119, x=-652, center=False)
                    myCanvas.show()
                if cases[18] == 1:
                    myCanvas.image(crossFull, y=152, x=-652, center=False)
                    myCanvas.show()
                if cases[19] == 1:
                    myCanvas.image(crossFull, y=185, x=-652, center=False)
                    myCanvas.show()
                if cases[20] == 1:
                    myCanvas.image(crossFull, y=219, x=-652, center=False)
                    myCanvas.show()
                if cases[21] == 1:
                    myCanvas.image(crossFull, y=251, x=-652, center=False)
                    myCanvas.show()
                if cases[22] == 1:
                    myCanvas.image(crossFull, y=284, x=-652, center=False)
                    myCanvas.show()
                if cases[23] == 1:
                    myCanvas.image(crossFull, y=317, x=-652, center=False)
                    myCanvas.show()
                if cases[24] == 1:
                    myCanvas.image(crossFull, y=351, x=-652, center=False)
                    myCanvas.show()
                if cases[25] == 1:
                    myCanvas.image(crossFull, y=383, x=-652, center=False)
                    myCanvas.show()
                if cases[26] == 1:
                    myCanvas.image(crossFull, y=416, x=-652, center=False)
                    myCanvas.show()
                if cases[27] == 1:
                    myCanvas.image(crossFull, y=449, x=-652, center=False)
                    myCanvas.show()
                if cases[28] == 1:
                    myCanvas.image(crossFull, y=482, x=-652, center=False)
                    myCanvas.show()
                if cases[29] == 1:
                    myCanvas.image(crossFull, y=515, x=-652, center=False)
                    myCanvas.show()

    else:
        if index == 0:
            if interruption0 == 1:
                interruption0 = 0
                resumptionLag12 = self.time() - startTime
            totalTime += self.time() - startTime
            self.log(",Poubelle," + str(self.time() - startTime))
            src = exp.get_file('corbeilleXP.wav')
            my_sampler = sampler(exp, src)
            my_sampler.play()
            if endInterruption:
                endInterruption = False
                resumptionLag1 = self.time() - resumptionLag1_startTime
        else:
            if en_colonne:
                if cases[index-1] == 0:
                    cases[index-1] = 1
                    goodClicks += 1
                    croix = crossFull
                else:
                    goodClicks -= 1
                    cases[index-1] = 0
                    croix = crossEmpty
                myCanvas.image(croix, y=y, x=-652, center=False)
                myCanvas.show()
                if interruption0 == 1:
                    interruption0 = 0
                    resumptionLag12 = self.time() - startTime
                totalTime += self.time() - startTime
                self.log("," + str(index) + "," +
                         str(self.time() - startTime))
                startTime = self.time()

                if goodClicks == clickTrigger and Interruption == True:
                    eyetracker.log("Intdebut")
                    self.sleep(250)
                    nbinterruptions2 += 1
                    isInterruption = True
                    src = exp.get_file('alerte2.wav')
                    my_sampler = sampler(exp, src)
                    my_sampler.play()
                    myCanvas.image(exp.get_file('fond.png'),
                                   y=-540, x=-960, center=False)
                    myCanvas.show()
                    myCanvas.image(exp.get_file('Popupfond.png'),
                                   y=-530, x=-654, center=False)
                    myCanvas.show()
                    myCanvas.rect(-634, -510, 600, 1028,
                                  color="black", fill=True)
                    myCanvas.show()
                    myCanvas.rect(-34, -510, 606, 1028,
                                  color="grey", fill=True)
                    myCanvas.show()
                    myCanvas.text("Votre reponse :", x=26, y=-
                                  340, color="black", center=False)
                    myCanvas.show()
                    myCanvas.rect(26, -290, 200, 100,
                                  color="black", fill=True)
                    myCanvas.show()
                    myCanvas.text("Rappelez les 3 derniers chiffres", x=-
                                  500, y=-490, max_width=600, color="white", center=False)
                    myCanvas.show()
                    self.sleep(250)
                    myKeyboard.flush()
                    createInterruption(0, tableInterruption[0])

                    interruptionStartTime = self.time()

                if endInterruption:
                    endInterruption = False

        self.log("Nb de clic,"+str(clickTrigger))
        self.log("TOT," + str(totalTime))
        if Interruption == True:
            self.log("resumptionLag1," + str(resumptionLag12))
            self.log("")

            numberTrials += 1
            numberTrials2 = 30 - numberTrials

            backBackground = exp.get_file("fond noir.jpg")
            myCanvas.image(backBackground, y=-540, x=-960, center=False)
            myCanvas.show()
            myCanvas.text('Vous pouvez cligner des yeux',
                          center=True, x=0, y=0, color=u'white')
            myCanvas.show()

            if numberTrials2 > 1:
                myCanvas.text('Nombre d\'essais restants : ' +
                              str(numberTrials2), center=True, x=0, y=30, color=u'white')
                myCanvas.show()

            if numberTrials2 == 1:
                myCanvas.text('Nombre d\'essai restant : '+str(numberTrials2),
                              center=True, x=0, y=30, color=u'white')
                myCanvas.show()

self.sleep(2500)
