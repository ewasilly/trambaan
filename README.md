Mijn Project
[ Korte beschrijving van de RailNL case]

Statespace:

u = (s * c_1 * (c_2)^a_m)^t

waarin
u de upper bound is
s het aantal stations is
c_1 het maximum aantal connecties is
c_2 het maximum aantal connecties is als je niet terug reist
a_m het aantal connecties dat maximaal in 2 uur past
t het maximale aantal trajecten is


Aan de slag (Getting Started)
Vereisten (Prerequisites)
Deze codebase is volledig geschreven in Python3.7

In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

pip install -r requirements.txt


Structuur (Structure)
Alle Python scripts staan in de folder Code. (Main en alle classes files)

In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code. (de csv files)

Test (Testing)
Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:
python main.py


Auteurs (Authors)
Ewa Sillem , Jasper Lankhorst, Louise Buijs


Dankwoord (Acknowledgments)
StackOverflow
w3 schools
Alle super behulpzame tutoren en tech-assistants van de minor programmeren (UvA)
