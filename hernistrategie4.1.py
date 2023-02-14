#Herní indexy : 1-Voják, 2-Tank, 3-Naklaďák
import os
import time

class Prvnilinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None

class Druhalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None

class Tretilinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None			

class Ctvrtalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None			

class Patalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None		

class Sestalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.brneni = 0
		self.brneni_g = "       "
		self.pozkozeni = None									

class Modrytym:
	def __init__(self):
		self.nazev = None
		self.kredit = 0
		self.lekarnicky = 0	
		self.aktualni_pozkozeni = None
		self.stav = None

#Obsahuje Linie : 1. , 2. , 3.		

class Cervenytym:
	def __init__(self):
		self.nazev = None
		self.kredit = 0
		self.lekarnicky = 0	
		self.aktualni_pozkozeni = None
		self.stav = None

#Obsahuje Linie : 4. , 5. , 6.	

prvnilinie = Prvnilinie()
druhalinie = Druhalinie()
tretilinie = Tretilinie()
ctvrtalinie = Ctvrtalinie()
patalinie = Patalinie()
sestalinie = Sestalinie()
modrytym = Modrytym()
cervenytym = Cervenytym()

modrytym.kredit = 1000
modrytym.lekarnicky = 0
cervenytym.kredit = 1000
cervenytym.lekarnicky = 0
modrytym.stav = "Stav je vyrovnaný"
cervenytym.stav = "Stav je vyrovnaný"

konec_aplikace = 0

while True:
	os.system('cls')
	print("")
	print("  _                     _     _             _             _                    ")
	print(" | |__   ___ _ __ _ __ (_)___| |_ _ __ __ _| |_ ___  __ _(_) ___   _ __  _   _ ")
	print(" | '_ \ / _ \ '__| '_ \| / __| __| '__/ _` | __/ _ \/ _` | |/ _ \ | '_ \| | | |")
	print(" | | | |  __/ |  | | | | \__ \ |_| | | (_| | ||  __/ (_| | |  __/_| |_) | |_| |")
	print(" |_| |_|\___|_|  |_| |_|_|___/\__|_|  \__,_|\__\___|\__, |_|\___(_) .__/ \__, |")
	print("                                                    |___/         |_|    |___/ ")
	print("                                                                               ")
	print("                                                                               ")
	print("                                                                               ")
	print("                                                                               ")
	print("                                   START HRY                                   ")
	print("                                      ->start<-                                ")
	print("                                                                               ")
	print("                                 NASTAVENÍ HRY                                 ")
	print("                                    ->nastaveni<-                              ")
	print("                                                                               ")
	print("                                   KONEC HRY                                   ")
	print("                                      ->konec<-                                ")
	print("                                                                               ")
	print("                                                                               ")
	print("                                                                               ")
	print("                                                                               ")
	print(" 4.1                                                      BetovecIndustries2019")
	menu = (input(""))
	if menu == "start":
		os.system('cls')
		modrytym.nazev = (input("Zadejte název prvního týmu : "))
		cervenytym.nazev = (input("Zadejte název druhého týmu: "))
		break
	elif menu == "nastaveni":
		while True:
			if modrytym.kredit == cervenytym.kredit:
				stav_kredit = "Stav kreditů je vyrovnaný" 
				modrytym.stav = "Stav je vyrovnaný"
				cervenytym.stav = "Stav je vyrovnaný"
			elif modrytym.kredit > cervenytym.kredit:
				stav_kredit = "Ve výhodě je hráč 1"
				modrytym.stav = "Tento tým je ve výhodě"
				cervenytym.stav = "Tento tým je v nevýhodě"
			elif modrytym.kredit < cervenytym.kredit:
				stav_kredit = "Ve výhodě je hráč 2"	
				modrytym.stav = "Tento tým je v nevýhodě"
				cervenytym.stav = "Tento tým je ve výhodě"
			if modrytym.lekarnicky == cervenytym.lekarnicky:
				stav_lekarnicky = "Stav lékárniček je vyrovnaný" 
			elif modrytym.lekarnicky > cervenytym.lekarnicky:
				stav_lekarnicky = "Ve výhodě je hráč 1"
			elif modrytym.lekarnicky < cervenytym.lekarnicky:
				stav_lekarnicky = "Ve výhodě je hráč 2"
			else:
				stav_kredit = "Hra nefunguje správně"			
			os.system('cls')
			print("")
			print("  _   _           _                        __                                  ")
			print(" | \ | | __ _____| |  __ ___   _____   __ /_/                                  ")
			print(" | . ` |/ _` / __| __/ _` \ \ / / _ \ '_ \| |                                  ")
			print(" | |\  | (_| \__ \ || (_| |\ V /  __/ | | | |                                  ")
			print(" |_| \_|\__,_|___/\__\__,_| \_/ \___|_| |_|_|                                  ")                      
			print(" | |         /_/  \__/      /_ |                                               ")
			print(" | |__  _ __ __ _  ___ ___   | |                                               ")
			print(" | '_ \| '__/ _` |/ __/ _ \  | |    KREDITY TÝMU: ", modrytym.kredit," ")
			print(" | | | | | | (_| | (_|  __/  | |           PŘIDAT 1000$ ->pridatkredit<-       ")
			print(" |_| |_|_|  \__,_|\___\___|  |_|           ODEBRAT 1000$ ->odebratkredit<-     ")
			print("                                                                               ")
			print("                                    LÉKÁRNIČKY TÝMU: ", modrytym.lekarnicky," ")
			print("                                           PŘIDAT LÉKÁRNIČKU ->pridatlekar<-   ")
			print("                                           ODEBRAT LÉKÁRNIČKU ->odebratlekar<- ")
			print("                                                                               ")
			print("       STAV:                                                                   ")
			print("       Kredity: ", stav_kredit)
			print("                                                                               ")
			print("       Lékárničky: ", stav_lekarnicky)
			print("                                                                               ")
			print("     HRÁČ2 ->hrac<-       ZPĚT DO MENU ->konec<-                               ")
			print("                                                                               ")
			print("                                                          BetovecIndustries2018")
			hrac1 = (input(""))
			if hrac1 == "pridatkredit":
				modrytym.kredit += 1000
			elif hrac1 == "odebratkredit":
				modrytym.kredit -= 1000
				if modrytym.kredit > 0:
					modrytym.kredit = 0
			elif hrac1 == "pridatlekar":
				modrytym.lekarnicky += 1
			elif hrac1 == "odebratlekar":
				modrytym.lekarnicky -= 1
				if modrytym.lekarnicky < 0:
					modrytym.lekarnicky = 0	
			elif hrac1 == "hrac":
				while True:
					if modrytym.kredit == cervenytym.kredit:
						stav_kredit = "Stav kreditů je vyrovnaný" 
						modrytym.stav = "Stav je vyrovnaný"
						cervenytym.stav = "Stav je vyrovnaný"
					elif modrytym.kredit > cervenytym.kredit:
						stav_kredit = "Ve výhodě je hráč 1"
						modrytym.stav = "Tento tým je ve výhodě"
						cervenytym.stav = "Tento tým je v nevýhodě"
					elif modrytym.kredit < cervenytym.kredit:
						stav_kredit = "Ve výhodě je hráč 2"	
						modrytym.stav = "Tento tým je v nevýhodě"
						cervenytym.stav = "Tento tým je ve výhodě"
					if modrytym.lekarnicky == cervenytym.lekarnicky:
						stav_lekarnicky = "Stav lékárniček je vyrovnaný" 
					elif modrytym.lekarnicky > cervenytym.lekarnicky:
						stav_lekarnicky = "Ve výhodě je hráč 1"
					elif modrytym.lekarnicky < cervenytym.lekarnicky:
						stav_lekarnicky = "Ve výhodě je hráč 2"		
					os.system('cls')
					print("")
					print("  _   _           _                        __                                  ")
					print(" | \ | | __ _____| |  __ ___   _____   __ /_/                                  ")
					print(" | . ` |/ _` / __| __/ _` \ \ / / _ \ '_ \| |                                  ")
					print(" | |\  | (_| \__ \ || (_| |\ V /  __/ | | | |                                  ")
					print(" |_| \_|\__,_|___/\__\__,_| \_/_\___|_| |_|_|                                  ") 
					print(" | |         /_/  \__/      |__ \                                              ")
					print(" | |__  _ __ __ _  ___ ___     ) |                                             ")
					print(" | '_ \| '__/ _` |/ __/ _ \   / /   KREDITY TÝMU: ", cervenytym.kredit," ")
					print(" | | | | | | (_| | (_|  __/  / /_          PŘIDAT 1000$ ->pridatkredit<-       ")
					print(" |_| |_|_|  \__,_|\___\___| |____|         ODEBRAT 1000$ ->odebratkredit<-     ")
					print("                                                                               ")
					print("                                    LÉKÁRNIČKY TÝMU: ", cervenytym.lekarnicky," ")
					print("                                           PŘIDAT LÉKÁRNIČKU ->pridatlekar<-   ")
					print("                                           ODEBRAT LÉKÁRNIČKU ->odebratlekar<- ")
					print("                                                                               ")
					print("       STAV:                                                                   ")
					print("       Kredity: ", stav_kredit)
					print("                                                                               ")
					print("       Lékárničky: ", stav_lekarnicky)
					print("                                                                               ")
					print("                                                                               ")
					print("     HRÁČ1 ->hrac<-                                                            ")
					print("                                                                               ")
					print("                                                          BetovecIndustries2018")
					hrac2 = (input(""))
					if hrac2 == "pridatkredit":
						cervenytym.kredit += 1000
					elif hrac2 == "odebratkredit":
						cervenytym.kredit -= 1000
						if cervenytym.kredit > 0:
							cervenytym.kredit = 0
					elif hrac2 == "pridatlekar":
						cervenytym.lekarnicky += 1
					elif hrac2 == "odebratlekar":
						cervenytym.lekarnicky -= 1
						if cervenytym.lekarnicky < 0:
							cervenytym.lekarnicky = 0
					elif hrac2 == "hrac":
						break		
					else: 
						continue
			elif hrac1 == "konec":		
				break								
			else:
				continue	
	elif menu == "konec":
		konec_aplikace = 1
		break							
	else:
		continue

###############################################################################

prvnilinie.herni_index = 1
prvnilinie.vitalita = 3
ctvrtalinie.herni_index = 1
ctvrtalinie.vitalita = 3
prvnilinie.brneni = 0
druhalinie.brneni = 0
tretilinie.brneni = 0
ctvrtalinie.brneni = 0
patalinie.brneni = 0
sestalinie.brneni = 0

while True:
	if konec_aplikace == 1:
		break
	elif prvnilinie.herni_index == 0:
		prvnilinie.grafika_1 = "        "
		prvnilinie.grafika_2 = "        "
		prvnilinie.grafika_3 = "        "
		prvnilinie.vitalita = 0
		prvnilinie.vitalita_g = "         "
		prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 0
	elif prvnilinie.herni_index == 1:
		prvnilinie.grafika_1 = "   O    "
		prvnilinie.grafika_2 = "  /:\   "
		prvnilinie.grafika_3 = "  / \   "
		if prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "▄ ▄ ▄    "
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "▄ ▄      "
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "▄        "		
		if prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "▄      "
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 1	
	elif prvnilinie.herni_index == 2:
		prvnilinie.grafika_1 = " _/-\==="
		prvnilinie.grafika_2 = ":     \ "
		prvnilinie.grafika_3 = "\O-O-O/ "
		if prvnilinie.vitalita == 4:
			prvnilinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "▄ ▄ ▄    "
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "▄ ▄      "
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "▄        "
		if prvnilinie.brneni == 2: 
			prvnilinie.brneni_g = "▄ ▄    "	
		elif prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "▄      "
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 2
	elif prvnilinie.herni_index == 3:
		prvnilinie.grafika_1 = ".---._  "
		prvnilinie.grafika_2 = ":   : \ "
		prvnilinie.grafika_3 = "´O-O-O/ "
		if prvnilinie.vitalita == 5:
			prvnilinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif prvnilinie.vitalita == 4:
			prvnilinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "▄ ▄ ▄    "
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "▄ ▄      "
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "▄        "
		if prvnilinie.brneni == 3: 
			prvnilinie.brneni_g = "▄ ▄ ▄  "		
		elif prvnilinie.brneni == 2: 
			prvnilinie.brneni_g = "▄ ▄    "	
		elif prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "▄      "
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 3	

	if druhalinie.herni_index == 0:
		druhalinie.grafika_1 = "        "
		druhalinie.grafika_2 = "        "
		druhalinie.grafika_3 = "        "
		druhalinie.vitalita = 0
		druhalinie.vitalita_g = "         "
		druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 0
	elif druhalinie.herni_index == 1:
		druhalinie.grafika_1 = "   O    "
		druhalinie.grafika_2 = "  /:\   "
		druhalinie.grafika_3 = "  / \   "
		if druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "▄ ▄ ▄    "
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "▄ ▄      "
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "▄        "
		if druhalinie.brneni == 1: 
			druhalinie.brneni_g = "▄      "
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 1	
	elif druhalinie.herni_index == 2:
		druhalinie.grafika_1 = " _/-\==="
		druhalinie.grafika_2 = ":     \ "
		druhalinie.grafika_3 = "\O-O-O/ "
		if druhalinie.vitalita == 4:
			druhalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "▄ ▄ ▄    "
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "▄ ▄      "
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "▄        "
		if druhalinie.brneni == 2: 
			druhalinie.brneni_g = "▄ ▄    "	
		elif druhalinie.brneni == 1: 
			druhalinie.brneni_g = "▄      "
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 2
	elif druhalinie.herni_index == 3:
		druhalinie.grafika_1 = ".---._  "
		druhalinie.grafika_2 = ":   : \ "
		druhalinie.grafika_3 = "´O-O-O/ "
		if druhalinie.vitalita == 5:
			druhalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif druhalinie.vitalita == 4:
			druhalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "▄ ▄ ▄    "
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "▄ ▄      "
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "▄        "
		if druhalinie.brneni == 3: 
			druhalinie.brneni_g = "▄ ▄ ▄  "		
		elif druhalinie.brneni == 2: 
			druhalinie.brneni_g = "▄ ▄    "	
		elif druhalinie.brneni == 1: 
			druhalinie.brneni_g = "▄      "
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 3

	if tretilinie.herni_index == 0:
		tretilinie.grafika_1 = "        "
		tretilinie.grafika_2 = "        "
		tretilinie.grafika_3 = "        "
		tretilinie.vitalita = 0
		tretilinie.vitalita_g = "         "
		tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 0
	elif tretilinie.herni_index == 1:
		tretilinie.grafika_1 = "   O    "
		tretilinie.grafika_2 = "  /:\   "
		tretilinie.grafika_3 = "  / \   "
		if tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "▄ ▄ ▄    "
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "▄ ▄      "
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "▄        "
		if tretilinie.brneni == 1: 
			tretilinie.brneni_g = "▄      "
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 1	
	elif tretilinie.herni_index == 2:
		tretilinie.grafika_1 = " _/-\==="
		tretilinie.grafika_2 = ":     \ "
		tretilinie.grafika_3 = "\O-O-O/ "
		if tretilinie.vitalita == 4:
			tretilinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "▄ ▄ ▄    "
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "▄ ▄      "
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "▄        "
		if tretilinie.brneni == 2: 
			tretilinie.brneni_g = "▄ ▄    "	
		elif tretilinie.brneni == 1: 
			tretilinie.brneni_g = "▄      "
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 2
	elif tretilinie.herni_index == 3:
		tretilinie.grafika_1 = ".---._  "
		tretilinie.grafika_2 = ":   : \ "
		tretilinie.grafika_3 = "´O-O-O/ "
		if tretilinie.vitalita == 5:
			tretilinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif tretilinie.vitalita == 4:
			tretilinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "▄ ▄ ▄    "
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "▄ ▄      "
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "▄        "
		if tretilinie.brneni == 3: 
			tretilinie.brneni_g = "▄ ▄ ▄  "		
		elif tretilinie.brneni == 2: 
			tretilinie.brneni_g = "▄ ▄    "	
		elif tretilinie.brneni == 1: 
			tretilinie.brneni_g = "▄      "
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 3

	if ctvrtalinie.herni_index == 0:
		ctvrtalinie.grafika_1 = "        "
		ctvrtalinie.grafika_2 = "        "
		ctvrtalinie.grafika_3 = "        "
		ctvrtalinie.vitalita = 0
		ctvrtalinie.vitalita_g = "         "
		ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 0
	elif ctvrtalinie.herni_index == 1:
		ctvrtalinie.grafika_1 = "   O    "
		ctvrtalinie.grafika_2 = "  /:\   "
		ctvrtalinie.grafika_3 = "  / \   "
		if ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "    ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "      ▄ ▄"
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "        ▄"
		if ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "      ▄"
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 1
	elif ctvrtalinie.herni_index == 2:
		ctvrtalinie.grafika_1 = "===/-\_ "
		ctvrtalinie.grafika_2 = " /     :"
		ctvrtalinie.grafika_3 = " \O-O-O/"
		if ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "    ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "      ▄ ▄"
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "        ▄"
		if ctvrtalinie.brneni == 2: 
			ctvrtalinie.brneni_g = "    ▄ ▄"	
		elif ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "      ▄"
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 2
	elif ctvrtalinie.herni_index == 3:
		ctvrtalinie.grafika_1 = "  _.---."
		ctvrtalinie.grafika_2 = " / :   :"
		ctvrtalinie.grafika_3 = " \O-O-O´"
		if ctvrtalinie.vitalita == 5:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "    ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "      ▄ ▄"
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "        ▄"
		if ctvrtalinie.brneni == 3: 
			ctvrtalinie.brneni_g = "  ▄ ▄ ▄"		
		elif ctvrtalinie.brneni == 2: 
			ctvrtalinie.brneni_g = "    ▄ ▄"	
		elif ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "      ▄"
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "	
		ctvrtalinie.pozkozeni = 3	

	if patalinie.herni_index == 0:
		patalinie.grafika_1 = "        "
		patalinie.grafika_2 = "        "
		patalinie.grafika_3 = "        "
		patalinie.vitalita = 0
		patalinie.vitalita_g = "         "
		patalinie.brneni_g = "       "
		patalinie.pozkozeni = 0
	elif patalinie.herni_index == 1:
		patalinie.grafika_1 = "   O    "
		patalinie.grafika_2 = "  /:\   "
		patalinie.grafika_3 = "  / \   "
		if patalinie.vitalita == 3:
			patalinie.vitalita_g = "    ▄ ▄ ▄"
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "      ▄ ▄"
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "        ▄"
		if patalinie.brneni == 1: 
			patalinie.brneni_g = "      ▄"
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "
		patalinie.pozkozeni = 1
	elif patalinie.herni_index == 2:
		patalinie.grafika_1 = "===/-\_ "
		patalinie.grafika_2 = " /     :"
		patalinie.grafika_3 = " \O-O-O/"
		if patalinie.vitalita == 4:
			patalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "    ▄ ▄ ▄"
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "      ▄ ▄"
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "        ▄"
		if patalinie.brneni == 2: 
			patalinie.brneni_g = "    ▄ ▄"	
		elif patalinie.brneni == 1: 
			patalinie.brneni_g = "      ▄"
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "
		patalinie.pozkozeni = 2
	elif patalinie.herni_index == 3:
		patalinie.grafika_1 = "  _.---."
		patalinie.grafika_2 = " / :   :"
		patalinie.grafika_3 = " \O-O-O´"
		if patalinie.vitalita == 5:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif patalinie.vitalita == 4:
			patalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "    ▄ ▄ ▄"
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "      ▄ ▄"
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "        ▄"
		if patalinie.brneni == 3: 
			patalinie.brneni_g = "  ▄ ▄ ▄"		
		elif patalinie.brneni == 2: 
			patalinie.brneni_g = "    ▄ ▄"	
		elif patalinie.brneni == 1: 
			patalinie.brneni_g = "      ▄"
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "	
		patalinie.pozkozeni = 3		

	if sestalinie.herni_index == 0:
		sestalinie.grafika_1 = "        "
		sestalinie.grafika_2 = "        "
		sestalinie.grafika_3 = "        "
		sestalinie.vitalita = 0
		sestalinie.vitalita_g = "         "
		sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 0	
	elif sestalinie.herni_index == 1:
		sestalinie.grafika_1 = "   O    "
		sestalinie.grafika_2 = "  /:\   "
		sestalinie.grafika_3 = "  / \   "
		if sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "    ▄ ▄ ▄"
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "      ▄ ▄"
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "        ▄"
		if sestalinie.brneni == 1: 
			sestalinie.brneni_g = "      ▄"
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 1	
	elif sestalinie.herni_index == 2:
		sestalinie.grafika_1 = "===/-\_ "
		sestalinie.grafika_2 = " /     :"
		sestalinie.grafika_3 = " \O-O-O/"
		if sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "    ▄ ▄ ▄"
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "      ▄ ▄"
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "        ▄"
		if sestalinie.brneni == 2: 
			sestalinie.brneni_g = "    ▄ ▄"	
		elif sestalinie.brneni == 1: 
			sestalinie.brneni_g = "      ▄"
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 2
	elif sestalinie.herni_index == 3:
		sestalinie.grafika_1 = "  _.---."
		sestalinie.grafika_2 = " / :   :"
		sestalinie.grafika_3 = " \O-O-O´"
		if sestalinie.vitalita == 5:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "    ▄ ▄ ▄"
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "      ▄ ▄"
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "        ▄"
		if sestalinie.brneni == 3: 
			sestalinie.brneni_g = "  ▄ ▄ ▄"		
		elif sestalinie.brneni == 2: 
			sestalinie.brneni_g = "    ▄ ▄"	
		elif sestalinie.brneni == 1: 
			sestalinie.brneni_g = "      ▄"
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "	
		sestalinie.pozkozeni = 3	

	modrytym.aktualni_pozkozeni = (prvnilinie.pozkozeni + druhalinie.pozkozeni + tretilinie.pozkozeni)
	cervenytym.aktualni_pozkozeni = (ctvrtalinie.pozkozeni + patalinie.pozkozeni + sestalinie.pozkozeni)		


	os.system('cls')
	print("Právě hraje tým", modrytym.nazev, "| Kredity:" , modrytym.kredit, "| Lékárničky:", modrytym.lekarnicky, "|", modrytym.stav)  
	print("-----------------------------------------------------------")
	print(" _   _   _   _                                                 _   _   _   _ ")
	print("| |_| |_| |_| |                                               | |_| |_| |_| |")
	print("|             |                                               |             |")
	print("|  ", prvnilinie.grafika_1, " |", " ", "Pozice:", "1.", "                           ", "4.", " ", "| ", ctvrtalinie.grafika_1, "  |")
	print("|  ", prvnilinie.grafika_2, " |", " ", "Vitalita:", prvnilinie.vitalita_g, "           ", ctvrtalinie.vitalita_g, " ", "| ", ctvrtalinie.grafika_2, "  |")
	print("|  ", prvnilinie.grafika_3, " |", " ", "Brnění:", prvnilinie.brneni_g, "                 ", ctvrtalinie.brneni_g, " ", "| ", ctvrtalinie.grafika_3, "  |")
	print("|             |                                               |             |")
	print("|             |                                               |             |")
	print("|  ", druhalinie.grafika_1, " |", " ", "Pozice:", "2.", "                           ", "5.", " ", "| ", patalinie.grafika_1, "  |")
	print("|  ", druhalinie.grafika_2, " |", " ", "Vitalita:", druhalinie.vitalita_g, "           ", patalinie.vitalita_g, " ", "| ", patalinie.grafika_2, "  |")
	print("|  ", druhalinie.grafika_3, " |", " ", "Brnění:", druhalinie.brneni_g, "                 ", patalinie.brneni_g, " ", "| ", patalinie.grafika_3, "  |")
	print("|             |                                               |             |")
	print("|             |                                               |             |")
	print("|  ", tretilinie.grafika_1, " |", " ", "Pozice:", "3.", "                           ", "6.", " ", "| ", sestalinie.grafika_1, "  |")
	print("|  ", tretilinie.grafika_2, " |", " ", "Vitalita:", tretilinie.vitalita_g, "           ", sestalinie.vitalita_g, " ", "| ", sestalinie.grafika_2, "  |")
	print("|  ", tretilinie.grafika_3, " |", " ", "Brnění:", tretilinie.brneni_g, "                 ", sestalinie.brneni_g, " ", "| ", sestalinie.grafika_3, "  |")

	print(" ____________      ____________      ____________ ")
	print("|            |    |            |    |            |")
	print("|   OBCHOD   |    |    ÚTOK    |    |  UZDRAVIT  |")
	print("|            |    |            |    |            |")
	print("| ->obchod<- |    |  ->utok<-  |    |->uzdravit<-|")
	print("|____________|    |____________|    |____________|")
	krok = (input("Váš další krok: "))

	if krok == "obchod":
		os.system('cls')
		print("Kredity:", modrytym.kredit, "$")  
		print(" _   _   _   _                                                 _   _   _   _ ")
		print("| |_| |_| |_| |                                               | |_| |_| |_| |")
		print("|             |                                               |             |")
		print("|  ", prvnilinie.grafika_1, " |", " ", "Pozice:", "1.", "                           ", "4.", " ", "| ", ctvrtalinie.grafika_1, "  |")
		print("|  ", prvnilinie.grafika_2, " |", " ", "Vitalita:", prvnilinie.vitalita_g, "           ", ctvrtalinie.vitalita_g, " ", "| ", ctvrtalinie.grafika_2, "  |")
		print("|  ", prvnilinie.grafika_3, " |", " ", "Brnění:", prvnilinie.brneni_g, "                 ", ctvrtalinie.brneni_g, " ", "| ", ctvrtalinie.grafika_3, "  |")
		print("|             |                                               |             |")
		print("|             |                                               |             |")
		print("|  ", druhalinie.grafika_1, " |", " ", "Pozice:", "2.", "                           ", "5.", " ", "| ", patalinie.grafika_1, "  |")
		print("|  ", druhalinie.grafika_2, " |", " ", "Vitalita:", druhalinie.vitalita_g, "           ", patalinie.vitalita_g, " ", "| ", patalinie.grafika_2, "  |")
		print("|  ", druhalinie.grafika_3, " |", " ", "Brnění:", druhalinie.brneni_g, "                 ", patalinie.brneni_g, " ", "| ", patalinie.grafika_3, "  |")
		print("|             |                                               |             |")
		print("|             |                                               |             |")
		print("|  ", tretilinie.grafika_1, " |", " ", "Pozice:", "3.", "                           ", "6.", " ", "| ", sestalinie.grafika_1, "  |")
		print("|  ", tretilinie.grafika_2, " |", " ", "Vitalita:", tretilinie.vitalita_g, "           ", sestalinie.vitalita_g, " ", "| ", sestalinie.grafika_2, "  |")
		print("|  ", tretilinie.grafika_3, " |", " ", "Brnění:", tretilinie.brneni_g, "                 ", sestalinie.brneni_g, " ", "| ", sestalinie.grafika_3, "  |")

		print(" ____________     ____________     ____________     ____________  ")
		print("|     O      |   |   _/-\===  |   |  .---._    |   |  ________  |")
		print("|    /:\     |   |  :     \   |   |  :   : \   |   | |  |__|  | |")
		print("|    / \     |   |  \O-O-O/   |   |  ´O-O-O/   |   | |________| |")
		print("|   [500$]   |   |  [1000$]   |   |  [1500$]   |   |   [500$]   |")
		print("| ->vojak<-  |   |  ->tank<-  |   |->vozidlo<- |   |  ->lekar<- |")
		print("|____________|   |____________|   |____________|   |____________|")
		obchod = (input("Zadejte vaši objednávku: "))
		if obchod == "vojak":
			os.system('cls')
			if modrytym.kredit <= 499:
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if prvnilinie.herni_index >= 1:
					if druhalinie.herni_index >= 1:
						if tretilinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							time.sleep(1)
							os.system('cls')
						else:
							modrytym.kredit -= 500
							tretilinie.herni_index = 1	
							tretilinie.vitalita = 3
					else:
						modrytym.kredit -= 500
						druhalinie.herni_index = 1	
						druhalinie.vitalita = 3
				else:
					modrytym.kredit -= 500
					prvnilinie.herni_index = 1	
					prvnilinie.vitalita = 3	
		elif obchod == "tank":
			if modrytym.kredit <= 999:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if prvnilinie.herni_index >= 1:
					if druhalinie.herni_index >= 1:
						if tretilinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							os.system('cls')
						else:
							modrytym.kredit -= 1000
							tretilinie.herni_index = 2	
							tretilinie.vitalita = 4
					else:
						modrytym.kredit -= 1000
						druhalinie.herni_index = 2
						druhalinie.vitalita = 4	

				else:
					modrytym.kredit -= 1000
					prvnilinie.herni_index = 2
					prvnilinie.vitalita = 4

		elif obchod == "vozidlo":
			if modrytym.kredit <= 1499:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if prvnilinie.herni_index >= 1:
					if druhalinie.herni_index >= 1:
						if tretilinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							time.sleep(1)
							os.system('cls')
						else:
							modrytym.kredit -= 1500
							tretilinie.herni_index = 3
							tretilinie.vitalita = 5	
					else:
						modrytym.kredit -= 1500
						druhalinie.herni_index = 3	
						druhalinie.vitalita = 5	
				else:
					modrytym.kredit -= 1500
					prvnilinie.herni_index = 3
					prvnilinie.vitalita = 5		
		elif obchod == "lekar":
			if modrytym.kredit <= 499:
				os.system('cls')
				print("Nemáš dostatek kreditů- Ztrácíš tah")
				time.sleep(1)	
				os.system('cls')
			else:
				modrytym.kredit -=500
				modrytym.lekarnicky += 1			
		else:
			os.system('cls')
			print("Neplatná volba - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')		
	elif krok == "utok":
		utok = (input("Zadejte pozici nakterou útočíš: "))
		if utok == "4":
			ctvrtalinie.vitalita = ctvrtalinie.vitalita - modrytym.aktualni_pozkozeni
		elif utok == "5":
			patalinie.vitalita = patalinie.vitalita - modrytym.aktualni_pozkozeni
		elif utok == "6":
			sestalinie.vitalita = sestalinie.vitalita - modrytym.aktualni_pozkozeni
		elif utok == "1":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		elif utok == "2":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		elif utok == "3":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		else:
			os.system('cls')
			print("Neplatná volba - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')	 
	elif krok == "uzdravit":
		if modrytym.lekarnicky >= 1:
			uzdravit = (input("Zadejte číslo vojáka kterého chcete vyléčit: "))
			if uzdravit == "1":
				if prvnilinie.herni_index == 1:
					prvnilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if prvnilinie.vitalita > 3:
						prvnilinie.vitalita = 3
				elif prvnilinie.herni_index == 2:
					prvnilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if prvnilinie.vitalita > 4:
						prvnilinie.vitalita = 4
				elif prvnilinie.herni_index == 3:
					prvnilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if prvnilinie.vitalita > 5:
						prvnilinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")
					time.sleep(1)
					os.system('cls')	
			elif uzdravit == "2":
				if druhalinie.herni_index == 1:
					druhalinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if druhalinie.vitalita > 3:
						druhalinie.vitalita = 3
				elif druhalinie.herni_index == 2:
					druhalinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if druhalinie.vitalita > 4:
						druhalinie.vitalita = 4
				elif druhalinie.herni_index == 3:
					druhalinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if druhalinie.vitalita > 5:
						druhalinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")
					time.sleep(1)
					os.system('cls')
			elif uzdravit == "3":
				if tretilinie.herni_index == 1:
					tretilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if tretilinie.vitalita > 3:
						tretilinie.vitalita = 3
				elif tretilinie.herni_index == 2:
					tretilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if tretilinie.vitalita > 4:
						tretilinie.vitalita = 4
				elif tretilinie.herni_index == 3:
					tretilinie.vitalita += 3
					modrytym.lekarnicky -= 1
					if tretilinie.vitalita > 5:
						tretilinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")
					time.sleep(1)
					os.system('cls')	
			elif uzdravit == "4":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			elif uzdravit == "5":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			elif uzdravit == "6":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
		else:
			os.system('cls')
			print("Nemáš dostatek lékárniček - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
	elif krok == "konec":
		konec = (input("Skutečně se chcete vzdát ? (A/N): ")) 	
		if konec == "N":
			os.system('cls')
			print("Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
			break
		else:
			prvnilinie.herni_index = 0
			druhalinie.herni_index = 0
			tretilinie.herni_index = 0
			break		
	elif krok == ";cheat":
		os.system('cls')
		print("Vítejte v cheat menu")
		cheat = (input("Zadejte název cheatu : ")) 
		if cheat == "kredit":
			modrytym.kredit += 1000
		elif cheat == "lekarnicky":
			modrytym.lekarnicky += 5	
		else:
			break					
	else:
		os.system('cls')
		print("Neplatná volba - Ztrácíš tah")
		time.sleep(1)		
		os.system('cls')

	if ctvrtalinie.vitalita <= 0:
		if ctvrtalinie.herni_index == 1:
			modrytym.kredit += 250
			ctvrtalinie.herni_index = 0
		if ctvrtalinie.herni_index == 2:
			modrytym.kredit += 500
			ctvrtalinie.herni_index = 0
		if ctvrtalinie.herni_index == 3:
			modrytym.kredit += 1000		
			ctvrtalinie.herni_index = 0		
	elif patalinie.vitalita <= 0:
		if patalinie.herni_index == 1:
			modrytym.kredit += 250
			patalinie.herni_index = 0
		if patalinie.herni_index == 2:
			modrytym.kredit += 500
			patalinie.herni_index = 0
		if patalinie.herni_index == 3:
			modrytym.kredit += 1000		
			patalinie.herni_index = 0		
	elif sestalinie.vitalita <= 0:
		if sestalinie.herni_index == 1:
			modrytym.kredit += 250
			sestalinie.herni_index = 0
		if sestalinie.herni_index == 2:
			modrytym.kredit += 500
			sestalinie.herni_index = 0
		if sestalinie.herni_index == 3:
			modrytym.kredit += 1000		
			sestalinie.herni_index = 0	

	if ctvrtalinie.herni_index <= 0 and patalinie.herni_index <= 0 and sestalinie.herni_index <= 0:
		break			

	#-------------------------------------------------------------------------------	
	#-------------------------------------------------------------------------------
	#-------------------------------------------------------------------------------
	#-------------------------------------------------------------------------------	
	#-----------------------------HRA HRÁČE 2---------------------------------------

	if prvnilinie.herni_index == 0:
		prvnilinie.grafika_1 = "        "
		prvnilinie.grafika_2 = "        "
		prvnilinie.grafika_3 = "        "
		prvnilinie.vitalita = 0
		prvnilinie.vitalita_g = "         "
		prvnilinie.brneni = "       "
		prvnilinie.pozkozeni = 0
	elif prvnilinie.herni_index == 1:
		prvnilinie.grafika_1 = "   O    "
		prvnilinie.grafika_2 = "  /:\   "
		prvnilinie.grafika_3 = "  / \   "
		if prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "    ▄ ▄ ▄"
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "      ▄ ▄"
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "        ▄"
		if prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "      ▄"
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 1	
	elif prvnilinie.herni_index == 2:
		prvnilinie.grafika_1 = "===/-\_ "
		prvnilinie.grafika_2 = " /     :"
		prvnilinie.grafika_3 = " \O-O-O/"
		if prvnilinie.vitalita == 4:
			prvnilinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "    ▄ ▄ ▄"
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "      ▄ ▄"
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "        ▄"
		if prvnilinie.brneni == 2: 
			prvnilinie.brneni_g = "    ▄ ▄"	
		elif prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "      ▄"
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 2
	elif prvnilinie.herni_index == 3:
		prvnilinie.grafika_1 = "  _.---."
		prvnilinie.grafika_2 = " / :   :"
		prvnilinie.grafika_3 = " \O-O-O´"
		if prvnilinie.vitalita == 5:
			prvnilinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif prvnilinie.vitalita == 4:
			prvnilinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif prvnilinie.vitalita == 3:
			prvnilinie.vitalita_g = "    ▄ ▄ ▄"
		elif prvnilinie.vitalita == 2:
			prvnilinie.vitalita_g = "      ▄ ▄"
		elif prvnilinie.vitalita == 1:
			prvnilinie.vitalita_g = "        ▄"
		if prvnilinie.brneni == 3: 
			prvnilinie.brneni_g = "  ▄ ▄ ▄"		
		elif prvnilinie.brneni == 2: 
			prvnilinie.brneni_g = "    ▄ ▄"	
		elif prvnilinie.brneni == 1: 
			prvnilinie.brneni_g = "      ▄"
		elif prvnilinie.brneni == 0: 
			prvnilinie.brneni_g = "       "
		prvnilinie.pozkozeni = 3	

	if druhalinie.herni_index == 0:
		druhalinie.grafika_1 = "        "
		druhalinie.grafika_2 = "        "
		druhalinie.grafika_3 = "        "
		druhalinie.vitalita = 0
		druhalinie.vitalita_g = "         "
		druhalinie.brneni = "       "
		druhalinie.pozkozeni = 0
	elif druhalinie.herni_index == 1:
		druhalinie.grafika_1 = "   O    "
		druhalinie.grafika_2 = "  /:\   "
		druhalinie.grafika_3 = "  / \   "
		if druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "    ▄ ▄ ▄"
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "      ▄ ▄"
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "        ▄"
		if druhalinie.brneni == 1: 
			druhalinie.brneni_g = "      ▄"
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 1	
	elif druhalinie.herni_index == 2:
		druhalinie.grafika_1 = "===/-\_ "
		druhalinie.grafika_2 = " /     :"
		druhalinie.grafika_3 = " \O-O-O/"
		if druhalinie.vitalita == 4:
			druhalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "    ▄ ▄ ▄"
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "      ▄ ▄"
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "        ▄"
		if druhalinie.brneni == 2: 
			druhalinie.brneni_g = "    ▄ ▄"	
		elif druhalinie.brneni == 1: 
			druhalinie.brneni_g = "      ▄"
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 2
	elif druhalinie.herni_index == 3:
		druhalinie.grafika_1 = "  _.---."
		druhalinie.grafika_2 = " / :   :"
		druhalinie.grafika_3 = " \O-O-O´"
		if druhalinie.vitalita == 5:
			druhalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif druhalinie.vitalita == 4:
			druhalinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif druhalinie.vitalita == 3:
			druhalinie.vitalita_g = "    ▄ ▄ ▄"
		elif druhalinie.vitalita == 2:
			druhalinie.vitalita_g = "      ▄ ▄"
		elif druhalinie.vitalita == 1:
			druhalinie.vitalita_g = "        ▄"
		if druhalinie.brneni == 3: 
			druhalinie.brneni_g = "  ▄ ▄ ▄"		
		elif druhalinie.brneni == 2: 
			druhalinie.brneni_g = "    ▄ ▄"	
		elif druhalinie.brneni == 1: 
			druhalinie.brneni_g = "      ▄"
		elif druhalinie.brneni == 0: 
			druhalinie.brneni_g = "       "
		druhalinie.pozkozeni = 3

	if tretilinie.herni_index == 0:
		tretilinie.grafika_1 = "        "
		tretilinie.grafika_2 = "        "
		tretilinie.grafika_3 = "        "
		tretilinie.vitalita = 0
		tretilinie.vitalita_g = "         "
		tretilinie.brneni = "       "
		tretilinie.pozkozeni = 0
	elif tretilinie.herni_index == 1:
		tretilinie.grafika_1 = "   O    "
		tretilinie.grafika_2 = "  /:\   "
		tretilinie.grafika_3 = "  / \   "
		if tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "    ▄ ▄ ▄"
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "      ▄ ▄"
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "        ▄"
		if tretilinie.brneni == 1: 
			tretilinie.brneni_g = "      ▄"
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 1	
	elif tretilinie.herni_index == 2:
		tretilinie.grafika_1 = "===/-\_ "
		tretilinie.grafika_2 = " /     :"
		tretilinie.grafika_3 = " \O-O-O/"
		if tretilinie.vitalita == 4:
			tretilinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "    ▄ ▄ ▄"
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "      ▄ ▄"
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "        ▄"
		if tretilinie.brneni == 2: 
			tretilinie.brneni_g = "    ▄ ▄"	
		elif tretilinie.brneni == 1: 
			tretilinie.brneni_g = "      ▄"
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 2
	elif tretilinie.herni_index == 3:
		tretilinie.grafika_1 = "  _.---."
		tretilinie.grafika_2 = " / :   :"
		tretilinie.grafika_3 = " \O-O-O´"
		if tretilinie.vitalita == 5:
			tretilinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif tretilinie.vitalita == 4:
			tretilinie.vitalita_g = "  ▄ ▄ ▄ ▄"
		elif tretilinie.vitalita == 3:
			tretilinie.vitalita_g = "    ▄ ▄ ▄"
		elif tretilinie.vitalita == 2:
			tretilinie.vitalita_g = "      ▄ ▄"
		elif tretilinie.vitalita == 1:
			tretilinie.vitalita_g = "        ▄"
		if tretilinie.brneni == 3: 
			tretilinie.brneni_g = "  ▄ ▄ ▄"		
		elif tretilinie.brneni == 2: 
			tretilinie.brneni_g = "    ▄ ▄"	
		elif tretilinie.brneni == 1: 
			tretilinie.brneni_g = "      ▄"
		elif tretilinie.brneni == 0: 
			tretilinie.brneni_g = "       "
		tretilinie.pozkozeni = 3

	if ctvrtalinie.herni_index == 0:
		ctvrtalinie.grafika_1 = "        "
		ctvrtalinie.grafika_2 = "        "
		ctvrtalinie.grafika_3 = "        "
		ctvrtalinie.vitalita = 0
		ctvrtalinie.vitalita_g = "         "
		ctvrtalinie.brneni = "       "
		ctvrtalinie.pozkozeni = 0
	elif ctvrtalinie.herni_index == 1:
		ctvrtalinie.grafika_1 = "   O    "
		ctvrtalinie.grafika_2 = "  /:\   "
		ctvrtalinie.grafika_3 = "  / \   "
		if ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		if ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "▄      "
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 1
	elif ctvrtalinie.herni_index == 2:
		ctvrtalinie.grafika_1 = " _/-\==="
		ctvrtalinie.grafika_2 = ":     \ "
		ctvrtalinie.grafika_3 = "\O-O-O/ "
		if ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		if ctvrtalinie.brneni == 2: 
			ctvrtalinie.brneni_g = "▄ ▄    "	
		elif ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "▄      "
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 2
	elif ctvrtalinie.herni_index == 3:
		ctvrtalinie.grafika_1 = ".---._  "
		ctvrtalinie.grafika_2 = ":   : \ "
		ctvrtalinie.grafika_3 = "´O-O-O/ "
		if ctvrtalinie.vitalita == 5:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		if ctvrtalinie.brneni == 3: 
			ctvrtalinie.brneni_g = "▄ ▄ ▄  "		
		elif ctvrtalinie.brneni == 2: 
			ctvrtalinie.brneni_g = "▄ ▄    "	
		elif ctvrtalinie.brneni == 1: 
			ctvrtalinie.brneni_g = "▄      "
		elif ctvrtalinie.brneni == 0: 
			ctvrtalinie.brneni_g = "       "
		ctvrtalinie.pozkozeni = 3	

	if patalinie.herni_index == 0:
		patalinie.grafika_1 = "        "
		patalinie.grafika_2 = "        "
		patalinie.grafika_3 = "        "
		patalinie.vitalita = 0
		patalinie.vitalita_g = "         "
		patalinie.brneni = "       "
		patalinie.pozkozeni = 0
	elif patalinie.herni_index == 1:
		patalinie.grafika_1 = "   O    "
		patalinie.grafika_2 = "  /:\   "
		patalinie.grafika_3 = "  / \   "
		if patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		if patalinie.brneni == 1: 
			patalinie.brneni_g = "▄      "
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "
		patalinie.pozkozeni = 1
	elif patalinie.herni_index == 2:
		patalinie.grafika_1 = " _/-\==="
		patalinie.grafika_2 = ":     \ "
		patalinie.grafika_3 = "\O-O-O/ "
		if patalinie.vitalita == 4:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		if patalinie.brneni == 2: 
			patalinie.brneni_g = "▄ ▄    "	
		elif patalinie.brneni == 1: 
			patalinie.brneni_g = "▄      "
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "
		patalinie.pozkozeni = 2
	elif patalinie.herni_index == 3:
		patalinie.grafika_1 = ".---._  "
		patalinie.grafika_2 = ":   : \ "
		patalinie.grafika_3 = "´O-O-O/ "
		if patalinie.vitalita == 5:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif patalinie.vitalita == 4:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		if patalinie.brneni == 3: 
			patalinie.brneni_g = "▄ ▄ ▄  "		
		elif patalinie.brneni == 2: 
			patalinie.brneni_g = "▄ ▄    "	
		elif patalinie.brneni == 1: 
			patalinie.brneni_g = "▄      "
		elif patalinie.brneni == 0: 
			patalinie.brneni_g = "       "
		patalinie.pozkozeni = 3		

	if sestalinie.herni_index == 0:
		sestalinie.grafika_1 = "        "
		sestalinie.grafika_2 = "        "
		sestalinie.grafika_3 = "        "
		sestalinie.vitalita = 0
		sestalinie.vitalita_g = "         "
		sestalinie.brneni = "       "
		sestalinie.pozkozeni = 0	
	elif sestalinie.herni_index == 1:
		sestalinie.grafika_1 = "   O    "
		sestalinie.grafika_2 = "  /:\   "
		sestalinie.grafika_3 = "  / \   "
		if sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		if sestalinie.brneni == 1: 
			sestalinie.brneni_g = "▄      "
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 1	
	elif sestalinie.herni_index == 2:
		sestalinie.grafika_1 = " _/-\==="
		sestalinie.grafika_2 = ":     \ "
		sestalinie.grafika_3 = "\O-O-O/ "
		if sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		if sestalinie.brneni == 2: 
			sestalinie.brneni_g = "▄ ▄    "	
		elif sestalinie.brneni == 1: 
			sestalinie.brneni_g = "▄      "
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 2
	elif sestalinie.herni_index == 3:
		sestalinie.grafika_1 = ".---._  "
		sestalinie.grafika_2 = ":   : \ "
		sestalinie.grafika_3 = "´O-O-O/ "
		if sestalinie.vitalita == 5:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		if sestalinie.brneni == 3: 
			sestalinie.brneni_g = "▄ ▄ ▄  "		
		elif sestalinie.brneni == 2: 
			sestalinie.brneni_g = "▄ ▄    "	
		elif sestalinie.brneni == 1: 
			sestalinie.brneni_g = "▄      "
		elif sestalinie.brneni == 0: 
			sestalinie.brneni_g = "       "
		sestalinie.pozkozeni = 3

	cervenytym.aktualni_pozkozeni = (ctvrtalinie.pozkozeni + patalinie.pozkozeni + sestalinie.pozkozeni)
	modrytym.aktualni_pozkozeni = (prvnilinie.pozkozeni + druhalinie.pozkozeni + tretilinie.pozkozeni)		

	os.system('cls')
	print("Právě hraje tým", cervenytym.nazev, "| Kredity:" , cervenytym.kredit, "| Lékárničky:", cervenytym.lekarnicky, "|", cervenytym.stav)   
	print("-----------------------------------------------------------")
	print(" _   _   _   _                                                 _   _   _   _ ")
	print("| |_| |_| |_| |                                               | |_| |_| |_| |")
	print("|             |                                               |             |")
	print("|  ", ctvrtalinie.grafika_1, " |", " ", "Pozice:", "4.", "                           ", "1.", " ", "| ", prvnilinie.grafika_1, "  |")
	print("|  ", ctvrtalinie.grafika_2, " |", " ", "Vitalita:", ctvrtalinie.vitalita_g, "           ", prvnilinie.vitalita_g, " ", "| ", prvnilinie.grafika_2, "  |")
	print("|  ", ctvrtalinie.grafika_3, " |", " ", "Brnění:", ctvrtalinie.brneni_g, "                 ", prvnilinie.brneni_g, " ", "| ", prvnilinie.grafika_3, "  |")
	print("|             |                                               |             |")
	print("|             |                                               |             |")
	print("|  ", patalinie.grafika_1, " |", " ", "Pozice:", "5.", "                           ", "2.", " ", "| ", druhalinie.grafika_1, "  |")
	print("|  ", patalinie.grafika_2, " |", " ", "Vitalita:", patalinie.vitalita_g, "           ", druhalinie.vitalita_g, " ", "| ", druhalinie.grafika_2, "  |")
	print("|  ", patalinie.grafika_3, " |", " ", "Brnění:", patalinie.brneni_g, "                 ", druhalinie.brneni_g, " ", "| ", druhalinie.grafika_3, "  |")
	print("|             |                                               |             |")
	print("|             |                                               |             |")
	print("|  ", sestalinie.grafika_1, " |", " ", "Pozice:", "6.", "                           ", "3.", " ", "| ", tretilinie.grafika_1, "  |")
	print("|  ", sestalinie.grafika_2, " |", " ", "Vitalita:", sestalinie.vitalita_g, "           ", tretilinie.vitalita_g, " ", "| ", tretilinie.grafika_2, "  |")
	print("|  ", sestalinie.grafika_3, " |", " ", "Brnění:", sestalinie.brneni_g, "                 ", tretilinie.brneni_g, " ", "| ", tretilinie.grafika_3, "  |")

	print(" ____________      ____________      ____________ ")
	print("|            |    |            |    |            |")
	print("|   OBCHOD   |    |    ÚTOK    |    |  UZDRAVIT  |")
	print("|            |    |            |    |            |")
	print("| ->obchod<- |    |  ->utok<-  |    |->uzdravit<-|")
	print("|____________|    |____________|    |____________|")
	krok = (input("Váš další krok: "))

	if krok == "obchod":
		os.system('cls')
		print("Kredity:", cervenytym.kredit, "$")  
		print(" _   _   _   _                                                 _   _   _   _ ")
		print("| |_| |_| |_| |                                               | |_| |_| |_| |")
		print("|             |                                               |             |")
		print("|  ", ctvrtalinie.grafika_1, " |", " ", "Pozice:", "4.", "                           ", "1.", " ", "| ", prvnilinie.grafika_1, "  |")
		print("|  ", ctvrtalinie.grafika_2, " |", " ", "Vitalita:", ctvrtalinie.vitalita_g, "           ", prvnilinie.vitalita_g, " ", "| ", prvnilinie.grafika_2, "  |")
		print("|  ", ctvrtalinie.grafika_3, " |", " ", "Brnění:", ctvrtalinie.brneni_g, "                 ", prvnilinie.brneni_g, " ", "| ", prvnilinie.grafika_3, "  |")
		print("|             |                                               |             |")
		print("|             |                                               |             |")
		print("|  ", patalinie.grafika_1, " |", " ", "Pozice:", "5.", "                           ", "2.", " ", "| ", druhalinie.grafika_1, "  |")
		print("|  ", patalinie.grafika_2, " |", " ", "Vitalita:", patalinie.vitalita_g, "           ", druhalinie.vitalita_g, " ", "| ", druhalinie.grafika_2, "  |")
		print("|  ", patalinie.grafika_3, " |", " ", "Brnění:", patalinie.brneni_g, "                 ", druhalinie.brneni_g, " ", "| ", druhalinie.grafika_3, "  |")
		print("|             |                                               |             |")
		print("|             |                                               |             |")
		print("|  ", sestalinie.grafika_1, " |", " ", "Pozice:", "6.", "                           ", "3.", " ", "| ", tretilinie.grafika_1, "  |")
		print("|  ", sestalinie.grafika_2, " |", " ", "Vitalita:", sestalinie.vitalita_g, "           ", tretilinie.vitalita_g, " ", "| ", tretilinie.grafika_2, "  |")
		print("|  ", sestalinie.grafika_3, " |", " ", "Brnění:", sestalinie.brneni_g, "                 ", tretilinie.brneni_g, " ", "| ", tretilinie.grafika_3, "  |")

		print(" ____________     ____________     ____________     ____________  ")
		print("|     O      |   |   _/-\===  |   |  .---._    |   |  ________  |")
		print("|    /:\     |   |  :     \   |   |  :   : \   |   | |  |__|  | |")
		print("|    / \     |   |  \O-O-O/   |   |  ´O-O-O/   |   | |________| |")
		print("|   [500$]   |   |  [1000$]   |   |  [1500$]   |   |   [500$]   |")
		print("| ->vojak<-  |   |  ->tank<-  |   |->vozidlo<- |   |  ->lekar<- |")
		print("|____________|   |____________|   |____________|   |____________|")
		obchod = (input("Zadejte vaši objednávku: "))
		if obchod == "vojak":
			if cervenytym.kredit <= 499:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if ctvrtalinie.herni_index >= 1:
					if patalinie.herni_index >= 1:
						if sestalinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							time.sleep(1)
							os.system('cls')
						else:
							cervenytym.kredit -= 500
							sestalinie.herni_index = 1
							sestalinie.vitalita = 3	
					else:
						cervenytym.kredit -= 500
						patalinie.herni_index = 1	
						patalinie.vitalita = 3
				else:
					cervenytym.kredit -= 500
					ctvrtalinie.herni_index = 1	
					ctvrtalinie.vitalita = 3	
		elif obchod == "tank":
			if cervenytym.kredit <= 999:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if ctvrtalinie.herni_index >= 1:
					if patalinie.herni_index >= 1:
						if sestalinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							time.sleep(1)
							os.system('cls')
						else:
							cervenytym.kredit -= 1000
							sestalinie.herni_index = 2	
							sestalinie.vitalita = 4
					else:
						cervenytym.kredit -= 1000
						patalinie.herni_index = 2
						patalinie.vitalita = 4	
				else:
					cervenytym.kredit -= 1000
					ctvrtalinie.herni_index = 2
					ctvrtalinie.vitalita = 4		
		elif obchod == "vozidlo":
			if cervenytym.kredit <= 1499:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			else:
				if ctvrtalinie.herni_index >= 1:
					if patalinie.herni_index >= 1:
						if sestalinie.herni_index >= 1:
							os.system('cls')
							print("Všechny sloty jsou zaplněné - Ztrácíš tah")
							time.sleep(1)
							os.system('cls')
						else:
							cervenytym.kredit -= 1500
							sestalinie.herni_index = 3	
							sestalinie.vitalita = 5	
					else:
						cervenytym.kredit -= 1500
						patalinie.herni_index = 3	
						patalinie.vitalita = 5	
				else:
					cervenytym.kredit -= 1500
					ctvrtalinie.herni_index = 3	
					ctvrtalinie.vitalita = 5	
		elif obchod == "lekar":
			if cervenytym.kredit <= 499:
				os.system('cls')
				print("Nemáš dostatek kreditů - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')	
			else:
				cervenytym.kredit -=500
				cervenytym.lekarnicky += 1			
		else:
			os.system('cls')
			print("Neplatná volba - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')		
	elif krok == "utok":
		utok = (input("Zadejte pozici nakterou útočíš: "))
		if utok == "1":
			prvnilinie.vitalita = prvnilinie.vitalita - cervenytym.aktualni_pozkozeni
		elif utok == "2":
			druhalinie.vitalita = druhalinie.vitalita - cervenytym.aktualni_pozkozeni
		elif utok == "3":
			tretilinie.vitalita = tretilinie.vitalita - cervenytym.aktualni_pozkozeni
		elif utok == "4":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		elif utok == "5":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		elif utok == "6":
			os.system('cls')
			print("Nemůžeš útočit na svoje vojáky - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
		else:
			os.system('cls')
			print("Neplatná volba - Ztrácíš tah")	
			time.sleep(1)
			os.system('cls') 
	elif krok == "uzdravit":
		if cervenytym.lekarnicky >= 1:
			uzdravit = (input("Zadejte číslo vojáka kterého chcete vyléčit: "))
			if uzdravit == "4":
				if ctvrtalinie.herni_index == 1:
					ctvrtalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if ctvrtalinie.vitalita > 3:
						ctvrtalinie.vitalita = 3
				elif ctvrtalinie.herni_index == 2:
					ctvrtalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if ctvrtalinie.vitalita > 4:
						ctvrtalinie.vitalita = 4
				elif ctvrtalinie.herni_index == 3:
					ctvrtalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if ctvrtalinie.vitalita > 5:
						ctvrtalinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")
					time.sleep(1)
					os.system('cls')	
			elif uzdravit == "5":
				if patalinie.herni_index == 1:
					patalinie.vitalita += 1
					cervenytym.lekarnicky -= 1
					if patalinie.vitalita > 3:
						patalinie.vitalita = 3
				elif patalinie.herni_index == 2:
					patalinie.vitalita += 1
					cervenytym.lekarnicky -= 1
					if patalinie.vitalita > 4:
						patalinie.vitalita = 4
				elif patalinie.herni_index == 3:
					patalinie.vitalita += 1
					cervenytym.lekarnicky -= 1
					if patalinie.vitalita > 5:
						patalinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")
					time.sleep(1)
					os.system('cls')	
			elif uzdravit == "6":
				if sestalinie.herni_index == 1:
					sestalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if sestalinie.vitalita > 3:
						sestalinie.vitalita = 3
				elif sestalinie.herni_index == 2:
					sestalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if sestalinie.vitalita > 4:
						sestalinie.vitalita = 4
				elif sestalinie.herni_index == 3:
					sestalinie.vitalita += 3
					cervenytym.lekarnicky -= 1
					if sestalinie.vitalita > 5:
						sestalinie.vitalita = 5
				else:
					os.system('cls')
					("Jednotka na této pozici má maximální vitalitu - Ztrácíš tah")	
					time.sleep(1)
					os.system('cls')
			elif uzdravit == "4":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			elif uzdravit == "5":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
			elif uzdravit == "6":
				os.system('cls')
				print("Nemůžeš uzdravit nepřátelské jednotky - Ztrácíš tah")
				time.sleep(1)
				os.system('cls')
		else:
			os.system('cls')
			print("Nemáš dostatek lékárniček - Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
	elif krok == "konec":
		konec = (input("Skutečně se chcete vzdát ? (A/N): ")) 	
		if konec == "N":
			os.system('cls')
			print("Ztrácíš tah")
			time.sleep(1)
			os.system('cls')
			break
		else:
			ctvrtalinie.herni_index = 0
			patalinie.herni_index = 0
			sestalinie.herni_index = 0
			break				
	elif krok == ";cheat":
		os.system('cls')
		print("Vítejte v cheat menu")
		cheat = (input("Zadejte název cheatu : ")) 
		if cheat == "kredit":
			cervenytym.kredit += 1000
		elif cheat == "lekarnicky":
			cervenytym.lekarnicky += 5	
		else:
			break					
	else:
		os.system('cls')
		print("Neplatná volba - Ztrácíš tah")	
		time.sleep(1)	
		os.system('cls')

	if ctvrtalinie.herni_index == 0:
		ctvrtalinie.grafika_1 = "        "
		ctvrtalinie.grafika_2 = "        "
		ctvrtalinie.grafika_3 = "        "
		ctvrtalinie.vitalita = 0
		ctvrtalinie.vitalita_g = "         "
		ctvrtalinie.brneni = "       "
		ctvrtalinie.pozkozeni = 0
	elif ctvrtalinie.herni_index == 1:
		ctvrtalinie.grafika_1 = "   O    "
		ctvrtalinie.grafika_2 = "  /:\   "
		ctvrtalinie.grafika_3 = "  / \   "
		if ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		ctvrtalinie.brneni = "MARAKOV"	
		ctvrtalinie.pozkozeni = 1
	elif ctvrtalinie.herni_index == 2:
		ctvrtalinie.grafika_1 = " _/-\==="
		ctvrtalinie.grafika_2 = ":     \ "
		ctvrtalinie.grafika_3 = "\O-O-O/ "
		if ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		ctvrtalinie.brneni = "T-34   "
		ctvrtalinie.pozkozeni = 2
	elif ctvrtalinie.herni_index == 3:
		ctvrtalinie.grafika_1 = ".---._  "
		ctvrtalinie.grafika_2 = ":   : \ "
		ctvrtalinie.grafika_3 = "´O-O-O/ "
		if ctvrtalinie.vitalita == 5:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif ctvrtalinie.vitalita == 4:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif ctvrtalinie.vitalita == 3:
			ctvrtalinie.vitalita_g = "▄ ▄ ▄    "
		elif ctvrtalinie.vitalita == 2:
			ctvrtalinie.vitalita_g = "▄ ▄      "
		elif ctvrtalinie.vitalita == 1:
			ctvrtalinie.vitalita_g = "▄        "
		ctvrtalinie.brneni = "BVP-1  "	
		ctvrtalinie.pozkozeni = 3	

	if patalinie.herni_index == 0:
		patalinie.grafika_1 = "        "
		patalinie.grafika_2 = "        "
		patalinie.grafika_3 = "        "
		patalinie.vitalita = 0
		patalinie.vitalita_g = "         "
		patalinie.brneni = "       "
		patalinie.pozkozeni = 0
	elif patalinie.herni_index == 1:
		patalinie.grafika_1 = "   O    "
		patalinie.grafika_2 = "  /:\   "
		patalinie.grafika_3 = "  / \   "
		if patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		patalinie.brneni = "MARAKOV"	
		patalinie.pozkozeni = 1
	elif patalinie.herni_index == 2:
		patalinie.grafika_1 = " _/-\==="
		patalinie.grafika_2 = ":     \ "
		patalinie.grafika_3 = "\O-O-O/ "
		if patalinie.vitalita == 4:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		patalinie.brneni = "T-34   "
		patalinie.pozkozeni = 2
	elif patalinie.herni_index == 3:
		patalinie.grafika_1 = ".---._  "
		patalinie.grafika_2 = ":   : \ "
		patalinie.grafika_3 = "´O-O-O/ "
		if patalinie.vitalita == 5:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif patalinie.vitalita == 4:
			patalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif patalinie.vitalita == 3:
			patalinie.vitalita_g = "▄ ▄ ▄    "
		elif patalinie.vitalita == 2:
			patalinie.vitalita_g = "▄ ▄      "
		elif patalinie.vitalita == 1:
			patalinie.vitalita_g = "▄        "
		patalinie.brneni = "BVP-1  "	
		patalinie.pozkozeni = 3		

	if sestalinie.herni_index == 0:
		sestalinie.grafika_1 = "        "
		sestalinie.grafika_2 = "        "
		sestalinie.grafika_3 = "        "
		sestalinie.vitalita = 0
		sestalinie.vitalita_g = "         "
		sestalinie.brneni = "       "
		sestalinie.pozkozeni = 0	
	elif sestalinie.herni_index == 1:
		sestalinie.grafika_1 = "   O    "
		sestalinie.grafika_2 = "  /:\   "
		sestalinie.grafika_3 = "  / \   "
		if sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		sestalinie.brneni = "MARAKOV"
		sestalinie.pozkozeni = 1	
	elif sestalinie.herni_index == 2:
		sestalinie.grafika_1 = " _/-\==="
		sestalinie.grafika_2 = ":     \ "
		sestalinie.grafika_3 = "\O-O-O/ "
		if sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		sestalinie.brneni = "T-34   "
		sestalinie.pozkozeni = 2
	elif sestalinie.herni_index == 3:
		sestalinie.grafika_1 = ".---._  "
		sestalinie.grafika_2 = ":   : \ "
		sestalinie.grafika_3 = "´O-O-O/ "
		if sestalinie.vitalita == 5:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄ ▄"
		elif sestalinie.vitalita == 4:
			sestalinie.vitalita_g = "▄ ▄ ▄ ▄  "
		elif sestalinie.vitalita == 3:
			sestalinie.vitalita_g = "▄ ▄ ▄    "
		elif sestalinie.vitalita == 2:
			sestalinie.vitalita_g = "▄ ▄      "
		elif sestalinie.vitalita == 1:
			sestalinie.vitalita_g = "▄        "
		sestalinie.brneni = "BVP-1  "	
		sestalinie.pozkozeni = 3			

	if prvnilinie.vitalita <= 0:
		if prvnilinie.herni_index == 1:
			cervenytym.kredit += 250
			prvnilinie.herni_index = 0
		if prvnilinie.herni_index == 2:
			cervenytym.kredit += 500
			prvnilinie.herni_index = 0
		if prvnilinie.herni_index == 3:
			cervenytym.kredit += 1000		
			prvnilinie.herni_index = 0	
	elif druhalinie.vitalita <= 0:
		if druhalinie.herni_index == 1:
			cervenytym.kredit += 250
			druhalinie.herni_index = 0
		if druhalinie.herni_index == 2:
			cervenytym.kredit += 500
			druhalinie.herni_index = 0
		if druhalinie.herni_index == 3:
			cervenytym.kredit += 1000		
			druhalinie.herni_index = 0	
	elif sestalinie.vitalita <= 0:
		if sestalinie.herni_index == 1:
			cervenytym.kredit += 250
			sestalinie.herni_index = 0
		if sestalinie.herni_index == 2:
			cervenytym.kredit += 500
			sestalinie.herni_index = 0
		if sestalinie.herni_index == 3:
			cervenytym.kredit += 1000		
			sestalinie.herni_index = 0	

	if prvnilinie.herni_index <= 0 and druhalinie.herni_index <= 0 and tretilinie.herni_index <= 0:
		break				

if ctvrtalinie.herni_index <= 0 and patalinie.herni_index <= 0 and sestalinie.herni_index <= 0:
	os.system('cls')
	print("Konec hry")	
	time.sleep(3)
	os.system('cls')
	print("Vyhrál tým", modrytym.nazev)
	time.sleep(3)
	os.system('cls')
elif prvnilinie.herni_index <= 0 and druhalinie.herni_index <= 0 and tretilinie.herni_index <= 0:
	os.system('cls')
	print("Konec hry")	
	time.sleep(3)
	os.system('cls')
	print("Vyhrál tým", cervenytym.nazev)
	time.sleep(3)
	os.system('cls')
elif konec_aplikace == 1:
	os.system('cls')
	print("Konec hry")	
	time.sleep(3)
	os.system('cls')	
else:
	os.system('cls')
	print("Jste diskvalifikován za používání chatů")	
	time.sleep(3)
	os.system('cls')
	print("Konec hry")	
	time.sleep(3)
	os.system('cls')



		