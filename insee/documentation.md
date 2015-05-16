# Documentation

Open-moulinette insee is an open data cleaner who concatene each Insee's files in one csv. Beacause Insee's file are often in xls format and not easy to reuse. Actualy we have more than 330 features, but they are not friendly-user :

`NB_B314` is the number of gas station by iris.

**The goal of this documentation is to enumerate each feature and explain it. Decription is in French as all the data concerne French's city.**


## List of file :

- [Nombre d'équipements et de services dans le domaine du commerce en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-commerce)
- [Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-sport-loisir-socio)
- [Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-sport-loisir-socio)
- [Nombre d'équipements et de services dans le domaine de l'enseignement du 1er degré en 2013] (http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-1er-degre)
-  [Nombre d'équipements et de services dans le domaine de l'enseignement du second degré en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-2eme-degre)
-  [Nombre d'équipements et de services dans le domaine de l'enseignement supérieur, de la formation et des services de l'éducation en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-sup-form-serv)
-  [Indicateurs de structure et de distribution des revenus](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=structure-distrib-revenus-2011)
-  [Nombre d'équipements et de services dans le domaine de l'action sociale en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-action-sociale)
-  [Nombre d'équipements et de services de santé en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-sante)
-  [Nombre de fonctions médicales et paramédicales en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-medical-para)
-   [Nombre d'équipements des services aux particuliers en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-particuliers)
-   [Nombre d'équipements et de services dans le domaine du tourisme et du transport en 2013](http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-tour-transp)

## Description géographique :

- CODGEO : L'IRIS, seuls les IRIS proposant au moins un équipement sont retenus.  **Les équipements non localisés** sont identifiable par un code IRIS se terminant par "ZZZZ" dans l'onglet "IRIS"
- LIBGEO : Libellé de l'IRIS, si celui-ci n'est pas identifible le libéllé sera égal à "non localisé à l'iris".
- COM : Code commune
- LIBCOM : Libellé de commune.
- REG : Région
- DEP : Département
- ARR : Arrondissement
- CV : Canton ville
- ZE2010 : Zone d'emploi
- UU2010 : Unité urbaine

**Attention :** Un équipement  est défini comme un service rendu par un établissement. Ainsi, un établissement peut être compté plusieurs fois dans la base, s’il rend plusieurs services.

## Nombre d'équipements et de services dans le domaine du commerce en 2013 :

 - NB_B101 : **Hypermarché**. Surface de vente déclarée supérieure à 2500 m²
 - NB_B102 : **Supermarché**. Surface de vente déclarée entre 400 et 2500 m². La NAF a conservé le seuil inférieur de 400m², différent du seuil administratif de la DGCCRF fixé à 300m²
 - NB_B103 : **Grande surface de bricolage**. Surface de vente déclarée supérieure à 400 m². La NAF a conservé le seuil inférieur de 400m², différent du seuil administratif de la DGCCRF fixé à 300m².
 - NB_B201 : **Supérette**. Surface de vente déclarée entre 120 et 400 m². Même remarque que pour NB_B102 pour le seuil de 400m². La limite de 120m² n'est utilisée que par la NA.
 Il est recommandé de regrouper NB_B201 avec les épiceries  NB_B202.
 - NB_B202 : **Epicerie**. Commerce de détail non spécialisé à prédominance alimentaire en surface de vente déclarée inférieure à 120m². Les multiservices en zone rurale, à la fois épicerie, café, vente de tabac, vente de journaux, restaurant, et peut-être autre chose encore, n'apparaissent ici que si la déclaration effectuée à Sirene mentionnait épicerie en premier (un sera retrouvé en épicerie, un autre en café ….)
 Il est recommandé de regrouper la variable NB_B202 avec les supérettes (NB_B201). 
 - NB_B203 : **Boulangerie**. Boulangerie avec ou sans pâtisserie. Y compris terminaux de cuisson, vente sans fabrication de produits de boulangerie. Ne comprend plus la vente de pizzas à emporter depuis le passage à la NAF rév.2.
 - NB_B205 : **Produits surgelés**. En magasin ou par livraison à domicile.
 - NB_B204 : **Boucherie charcuterie**. Y compris vente de volailles, de triperie, et plats préparés à base de viande.
 - NB_B206 : **Poissonnerie**
 - NB_B301 : **Librairie papeterie journaux** y compris journaux et périodiques.
 - NB_B302 : **Magasin de vêtements** y compris accessoires du vêtements : gants, cravates, ceintures...
 - NB_B303 : **Magasin d'équipements du foyer**. Lustrerie, ustensiles ménagers, vaisselle, rideaux et voilages …
 - NB_B304 : **Magasin de chaussures** y compris chaussures de sport.
 - NB_B305 : **Magasin d'électroménager et de mat. audio-vidéo**. "Blanc" (réfrigérateurs, appareils de cuisson électriques ou mixtes, lave-vaisselle, lave-linge, petit électroménager …)  et "brun" (téléviseurs, radios, magnétophones, magnétoscopes, lecteurs DVD, caméscopes, chaînes HIFI …).
Ne comprend plus la vente d'instruments de musique ou de disques, bandes et cassettes vierges ou enregistrés depuis le changement de nomenclature (NAF rév;2) au 1er janvier 2009 : différence d'environ 2 100 à compter de 2009.
 - NB_B306 : **Magasin de meubles** y compris commerce de sommiers et matelas.
 - NB_B307 : **Magasin d'articles de sports et de loisirs** y compris vêtements et chaussures à usage sportif exclusif.
 - NB_B308 : **Magasin de revêtements murs et sols**. Tapis et moquettes, papiers peints et revêtements divers.
 - NB_B309 : **Droguerie quincaillerie bricolage**. En surface de vente déclarée inférieure à 400 m².
 - NB_B310 : **Parfumerie** y compris commerce de produits de beauté.
 - NB_B311 : **Horlogerie Bijouterie**. Montres et autres articles d'horlogerie, articles de bijouterie et d’orfèvrerie.
 - NB_B312 : **Fleuriste** y compris commerce de plants, arbres et arbustes.
 - NB_B313 : **Magasin d'optique** y compris activité des opticiens
 - NB_B314 : **Station service**. Commerce de détail de carburant ayant vendu au moins 500 000 litres de carburant au cours de l’année. 
- nb_commerce : somme de l'ensemble des indicateurs du fichiers.

## Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013 :

 - NB_F101 : **Bassin de natation**. Bassins de natation, sportive et/ou ludique
 - NB_F101_NB_AIREJEU : **Bassin de natation - nombre de bassins **
 - NB_F101_NB_COU : **Bassin de natation avec au moins un bassin couvert**
 - NB_F101_NB_ECL : **Bassin de natation avec au moins un bassin éclairé**
 - NB_F102 : **Boulodrome**
 - NB_F102_NB_AIREJEU : **Boulodrome - nombre de terrains**. Terrain de boules, de pétanque 
 - NB_F102_NB_COU : **Boulodrome avec au moins un terrain couvert**
 - NB_F102_NB_ECL : **Boulodrome avec au moins un terrain éclairé**
 - NB_F103 : **Tennis**
 - NB_F103_NB_AIREJEU : **Tennis - nombre de courts **
 - NB_F103_NB_COU : **Tennis avec au moins un court couvert**
 - NB_F103_NB_ECL : **Tennis avec au moins un court éclairé**
 - NB_F104 : **Équipement de cyclisme**
 - NB_F104_NB_AIREJEU : **Équipement de cyclisme - nombre de pistes**. Vélodrome, anneau/piste
 - NB_F104_NB_COU : **Équipement de cyclisme avec au moins une piste couverte**
 - NB_F104_NB_ECL : **Équipement de cyclisme avec au moins une piste éclairée**
 - NB_F105 : **Domaine skiable**
 - NB_F105_NB_AIREJEU : **Domaine skiable - nombre de pistes**. Station de ski, domaine nordique 
 - NB_F105_NB_COU : **Domaine skiable avec au moins une piste couverte**
 - NB_F105_NB_ECL : **Domaine skiable avec au moins une piste éclairée**
 - NB_F106 : **Centre équestre**
 - NB_F106_NB_AIREJEU : **Centre équestre - nombre de carrières, manèges**. Carrière, manège, carrière de dressage/rond de longe, structure de tourisme équestre 
 - NB_F106_NB_COU : **Centre équestre avec au moins un équipement couvert**
 - NB_F106_NB_ECL : **Centre équestre avec au moins un équipement éclairé**
 - NB_F107 : **Athlétisme**
 - NB_F107_NB_AIREJEU : **Athlétisme - nombre d'aires de pratique**. Stade d'athlétisme, aire de lancer, aire de saut, piste
 - NB_F107_NB_COU : **Athlétisme avec au moins une aire de pratique couverte**
 - NB_F107_NB_ECL : **Athlétisme avec au moins une aire de pratique éclairée**
 - NB_F108 : **Terrain de golf**
 - NB_F108_NB_AIREJEU : **Terrain de golf - nombre d'aires de pratique**. Parcours 9 ou 18 trous, parcours d'initiation, practice
 - NB_F108_NB_COU : **Terrain de golf avec au moins une aire de pratique couverte**
 - NB_F108_NB_ECL : **Terrain de golf avec au moins une aire de pratique éclairée**
 - NB_F109 : **Parcours sportif**
 - NB_F109_NB_AIREJEU : **Parcours sportif - nombre de parcours**. Parcours sportif/santé 
 - NB_F109_NB_COU : **Parcours sportif avec au moins un parcours couvert**
 - NB_F109_NB_ECL : **Parcours sportif avec au moins un parcours éclairé**
 - NB_F110 : **Sports de glace**
 - NB_F110_NB_AIREJEU : **Sports de glace - nombre d'aires de pratique**. Aire de sports de glace, sportive et/ou ludique 
 - NB_F110_NB_COU : **Sports de glace avec au moins une aire de pratique couverte**
 - NB_F110_NB_ECL : **Sports de glace avec au moins une aire de pratique éclairée**
 - NB_F111 : **Plateau extérieur ou salle multisports**
 - NB_F111_NB_AIREJEU : **Plateau extérieur ou salle multisports - nombre d'aires de pratique**. Plateau EPS, multisports, city-stade, salle multisports (gymnase) 
 - NB_F111_NB_COU : **Plateau extérieur ou salle multisports avec au moins une aire de pratique couverte**
 - NB_F111_NB_ECL : **Plateau extérieur ou salle multisports avec au moins une aire de pratique éclairée**
 - NB_F112 : **Salle ou terrain de petits jeux**
 - NB_F112_NB_AIREJEU : **Salle ou terrain de petits jeux - nombre d'aires de pratique**. Salle ou terrain de basket-ball, de beach-volley, de handball, de volley ball, de badminton, salle de tennis de table 
 - NB_F112_NB_COU : **Salle ou terrain de petits jeux avec au moins une aire de pratique couverte**
 - NB_F112_NB_ECL : **Salle ou terrain de petits jeux avec au moins une aire de pratique éclairée**
 - NB_F113 : **Terrain de grands jeux**
 - NB_F113_NB_AIREJEU : **Terrain de grands jeux - nombre de terrains**. Terrain de football, de rugby, de football américain, de rugby à XIII 
 - NB_F113_NB_COU : **Terrain de grands jeux avec au moins un terrain couvert**
 - NB_F113_NB_ECL : **Terrain de grands jeux avec au moins un terrain éclairé**
 - NB_F114 : **Salle de combat**
 - NB_F114_NB_AIREJEU : **Salle de combat - nombre d'aires de pratique**. Dojo, salle de boxe, d'arts martiaux, de lutte, d'escrime
 - NB_F114_NB_COU : **Salle de combat avec au moins une aire de pratique couverte**
 - NB_F114_NB_ECL : **Salle de combat avec au moins une aire de pratique éclairée**
 - NB_F115 : **Salle ou terrain spécialisé**
 - NB_F115_NB_AIREJEU : **Salle ou terrain spécialisé - nombre d'aires de pratique**. Salle de culturisme, de danse, de gymnastique sportive, de patinage sur roulette, de raquetball, de trampoline, d'haltérophilie, salle ou terrain de squash, structure artificielle d'escalade 
 - NB_F115_NB_COU : **Salle ou terrain spécialisé avec au moins une aire de pratique couverte**
 - NB_F115_NB_ECL : **Salle ou terrain spécialisé avec au moins une aire de pratique éclairée**
 - NB_F116 : **Salle non spécialisée**
 - NB_F116_NB_AIREJEU : **Salle non spécialisée - nombre d'équipements où s'exerce au moins une activité physique et/ou sportive**. Salle polyvalente, des fêtes, autre salle non spécialisée
 - NB_F116_NB_COU : **Salle non spécialisée avec au moins un équipement couvert**
 - NB_F116_NB_ECL : **Salle non spécialisée avec au moins un équipement éclairé**
 - NB_F117 : **Roller-Skate-Vélo bicross ou freestyle**
 - NB_F117_NB_AIREJEU : **Roller-Skate-Vélo bicross ou freestyle - nombre de pistes**. Anneau de roller, skate-park, piste de bicross, espace de vélo freestyle 
 - NB_F117_NB_COU : **Roller-Skate-Vélo bicross ou freestyle avec au moins un équipement couvert**
 - NB_F117_NB_ECL : **Roller-Skate-Vélo bicross ou freestyle avec au moins un équipement éclairé**
 - NB_F118 : **Sports nautiques**
 - NB_F118_NB_AIREJEU : **Sports nautiques - nombre d'aires de pratique**. Site d'activités nautiques, stade de ski nautique et/ou d'aviron
 - NB_F118_NB_COU : **Sports nautiques avec au moins une aire de pratique couverte**
 - NB_F118_NB_ECL : **Sports nautiques avec au moins une aire de pratique éclairée**
 - NB_F201 : **Baignade aménagée**
 - NB_F201_NB_AIREJEU : **Baignade aménagée - nombre d'aires de pratique**. Site d'activités aquatiques, baignade aménagée. Zone délimitée (matériellement, par des bouées, des lignes d'eau, etc) pour la baignade surveillée. En rivière, mer, plan d'eau intérieur 
 - NB_F202 : **Port de plaisance - Mouillage**
 - NB_F202_NB_AIREJEU : **Port de plaisance - Mouillage - nombre de ports, de zones**. Port de plaisance, zone de mouillage
 - NB_F203 : **Boucle de randonnée**
 - NB_F203_NB_AIREJEU : **Boucle de randonnée - nombre de circuits**. Uniquement les boucles de randonnée dont les points de départ et d'arrivée se situent sur la même commune
 - NB_F301 : **Cinéma **. Projection en salle de cinéma, en plein air ou autres. Implantations physiques, qu'il y ait une seule salle de projection ou plusieurs au sein d'un complexe. Il n'y a ni le nombre de salles présentes, ni leur nombre de places offertes.
 - NB_F302 : **Théâtre**. Ensemble des lieux gérés par le Centre National du Théâtre où une représentation de théâtre peut se tenir. Ces lieux peuvent être labellisés (théâtres nationaux et privés, scènes nationales et conventionnées, compagnies avec lieux d’accueil, compagnies dramatiques nationales et régionales, pôles cirque, centres chorégraphiques) ou non. 
 - NB_F302_NB_SALLES : **Théâtre - nombre de salles**
 - nb_sport : Somme de l'ensemble des indicateurs non détaillés : uniquement les **NB_F..**  (cf ci-dessous)


**Note :** Pour chacune des installations sportives, on dispose de plusieurs informations : 
exemple pour les bassins de natation de la commune de Marseille  

- NB_F101           : 38  bassins de natation (installations pour la natation)
- NB_F101_NB_BASNAT : 47  cumul des bassins de natation dénombrés dans les 38 installations localisées
- NB_F101_NB_COU    : 25  installations sur les 38 disposent d'au moins un bassin couvert 
- NB_F101_NB_ECL    : 27  installations sur les 38 possèdant un éclairage

Il en va de même pour les autres installations sportive **NB_F1..**


## Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013 :

**Note** : Le fichier contient 3 onglets, un onglet général et deux onglet publique et privé afin de faire la distinction de secteur. Actuellement seulement les données générales (publiques + privées) sont présent.

 - NB_C101 : **Ecole maternelle**. Ecole  assurant tous les niveaux de maternelle. Y compris annexe d'IUFM, maternelle d'application et spécialisée. Y compris écoles en Regroupement Pédagogique Intercommunal (RPI) concentré (soit toutes les classes regroupées), non compris  classes de RPI dispersés (cf. NB_C102). Le RPI concentré est la spécificité d'une école, maternelle ou élémentaire, possédant toutes les classes, qui accueille les élèves de plusieurs communes adhérant au RPI.
 - NB_C101_NB_CANT : **Ecole maternelle avec cantine** 
 - NB_C101_NB_EP : **Ecole maternelle appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un : RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR). 
 - NB_C101_NB_RPIC : **Ecole maternelle en RPIC**. Ecole maternelle en RPIC. Le RPI concentré est la spécificité d'une école, maternelle ou élémentaire, possédant toutes les classes, qui accueille les élèves de plusieurs communes adhérant au RPI.
 - NB_C102 : **Classe maternelle de RPI dispersé**. Classe maternelle de RPI dispersé. Tous les niveaux de maternelle ne sont pas assurés dans l'établissement. Le RPI dispersé est la structure d'un groupe scolaire dont les classes sont "dispersées" dans les communes faisant partie du RPI dit dispersé. 
 - NB_C102_NB_CANT : **Classe maternelle de RPI dispersé avec cantine**
 - NB_C102_NB_EP : **Ecole maternelle de RPI dispersé appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un :RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR). 
 - NB_C104 : **Ecole élémentaire**. Ecole assurant tous les niveaux d'école élémentaire. Y compris annexe d'IUFM, élémentaire d'application, spécialisée ou régionale. Y compris écoles en regroupement pédagogique intercommunal (RPI) concentré (soit toutes les classes regroupées), non compris classes de RPI dispersés (cf. NB_ C105). Le RPI concentré est la spécificité d'une école, maternelle ou élémentaire, possédant toutes les classes, qui accueille les élèves de plusieurs communes adhérant au RPI.
 - NB_C104_NB_CANT : **Ecole élémentaire avec cantine**. 
 - NB_C104_NB_CL_PELEM : **Ecole élémentaire avec classe pré-élémentaire**
 - NB_C104_NB_EP : **Ecole élémentaire appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un :RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. Soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR).
 - NB_C104_NB_RPIC : **Ecole élémentaire en RPIC**. Ecole élémentaire en RPIC. Le RPI concentré est la spécificité d'une école, maternelle ou élémentaire, possédant toutes les classes, qui accueille les élèves de plusieurs communes adhérant au RPI.
 - NB_C105 : **Classe élémentaire de RPI dispersé**. Classe élémentaire de RPI dispersé. Tous les niveaux d'école élémentaire ne sont pas assurés dans l'établissement. Le RPI dispersé est la structure d'un groupe scolaire dont les classes sont "dispersées" dans les communes faisant partie du RPI dit dispersé. 
 - NB_C105_NB_CANT : **Classe élémentaire de RPI avec cantine**. 
 - NB_C105_NB_CL_PELEM : **Classe élémentaire de RPI dispersé avec classe pré-élémentaire**
 - NB_C105_NB_EP : **Classe élémentaire de RPI dispersé appartenant à un réseau d'éducation prioritaire**.Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un : RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. Soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR).
 - nb_enseignement_1 : Somme de l'ensemble des indicateurs non détaillés : uniquement sur les **NB_C1..**


## Nombre d'équipements et de services dans le domaine de l'enseignement du second degré en 2013 : 

**Note** : Le fichier contient 3 onglets, un onglet général et deux onglet publique et privé afin de faire la distinction de secteur. Actuellement seulement les données générales (publiques + privées) sont présent.

 - NB_C201 : **Collège** y compris collège climatique ou spécialisé.. 
 - NB_C201_NB_CANT : **Collège avec cantine**
 - NB_C201_NB_INT : **Collège avec internat**
 - NB_C201_NB_EP : **Collège appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. Soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR).
 - NB_C301 : **Lycée d'enseignement général et/ou technologique** y compris lycée polyvalent ou climatique et école secondaire spécialisée. Hors tutelle du ministère de l'agriculture
 - NB_C301_NB_CANT : **Lycée d'enseignement général et/ou technologique avec cantine**
 - NB_301_NB_CL_PGE : **Lycée d'enseignement général et/ou technologique avec présence de classe préparatoire aux grandes écoles**
 - NB_C301_NB_INT : **Lycée d'enseignement général et/ou technologique avec internat**
 - NB_C301_NB_EP : **Lycée d'enseignement général et/ou technologique appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un : RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. Soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR).
 - NB_C302 : **Lycée d'enseignement professionnel** y compris école de métiers et école professionnelle spécialisée. Hors tutelle du ministère de l'agriculture. 
 - NB_C302_NB_CANT : **Lycée d'enseignement professionnel avec cantine**
 - NB_C302_NB_INT : **Lycée d'enseignement professionnel avec internat**
 - NB_C302_NB_EP : **Lycée d'enseignement professionnel appartenant à un réseau d'éducation prioritaire**. Uniquement pour les écoles maternelles et élémentaires, les collèges (sauf C203) et les lycées (sauf agricoles et C304 et C305)
Appartenance à un réseau d’éducation prioritaire (définition Éducation nationale). En lieu et place des anciennes ZEP (zones d’éducation prioritaire), un REP est constitué. Il s’agit soit d’un RAR (réseau ambition réussite) : chaque réseau est constitué d’un collège ambition réussite -il devient l’unité de référence du réseau- et des écoles élémentaires et maternelles de son secteur. Chaque collège est reconnu par une spécialité de haut niveau d’ordre culturel, scientifique, linguistique, sportif ou environnemental. Il dispose de moyens supplémentaires. Soit d’un  RES (réseau de réussite scolaire) : les autres réseaux (anciens ZEP et non RAR).
 - NB_C303 : **Lycée technique et/ou professionnel agricole**. Sous tutelle du ministère de l'agriculture. Y compris maison rurale et autre enseignement agricole privé.
 - NB_C303_NB_INT : **Lycée technique et/ou professionnel agricole avec internat**
 - NB_C304 : **SGT : Section d'enseignement général et technologique**. Présence d'enseignement général et technologique au sein d'un lycée professionnel
 - NB_C304_NB_CANT : **SGT avec cantine**
 - NB_C305 : **SEP : Section d'enseignement professionnel**. Présence d'enseignement professionnel au sein d'un lycée d’enseignement général et/ou technologique
 - NB_C305_NB_CANT : **SEP avec cantine**
 - nb_enseignement_2 : Somme de l'ensemble des indicateurs non détaillés : uniquement sur les **NB_C2..** et **NB_C3..**


## Nombre d'équipements et de services dans le domaine de l'enseignement supérieur, de la formation et des services de l'éducation en 2013 : 

**Note** : Le fichier contient 3 onglets, un onglet général et deux onglet publique et privé afin de faire la distinction de secteur. Actuellement seulement les données générales (publiques + privées) sont présent.

 - NB_C401 : **Section Technicien Supérieur, Classe Préparatoire aux Grandes Ecoles**. Seules formations au diplôme de technicien supérieur, et classes préparatoires aux grandes écoles.
 - NB_C402 : **Formation santé**.  Ecoles de formation sanitaire et sociale (y compris établissements sous tutelle du ministère de la santé) publiques ou privées : formation de personnels médicaux et para-médicaux, techniques (laborantins), sanitaires (aides-soignants, ambulanciers), sociaux (service social, éducateurs ...).
 - NB_C403 : **Formation commerce**. Ecoles de commerce, gestion, administration d'entreprises, comptabilité, vente. Comprend notamment les réseaux d'écoles des CCI.
 - NB_C409 : **Autre formation post bac non universitaire**. Ecoles de formation d'enseignants non IUFM, d'administration publique (y compris de fonctionnaires), technico professionnelles des services, de formation artistique, d'architecture, de formation agricole ou halieutique, technico professionnelles industrielles, juridiques.
 - NB_C501 : **Unité de Formation et de Recherche** y compris UFR de médecine, odontologie, pharmacie. Y compris antennes délocalisées des UFR ou autres composantes.
 - NB_C502 : **Institut universitaire**. IUP, IUT yc antennes délocalisées, IUFM ycompris antennes d'IUFM.
 - NB_C503 : **Ecole d'ingénieurs**. Ecoles d'ingénieurs publiques sous tutelle du ministère de l'enseignement supérieur et de la recherche ou d'un autre ministère, et écoles privées.
 - NB_C504 : **Enseignement général supérieur privé**. Etablissements privés d'enseignement universitaire, centres ou facultés privés, instituts catholiques.
 - NB_C509 : **Autre enseignement supérieur**. Ecoles normales supérieures, instituts nationaux polytechniques, instituts d'administration des entreprises, instituts de préparation à l'administration générale, instituts d'études politiques, institut du travail, centres régionaux associés aux CNAM, Universite de technologie et centre univ formation et recherche.
 - NB_C601 : **Centre de formation d'apprentis**. Centre de formation d'apprentis avec convention régionale ou nationale, y compris antennes et sections d'apprentissage, non compris l'apprentissage agricole. 
 - NB_C602 : **GRETA**. Groupements d'établissements pour la formation continue. Les annexes de GRETA ne sont pas immatriculées. Ils sont toujours rattachés à un EPLE (Etablissement public local d'enseignement).
 - NB_C603 : **CFPPA**. Centres de formation professionnelle et de promotion agricole (toujours rattachés à un EPLE agricole).
 - NB_C604 : **Formation aux métiers du sport**. Etablissements de formation aux métiers du sport : écoles et instituts nationaux de la jeunesse et des sports (INSEP, INJEP, ENSA, ENEV, ENSFS, ENE), centres d'éducation populaire et de sport (CREPS). Ils sont sous la tutelle du ministère de la jeunesse et des sports.
 - NB_C605 : **Centre de formation d'apprentis agricole**. Créé à compter de 2010 : les CFA agricoles sont séparés des autres classés en NB_C601.
 - NB_C605_NB_INT : **Centre de formation d'apprentis agricole avec internat**
 - NB_C609 : **Autre formation continue**. Etablissements de formation continue autres : regroupe les centres d'enseignement à distance (CNED et ses centres d'enseignement, centres privés soumis à déclaration), les établissements de formation continue hors Education nationale ou hors agriculture.
 - NB_C701 : **Résidence universitaire**. L'insse ne fournit pas la différence entre NB_C701 et NB_C702, mais en regardant les chiffres on peux constater des différences.
 - NB_C702 : **Restaurant universitaire**.
 - nb_enseignement_sup : Somme de l'ensemble des indicateurs non détaillés (NB_C605_NB_INT est exclu).

## Indicateurs de structure et de distribution des revenus

Les revenus fiscaux localisés des ménages sont établis à partir des fichiers exhaustifs des déclarations de revenus des personnes physiques, de la taxe d'habitation et du fichier d’imposition des personnes physiques fournis à l'Insee par la Direction générale des finances publiques.

**Note** : La liste des indicateurs disponibles varie selon les seuils de population (nombre de ménages fiscaux ou population fiscale). Is se peux donc que certain des indicateurs soient vide :
 - aucun indicateur pour les zones de moins de 50 ménages fiscaux.
 - 2 indicateurs pour les zones de 50 ménages fiscaux à moins de 2 000 personnes au sens du ménage fiscal.
 - 23 indicateurs pour les zones de 2 000 personnes ou plus au sens du ménage fiscal

### Par ménage :

Le revenu fiscal par ménage correspond à l'ensemble des revenus déclarés par les foyers fiscaux qui composent le ménage fiscal. Cette unité d'observation permet de raisonner en termes de "masse" des revenus déclarés au sein d'une zone.

 - NBMEN11 : **Nb de ménages fiscaux**
 - RFMQ111 : **1er quartile (€)**
 - RFMQ211 : **Médiane (€)**
 - RFMQ311 : **3ème quartile (€)**
 - RFMIQ11 : **Écart interquartile (€)**
 - RFMD111 : **1er décile (€)**
 - RFMD211 : **2ème décile (€)**
 - RFMD311 : **3ème décile (€)**
 - RFMD411 : **4ème décile (€)**
 - RFMD611 : **6ème décile (€)**
 - RFMD711 : **7ème décile (€)**
 - RFMD811 : **8ème décile (€)**
 - RFMD911 : **9ème décile (€)**
 - RFMRD11 : **Rapport interdécile**
 - RFMET11 : **Ecart-type (€)**

### Par personne :

Le revenu fiscal par personne est le revenu du ménage rapporté au nombre de personnes qui le composent. Le nombre de personnes du ménage fiscal est obtenu par cumul des personnes inscrites sur les déclarations de revenus qui le composent. On adopte le terme de personne et non celui d'habitant pour marquer le fait que toute personne rattachée fiscalement à un ménage ne vit pas forcément au sein de celui-ci : elle peut habiter ailleurs, cas fréquent chez les étudiants (rattachés fiscalement à leurs parents tout en occupant un logement indépendant).

 - NBPERS11 : **Nb de ménages fiscaux**
 - RFPQ111 : **1er quartile (€)**
 - RFPQ211 : **Médiane (€)**
 - RFPQ311 : **3ème quartile (€)**
 - RFPIQ11 : **Écart interquartile (€)**
 - RFPD111 : **1er décile (€)**
 - RFPD211 : **2ème décile (€)**
 - RFPD311 : **3ème décile (€)**
 - RFPD411 : **4ème décile (€)**
 - RFPD611 : **6ème décile (€)**
 - RFPD711 : **7ème décile (€)**
 - RFPD811 : **8ème décile (€)**
 - RFPD911 : **9ème décile (€)**
 - RFPRD11 : **Rapport interdécile**
 - RFPET11 : **Ecart-type (€)**

### Par Unité de consommation :

Le revenu fiscal par unité de consommation (UC) est le revenu du ménage rapporté au nombre d'unités de consommation qui le composent. Par convention, le nombre d'unités de consommation d'un " ménage fiscal " est évalué de la manière suivante :
- le premier adulte du ménage compte pour une unité de consommation ; 
- les autres personnes de 14 ans ou plus comptent chacune pour 0,5 ; 
- les enfants de moins de 14 ans comptent chacun pour 0,3. 
Cette échelle d'équivalence est utilisée couramment par l'Insee et Eurostat pour étudier les revenus ainsi exprimés par  "équivalent adulte".

Le revenu fiscal exprimé par UC présente l'avantage de prendre en compte les diverses compositions des ménages et donc les économies d'échelle liées à la vie en groupe. Dans de nombreux cas, l'étude des revenus se place dans une problématique de comparaison des niveaux de revenu entre plusieurs zones ou d'analyse des inégalités de revenus entre les ménages au sein d'une zone. L'utilisation du revenu rapporté au nombre d'unités de consommation du ménage est alors préconisé car il devient un revenu par équivalent adulte, comparable d'un lieu à un autre et entre ménages de compositions différentes.

 - NBUC11 : **Nombre d'UC**
 - RFUCQ111 : **1er quartile (€)**
 - RFUCQ211 : **Médiane (€)**
 - RFUCQ311 : **3ème quartile (€)**
 - RFUCIQ11 : **Écart interquartile (€)**
 - RFUCD111 : **1er décile (€)**
 - RFUCD211 : **2ème décile (€)**
 - RFUCD311 : **3ème décile (€)**
 - RFUCD411 : **4ème décile (€)**
 - RFUCD611 : **6ème décile (€)**
 - RFUCD711 : **7ème décile (€)**
 - RFUCD811 : **8ème décile (€)**
 - RFUCD911 : **9ème décile (€)**
 - RFUCRD11 : **Rapport interdécile**
 - RFUCET11 : **Ecart-type (€)**
 - RFUCGI11 : **Indice de Gini**. Indicateur du degré de concentration des revenus fiscaux par UC parmi les personnes de la zone étudiée. Il est compris entre 0 (concentration minimale lorsque toutes les personnes présentent un revenu identique) et 1 (concentration maximale lorsqu’une seule personne concentre la totalité des revenus de la zone).

### Indicateur de structure :

 - PMIMP11 : **Part des ménages imposés (%)**
 - PTSA11 : **Part des traitements/ salaires (%)**. Pourcentage que représentent les revenus d'activités salariées dans le total des revenus fiscaux de la zone. Les revenus d'activités salariées incluent les salaires, indemnités journalières de maladie, indemnités de chômage, avantages en nature, certaines préretraites mais aussi les revenus perçus à l’étranger par des résidents en France (ces revenus sont comptés par défaut dans les revenus d'activités salariées car la déclaration de revenus ne permet pas de les ventiler par catégorie)
 - PCHO11 : **dont indemnités de chômage (%)**. Donne la part de ces indemnités dans le revenu total.
 - PPEN11 : **Part des pensions/retraites/rentes (%)**. Pourcentage que représentent les pensions, retraites et rentes dans le total des revenus fiscaux de la zone, net des pensions alimentaires versées. Les pensions, retraites et rentes incluent les retraites mais aussi les pensions d’invalidité et les pensions alimentaires nettes (déduction faites des pensions versées) et les rentes viagères (à titre gratuit et onéreux).
 - PBEN11 : **Part des bénéfices (%)**. Pourcentage que représentent les revenus des activités non salariées dans le total des revenus fiscaux de la zone, net de déficits. Il s’agit des revenus nets de déficits et hors plus-values des indépendants. Ils comprennent les Bénéfices Agricoles (BA), les Bénéfices Industriels et Commerciaux professionnels (BIC) et les Bénéfices Non Commerciaux professionnels (BNC). Sur la déclaration, les indépendants relevant du régime micro-entreprise pour les BIC et du régime déclaratif spécial pour les BNC reportent le montant hors taxes du chiffre d’affaires ou des recettes. Pour les autres régimes, c’est un bénéfice net de déficit qui est reporté.
 - PAUT11 : **Part des autres revenus (%)**. Pourcentage que représentent les revenus du patrimoine déclarés et autres revenus dans le total des revenus fiscaux de la zone. Ils comprennent essentiellement des revenus du patrimoine : les revenus des valeurs et capitaux mobiliers imposables au titre de l’IRPP ainsi que les produits de placement soumis à prélèvement libératoire indiqués sur la déclaration de revenus (ce qui exclut les revenus défiscalisés comme le livret A et une partie des produits de placements soumis à prélèvement libératoire non déclarés), les revenus fonciers nets (loyers, fermages, parts de SCI, affichage), les revenus accessoires (Bénéfices Industriels et Commerciaux (BIC) non professionnels, des Bénéfices Non Commerciaux (BNC) non professionnels, et recettes brutes de locations meublées non professionnelles).

## Nombre d'équipements et de services dans le domaine de l'action sociale en 2013 :

 - NB_D401 : **Personnes âgées : hébergement**. Etablissement d'hébergement pour personnes âgées. Hospices, maisons de retraite, logements foyers et résidences d'hébergement temporaire. 
 - NB_D402 : **Personnes âgées : soins à domicile**. Services de soins à domicile et centres de jour pour personnes âgées. Localisé au siège du service.
 - NB_D403 : **Personnes âgées : services d'aide**. Services d'aide ménagère à domicile, alarme médico-sociale et services d'aide aux personnes âgées. Localisé au siège du service.
 - NB_D404 : **Personnes âgées : foyer restaurant**. Foyer club restaurant.
 - NB_D405 : **Personnes âgées : services de repas à domicile**. Localisé au siège du service.
 - NB_D501 : **Garde d'enfant d'âge préscolaire**. Crèches collectives ou parentales, haltes-garderie y compris parentales, garderies et jardins d'enfants, établissement d'accueil collectif et/ou familial y compris parental.
 - NB_D601 : **Enfants handicapés : hébergement**. Institut médico-éducatif, médico-pédagogique, médico-professionnel, jardin d'enfants spécialisé, institut de rééducation, établissement pour déficients moteurs et/ou cérébraux, visuels et/ou auditifs, centre d'accueil familial spécialisé et foyer d'hébergement.
 - NB_D602 : **Enfants handicapés :services à domicile ou ambulatoires**. Service d'éducation spéciale et de soins à domicile, centre médico-psycho-pédagogique (CMPP), centre action médico-sociale précoce (CAMSP), bureau d'aide psychologique universitaire (BAPU).
 - NB_D603 : **Adultes handicapés : hébergement**. Centre de placement familial, foyer d'hébergement, maison d’accueil spécialisée (MAS), foyer occupationnel, foyer d'accueil médicalisé (FAM)
 - NB_D604 : **Adultes handicapés : services**. Centre de pré-orientation, de rééducation professionnelle, service auxiliaire de vie, service d'accompagnement à la vie sociale (SAVS).
 - NB_D605 : **Travail protégé**. Centre d’aide par le travail (CAT) et atelier protégé.
 - NB_D701 : **Aide sociale à l'enfance : hébergement**. Etablissement d'accueil mère-enfant, pouponnière à caractère social, foyer de l'enfance, village et maison d'enfants à caractère social, centre de placement familial socio-éducatif. Tutelle des conseils généraux. 
 - NB_D702 : **Aide sociale à l'enfance : action éducative**. Foyer d'action éducative (FAE), service éducatif auprès des tribunaux (SEAT), centre d'action éducative (CAE), service d'action éducative en milieu ouvert (AEMO).
 - NB_D703 : **CHRS : centre d'hébergement et de réadaptation sociale**
 - NB_D704 : **Centre provisoire d'hébergement**
 - NB_D705 : **Centre accueil demandeur d'asile**
 - NB_D709 : **Autres établissements pour adultes et familles en difficulté**. Aire de stationnement pour nomades, foyer d'hébergement de travailleurs migrants, foyer de jeunes travailleurs, hébergement des familles de malades, logement-foyer non-spécialisé.
 - nb_equipement_social :  Somme de l'ensemble des indicateurs non détaillés.



















