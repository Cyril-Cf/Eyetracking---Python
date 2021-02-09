# Eyetracking---Python

Ce script a été créé dans le but de mesurer l'orientation du regard des utilisateurs au moyen du logiciel OpenSesame (https://github.com/open-cogsci/OpenSesame/releases). Il remplit 2 usages : 

- Simuler un environnement de boite email avec faible interaction (exemple ci-dessous). Les utilisateurs devaient selectionner tous les emails correspondant aux critères de recherche en haut de la page et cliquer sur la poubelle pour les supprimer.

![boite_mail](/Boite_mail.jpg) 

- Mesurer l'activité occulaire au moyen d'un Eye Tracker. Le script devait ainsi enregistrer puis rapporter les coordonnées et timestamps dans un fichier CSV à l'issue de la séance. La réalisation de carte de chaleurs se faisait par des traitements statistiques subséquents :

![heatmap](/Heatmap.png) 
![Regards](/Regards.png) 

Afin de fonctionner, ce script ne peut être lancé que depuis le logiciel OpenSesame et avec les librairies de medias correspondant. Ce repo sert avant tout à montrer les possibilités de ce logiciel et une façon de coder en Python un inline script correspondant à cette demande. Si vous avez davantage de questions, n'hésitez pas à m'envoyer un message.
