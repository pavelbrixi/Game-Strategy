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
		self.zbran = None
		self.pozkozeni = None

class Druhalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.zbran = None
		self.pozkozeni = None

class Tretilinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.zbran = None
		self.pozkozeni = None			

class Ctvrtalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.zbran = None
		self.pozkozeni = None			

class Patalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.zbran = None
		self.pozkozeni = None		

class Sestalinie:
	def __init__(self):
		self.herni_index = 0
		self.grafika_1 = None
		self.grafika_2 = None
		self.grafika_3 = None
		self.vitalita = None
		self.vitalita_g = None
		self.zbran = None
		self.pozkozeni = None									

class Modrytym:
	def __init__(self):
		self.nazev = None
		self.kredit = 1000
		self.lekarnicky = 0	
		self.aktualni_pozkozeni = None

#Obsahuje Linie : 1. , 2. , 3.		

class Cervenytym:
	def __init__(self):
		self.nazev = None
		self.kredit = 1000
		self.lekarnicky = 0	
		self.aktualni_pozkozeni = None

#Obsahuje Linie : 4. , 5. , 6.			

prvnilinie = Prvnilinie()
druhalinie = Druhalinie()
tretilinie = Tretilinie()
ctvrtalinie = Ctvrtalinie()
patalinie = Patalinie()
sestalinie = Sestalinie()
modrytym = Modrytym()
cervenytym = Cervenytym()

os.system('cls')
modrytym.nazev = (input("Zadejte název prvního týmu : "))
cervenytym.nazev = (input("Zadejte název druhého týmu: "))

prvnilinie.herni_index = 1
prvnilinie.vitalita = 3
ctvrtalinie.herni_index = 1
ctvrtalinie.vitalita = 3

while True:
	if prvnilinie.herni_index == 0:
		prvnilinie.grafika_1 = "        "
		prvnilinie.grafika_2 = "        "
		prvnilinie.grafika_3 = "        "
		prvnilinie.vitalita = 0
		prvnilinie.vitalita_g = "         "
		prvnilinie.zbran = "       "
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
		prvnilinie.zbran = "MARAKOV"
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
		prvnilinie.zbran = "T-34   "
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
		prvnilinie.zbran = "BVP-1  "
		prvnilinie.pozkozeni = 3	

	if druhalinie.herni_index == 0:
		druhalinie.grafika_1 = "        "
		druhalinie.grafika_2 = "        "
		druhalinie.grafika_3 = "        "
		druhalinie.vitalita = 0
		druhalinie.vitalita_g = "         "
		druhalinie.zbran = "       "
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
		druhalinie.zbran = "MARAKOV"
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
		druhalinie.zbran = "T-34   "
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
		druhalinie.zbran = "BVP-1  "
		druhalinie.pozkozeni = 3

	if tretilinie.herni_index == 0:
		tretilinie.grafika_1 = "        "
		tretilinie.grafika_2 = "        "
		tretilinie.grafika_3 = "        "
		tretilinie.vitalita = 0
		tretilinie.vitalita_g = "         "
		tretilinie.zbran = "       "
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
		tretilinie.zbran = "MARAKOV"
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
		tretilinie.zbran = "T-34   "
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
		tretilinie.zbran = "BVP-1  "
		tretilinie.pozkozeni = 3

	if ctvrtalinie.herni_index == 0:
		ctvrtalinie.grafika_1 = "        "
		ctvrtalinie.grafika_2 = "        "
		ctvrtalinie.grafika_3 = "        "
		ctvrtalinie.vitalita = 0
		ctvrtalinie.vitalita_g = "         "
		ctvrtalinie.zbran = "       "
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
		ctvrtalinie.zbran = "MARAKOV"	
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
		ctvrtalinie.zbran = "T-34   "
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
		ctvrtalinie.zbran = "BVP-1  "	
		ctvrtalinie.pozkozeni = 3	

	if patalinie.herni_index == 0:
		patalinie.grafika_1 = "        "
		patalinie.grafika_2 = "        "
		patalinie.grafika_3 = "        "
		patalinie.vitalita = 0
		patalinie.vitalita_g = "         "
		patalinie.zbran = "       "
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
		patalinie.zbran = "MARAKOV"	
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
		patalinie.zbran = "T-34   "
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
		patalinie.zbran = "BVP-1  "	
		patalinie.pozkozeni = 3		

	if sestalinie.herni_index == 0:
		sestalinie.grafika_1 = "        "
		sestalinie.grafika_2 = "        "
		sestalinie.grafika_3 = "        "
		sestalinie.vitalita = 0
		sestalinie.vitalita_g = "         "
		sestalinie.zbran = "       "
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
		sestalinie.zbran = "MARAKOV"
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
		sestalinie.zbran = "T-34   "
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
		sestalinie.zbran = "BVP-1  "	
		sestalinie.pozkozeni = 3	

	print("_______________________________________________________________________________")
	print("Právě hraje hráč: ", modrytym.nazev, "   Kredity: ", modrytym.kredit, " $    Lékárničky: ", modrytym.lekarnicky)
	print("_______________________________________________________________________________")
	print("|                |                                                             ")
	print("| Pozice: 1.     |                                 4.   ", ctvrtalinie.vitalita_g, "  ")
	print("| Vitalita:      |   ", prvnilinie.grafika_1, "                           ", ctvrtalinie.grafika_1, "   ")
	print("|  ", prvnilinie.vitalita_g, "     |   ", prvnilinie.grafika_2, "                           ", ctvrtalinie.grafika_2, "   ")
	print("| Zbraň: ", prvnilinie.zbran, " |   ", prvnilinie.grafika_3, "                           ", ctvrtalinie.grafika_3, "   ")
	print("|                |                                                 ")
	print("| Pozice: 2.     |                                 5.   ", patalinie.vitalita_g, "  ")
	print("| Vitalita:      |   ", druhalinie.grafika_1, "                           ", patalinie.grafika_1, "   ")
	print("|  ", druhalinie.vitalita_g, "     |   ", druhalinie.grafika_2, "                           ", patalinie.grafika_2, "   ")
	print("| Zbraň: ", druhalinie.zbran, " |   ", druhalinie.grafika_3, "                           ", patalinie.grafika_3, "   ")
	print("|                |                                                 ")
	print("| Pozice: 3.     |                                          6.   ", sestalinie.vitalita_g, "  ")
	print("| Vitalita:      |   ", tretilinie.grafika_1, "                           ", sestalinie.grafika_1, "   ")
	print("|  ", tretilinie.vitalita_g, "     |   ", tretilinie.grafika_2, "                           ", sestalinie.grafika_2, "   ")
	print("| Zbraň: ", tretilinie.zbran, " |   ", tretilinie.grafika_3, "                           ", sestalinie.grafika_3, "   ")
	input()
