# Set up a few things
from openexp.mouse import mouse
from openexp.canvas import canvas
from openexp.keyboard import keyboard
from openexp.sampler import sampler
from random import random,shuffle


my_mouse = mouse(exp, visible=True)
index = 99
my_canvas = self.copy_sketchpad('planche1')
my_keyboard = keyboard(exp, timeout=None)
cases = []
for i in range(30):
	cases.append(0)
start_time = self.time()
total_time = 0


intervalle = False
complexite = False #true = facile
duree = False #true = rapide
Interruption = False


if str(self.get("Image")) == "16.jpg" or str(self.get("Image")) == "17.jpg" or str(self.get("Image")) == "10.jpg":
	Interruption = True
	intervalle = True
	complexite = True
	duree = True
	self.log("Intervalle simple rapide")

if str(self.get("Image")) == "1.jpg" or str(self.get("Image")) == "7.jpg" or str(self.get("Image")) == "5.jpg":
	Interruption = True
	intervalle = True
	complexite = True
	self.log("Intervalle simple lent")
	
if str(self.get("Image")) == "8.jpg" or str(self.get("Image")) == "29.jpg" or str(self.get("Image")) == "2.jpg":
	Interruption = True
	intervalle = True
	duree = True
	self.log("Intervalle complexe rapide")

if str(self.get("Image")) == "4.jpg" or str(self.get("Image")) == "19.jpg" or str(self.get("Image")) == "28.jpg":
	Interruption = True
	intervalle = True
	self.log("Intervalle complexe lent")

if str(self.get("Image")) == "20.jpg" or str(self.get("Image")) == "21.jpg" or str(self.get("Image")) == "26.jpg":
	Interruption = True
	complexite = True
	duree = True
	self.log("Pas intervalle simple rapide")

if str(self.get("Image")) == "14.jpg" or str(self.get("Image")) == "18.jpg" or str(self.get("Image")) == "30.jpg":
	Interruption = True
	complexite = True
	self.log("Pas intervalle simple lent")

if str(self.get("Image")) == "6.jpg" or str(self.get("Image")) == "9.jpg" or str(self.get("Image")) == "12.jpg":
	Interruption = True
	duree = True
	self.log("Pas intervalle complexe rapide")

if str(self.get("Image")) == "13.jpg" or str(self.get("Image")) == "24.jpg" or str(self.get("Image")) == "25.jpg":
	Interruption = True
	self.log("Pas intervalle complexe lent")

if str(self.get("Image")) == "3.jpg" or str(self.get("Image")) == "11.jpg" or str(self.get("Image")) == "15.jpg" or str(self.get("Image")) == "22.jpg" or str(self.get("Image")) == "23.jpg" or str(self.get("Image")) == "27.jpg":
	self.log("Non interrompu")


self.log(self.get("Image"))
self.log("VD,Croix,Temps,Reponse 1,Reponse 2,Reponse 3")


def create_interruption(numero_tableau, taille_exercice):
	global my_canvas,printing_time,my_keyboard,display_response_time,display_chiffre_time
	
	suite_generee = ""
	x = str(int(9.0*random()))
	
	my_canvas.rect(26,-290,200,100, color="black",fill=True)
	my_canvas.show()
	self.sleep(display_chiffre_time)
	
	for i in range(taille_exercice):
		while x in suite_generee:
			x = str(int(9.0*random()))
		suite_generee += x
		chiffre = exp.get_file(u'chiffre'+x+'.jpg')
		my_canvas.image(chiffre, y=-240, x=-460, scale=0.1,center=False)
		my_canvas.show()
		self.sleep(printing_time)
		if intervalle == True:
			my_canvas.image(chiffrenoir, y=-240, x=-460, scale=0.1,center=False)
			my_canvas.show()
			self.sleep(1000)
		
	my_canvas.image(exp.get_file(u'chiffrePi.jpg'), y=-240, x=-460, scale=0.1,center=False)
	my_canvas.show()
	self.sleep(display_response_time)
	my_canvas.rect(31,-285,190,90, color="white",fill=True)
	my_canvas.show()
	my_keyboard.flush()
	
	self.log(suite_generee)
	return suite_generee
	
clics_attendus = clics[nbinterruptions2]
good_clics = 0
is_interruption = False
has_fin_interruption = False
temoin_rl = False

current_interruption = 0
display_response_time = 500
display_chiffre_time = 1000
printing_time = 1000
chiffres_tapes = ",,,"
chiffres_a_afficher = ""
longueur_demande = 3
rl = 0
rl2 = 0
interr0 = 0
typeinterruption = 0

if Interruption == True:
	if complexite == True:
		if duree == True:
			suites_interruption = tabfacile1[nbinterruptionsSR]
			nb_interruptionsSR = len(tabfacile1[nbinterruptionsSR])
			nbinterruptionsSR += 1
			typeinterruption += 1
			tab_interruption = suites_interruption
		else:
			suites_interruption = tabfacile2[nbinterruptionsSL]
			nb_interruptionsSL = len(tabfacile2[nbinterruptionsSL])
			nbinterruptionsSL += 1
			typeinterruption += 2
			tab_interruption = suites_interruption

	else:
		if duree == True:
			suites_interruption = tabcomplexe1[nbinterruptionsCR]
			nb_interruptionsCR = len(tabcomplexe1[nbinterruptionsCR])
			nbinterruptionsCR += 1
			typeinterruption += 3
			tab_interruption = suites_interruption
		else:		
			suites_interruption = tabcomplexe2[nbinterruptionsCL]
			nb_interruptionsCL = len(tabcomplexe2[nbinterruptionsCL])
			nbinterruptionsCL += 1
			typeinterruption += 4
			tab_interruption = suites_interruption


chiffrenoir = exp.get_file(u'chiffrenoir.jpg')
croix_pleine = exp.get_file(u'croix.png')
croix_vide = exp.get_file(u'vide.png')
while index != 0:
	en_colonne=False
	
	button, position, timestamp = my_mouse.get_click(timeout=100)
	if position != None:
		x, y = position
	else:
		x = -1
		y = -1

	if x>=-641 and x<-557 and y>=-527 and y<-470 and total_time > 1000:
			index = 0
			
	if x>=-653 and x<-638 and y>=-442 and y<-426:
		y = -440
		index = 1
		en_colonne=True

	if x>=-653 and x<-638 and y>=-408 and y<-393:
		y = -408
		index = 2
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-376	and y<-360:
		y = -374
		index = 3
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-343 and y<-326:
		y = -341
		index = 4
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-310 and y<-293:
		y = -308
		index = 5
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-277 and y<-261:
		y = -275
		index = 6
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-244 and y<-227:
		y = -242
		index = 7
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-211 and y<-195:
		y = -210
		index = 8
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-178 and y<-162:
		y = -177
		index = 9
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-145 and y<-128:
		y = -144
		index = 10
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-112 and y<-95:
		y = -111
		index = 11
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-79 and y<-63:
		y = -79
		index = 12
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-46 and y<-30:
		y = -46
		index = 13
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=-14 and y<3:
		y = -12
		index = 14
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=19	and y<36:
		y = 21
		index = 15
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=52 and y<69:
		y = 53
		index = 16
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=86 and y<103:
		y = 86
		index = 17
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=118 and y<135:
		y = 119
		index = 18
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=151 and y<168:
		y = 152
		index = 19
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=184 and y<201:
		y = 185
		index = 20
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=219 and y<234:
		y = 219
		index = 21
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=250 and y<268:
		y = 251
		index = 22
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=284 and y<301:
		y = 284
		index = 23
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=316 and y<332:
		y = 317
		index = 24
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=350 and y<365:
		y = 351
		index = 25
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=382 and y<399:
		y = 383
		index = 26
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=415 and y<432:
		y = 416
		index = 27
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=448 and y<465:
		y = 449
		index = 28
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=481 and y<497:
		y = 482
		index = 29
		en_colonne=True
		
	if x>=-653 and x<-638 and y>=514 and y<530:
		y=515
		index = 30
		en_colonne=True
		
		
	if is_interruption:
		key, end_time = my_keyboard.get_key(timeout=3000)
		if key != None:
			if len(chiffres_tapes) < (2*longueur_demande + 3):
				chiffres_a_afficher += key
				chiffres_tapes += key + ","
				my_canvas.text(chiffres_a_afficher,x=66,y=-250,color="black", center=False)
				my_canvas.show()
		else:
			self.log(chiffres_tapes)
			current_interruption += 1
									
			if typeinterruption == 1 and current_interruption < nb_interruptionsSR:
				suite_generee = create_interruption(current_interruption, tab_interruption[current_interruption])
				int_start_time = self.time()
				chiffres_tapes = ",,,"
				chiffres_a_afficher = ""
			elif typeinterruption == 2 and current_interruption < nb_interruptionsSL:
				suite_generee = create_interruption(current_interruption, tab_interruption[current_interruption])
				int_start_time = self.time()
				chiffres_tapes = ",,,"
				chiffres_a_afficher = ""
			elif typeinterruption == 3 and current_interruption < nb_interruptionsCR:
				suite_generee = create_interruption(current_interruption, tab_interruption[current_interruption])
				int_start_time = self.time()
				chiffres_tapes = ",,,"
				chiffres_a_afficher = ""
			elif typeinterruption == 4 and current_interruption < nb_interruptionsCL:
				suite_generee = create_interruption(current_interruption, tab_interruption[current_interruption])
				int_start_time = self.time()
				chiffres_tapes = ",,,"
				chiffres_a_afficher = ""				
				
			else:
				eyetracker.log("Intfin")
				is_interruption = False
				temoin_rl = True
				interr0 = 1
				rl = self.time()
				start_time = self.time()
				rl_start_time = self.time()
				my_canvas.image(exp.get_file(self.get("Image")), y=-540, x=-960, center=False)
				my_canvas.show()				
				if cases[0] == 1:
					my_canvas.image(croix_pleine, y=-440, x=-652, center=False)
					my_canvas.show()
				if cases[1] == 1:
					my_canvas.image(croix_pleine, y=-408, x=-652, center=False)
					my_canvas.show()
				if cases[2] == 1:
					my_canvas.image(croix_pleine, y=-374, x=-652, center=False)
					my_canvas.show()
				if cases[3] == 1:
					my_canvas.image(croix_pleine, y=-341, x=-652, center=False)
					my_canvas.show()
				if cases[4] == 1:
					my_canvas.image(croix_pleine, y=-308, x=-652, center=False)
					my_canvas.show()
				if cases[5] == 1:
					my_canvas.image(croix_pleine, y=-275, x=-652, center=False)
					my_canvas.show()
				if cases[6] == 1:
					my_canvas.image(croix_pleine, y=-242, x=-652, center=False)
					my_canvas.show()
				if cases[7] == 1:
					my_canvas.image(croix_pleine, y=-210, x=-652, center=False)
					my_canvas.show()
				if cases[8] == 1:
					my_canvas.image(croix_pleine, y=-177, x=-652, center=False)
					my_canvas.show()
				if cases[9] == 1:
					my_canvas.image(croix_pleine, y=-144, x=-652, center=False)
					my_canvas.show()
				if cases[10] == 1:
					my_canvas.image(croix_pleine, y=-111, x=-652, center=False)
					my_canvas.show()
				if cases[11] == 1:
					my_canvas.image(croix_pleine, y=-79, x=-652, center=False)
					my_canvas.show()
				if cases[12] == 1:
					my_canvas.image(croix_pleine, y=-46, x=-652, center=False)
					my_canvas.show()
				if cases[13] == 1:
					my_canvas.image(croix_pleine, y=-12, x=-652, center=False)
					my_canvas.show()
				if cases[14] == 1:
					my_canvas.image(croix_pleine, y=21, x=-652, center=False)
					my_canvas.show()
				if cases[15] == 1:
					my_canvas.image(croix_pleine, y=53, x=-652, center=False)
					my_canvas.show()
				if cases[16] == 1:
					my_canvas.image(croix_pleine, y=86, x=-652, center=False)
					my_canvas.show()
				if cases[17] == 1:
					my_canvas.image(croix_pleine, y=119, x=-652, center=False)
					my_canvas.show()
				if cases[18] == 1:
					my_canvas.image(croix_pleine, y=152, x=-652, center=False)
					my_canvas.show()
				if cases[19] == 1:
					my_canvas.image(croix_pleine, y=185, x=-652, center=False)
					my_canvas.show()
				if cases[20] == 1:
					my_canvas.image(croix_pleine, y=219, x=-652, center=False)
					my_canvas.show()
				if cases[21] == 1:
					my_canvas.image(croix_pleine, y=251, x=-652, center=False)
					my_canvas.show()
				if cases[22] == 1:
					my_canvas.image(croix_pleine, y=284, x=-652, center=False)
					my_canvas.show()
				if cases[23] == 1:
					my_canvas.image(croix_pleine, y=317, x=-652, center=False)
					my_canvas.show()
				if cases[24] == 1:
					my_canvas.image(croix_pleine, y=351, x=-652, center=False)
					my_canvas.show()
				if cases[25] == 1:
					my_canvas.image(croix_pleine, y=383, x=-652, center=False)
					my_canvas.show()
				if cases[26] == 1:
					my_canvas.image(croix_pleine, y=416, x=-652, center=False)
					my_canvas.show()
				if cases[27] == 1:
					my_canvas.image(croix_pleine, y=449, x=-652, center=False)
					my_canvas.show()
				if cases[28] == 1:
					my_canvas.image(croix_pleine, y=482, x=-652, center=False)
					my_canvas.show()
				if cases[29] == 1:
					my_canvas.image(croix_pleine, y=515, x=-652, center=False)
					my_canvas.show()
			
	else:
		if index==0:
			if interr0 == 1:
				interr0 = 0
				rl2 = self.time() - start_time
			total_time += self.time() - start_time
			self.log(",Poubelle," + str(self.time() - start_time))
			src = exp.get_file('corbeilleXP.wav')
			my_sampler = sampler(exp, src)
			my_sampler.play()
			if temoin_rl:
				temoin_rl = False
				rl = self.time() - rl_start_time
		else:
			if en_colonne:
				if cases[index-1] == 0:
					cases[index-1] = 1
					good_clics += 1
					croix = croix_pleine
				else:
					good_clics -= 1
					cases[index-1] = 0
					croix = croix_vide
				my_canvas.image(croix, y=y, x=-652, center=False)
				my_canvas.show()
				if interr0 == 1:
					interr0 = 0
					rl2 = self.time() - start_time
				total_time += self.time() - start_time
				self.log("," + str(index) + "," + str(self.time() - start_time))
				start_time = self.time()
				
				if good_clics == clics_attendus and Interruption == True:
					eyetracker.log("Intdebut")
					self.sleep(250)
					nbinterruptions2 += 1
					is_interruption = True
					src = exp.get_file('alerte2.wav')
					my_sampler = sampler(exp, src)
					my_sampler.play()
					my_canvas.image(exp.get_file('fond.png'),y=-540,x=-960, center=False)
					my_canvas.show()
					my_canvas.image(exp.get_file('Popupfond.png'),y=-530,x=-654, center=False)
					my_canvas.show()		
					my_canvas.rect(-634,-510, 600,1028, color = "black", fill = True)
					my_canvas.show()		
					my_canvas.rect(-34,-510, 606, 1028, color = "grey", fill = True)
					my_canvas.show()
					my_canvas.text("Votre reponse :",x=26, y=-340,color="black",center=False)
					my_canvas.show()
					my_canvas.rect(26,-290,200,100, color="black",fill=True)
					my_canvas.show()
					my_canvas.text("Rappelez les 3 derniers chiffres",x=-500,y=-490, max_width=600, color="white", center=False)
					my_canvas.show()
					self.sleep(250)			
					my_keyboard.flush()
					create_interruption(0, tab_interruption[0])


					int_start_time = self.time()
					
				if temoin_rl:
					temoin_rl = False

self.log("Nb de clic,"+str(clics_attendus))
self.log("TOT," + str(total_time))
if Interruption == True:
	self.log("RL," + str(rl2))
self.log("")

nbessai += 1
nbessai2 = 30 - nbessai

Fondnoir1 = exp.get_file("fond noir.jpg")
my_canvas.image(Fondnoir1, y=-540, x=-960, center=False)
my_canvas.show()
my_canvas.text('Vous pouvez cligner des yeux', center=True, x=0, y=0, color= u'white')
my_canvas.show()

if nbessai2 > 1:
	my_canvas.text('Nombre d\'essais restants : '+str(nbessai2), center=True, x=0, y=30, color= u'white')
	my_canvas.show()
	
if nbessai2 == 1:
	my_canvas.text('Nombre d\'essai restant : '+str(nbessai2), center=True, x=0, y=30, color= u'white')
	my_canvas.show()



self.sleep(2500)
