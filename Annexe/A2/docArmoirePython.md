# Une armoire c'est quoi ?

- c'est un appareil électrique commandable à distance
- il dispose de 7 charges différentes (numérotées de 0 à 6)  et de deux source d'alimentation 
(source1 et source2)

- chaque charge peut être en marche ou pas et soit sur source 1 soit sur source 2 indépendament des autres
- on peut connaitre des infos sur chaque charges (U,I,P,PR) et sur chaque source (i.e. le cumul des charges en marche sur la source concernée)
# Documentation code python de manipulation des armoires


## Prerequis logiciel

- utilisation de la librairie EasyModbus.py
- utilisation d'un code bitManip.py

## Code disponible

### Note
Actuellement les codes pour l'armoire 6 et 5 sont  opérationnels.

### Utilisation

- charger le fichier correspondant à l'armoire à utiliser (exemple Armoire6.py) et ses dépendances

**Méthodes**

* Constructeur *ArmoireX()* où X vaut 6

* actions générales
    - **resetAll**: remet tout à l'état d'origine
    - **resetSource** / **resetCharge**: remet la partie source/charge à l'état d'origine
 * actions sur les charges  
    - **setCharge** / **unsetCharge** / **toggleCharge**(*n°charge*): met sur ON/OFF/état inverse la charge. *N°charge* doit être compris entre 0 et 6
* Actions sur les sources
    - **setSource1** / **setSource2** / **togglesource**(*n°charge*): met sur l'alimentaion 1/l'alimentation 2/inverse la source. *N°charge* doit être compris entre 0 et 6
* Actions sur les sources
   
* lecture de valeurs (
retourne une liste de valeurs  [U,I,PA,PR])
    - **readSecteur1**: mesure pour la source 1
    - **readSecteur2**: mesure pour la source 2
    - **readMesure**(*n°charge*): mesure pour la charge paramètre (compris en 0 et 6)
