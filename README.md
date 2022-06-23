# Proiect arduino practica

Ziua 1 - Am discutat despre ce am dori de la practica

Ziua 2 - Serviciu Clinceni

Ziua 3 - Liber dupa serviciu

Ziua 4 - Am testat modulele pe care le aveam eu: led-uri si servo

Ziua 5 - Am legat ecranul LCD si am facut functia de scriere pe ecran
	   - Am legat senzorul de proximitate si am scris functia care returneaza distanta in cm
	   - Am creat functia mai cauta care roteste servo de la 10 pana la 170 de grade
	   - In loop am pus ca servo-ul, pe care am montat senzorul de proximitate sa se roteasca pana da de un obiect la distanta de sub 100 de cm
	   - In cazul in care gaseste, ia inputul de la telecomanda si il afiseaza pe LCD in hexa, alaturi de distanta

Ziua 6 - Am implementat diferite functionalitati(joc reflex, pastreaza linistea, pastreaza distanta)

Ziua 7 - Am implementat alte functionalitati (roll dice, 6 din 49)

ziua 8 - Am primit raspberry si am facut un program de test al conexiunii seriale (print in consola pe raspberry, print pe LCD la arduino)

ziua 9 - Pentru a programa pe raspberry am folosit putty (protocol: ssh)
	   - Cu ajutorul biblotecii guizero am facut un mic user interface care ma ajuta sa controlez Arduino
       - Am implementat o functionalitate noua: moveServo (trimit prin raspberry un unghi, iar Arduino returneaza distanta pana la senzorul de proximitate, pe care o afisez pe ecran)
	   - proiect.ino = proiect vechi, doar arduino
	   - withRaspberry.ino = proiect nou
	   - proiect.py = aplicatia facuta pentru control arduino