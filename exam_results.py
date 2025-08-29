print("Balları daxil et:")
students={"Aysu":int(input("Aysu:")),"Aynur":int(input("Aynur:")),"Bahar":int(input("Bahar:")),"Babək":int(input("Babək:")),"Cavidan:":int(input("Cavidan:")),"Damla:":int(input("Damla:")),"Fatimə:":int(input("Fatimə:")),"Günel:":int(input("Günel:")),"Xalid:":int(input("Xalid:")),"Zəhra:":int(input("Zəhra:"))}
elacilar={}
zerbeciler={}
tekmillesdirilenler={}
elacilarin_bal_cemi=0
elacilarin_sayi=0
zerbecilerin_bal_cemi=0
zerbecilerin_sayi=0
for student, point  in students.items():
		if point > 80 and point<=100:
			elacilar[student]=point
			elacilarin_sayi+=1
			elacilarin_bal_cemi+=point
		elif point>60 and point<=80:
			zerbeciler[student]=point
			zerbecilerin_sayi+=1
			zerbecilerin_bal_cemi+=point
		elif point<=60:
			tekmillesdirilenler[student]=point
print("elacilar:",elacilar)
print("zerbeciler:",zerbeciler)
print("tekmillesdirilmeye ehtiyaci olanlar:",tekmillesdirilenler)
if elacilarin_sayi>0:
	print("elacilarin ortalamasi:",elacilarin_bal_cemi/elacilarin_sayi)
if zerbecilerin_sayi>0:
	print("zerbecilerin ortalamasi:",zerbecilerin_bal_cemi/zerbecilerin_sayi)