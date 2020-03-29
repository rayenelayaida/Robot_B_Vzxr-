# Robot_B_Vzxr

## Objectif

On s'intéresse à un système simplifié de lecture d'instructions par un petit robot téléguidé, nommé __B-VZXR__. Le but de l'exercice est de construire un programme qui lit une suite d'instruction et donne la position finale de __B-VZXR__.

## Détails

## L'univers du robot

B-VZXR vit dans un espace rectangulaire plat, comme un échiquier de taille n * p. Chacune des n * p positions, ou cases, est définie par son abscisse et son ordonnée. Le robot naît toujours sur la case en bas à gauche (ie. d'abscisse et d'ordonnée nulle), la tête vers le haut.

## Le langage du robot

Le petit robot ne comprend qu'un seul type d'instruction, qu'il lit de manière séquentielle. Une instruction est composée de deux éléments :

* Une chaîne de caractère : __"right" ou "left"__ 
* Un nombre positif ou nul : __0, 1, 2…__


Lorsque B-VZXR lit une instruction :

* il va se tourner d'un quart de tour : 
  * vers sa droite si la chaîne de caractère vaut __"right"__ 
  * vers sa gauche si la chaîne de caractère vaut __"left" __
  
* il va ensuite avancer de k cases selon la valeur du nombre 
* si il devait rencontrer un mur, il s'arrèterait d'avancer et lirait l'instruction suivante

## Exemple

On considère un univers de taille __6 * 4__. On transmet à __B-VZXR__ la liste d'instructions suivantes :

1.  __right, 3__ 
2.  __left, 2__
3.  __left, 1__ 
4.  __left, 0__ 
5.  __left, 3__ 
6.  __right, 1__ 
7.  __right, 10__
8.  __right, 2__


Dans ce cas là, le robot, qui commence dans la case __(0,0)__, la tête vers le haut, va lire la première instruction  __"right", 3__  et va donc se tourner vers la droite et avancer de trois cases. Il sera alors dans la case __(3, 0)__. Après avoir exécuté la seconde instruction  __"left", 2__ , il sera sur la case __(3, 2)…__ La suite de son voyage est lisible sur l'image ci-dessous.

![cat](https://github.com/rayenelayaida/Robot_B_Vzxr-/blob/master/Exemple.PNG)

On notera que __B-VZXR__ lit l'instruction  __"right", 10__ , il rencontre un mur et va donc rester sur la case en face du mur. Il lira ensuite la prochaine instruction. À la fin de son périple, il va se retrouver sur la case __(0, 3)__.
