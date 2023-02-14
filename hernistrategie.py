import os
import time

#Grafika
class Grafika:
	def __init__(self):
		self.prvniradek = "    O  "
		self.druhyradek = "   /|\ " 
		self.tretiradek = "   / \ " 



#Vojáci týmu 1
class Vojak11:
	def __init__(self):
		self.unikatni_cislo = 11
		self.tym = 1
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"

class Vojak12:
	def __init__(self):
		self.unikatni_cislo = 12
		self.tym = 1
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"

class Vojak13:
	def __init__(self):
		self.unikatni_cislo = 13
		self.tym = 1
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"				

#Vojáci týmu 2
class Vojak21:
	def __init__(self):
		self.unikatni_cislo = 21
		self.tym = 2
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"

class Vojak22:
	def __init__(self):
		self.unikatni_cislo = 22
		self.tym = 2
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"	
		
class Vojak23:
	def __init__(self):
		self.unikatni_cislo = 23
		self.tym = 2
		self.aktualni_vitalita = 100
		self.maximalni_pozkozeni = 50
		self.pocet_zasahu = 0
		self.zbran = "AK47"			

#Týmy
class Tym1:
	def __init__(self):
		self.tym1_nazev = None
		self.tym1_barva = "modrý"
		self.tym1_kredit = 1000
		self.tym1_seznam_vojaku = None
		self.tym1_pocet_vojaku = 3
		self.tym1_pocet_lekarnicek = 0

class Tym2:
	def __init__(self):
		self.tym2_nazev = None
		self.tym2_barva = "červený"
		self.tym2_kredit = 1000
		self.tym2_seznam_vojaku = None	
		self.tym2_pocet_vojaku = 1
		self.tym2_pocet_lekarnicek = 0

grafika = Grafika()
vojak11 = Vojak11()
vojak12 = Vojak12()
vojak13 = Vojak13()
vojak21 = Vojak21()
vojak22 = Vojak22()
vojak23 = Vojak23()
tym1 = Tym1()
tym2 = Tym2()



tym1.tym1_nazev = (input("Zadejte název prvního týmu: "))
tym2.tym2_nazev = (input("Zadejte název druhého týmu: "))

while tym2.tym2_pocet_vojaku >= 1 or tym1.tym1_pocet_vojaku >= 1:	

	os.system('cls')
	print("-----------------------------------------------------------")
	print("Právě hraje", tym1.tym1_barva, "tým", tym1.tym1_nazev, "s kreditem:", tym1.tym1_kredit, "$", "Lékarniček:", tym1.tym1_pocet_lekarnicek)
	print("-----------------------------------------------------------")
	print("")
	if tym1.tym1_pocet_vojaku == 1 and tym2.tym2_pocet_vojaku == 1:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")

	if tym1.tym1_pocet_vojaku == 2 and tym2.tym2_pocet_vojaku == 1:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")	

	if tym1.tym1_pocet_vojaku == 3 and tym2.tym2_pocet_vojaku == 1:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak13.zbran, "          ", "       ", "      ", "    ")		

	if tym1.tym1_pocet_vojaku == 1 and tym2.tym2_pocet_vojaku == 2:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")

	if tym1.tym1_pocet_vojaku == 1 and tym2.tym2_pocet_vojaku == 3:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak23.zbran)	

	if tym1.tym1_pocet_vojaku == 2 and tym2.tym2_pocet_vojaku == 2:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")	

	if tym1.tym1_pocet_vojaku == 3 and tym2.tym2_pocet_vojaku == 3:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
		#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak13.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak23.zbran)

	if tym1.tym1_pocet_vojaku == 2 and tym2.tym2_pocet_vojaku == 3:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak23.zbran)	

	if tym1.tym1_pocet_vojaku == 3 and tym2.tym2_pocet_vojaku == 2:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak11.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak21.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak12.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak22.zbran)
		print("")
	#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak13.zbran, "          ", "       ", "      ", "    ")	

	print("")

	print(" ____________      ____________      ____________ ")
	print("|   KOUPIT   |    |            |    |            |")
	print("|   VOJÁKA   |    |            |    |  UZDRAVIT  |")
	print("|   [500$]   |    |    ÚTOK    |    |   VOJÁKA   |")
	print("|            |    |            |    |            |")
	print("| ->koupit<- |    |  ->utok<-  |    |->uzdravit<-|")
	print("|____________|    |____________|    |____________|")

	zadani = (input("Váš další krok: "))
	if zadani == "koupit":
		if tym1.tym1_pocet_vojaku == 3:
			print("Máte maximální počet vojáků - ztrácíš tah")
			time.sleep(1)
		else:	
			if tym2.tym2_kredit >= 499:
				print("Nemáte dostatek kreditů - ztrácíš tah")
			else:
				tym1.tym1_pocet_vojaku += 1
				tym1.tym1_kredit -= 500
				print("Zakoupil jsi vojáka")
				time.sleep(1)
	elif zadani == "utok":
		utok = (input("Napište číslo vojáka na kterého útočíte: "))

		if utok == "21":
			vojak21.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "22":
			vojak22.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "23":
			vojak23.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "11":
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
		elif utok == "12":
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
		elif utok == "13":	
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
	elif zadani == "uzdravit":
		if tym1.tym1_pocet_lekarnicek >= 1:
			uzdraveni = (input("Napište číslo vojáka kterého chcete uzdravit: "))
			if uzdraveni == "11":
				vojak11.aktualni_vitalita += 50
				print("Vyléčil jsi vojáka 11 ")
				time.sleep(1)
				if vojak11.aktualni_vitalita >= 101:
					vojak11.aktualni_vitalita = 100	
			elif uzdraveni == "12":
				vojak12.aktualni_vitalita += 50
				print("Vyléčil jsi vojáka 12 ")
				time.sleep(1)
				if vojak12.aktualni_vitalita >= 101:
					vojak12.aktualni_vitalita = 100	
			elif uzdraveni == "13":
				vojak13.aktualni_vitalita = +50
				print("Vyléčil jsi vojáka 13 ")
				time.sleep(1)
				if vojak13.aktualni_vitalita >= 101:
					vojak13.aktualni_vitalita = 100	
			elif uzdraveni == "21":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)
			elif uzdraveni == "22":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)
			elif uzdraveni == "23":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)		
		else:	
			print("Nemáte dostatek lékarniček")
			time.sleep(1)
	else:
		print("Ztrácíš tah")
		time.sleep(1)	

	if vojak21.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 21")
		time.sleep(3)	
		tym2.tym2_pocet_vojaku -= 1	

	if vojak22.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 22")
		time.sleep(3)	
		tym2.tym2_pocet_vojaku -= 1	

	if vojak23.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 23")
		time.sleep(3)	
		tym2.tym2_pocet_vojaku -= 1		

	if tym1.tym1_pocet_vojaku == 0:
		break
	elif tym2.tym2_pocet_vojaku == 0:
		break			

	os.system('cls')
	print("-----------------------------------------------------------")
	print("Právě hraje", tym2.tym2_barva, "tým", tym2.tym2_nazev, "s kreditem:", tym2.tym2_kredit, "$", "Lékarniček:", tym2.tym2_pocet_lekarnicek)
	print("-----------------------------------------------------------")

	if tym2.tym2_pocet_vojaku == 1 and tym1.tym1_pocet_vojaku == 1:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")

	if tym2.tym2_pocet_vojaku == 2 and tym1.tym1_pocet_vojaku == 1:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")	

	if tym2.tym2_pocet_vojaku == 3 and tym1.tym1_pocet_vojaku == 1:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", "       ", "      ", "    ")
		print("")
		#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak23.zbran, "          ", "       ", "      ", "    ")		

	if tym2.tym2_pocet_vojaku == 1 and tym1.tym1_pocet_vojaku == 2:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")

	if tym2.tym2_pocet_vojaku == 1 and tym1.tym1_pocet_vojaku == 3:
		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak13.zbran)	

	if tym2.tym2_pocet_vojaku == 2 and tym1.tym1_pocet_vojaku == 2:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", "       ", "            ", "  ")
		print("       ", "         ", "   ", "        ", "       ", "         ", "   ")
		print("       ", "     ", "    ", "          ", "       ", "      ", "    ")	

	if tym2.tym2_pocet_vojaku == 3 and tym1.tym1_pocet_vojaku == 3:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
		#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak23.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak13.zbran)

	if tym2.tym2_pocet_vojaku == 2 and tym1.tym1_pocet_vojaku == 3:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
		#Třetí linie
		print("       ", "            ", "  ", "      ", grafika.prvniradek, "Voják číslo:", vojak13.unikatni_cislo)
		print("       ", "         ", "   ", "        ", grafika.druhyradek, "Vitalita:", vojak13.aktualni_vitalita)
		print("       ", "     ", "    ", "           ", grafika.tretiradek, "Zbraň:", vojak13.zbran)	

	if tym2.tym2_pocet_vojaku == 3 and tym1.tym1_pocet_vojaku == 2:	

		#První linie
		print(grafika.prvniradek, "Voják číslo:", vojak21.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak11.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak21.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak11.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak21.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak11.zbran)
		print("")
		#Druhá linie
		print(grafika.prvniradek, "Voják číslo:", vojak22.unikatni_cislo, "      ", grafika.prvniradek, "Voják číslo:", vojak12.unikatni_cislo)
		print(grafika.druhyradek, "Vitalita:", vojak22.aktualni_vitalita, "        ", grafika.druhyradek, "Vitalita:", vojak12.aktualni_vitalita)
		print(grafika.tretiradek, "Zbraň:", vojak22.zbran, "          ", grafika.tretiradek, "Zbraň:", vojak12.zbran)
		print("")
	#Třetí linie
		print(grafika.prvniradek, "Voják číslo:", vojak23.unikatni_cislo, "      ", "       ", "            ", "  ")
		print(grafika.druhyradek, "Vitalita:", vojak23.aktualni_vitalita, "        ", "       ", "         ", "   ")
		print(grafika.tretiradek, "Zbraň:", vojak23.zbran, "          ", "       ", "      ", "    ")	

	print("")

	print(" ____________      ____________      ____________ ")
	print("|   KOUPIT   |    |            |    |            |")
	print("|   VOJÁKA   |    |            |    |  UZDRAVIT  |")
	print("|   [500$]   |    |    ÚTOK    |    |   VOJÁKA   |")
	print("|            |    |            |    |            |")
	print("| ->koupit<- |    |  ->utok<-  |    |->uzdravit<-|")
	print("|____________|    |____________|    |____________|")

	zadani = (input("Váš další krok: "))
	if zadani == "koupit":
		if tym2.tym2_pocet_vojaku == 3:
			print("Máte maximální počet vojáků - ztrácíš tah")
			time.sleep(1)
		else:	
			if tym2.tym2_kredit >= 499:
				print("Nemáte dostatek kreditů - ztrácíš tah")
			else:
				tym2.tym2_pocet_vojaku += 1
				tym2.tym2_kredit -= 500
				print("Zakoupil jsi vojáka")
				time.sleep(1)
	elif zadani == "utok":
		utok = (input("Napište číslo vojáka na kterého útočíte: "))

		if utok == "11":
			vojak11.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "12":
			vojak12.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "13":
			vojak13.aktualni_vitalita -= 40
			print("Zásah! způsobil jsi požkození 40")
			time.sleep(1)
		elif utok == "21":
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
		elif utok == "22":
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
		elif utok == "23":	
			print("nemůžeš útočit na svoje vojáky - ztrácíš tah")
			time.sleep(1)
	elif zadani == "uzdravit":
		if tym2.tym2_pocet_lekarnicek >= 1:
			uzdraveni = (input("Napište číslo vojáka kterého chcete uzdravit: "))
			if uzdraveni == "21":
				vojak21.aktualni_vitalita += 50
				print("Vyléčil jsi vojáka 11 ")
				time.sleep(1)
				if vojak21.aktualni_vitalita >= 101:
					vojak21.aktualni_vitalita = 100	
			elif uzdraveni == "22":
				vojak22.aktualni_vitalita += 50
				print("Vyléčil jsi vojáka 12 ")
				time.sleep(1)
				if vojak22.aktualni_vitalita >= 101:
					vojak22.aktualni_vitalita = 100	
			elif uzdraveni == "23":
				vojak23.aktualni_vitalita += 50
				print("Vyléčil jsi vojáka 13 ")
				time.sleep(1)
				if vojak23.aktualni_vitalita >= 101:
					vojak23.aktualni_vitalita = 100	
			elif uzdraveni == "11":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)
			elif uzdraveni == "12":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)
			elif uzdraveni == "13":
				print("Nemůžeš uzdravit nepřátele - ztrácíš tah")
				time.sleep(1)		
		else:	
			print("Nemáte dostatek lékarniček")
			time.sleep(1)
	else:
		print("Ztrácíš tah")
		time.sleep(1)	

	if vojak11.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 11")
		time.sleep(3)	
		tym1.tym1_pocet_vojaku -= 1	

	if vojak12.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 12")
		time.sleep(3)	
		tym1.tym1_pocet_vojaku -= 1	

	if vojak13.aktualni_vitalita <= 0:
		os.system('cls')
		print("Zemřel voják s čéslem 13")
		time.sleep(3)	
		tym1.tym1_pocet_vojaku -= 1	
		
	if tym2.tym2_pocet_vojaku == 0:
		break
	elif tym1.tym1_pocet_vojaku == 0:
		break	

if tym1.tym1_pocet_vojaku == 0:
	os.system('cls')
	print("Vyhrál červený tým", tym2.tym2_nazev,)
	time.sleep(3)
elif tym2.tym2_pocet_vojaku == 0:
	os.system('cls')
	print("Vyhrál modrý tým", tym1.tym1_nazev)
	time.sleep(3)

os.system('cls')
print("Konec hry")
time.sleep(3)
os.system('cls')
