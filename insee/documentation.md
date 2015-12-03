# Documentation

Insee's files are often in xls format and not easy to reuse (with different pages, header lines etc). This script aggregates the 650 indicators available for each Iris in one single clean file.

In the `output.csv` the column names are like `NB_B314`  (which is the number of gas station by iris) so **this document enumerates each column and explains it**. Decription is in French as all the data concerne French's city.


## List of file :

- [Nombre d'équipements et de services dans le domaine du commerce en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-du-commerce-en-2013)
- [Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-du-sport-des-loisirs-et-de-la-culture-en-2013)
- [Nombre d'équipements et de services dans le domaine de l'enseignement du 1er degré en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-de-lenseignement-du-1er-degr%C3%A9-en-2013)
-  [Nombre d'équipements et de services dans le domaine de l'enseignement du second degré en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-de-lenseignement-du-second-degr%C3%A9-en-2013)
-  [Nombre d'équipements et de services dans le domaine de l'enseignement supérieur, de la formation et des services de l'éducation en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-de-lenseignement-sup%C3%A9rieur-de-la-formation-et-des-services-de-l%C3%A9ducation-en-2013)
-  [Indicateurs de structure et de distribution des revenus](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#indicateurs-de-structure-et-de-distribution-des-revenus)
-  [Nombre d'équipements et de services dans le domaine de l'action sociale en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-de-laction-sociale-en-2013)
-  [Nombre d'équipements et de services de santé en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-de-sant%C3%A9-en-2013)
-  [Nombre de fonctions médicales et paramédicales en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-de-fonctions-m%C3%A9dicales-et-param%C3%A9dicales-en-2013)
-   [Nombre d'équipements des services aux particuliers en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-des-services-aux-particuliers-en-2013)
-   [Nombre d'équipements et de services dans le domaine du tourisme et du transport en 2013](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#nombre-d%C3%A9quipements-et-de-services-dans-le-domaine-du-tourisme-et-du-transport-en-2013)
-	[Base de données infracommunales : logement en 2011](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#base-de-données-infracommunales--logement-en-2011)
-	[Base de données infracommunales : diplômes - formation en 2011](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#base-de-données-infracommunales--diplômes---formation-en-2011)
-	[Base de données infracommunales : couples - familles - ménages en 2011](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#base-de-données-infracommunales--couples---familles---ménages-en-2011)
-	[Base de données infracommunales : population en 2011](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#base-de-données-infracommunales--population-en-2011)
-	[Base de données infracommunales : activité des résidents en 2011](https://github.com/armgilles/open-moulinette/blob/insee/insee/documentation.md#base-de-données-infracommunales--activité-des-résidents-en-2011)

## Description géographique

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

## Précisions

Certains indicateurs sont en doublons (ils apparaissent dans plusieurs fichiers) :
- P11_PMEN
- P11_POP0610
- P11_POP1824
- P11_POP1524
- P11_POP2554
- P11_POP80P
- P11_POP5564

Ils ont été dédoublonner dans le fichier final car ils ont strictement les même valeurs suivant leurs fichiers d'origines. Cependant ces doublons ont été garder dans cette documentation pour une meilleur compréhension.

##Nombre d'équipements et de services dans le domaine du commerce en 2013

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
 - - nb_commerce : somme de l'ensemble des indicateurs du fichiers.

##Nombre d'équipements et de services dans le domaine du sport, des loisirs et de la culture en 2013

 - NB_F101 : **Bassin de natation**. Bassins de natation, sportive et/ou ludique
 - NB_F101_NB_AIREJEU : **Bassin de natation - nombre de bassins**
 - NB_F101_NB_COU : **Bassin de natation avec au moins un bassin couvert**
 - NB_F101_NB_ECL : **Bassin de natation avec au moins un bassin éclairé**
 - NB_F102 : **Boulodrome**
 - NB_F102_NB_AIREJEU : **Boulodrome - nombre de terrains**. Terrain de boules, de pétanque 
 - NB_F102_NB_COU : **Boulodrome avec au moins un terrain couvert**
 - NB_F102_NB_ECL : **Boulodrome avec au moins un terrain éclairé**
 - NB_F103 : **Tennis**
 - NB_F103_NB_AIREJEU : **Tennis - nombre de courts**
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
 - NB_F301 : **Cinéma**. Projection en salle de cinéma, en plein air ou autres. Implantations physiques, qu'il y ait une seule salle de projection ou plusieurs au sein d'un complexe. Il n'y a ni le nombre de salles présentes, ni leur nombre de places offertes.
 - NB_F302 : **Théâtre**. Ensemble des lieux gérés par le Centre National du Théâtre où une représentation de théâtre peut se tenir. Ces lieux peuvent être labellisés (théâtres nationaux et privés, scènes nationales et conventionnées, compagnies avec lieux d’accueil, compagnies dramatiques nationales et régionales, pôles cirque, centres chorégraphiques) ou non. 
 - NB_F302_NB_SALLES : **Théâtre - nombre de salles**
 - nb_sport : Somme de l'ensemble des indicateurs non détaillés : uniquement les **NB_F1.**  (cf ci-dessous)
 - nb_nb_airjeu_sport : Somme de l'ensemble des indicateurs air de jeux : uniquement les **NB_F1.._NB_AIREJEU**


**Note :** Pour chacune des installations sportives, on dispose de plusieurs informations : 
exemple pour les bassins de natation de la commune de Marseille  

- NB_F101           : 38  bassins de natation (installations pour la natation)
- NB_F101_NB_BASNAT : 47  cumul des bassins de natation dénombrés dans les 38 installations localisées
- NB_F101_NB_COU    : 25  installations sur les 38 disposent d'au moins un bassin couvert 
- NB_F101_NB_ECL    : 27  installations sur les 38 possèdant un éclairage

Il en va de même pour les autres installations sportive **NB_F1..**


##Nombre d'équipements et de services dans le domaine de l'enseignement du 1er degré en 2013

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


##Nombre d'équipements et de services dans le domaine de l'enseignement du second degré en 2013 

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


##Nombre d'équipements et de services dans le domaine de l'enseignement supérieur, de la formation et des services de l'éducation en 2013

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
 - nb_enseignement_sup : Somme de l'ensemble des indicateurs non détaillés (NB_C605_NB_INT, NB_C701, NB_C702 sont exclus).

##Indicateurs de structure et de distribution des revenus

Les revenus fiscaux localisés des ménages sont établis à partir des fichiers exhaustifs des déclarations de revenus des personnes physiques, de la taxe d'habitation et du fichier d’imposition des personnes physiques fournis à l'Insee par la Direction générale des finances publiques.

**Note** : La liste des indicateurs disponibles varie selon les seuils de population (nombre de ménages fiscaux ou population fiscale). Is se peux donc que certain des indicateurs soient vide :
 - aucun indicateur pour les zones de moins de 50 ménages fiscaux.
 - 2 indicateurs pour les zones de 50 ménages fiscaux à moins de 2 000 personnes au sens du ménage fiscal.
 - 23 indicateurs pour les zones de 2 000 personnes ou plus au sens du ménage fiscal

###Par ménage :

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

###Par personne :

Le revenu fiscal par personne est le revenu du ménage rapporté au nombre de personnes qui le composent. Le nombre de personnes du ménage fiscal est obtenu par cumul des personnes inscrites sur les déclarations de revenus qui le composent. On adopte le terme de personne et non celui d'habitant pour marquer le fait que toute personne rattachée fiscalement à un ménage ne vit pas forcément au sein de celui-ci : elle peut habiter ailleurs, cas fréquent chez les étudiants (rattachés fiscalement à leurs parents tout en occupant un logement indépendant).

 - NBPERS11 : **Nb de personnes des ménages fiscaux**
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

###Par Unité de consommation :

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

###Indicateur de structure :

 - PMIMP11 : **Part des ménages imposés (%)**
 - PTSA11 : **Part des traitements/ salaires (%)**. Pourcentage que représentent les revenus d'activités salariées dans le total des revenus fiscaux de la zone. Les revenus d'activités salariées incluent les salaires, indemnités journalières de maladie, indemnités de chômage, avantages en nature, certaines préretraites mais aussi les revenus perçus à l’étranger par des résidents en France (ces revenus sont comptés par défaut dans les revenus d'activités salariées car la déclaration de revenus ne permet pas de les ventiler par catégorie)
 - PCHO11 : **dont indemnités de chômage (%)**. Donne la part de ces indemnités dans le revenu total.
 - PPEN11 : **Part des pensions/retraites/rentes (%)**. Pourcentage que représentent les pensions, retraites et rentes dans le total des revenus fiscaux de la zone, net des pensions alimentaires versées. Les pensions, retraites et rentes incluent les retraites mais aussi les pensions d’invalidité et les pensions alimentaires nettes (déduction faites des pensions versées) et les rentes viagères (à titre gratuit et onéreux).
 - PBEN11 : **Part des bénéfices (%)**. Pourcentage que représentent les revenus des activités non salariées dans le total des revenus fiscaux de la zone, net de déficits. Il s’agit des revenus nets de déficits et hors plus-values des indépendants. Ils comprennent les Bénéfices Agricoles (BA), les Bénéfices Industriels et Commerciaux professionnels (BIC) et les Bénéfices Non Commerciaux professionnels (BNC). Sur la déclaration, les indépendants relevant du régime micro-entreprise pour les BIC et du régime déclaratif spécial pour les BNC reportent le montant hors taxes du chiffre d’affaires ou des recettes. Pour les autres régimes, c’est un bénéfice net de déficit qui est reporté.
 - PAUT11 : **Part des autres revenus (%)**. Pourcentage que représentent les revenus du patrimoine déclarés et autres revenus dans le total des revenus fiscaux de la zone. Ils comprennent essentiellement des revenus du patrimoine : les revenus des valeurs et capitaux mobiliers imposables au titre de l’IRPP ainsi que les produits de placement soumis à prélèvement libératoire indiqués sur la déclaration de revenus (ce qui exclut les revenus défiscalisés comme le livret A et une partie des produits de placements soumis à prélèvement libératoire non déclarés), les revenus fonciers nets (loyers, fermages, parts de SCI, affichage), les revenus accessoires (Bénéfices Industriels et Commerciaux (BIC) non professionnels, des Bénéfices Non Commerciaux (BNC) non professionnels, et recettes brutes de locations meublées non professionnelles).

##Nombre d'équipements et de services dans le domaine de l'action sociale en 2013

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
 - nb_equipement_social :  Somme de l'ensemble des indicateurs.


##Nombre d'équipements et de services de santé en 2013

 - NB_D101 : **Etablissement santé court séjour**. Etablissement hospitalier (y compris cliniques privées) exerçant des soins de courte durée en médecine et/ou chirurgie. Contient centres hospitaliers et hôpitaux locaux, hôpitaux des armées. Les syndicats inter-hospitalier avec discipline de soins et les autres établissements de la loi hospitalière figurent dans ce groupe. Les établissements de soins du Service de santé des armées ne sont pas suivis (cat 115). Non compris les maternités autonomes classées en NB_D107. On trouve à la même adresse établissements hospitaliers et syndicat inter-hospitalier ou unités de médecine et de chirurgie ou unités avec adresse "administrative" commune.
 - NB_D102 : **Etablissement santé moyen séjour**. Etablissement hospitalier (y compris cliniques privées) exerçant des soins de suite et de réadaptation (ou moyen séjour). Contient les mêmes établissements que NB_D101 s'ils disposent d'un tel service de soins, plus les maisons de régime (cat=119) et les établissements de lutte contre la tuberculose (cat=144), les établissements de convalescence et de repos et ceux de réadaptation fonctionnelle. Sont rajoutés les établissements d'enfants à caractère sanitaire, estimés de moyen séjour (Maisons d'enfants et pouponnières). Pour la catégorie 114 -Hôpital des armées, il n'y a pas moyen de savoir s'il y a du moyen séjour. Ils n'ont été retenus qu'en court séjour (variable NB_D101).
 - NB_D103 : **Etablissement santé long séjour**. Etablissement hospitalier (y compris cliniques privées) exerçant des soins de longue durée.
 - NB_D104 : **Etablissement psychiatrique**. Centre hospitalier spécialisé contre les maladies mentales (CHS) ou établissements hospitaliers (y compris cliniques privées) exerçant des soins de psychiatrie adulte et/ou infanto juvénile. Structures avec hébergement : y compris les maisons de santé pour maladies mentales et les centres de postcure pour malades mentaux.
 - NB_D105 : **Centre lutte cancer**. Etablissement hospitalier non regroupé autre part.
 - NB_D106 : **Urgences**. Services d'intervention (SAMU -SMUR) et d'accueil des urgences.
 - NB_D107 : **Maternité**. Soins en gynécologie et obstétrique. Etablissements autonomes ou activité parmi d'autres au sein d'un établissement hospitalier.
 - NB_D108 : **Centre de santé**. Dispensaires ou centres de soins dentaires, médicaux, infirmiers ou polyvalents. Les centres d'examen ne peuvent être assimilés à des centres de soins et ont été classés en NB_D110. On trouve à la même adresse centre médical et centre dentaire ou centre infirmier.
 - NB_D109 : **Structures psychiatriques en ambulatoire**. Centre médico psychologique, atelier ou appartement thérapeutique, accueil thérapeutique à temps partiel, centre de crise. Structures sans hébergement. Ce sont aussi des établissements relevant de la loi hospitalière. On trouve à la même adresse des unités soumises à des gestions différentes (tarification, tutelle ...).
 - NB_D110 : **Centre médecine préventive**. Dispensaires antituberculeux, antivénériens, antihansénien, centre de vaccination BCG, de consultation pour le cancer, d'examens de santé et polyvalents. Pour ces catégories, il n'y a pas d'autorisation.
 - NB_D111 : **Dialyse**. Relève de la loi hospitalière. Centres de dialyse ambulatoire, qu'ils soient autonomes ou que ce soit une activité parmi d'autres au sein d'un établissement. On trouve à la même adresse le centre de dialyse et la structure alternative de dialyse à domicile.
 - NB_D112 : **Hospitalisation à domicile**. Relève de la loi hospitalière. Hors dialyse. Il y a très peu d'établissements pratiquant uniquement l'hospitalisation à domicile.
 - NB_D113 : **Maison de santé Pluridisciplinaires**. Elles regroupent dans un cadre d’exercice libéral des professionnels médicaux et paramédicaux
 - NB_D301 : **Pharmacie** y compris commerce de produits vétérinaires, herboristerie.
 - NB_D302 : **Laboratoire d'analyses médicales**. Laboratoires ouverts au public ; les services d'analyses biologiques des établissements hospitaliers n'y figurent pas.
 - NB_D303 : **Ambulance**. Activité pouvant être exercée avec celle de taxi en milieu rural.
 - NB_D304 : **Transfusion sanguine**. Etablissements autonomes.
 - NB_D305 : **Etablissement thermal**. Relève de la loi hospitalière.
 - NB_D306 : **Etablissement lutte contre l'alcoolisme**. Centre de postcure pour alcooliques et centres de soins spécialisés pour toxicomanes.
 - nb_equipement_sante : Somme de l'ensemble des indicateurs.
 
##Nombre de fonctions médicales et paramédicales en 2013

**Note** : 
- NB_D201 à NB_D213 sont retenus les praticiens exerçant leur activité en dehors d'un établissement sanitaire, puisque ceux-ci sont appréhendés dans FINESS. Sont donc exclus par exemple les médecins fonctionnaires et les médecins salariés exerçant en établissement sanitaire ou leur partie d'activité y est exercée. Dans la source peuvent être mentionnées plusieurs adresses d'exercice. Sont seules retenues celles répondant aux critères en tête de colonne. Ainsi un salarié hospitalier exerçant aussi en cabinet libéral à une autre adresse que celle de l'hôpital (ou de la clinique) ne sera retenu qu'à l'adresse(s) du cabinet. 
Ne sont retenues que les spécialités proposées par la DREES, les plus importantes en effectifs de libéraux et où au moins la moitié des praticiens exercent sous forme libérale. Si le praticien exerce dans plusieurs spécialités, seule la principale a été retenue. 
- NB_D231 à NB_D240 : Auxiliaires médicaux. N'ont pas été retenues les catégories Infirmiers psychiatriques et Psychologues, non présentées par la DREES dans ses publications. Certaines professions sont peu nombreuses et/ou n'exercent pas en libéral, par exemple les psychomotriciens et les ergothérapeutes.

- NB_D201 : **Médecin omnipraticien**. Médecin "généraliste", y compris compris médecins non-spécialistes ayant une compétence particulière (acupuncteurs, homéopathes, allergologues, gynécologues ...)
- NB_D202 : **Spécialiste en cardiologie**
- NB_D203 : **Spécialiste en dermatologie vénéréologie**
- NB_D204 : **Spécialiste en gynécologie médicale**
- NB_D205 : **Spécialiste en gynécologie obstétrique**
- NB_D206 : **Spécialiste en gastro-entérologie hépatologie**
- NB_D207 : **Spécialiste en psychiatrie**
- NB_D208 : **Spécialiste en ophtalmologie**
- NB_D209 : **Spécialiste en oto-rhino-laryngologie**
- NB_D210 : **Spécialiste en pédiatrie**
- NB_D211 : **Spécialiste en pneumologie**
- NB_D212 : **Spécialiste en radiodiagnostic et imagerie médicale**
- NB_D213 : **Spécialiste en stomatologie**
- NB_D221 : **Chirurgien dentiste**
- NB_D231 : **Sage-femme**
- NB_D232 : **Infirmier**
- NB_D233 : **Masseur kinésithérapeute**
- NB_D235 : **Orthophoniste**
- NB_D236 : **Orthoptiste**
- NB_D237 : **Pédicure-podologue**
- NB_D238 : **Audio prothésiste**. Pour appréhender tous les lieux où le service est rendu, ont été retenus tous les professionnels exerçant à titre libéral ou comme salariés du privé, à l'exclusion des structures ne recevant pas habituellement du public (étab. d'enseignement, administration, entreprises ...). Possibilité d'avoir un ou plusieurs libéraux et/ou un ou plusieurs salariés à la même adresse.
- NB_D239 : **Ergothérapeute**
- NB_D240 : **Psychomotricien**
- nb_fonction_medical : Somme de l'ensemble des indicateurs.


##Nombre d'équipements des services aux particuliers en 2013

- NB_A101 : **Police**. Ces services de la sécurité publique (hors CRS, police de l'air et des frontières, services régionaux des renseignements généraux, services de contrôle de l'immigration, services généraux d'administration de la police) ne comprennent pas les services nationaux, et non plus les services de police municipale (peu nombreux).
- NB_A104 : **Gendarmerie**. Unité de gendarmerie recevant du public. Comprend les brigades territoriales autonomes, les brigades territoriales de proximité, les communautés de brigades.
- NB_A105 : **Cour d’appel**. La cour d'appel réexamine les affaires déjà jugées en premier degré (1er ressort ou 1ère instance) en matière civile, commerciale, sociale ou pénale. Seule exception : les appels des décisions des cours d'assises sont jugés par une autre cour d'assises.
La cour d’appel est composée uniquement de magistrats professionnels.
- NB_A106 : **Tribunal de grande instance**. Le tribunal de grande instance a large compétence en matière civile. Il tranche ; les litiges civils opposant des personnes privées (physiques ou morales) qui ne sont pas attribués par la loi à une autre juridiction civile ; les litiges civils portant sur des sommes supérieures à 10 000 euros. 
Le tribunal de grande instance a aussi compétence exclusive pour de nombreuses affaires quel que soit le montant de la demande : état des personnes, famille, rectifications d’actes civils, successions, actions civiles pour diffamation ou injures, immobilier, brevets d’invention, droit des marques, … Il est composé d’un ou plusieurs juges professionnels
- NB_A107 : **Tribunal d’instance**. Le tribunal d’instance a une compétence générale pour tous les petits délits civils. Il juge toutes les affaires conflictuelles (accidents de la circulation, charges de copropriétés, dettes, malfaçons, crédits à la consommation, …) où les demandes portent sur des sommes inférieures à 10 000 euros.
 Il juge des tutelles et statue sur les demandes d’ouverture d’un régime de protection. Il juge également les conflits non réglés par le juge de proximité.
Il est composé d’un ou plusieurs juges professionnels.
- NB_A108 : **Conseil de prud’hommes**. Le conseil de prud'hommes règle les litiges individuels (congés payés, salaires, primes, licenciement, clause de non-concurrence, durée du préavis) qui surviennent entre salariés ou apprentis et employeurs, à l'occasion du contrat de travail ou d'apprentissage…, à l'exception des litiges collectifs, comme l'exercice du droit de grève. Ce tribunal est composé de juges non professionnels élus, représentant, en nombre égal et pour moitié, les employeurs et les salariés. Chaque conseil de prud’hommes est divisé en 5 sections, représentant les principaux secteurs du monde du travail : encadrement, industrie, commerce et services commerciaux, agriculture, activités diverses.
- NB_A109 : **Tribunal de commerce**. Le tribunal de commerce tranche, de manière générale, les litiges entre commerçants ou entre commerçants et sociétés commerciales, et ceux qui portent sur les actes de commerce.
Il est composé de juges non professionnels, des commerçants bénévoles, élus pour 2 ou 4 ans par d’autres commerçants.
- NB_A110 : **Agence de proximité**. Elle constitue la majorité des unités opérationnelles du réseau de proximité. Elle rend tous les services de Pôle Emploi. 
- NB_A111 : **Relais pôle emploi**. Il appartient au réseau de proximité et se situe dans des communes à plus de 30 minutes ou 30 kilomètres de l’agence de proximité et a suffisamment de demandeurs d’emploi concernés pour justifier la présence d’au moins 7 conseillers de pôle emploi en permanence.
- NB_A112 : **Permanence pôle emploi**. Elle appartient au réseau de proximité et se caractérise par la présence planifiée et régulière d’un conseiller, une demi-journée par mois au moins pour des entretiens de suivi sur rendez-vous. Ce lieu est porté par un partenaire.
- NB_A115 : **Agence spécialisée**. Elle intervient sur des segments spécifiques de public : cadre, spectacle, emploi à l’international, etc.
- NB_A116 : **Relais et maison de service publicAgence thématique**. Ce sont des lieux d’accueil, d’information et d’orientation à destination des usagers des services publics, et regroupant, en particulier, l’ensemble des services sur l’emploi. Ils permettent d’améliorer la proximité et l’accessibilité des services.
- NB_A117 : **Point d'information et de médiation multiservices**. Ces services sont liés à la politique de la ville. Animés par une équipe de professionnels,  ils proposent des services de proximité à la disposition des habitants et facilitent ainsi l’utilisation des services publics. 
- NB_A118 : **Espace public numérique et autres**. Il propose un accompagnement à la recherche d’emploi : recherche sur internet, mise en page de CV, lettres de motivation, etc …
- NB_A119 : **DGFiP**. Elle scelle la fusion de la Direction Générale des Impôts (DGI) et de la Direction Générale de la Comptabilité Publique (DGCP) au niveau national.
- NB_A120 : **DRFiP**. Elle s’inscrit dans la démarche nationale de rapprochement des deux administrations,  des impôts et de la comptabilité publique dans chaque région.
- NB_A121 : **DDFiP**. La création des DDFiP s’inscrit dans la démarche nationale de rapprochement des deux administrations des impôts et de la comptabilité publique. Dans les départements, les trésoreries générales et les directions des services fiscaux ont fusionné au sein d’une direction départementale avec à leur tête un responsable unique.
- NB_A203 : **Banque, Caisse d'Epargne**. Etablissements de crédit agréés, y compris banques mutualistes ou coopératives et caisses d'épargne et de prévoyance. Ne comprend pas les guichets financiers de La Poste.
Fait apparaître, en plus des agences recherchées, des services administratifs ou des Points-contacts que l'on ne peut pas distinguer des guichets.
- NB_A205 : **Pompes funèbres**. Comprend les activités de pompes funèbres quelle que soit la forme juridique (mise en bière, transport, services d'inhumation ou de crémation).
- NB_A206 : **Bureau de poste**. Le bureau de poste, en gestion directe par La Poste, offre la totalité des produits et services délivrés à la population tant pour ce qui concerne le courrier et les colis (courrier simple, recommandé, réexpédition, prêt à poster, …) que pour les services financiers (ouverture de comptes, dépôts, retraits, assurances-vie, PEL, actions, …).
- NB_A207 : **Relais poste commerçant**. Le relais poste commerçant est géré principalement par des commerçants dans le cadre de conventions de partenariat signées entre La Poste et des partenaires privés.
Il offre une grande partie des produits et services de proximité délivrés à la population concernant le courrier et les colis (courrier simple, recommandé, prêt à poster, à l’exception de l’établissement d’une procuration postale…).  Les services financiers sont limités au retrait d’espèces (maximum 150 euros par semaine) et au paiement de mandat cash.
- NB_A208 : **Agence postale communale**. L’agence postale communale est gérée par des agents territoriaux dans le cadre de conventions de partenariat signées entre La Poste et les communes concernées. 
Elle offre une grande partie des produits et services délivrés à la population tant pour ce qui concerne le courrier et les colis (comparable aux prestations des bureaux de poste) que pour les services financiers (légèrement moindre aux prestations des bureaux de poste : ouverture de compte et produits financiers d’assurance-vie, PEL ou actions impossibles).
- NB_A301 : **Réparation auto et de matériel agricole**.  Le code APE principal ne suffit pas pour distinguer l'activité, notamment en zone rurale. On complète la recherche sur le code APRM (activité artisanale), cette activité étant souvent exercée derrière une activité principale de commerce. On n'a retenu dans ce cas que les unités exerçant une activité de réparation complémentaire du commerce de véhicules automobiles, du commerce de détail de carburants et du commerce de gros de matériel agricole.
- NB_A302 : **Contrôle technique automobile**. Contrôle périodique des véhicules avec délivrance d'un certificat.
- NB_A303 : **Location auto-utilitaires légers**. Location sans chauffeur, y compris d'utilitaires légers.
- NB_A304 : **Ecole de conduite**.  Inclus les écoles de formation à la conduite sportive, au pilotage (autre que professionnel) de bateaux et d'avions.
- NB_A401 : **Maçon**. Il s'agit de l'activité principale déclarée. Il y a souvent multi-activité chez les artisans.
- NB_A402 : **Plâtrier peintre**.  Il s'agit de l'activité principale déclarée. Possibilité d'une seule des activités citées ou de multi-activité.
- NB_A403 : **Menuisier, charpentier, serrurier**.  Il s'agit de l'activité principale déclarée. Possibilité d'une seule des activités citées ou de multi-activité.
- NB_A404 : **Plombier, couvreur, chauffagiste**. Il s'agit de l'activité principale déclarée. Possibilité d'une seule des activités citées ou de multi-activité.
- NB_A405 : **Electricien**.  Il s'agit de l'activité principale déclarée. Possibilité d'une seule des activités citées ou de multi-activité.
- NB_A406 : **Entreprise générale du bâtiment**.  Il s'agit de l'activité principale déclarée. Possibilité d'une seule des activités citées ou de multi-activité.
- NB_A501 : **Coiffure**. Comprend les salons et la coiffure à domicile.
- NB_A502 : **Vétérinaire**. Services en clinique, en cabinet ou en visite pour animaux d'élevage ou de compagnie.
- NB_A503 : **Agence de travail temporaire**.  Fourniture, sur une base temporaire, de personnel intérimaire.
- NB_A504 : **Restaurant**. Ne comprend plus tous les hôtels-restaurants en raison du passage à la NAF rév.2 qui sépare les 2 activités. Différence d'environ 17 000 hôtels-restaurants à compter de 2009
- NB_A505 : **Agence immobilière**. Activités intermédiaires en achat, vente et location de biens immobiliers, fonciers et commerciaux.
- NB_A506 : **Blanchisserie-Teinturerie**. Comprend l'activité des blanchisseries de détail, y compris les dépôts, le service des laveries automatiques en libre service, le nettoyage des vêtements (pressing).
- NB_A507 : **Soins de beauté**. Soins esthétiques, de manucure et de pédicure.
- nb_service_particulier : Somme de l'ensemble des indicateurs.

##Nombre d'équipements et de services dans le domaine du tourisme et du transport en 2013

 - NB_E101 : **Taxi**
 - NB_E102 : **Aéroport** en activité avec plus de 1 000 passagers (mouvement commercial au départ ou à l’arrivée de l’aéroport hors transit).
 - NB_E103 : **Gare avec train TAGV (train à grande vitesse)**. Gare desservie par au moins un train à grande vitesse
 - NB_E104 : **Gare sous convention avec l’État**. Gare desservie par au moins un train sous convention avec l’État (sans TAGV)
 - NB_E105 : **Gare sous convention avec les conseils régionaux ou les STIF**. Gare desservie par au moins un train sous convention avec les conseils régionaux ou les STIF (transport Île de France) (sans TAGV et sans convention État)
 - NB_G101 : **Agence de voyage**. Agences de voyage et voyagistes. Ne comprend plus les services de réservation et d'information touristique suite au passage à la NAF rév.2. Différence de -2 800 à compter de 2009.
 - NB_G102 : **Hôtel homologué**. Hôtels homologués, auxquels sont rajoutés les hôtels de chaîne à 0 étoile. Ne sont donc pas pris en compte les anciens "hôtels de préfecture". Avec ou sans restaurant.
 - NB_G103 : **Camping homologué**. Campings homologués, classés de 0 à 4 étoiles.  Donc y compris campings des comités d'entreprise, à clientèle spécifique (ouvriers, colonies de vacances, forains…) si  cette clientèle est de passage - c'est à dire ne restant pas pendant toute la période d'ouverture du camping - et campings de VVF. 
Non compris services de réservation et activités liées.
 - NB_G104 : **Information Touristique**. Comprend les services de réservation et d'information touristique.
 - nb_transport_tourisme : Somme de l'ensemble des indicateurs.

##Base de données infracommunales : logement en 2011

 - P11_LOG : **Logements en 2011 (princ)**
 - P11_RP : **Résidences principales en 2011 (princ)**
 - P11_RSECOCC : **Rés secondaires et logts occasionnels en 2011 (princ)**
 - P11_LOGVAC : **Logements vacants en 2011 (princ)**
 - P11_MAISON : **Maisons en 2011 (princ)**
 - P11_APPART : **Appartements en 2011 (princ)**
 - P11_RP_1P : **Rés princ 1 pièce en 2011 (princ)**
 - P11_RP_2P : **Rés princ 2 pièces en 2011 (princ)**
 - P11_RP_3P : **Rés princ 3 pièces en 2011 (princ)**
 - P11_RP_4P : **Rés princ 4 pièces en 2011 (princ)**
 - P11_RP_5PP : **Rés princ 5 pièces ou plus en 2011 (princ)**
 - P11_NBPI_RP : **Pièces rés princ en 2011 (princ)**
 - P11_RPMAISON : **Rés princ type maison en 2011 (princ)**
 - P11_NBPI_RPMAISON : **Pièces rés princ type maison en 2011 (princ)**
 - P11_RPAPPART : **Rés princ type appartement en 2011 (princ)**
 - P11_NBPI_RPAPPART : **Pièces rés princ type appartement en 2011 (princ)**
 - P11_RP_M40M2 : **Rés princ de moins de 40 m2 en 2011 (princ)**
 - P11_RP_4099M2 : **Rés princ de 40 à 99 m2 en 2011 (princ)**
 - P11_RP_100M2P : **Rés princ de 100 m2 ou plus en 2011 (princ)**
 - P11_RP_ACHTT  : **Rés princ avt 2009 en 2011 (princ)**
 - P11_RP_ACHT1  : **Rés princ avt 1946 en 2011 (princ)**
 - P11_RP_ACHT2  : **Rés princ 1946 à 1990 en 2011 (princ)**
 - P11_RP_ACHT3  : **Rés princ 1991 à 2008 en 2011 (princ)**
 - P11_RPMAISON_ACHTT : **Rés princ Type maison avt 2009 en 2011 (princ)**
 - P11_RPMAISON_ACHT1  : **Rés princ Type maison avt 1946 en 2011 (princ)**
 - P11_RPMAISON_ACHT2  : **Rés princ Type maison 1946 à 1990 en 2011 (princ)**
 - P11_RPMAISON_ACHT3  : **Rés princ Type maison 1991 à 2008 en 2011 (princ)**
 - P11_RPAPPART_ACHTT  : **Rés princ Type appart avt 2009 en 2011 (princ)**
 - P11_RPAPPART_ACHT1  : **Rés princ Type appart avt 1946 en 2011 (princ)**
 - P11_RPAPPART_ACHT2  : **Rés princ Type appart 1946 à 1990 en 2011 (princ)**
 - P11_RPAPPART_ACHT3  : **Rés princ Type appart 1991 à 2008 en 2011 (princ)**
 - P11_MEN : **Ménages en 2011 (princ)**
 - P11_MEN_ANEM0002 : **Ménages emménagés moins 2 ans en 2011 (princ)**
 - P11_MEN_ANEM0204 : **Ménages emménagés entre 2-4 ans en 2011 (princ)**
 - P11_MEN_ANEM0509 : **Ménages emménagés entre 5-9 ans en 2011 (princ)**
 - P11_MEN_ANEM10P : **Ménages emménagés depuis 10 ans ou plus en 2011 (princ)**
 - P11_PMEN : **Pop ménages en 2011 (princ)**
 - P11_PMEN_ANEM0002 : **Pop mén emménagés moins 2 ans en 2011 (princ)**
 - P11_PMEN_ANEM0204 : **Pop mén emménagés entre 2-4 ans en 2011 (princ)**
 - P11_PMEN_ANEM0509 : **Pop mén emménagés entre 5-9 ans en 2011 (princ)**
 - P11_PMEN_ANEM10P : **Pop mén emménagés depuis 10 ans ou plus en 2011 (princ)**
 - P11_NBPI_RP_ANEM0002 : **Pièces Rés princ Mén. emménagés moins 2 ans en 2011 (princ)**
 - P11_NBPI_RP_ANEM0204 : **Pièces Rés princ Mén. emménagés entre 2-4 ans en 2011 (princ)**
 - P11_NBPI_RP_ANEM0509 : **Pièces Rés princ Mén. emménagés entre 5-9 ans en 2011 (princ)**
 - P11_NBPI_RP_ANEM10P : **Pièces Rés princ Mén. emménagés depuis 10 ans ou plus en 2011 (princ)**
 - P11_RP_PROP : **Rés princ occupées Propriétaires en 2011 (princ)**
 - P11_RP_LOC : **Rés princ occupées Locataires en 2011 (princ)**
 - P11_RP_LOCHLMV : **Rés princ HLM louée vide en 2011 (princ)**
 - P11_RP_GRAT : **Rés princ logé gratuit en 2011 (princ)**
 - P11_NPER_RP : **Personnes Rés princ en 2011 (princ)**
 - P11_NPER_RP_PROP : **Pers Rés princ occupées Propriétaires en 2011 (princ)**
 - P11_NPER_RP_LOC : **Pers Rés princ occupées Locataires en 2011 (princ)**
 - P11_NPER_RP_LOCHLMV : **Pers Rés princ HLM louées vides en 2011 (princ)**
 - P11_NPER_RP_GRAT : **Pers Rés princ occupées gratuit en 2011 (princ)**
 - P11_ANEM_RP : **Anc tot Emméngt Rés princ (années) en 2011 (princ)**
 - P11_ANEM_RP_PROP : **Anc tot Emméngt Rés princ occ par Propriétaires (années) en 2011 (princ)**
 - P11_ANEM_RP_LOC : **Anc tot Emméngt Rés princ occ par Locataires (années) en 2011 (princ)**
 - P11_ANEM_RP_LOCHLMV : **Anc tot Emméngt Rés princ HLM louées vides (années) en 2011 (princ)**
 - P11_ANEM_RP_GRAT : **Anc tot Emméngt Rés princ occ gratuit (années) en 2011 (princ)**
 - P11_RP_SDB : **Rés princ SDB baignoire douche (MET) en 2011 (princ)**
 - P11_RP_CCCOLL : **Rés princ Chauffage Central Collectif (MET) en 2011 (princ)**
 - P11_RP_CCIND : **Rés princ Chauffage Central Individuel (MET) en 2011 (princ)**
 - P11_RP_CINDELEC : **Rés princ Chauffage Individuel Electrique (MET) en 2011 (princ)**
 - P11_RP_GARL : **Ménages au moins un parking en 2011 (princ)**
 - P11_RP_VOIT1P : **Ménages au moins une voiture en 2011 (princ)**
 - P11_RP_VOIT1 : **Ménages une voiture en 2011 (princ)**
 - P11_RP_VOIT2P : **Ménages deux voitures ou plus en 2011 (princ)**
 - P11_RP_ELEC : **Rés princ avec électricité (DOM) en 2011 (princ)**
 - P11_RP_EAUCH : **Rés princ avec eau chaude (DOM) en 2011 (princ)**
 - P11_RP_BDWC : **Rés princ avec Bain/Douche WC (DOM) en 2011 (princ)**
 - P11_RP_CHOS : **Rés princ avec chauffe-eau solaire (DOM) en 2011 (princ)**
 - P11_RP_CLIM : **Rés princ avec pièce climatisée (DOM) en 2011 (princ)**
 - P11_RP_TTEGOU : **Rés princ avec tout à l'égout (DOM) en 2011 (princ)**
 - P11_RP_HABFOR : **Habitations de fortune (DOM) en 2011 (princ)**
 - P11_RP_CASE : **Cases traditionnelles (DOM) en 2011 (princ)**
 - P11_RP_MIBOIS : **Maisons ou Immeubles en bois (DOM) en 2011 (princ)**
 - P11_RP_MIDUR : **Maisons ou Immeubles en dur (DOM) en 2011 (princ)**

##Base de données infracommunales : diplômes - formation en 2011

- **La population non scolarisée** comprend les personnes non inscrites dans un établissement d'enseignement.

- **Population scolarisée** est scolarisé tout individu inscrit, au moment de la collecte du recensement, dans un établissement d'enseignement (y compris apprentissage) pour l'année scolaire en cours.
Remarque(s). Depuis 2004, avec le recensement rénové. Les élèves mineurs résidant dans une cité universitaire sont recensés dans le logement de leurs parents contrairement au recensement de 1999 où ils étaient comptabilisés dans les communautés de la commune de la cité universitaire. Les élèves mineurs vivant en internat sont comptés au lieu de résidence de leurs parents comme au recensement de 1999. Les élèves ou étudiants majeurs résidant dans une cité universitaire sont comptabilisés dans les communautés de la commune de la cité universitaire comme au recensement de 1999. Les élèves ou étudiants majeurs vivant en internat (lycée agricole, école militaire, ...) sont recensés au lieu où est situé l'internat contrairement au recensement de 1999 où ils étaient comptabilisés au lieu de résidence de leurs parents.


- P11_POP0205 : **Pop 2-5 ans en 2011 (princ)**
- P11_POP0610 : **Pop 6-10 ans en 2011 (princ)**
- P11_POP1114 : **Pop 11-14 ans en 2011 (princ)**
- P11_POP1517 : **Pop 15-17 ans en 2011 (princ)**
- P11_POP1824 : **Pop 18-24 ans en 2011 (princ)**
- P11_POP2529 : **Pop 25-29 ans en 2011 (princ)**
- P11_POP30P : **Pop 30 ans ou plus en 2011 (princ)**
- P11_SCOL0205 : **Pop scolarisée 2-5 ans en 2011 (princ)**
- P11_SCOL0610 : **Pop scolarisée 6-10 ans en 2011 (princ)**
- P11_SCOL1114 : **Pop scolarisée 11-14 ans en 2011 (princ)**
- P11_SCOL1517 : **Pop scolarisée 15-17 ans en 2011 (princ)**
- P11_SCOL1824 : **Pop scolarisée 18-24 ans en 2011 (princ)**
- P11_SCOL2529 : **Pop scolarisée 25-29 ans en 2011 (princ)**
- P11_SCOL30P : **Pop scolarisée 30 ans ou plus en 2011 (princ)**
- P11_NSCOL15P : **Pop 15 ans ou plus non scolarisée en 2011 (princ)**
- P11_NSCOL15P_DIPL0 : **Pop 15 ans ou plus non scol. Sans diplôme en 2011 (princ)**
- P11_NSCOL15P_CEP : **Pop 15 ans ou plus non scol. CEP en 2011 (princ)**
- P11_NSCOL15P_BEPC : **Pop 15 ans ou plus non scol. BEPC, brevet collèges en 2011 (princ)**
- P11_NSCOL15P_CAPBEP : **Pop 15 ans ou plus non scol. CAP-BEP en 2011 (princ)**
- P11_NSCOL15P_BAC : **Pop 15 ans ou plus non scol. BAC-BP en 2011 (princ)**
- P11_NSCOL15P_BACP2 : **Pop 15 ans ou plus non scol. Enseignement sup court en 2011 (princ)**
- P11_NSCOL15P_SUP : **Pop 15 ans ou plus non scol. Enseignement sup long en 2011 (princ)**
- P11_HNSCOL15P : **Hommes 15 ans ou plus non scolarisés en 2011 (princ)**
- P11_HNSCOL15P_DIPL0 : **Hommes 15 ans ou plus non scol. Sans diplôme en 2011 (princ)**
- P11_HNSCOL15P_CEP : **Hommes 15 ans ou plus non scol. CEP en 2011 (princ)**
- P11_HNSCOL15P_BEPC : **Hommes 15 ans ou plus non scol. BEPC, brevet collèges en 2011 (princ)**
- P11_HNSCOL15P_CAPBEP : **Hommes 15 ans ou plus non scol. CAP-BEP en 2011 (princ)**
- P11_HNSCOL15P_BAC : **Hommes 15 ans ou plus non scol. BAC-BP en 2011 (princ)**
- P11_HNSCOL15P_BACP2 : **Hommes 15 ans ou plus non scol. Enseignement sup court en 2011 (princ)**
- P11_HNSCOL15P_SUP : **Hommes 15 ans ou plus non scol. Enseignement sup long en 2011 (princ)**
- P11_FNSCOL15P : **Femmes 15 ans ou plus non scolarisées en 2011 (princ)**
- P11_FNSCOL15P_DIPL0 : **Femmes 15 ans ou plus non scol. Sans diplôme en 2011 (princ)**
- P11_FNSCOL15P_CEP : **Femmes 15 ans ou plus non scol. CEP en 2011 (princ)**
- P11_FNSCOL15P_BEPC : **Femmes 15 ans ou plus non scol. BEPC, brevet collèges en 2011 (princ)**
- P11_FNSCOL15P_CAPBEP : **Femmes 15 ans ou plus non scol. CAP-BEP en 2011 (princ)**
- P11_FNSCOL15P_BAC : **Femmes 15 ans ou plus non scol. BAC-BP en 2011 (princ)**
- P11_FNSCOL15P_BACP2 : **Femmes 15 ans ou plus non scol. Enseignement sup court en 2011 (princ)**
- P11_FNSCOL15P_SUP : **Femmes 15 ans ou plus non scol. Enseignement sup long en 2011 (princ)**

##Base de données infracommunales : couples - familles - ménages en 2011

 - C11_MEN : **Ménages en 2011 (compl)**
 - C11_MENPSEUL : **Ménages 1 personne en 2011 (compl)**
 - C11_MENHSEUL : **Ménages Hommes seuls en 2011 (compl)**
 - C11_MENFSEUL : **Ménages Femmes seules en 2011 (compl)**
 - C11_MENSFAM : **Ménages Autres sans famille en 2011 (compl)**
 - C11_MENFAM : **Ménages avec famille(s) en 2011 (compl)**
 - C11_MENCOUPSENF : **Mén fam princ Couple sans enfant en 2011 (compl)**
 - C11_MENCOUPAENF : **Mén fam princ Couple avec enfant(s) en 2011 (compl)**
 - C11_MENFAMMONO : **Mén fam princ Famille mono en 2011 (compl)**
 - C11_PMEN : **Pop Ménages en 2011 (compl)**
 - C11_PMEN_MENPSEUL : **Pop mén Personnes seules en 2011 (compl)**
 - C11_PMEN_MENHSEUL : **Pop mén Hommes seuls en 2011 (compl)**
 - C11_PMEN_MENFSEUL : **Pop mén Femmes seules en 2011 (compl)**
 - C11_PMEN_MENSFAM : **Pop mén Autres sans famille en 2011 (compl)**
 - C11_PMEN_MENFAM : **Pop mén avec famille(s) en 2011 (compl)**
 - C11_PMEN_MENCOUPSENF : **Pop mén fam princ Couple sans enfant en 2011 (compl)**
 - C11_PMEN_MENCOUPAENF : **Pop mén fam princ Couple avec enfant(s) en 2011 (compl)**
 - C11_PMEN_MENFAMMONO : **Pop mén fam princ Famille mono en 2011 (compl)**
 - P11_POP15P : **Pop 15 ans ou plus en 2011 (princ)**
 - P11_POP1524 : **Pop 15-24 ans en 2011 (princ)**
 - P11_POP2554 : **Pop 25-54 ans en 2011 (princ)**
 - P11_POP5579 : **Pop 55-79 ans en 2011 (princ)**
 - P11_POP80P : **Pop 80 ans ou plus en 2011 (princ)**
 - P11_POPMEN15P : **Pop mén 15 ans ou plus en 2011 (princ)**
 - P11_POPMEN1524 : **Pop mén 15-24 ans en 2011 (princ)**
 - P11_POPMEN2554 : **Pop mén 25-54 ans en 2011 (princ)**
 - P11_POPMEN5579 : **Pop mén 55-79 ans en 2011 (princ)**
 - P11_POPMEN80P : **Pop mén 80 ans ou plus en 2011 (princ)**
 - P11_POP15P_PSEUL : **Pop 15 ans ou plus ans vivant seule en 2011 (princ)**
 - P11_POP1524_PSEUL : **Pop 15-24 ans vivant seule en 2011 (princ)**
 - P11_POP2554_PSEUL : **Pop 25-54 ans vivant seule en 2011 (princ)**
 - P11_POP5579_PSEUL : **Pop 55-79 ans vivant seule en 2011 (princ)**
 - P11_POP80P_PSEUL : **Pop 80 ans ou plus vivant seule en 2011 (princ)**
 - P11_POP15P_MARIE : **Pop 15 ans ou plus Marié en 2011 (princ)**
 - P11_POP15P_CELIB : **Pop 15 ans ou plus Célibataire en 2011 (princ)**
 - P11_POP15P_VEUF : **Pop 15 ans ou plus Veuf en 2011 (princ)**
 - P11_POP15P_DIVOR : **Pop 15 ans ou plus Divorcé en 2011 (princ)**
 - C11_MEN_CS1 : **Ménages Pers Réf Agri. expl. en 2011 (compl)**
 - C11_MEN_CS2 : **Ménages Pers Réf Art. Comm. Chefs entr. en 2011 (compl)**
 - C11_MEN_CS3 : **Ménages Pers Réf Cadres Prof int sup en 2011 (compl)**
 - C11_MEN_CS4 : **Ménages Pers Réf Prof intermédiaire en 2011 (compl)**
 - C11_MEN_CS5 : **Ménages Pers Réf Employé en 2011 (compl)**
 - C11_MEN_CS6 : **Ménages Pers Réf Ouvrier en 2011 (compl)**
 - C11_MEN_CS7 : **Ménages Pers Réf Retraité en 2011 (compl)**
 - C11_MEN_CS8 : **Ménages Pers Réf Autre en 2011 (compl)**
 - C11_PMEN_CS1 : **Pop mén Pers Réf Agri. expl. en 2011 (compl)**
 - C11_PMEN_CS2 : **Pop mén Pers Réf Art Com Chef ent en 2011 (compl)**
 - C11_PMEN_CS3 : **Pop mén Pers Réf Cadres Prof int sup en 2011 (compl)**
 - C11_PMEN_CS4 : **Pop mén Pers Réf Prof intermédiaire en 2011 (compl)**
 - C11_PMEN_CS5 : **Pop mén Pers Réf Employé en 2011 (compl)**
 - C11_PMEN_CS6 : **Pop mén Pers Réf Ouvrier en 2011 (compl)**
 - C11_PMEN_CS7 : **Pop mén Pers Réf Retraité en 2011 (compl)**
 - C11_PMEN_CS8 : **Pop mén Pers Réf Autre en 2011 (compl)**
 - C11_FAM : **Familles en 2011 (compl)**
 - C11_COUPAENF : **Fam Couple avec enfant(s) en 2011 (compl)**
 - C11_FAMMONO : **Fam Monoparentales en 2011 (compl)**
 - C11_COUPSENF : **Fam Couple sans enfant en 2011 (compl)**
 - C11_NE24F0 : **Fam 0 enfant moins 25 ans en 2011 (compl)**
 - C11_NE24F1 : **Fam 1 enfant moins 25 ans en 2011 (compl)**
 - C11_NE24F2 : **Fam 2 enfants moins 25 ans en 2011 (compl)**
 - C11_NE24F3 : **Fam 3 enfants moins 25 ans en 2011 (compl)**
 - C11_NE24F4P : **Fam 4 enfants ou plus moins 25 ans en 2011 (compl)**

 ##Base de données infracommunales : population en 2011

 - P11_POP : **Population en 2011 (princ)**
 - P11_POP0002 : **Pop 0-2 ans en 2011 (princ)**
 - P11_POP0305 : **Pop 3-5 ans en 2011 (princ)**
 - P11_POP0610 : **Pop 6-10 ans en 2011 (princ)**
 - P11_POP1117 : **Pop 11-17 ans en 2011 (princ)**
 - P11_POP1824 : **Pop 18-24 ans en 2011 (princ)**
 - P11_POP2539 : **Pop 25-39 ans en 2011 (princ)**
 - P11_POP4054 : **Pop 40-54 ans en 2011 (princ)**
 - P11_POP5564 : **Pop 55-64 ans en 2011 (princ)**
 - P11_POP6579 : **Pop 65-79 ans en 2011 (princ)**
 - P11_POP80P : **Pop 80 ans ou plus en 2011 (princ)**
 - P11_POP0014 : **Pop 0-14 ans en 2011 (princ)**
 - P11_POP1529 : **Pop 15-29 ans en 2011 (princ)**
 - P11_POP3044 : **Pop 30-44 ans en 2011 (princ)**
 - P11_POP4559 : **Pop 45-59 ans en 2011 (princ)**
 - P11_POP6074 : **Pop 60-74 ans en 2011 (princ)**
 - P11_POP75P : **Pop 75 ans ou plus en 2011 (princ)**
 - P11_POP0019 : **Pop 0-19 ans en 2011 (princ)**
 - P11_POP2064 : **Pop 20-64 ans en 2011 (princ)**
 - P11_POP65P : **Pop 65 ans ou plus en 2011 (princ)**
 - P11_POPH : **Pop Hommes en 2011 (princ)**
 - P11_H0014 : **Pop Hommes 0-14 ans en 2011 (princ)**
 - P11_H1529 : **Pop Hommes 15-29 ans en 2011 (princ)**
 - P11_H3044 : **Pop Hommes 30-44 ans en 2011 (princ)**
 - P11_H4559 : **Pop Hommes 45-59 ans en 2011 (princ)**
 - P11_H6074 : **Pop Hommes 60-74 ans en 2011 (princ)**
 - P11_H75P : **Pop Hommes 75 ans ou plus en 2011 (princ)**
 - P11_H0019 : **Pop Hommes 0-19 ans en 2011 (princ)**
 - P11_H2064 : **Pop Hommes 20-64 ans en 2011 (princ)**
 - P11_H65P : **Pop Hommes 65 ans ou plus en 2011 (princ)**
 - P11_POPF : **Pop Femmes en 2011 (princ)**
 - P11_F0014 : **Pop Femmes 0-14 ans en 2011 (princ)**
 - P11_F1529 : **Pop Femmes 15-29 ans en 2011 (princ)**
 - P11_F3044 : **Pop Femmes 30-44 ans en 2011 (princ)**
 - P11_F4559 : **Pop Femmes 45-59 ans en 2011 (princ)**
 - P11_F6074 : **Pop Femmes 60-74 ans en 2011 (princ)**
 - P11_F75P : **Pop Femmes 75 ans ou plus en 2011 (princ)**
 - P11_F0019 : **Pop Femmes 0-19 ans en 2011 (princ)**
 - P11_F2064 : **Pop Femmes 20-64 ans en 2011 (princ)**
 - P11_F65P : **Pop Femmes 65 ans ou plus en 2011 (princ)**
 - C11_POP15P : **Pop 15 ans ou plus en 2011 (compl)**
 - C11_POP15P_CS1 : **Pop 15 ans ou plus Agriculteurs exploitants en 2011 (compl)**
 - C11_POP15P_CS2 : **Pop 15 ans ou plus Artisans, Comm., Chefs entr. en 2011 (compl)**
 - C11_POP15P_CS3 : **Pop 15 ans ou plus Cadres, Prof. intel. sup. en 2011 (compl)**
 - C11_POP15P_CS4 : **Pop 15 ans ou plus Prof. intermédiaires en 2011 (compl)**
 - C11_POP15P_CS5 : **Pop 15 ans ou plus Employés en 2011 (compl)**
 - C11_POP15P_CS6 : **Pop 15 ans ou plus Ouvriers en 2011 (compl)**
 - C11_POP15P_CS7 : **Pop 15 ans ou plus Retraités en 2011 (compl)**
 - C11_POP15P_CS8 : **Pop 15 ans ou plus Autres en 2011 (compl)**
 - C11_H15P : **Pop 15 ans ou plus Hommes en 2011 (compl)**
 - C11_H15P_CS1 : **Pop 15 ans ou plus Hommes Agriculteurs exploitants en 2011 (compl)**
 - C11_H15P_CS2 : **Pop 15 ans ou plus Hommes Artisans, Comm., Chefs entr. en 2011 (compl)**
 - C11_H15P_CS3 : **Pop 15 ans ou plus Hommes Cadres, Prof. intel. sup. en 2011 (compl)**
 - C11_H15P_CS4 : **Pop 15 ans ou plus Hommes Prof. intermédiaires en 2011 (compl)**
 - C11_H15P_CS5 : **Pop 15 ans ou plus Hommes Employés en 2011 (compl)**
 - C11_H15P_CS6 : **Pop 15 ans ou plus Hommes Ouvriers en 2011 (compl)**
 - C11_H15P_CS7 : **Pop 15 ans ou plus Hommes Retraités en 2011 (compl)**
 - C11_H15P_CS8 : **Pop 15 ans ou plus Hommes Autres en 2011 (compl)**
 - C11_F15P : **Pop 15 ans ou plus Femmes en 2011 (compl)**
 - C11_F15P_CS1 : **Pop 15 ans ou plus Femmes Agriculteurs exploitants en 2011 (compl)**
 - C11_F15P_CS2 : **Pop 15 ans ou plus Femmes Artisans, Comm., Chefs entr. en 2011 (compl)**
 - C11_F15P_CS3 : **Pop 15 ans ou plus Femmes Cadres, Prof. intel. sup. en 2011 (compl)**
 - C11_F15P_CS4 : **Pop 15 ans ou plus Femmes Prof. intermédiaires en 2011 (compl)**
 - C11_F15P_CS5 : **Pop 15 ans ou plus Femmes Employés en 2011 (compl)**
 - C11_F15P_CS6 : **Pop 15 ans ou plus Femmes Ouvriers en 2011 (compl)**
 - C11_F15P_CS7 : **Pop 15 ans ou plus Femmes Retraités en 2011 (compl)**
 - C11_F15P_CS8 : **Pop 15 ans ou plus Femmes Autres en 2011 (compl)**
 - P11_POP_FR : **Pop Français en 2011 (princ)**
 - P11_POP_ETR : **Pop Etrangers en 2011 (princ)**
 - P11_POP_IMM : **Pop Immigrés en 2011 (princ)**
 - P11_PMEN : **Pop ménages en 2011 (princ)**
 - P11_PHORMEN : **Pop hors ménages en 2011 (princ)**

##Base de données infracommunales : activité des résidents en 2011

 - P11_POP1564 : **Pop 15-64 ans en 2011 (princ)**
 - P11_POP1524 : **Pop 15-24 ans en 2011 (princ)**
 - P11_POP2554 : **Pop 25-54 ans en 2011 (princ)**
 - P11_POP5564 : **Pop 55-64 ans en 2011 (princ)**
 - P11_H1564 : **Pop 15-64 ans Hommes en 2011 (princ)**
 - P11_H1524 : **Pop 15-24 ans Hommes en 2011 (princ)**
 - P11_H2554 : **Pop 25-54 ans Hommes en 2011 (princ)**
 - P11_H5564 : **Pop 55-64 ans Hommes en 2011 (princ)**
 - P11_F1564 : **Pop 15-64 ans Femmes en 2011 (princ)**
 - P11_F1524 : **Pop 15-24 ans Femmes en 2011 (princ)**
 - P11_F2554 : **Pop 25-54 ans Femmes en 2011 (princ)**
 - P11_F5564 : **Pop 55-64 ans Femmes en 2011 (princ)**
 - P11_ACT1564 : **Actifs 15-64 ans en 2011 (princ)**
 - P11_ACT1524 : **Actifs 15-24 ans en 2011 (princ)**
 - P11_ACT2554 : **Actifs 25-54 ans en 2011 (princ)**
 - P11_ACT5564 : **Actifs 55-64 ans en 2011 (princ)**
 - P11_HACT1564 : **Actifs 15-64 ans Hommes en 2011 (princ)**
 - P11_HACT1524 : **Actifs 15-24 ans Hommes en 2011 (princ)**
 - P11_HACT2554 : **Actifs 25-54 ans Hommes en 2011 (princ)**
 - P11_HACT5564 : **Actifs 55-64 ans Hommes en 2011 (princ)**
 - P11_FACT1564 : **Actifs 15-64 ans Femmes en 2011 (princ)**
 - P11_FACT1524 : **Actifs 15-24 ans Femmes en 2011 (princ)**
 - P11_FACT2554 : **Actifs 25-54 ans Femmes en 2011 (princ)**
 - P11_FACT5564 : **Actifs 55-64 ans Femmes en 2011 (princ)**
 - P11_ACTOCC1564 : **Actifs occupés 15-64 ans en 2011 (princ)**
 - P11_ACTOCC1524 : **Actifs occupés 15-24 ans en 2011 (princ)**
 - P11_ACTOCC2554 : **Actifs occupés 25-54 ans en 2011 (princ)**
 - P11_ACTOCC5564 : **Actifs occupés 55-64 ans en 2011 (princ)**
 - P11_HACTOCC1564 : **Actifs occupés 15-64 ans Hommes en 2011 (princ)**
 - P11_HACTOCC1524 : **Actifs occupés 15-24 ans Hommes en 2011 (princ)**
 - P11_HACTOCC2554 : **Actifs occupés 25-54 ans Hommes en 2011 (princ)**
 - P11_HACTOCC5564 : **Actifs occupés 55-64 ans Hommes en 2011 (princ)**
 - P11_FACTOCC1564 : **Actifs occupés 15-64 ans Femmes en 2011 (princ)**
 - P11_FACTOCC1524 : **Actifs occupés 15-24 ans Femmes en 2011 (princ)**
 - P11_FACTOCC2554 : **Actifs occupés 25-54 ans Femmes en 2011 (princ)**
 - P11_FACTOCC5564 : **Actifs occupés 55-64 ans Femmes en 2011 (princ)**
 - P11_CHOM1564 : **Chômeurs 15-64 ans en 2011 (princ)**
 - P11_CHOM1524 : **Chômeurs 15-24 ans en 2011 (princ)**
 - P11_CHOM2554 : **Chômeurs 25-54 ans en 2011 (princ)**
 - P11_CHOM5564 : **Chômeurs 55-64 ans en 2011 (princ)**
 - P11_HCHOM1564 : **Chômeurs 15-64 ans Hommes en 2011 (princ)**
 - P11_FCHOM1564 : **Chômeurs 15-64 ans Femmes en 2011 (princ)**
 - P11_INACT1564 : **Inactifs 15-64 ans en 2011 (princ)**
 - P11_HINACT1564 : **Inactifs 15-64 ans Hommes en 2011 (princ)**
 - P11_FINACT1564 : **Inactifs 15-64 ans Femmes en 2011 (princ)**
 - P11_ETUD1564 : **Elèv. Etud. Stag. non rémunérés 15-64 ans en 2011 (princ)**
 - P11_HETUD1564 : **Elèv. Etud. Stag. non rémunérés 15-64 ans Hommes en 2011 (princ)**
 - P11_FETUD1564 : **Elèv. Etud. Stag. non rémunérés 15-64 ans Femmes en 2011 (princ)**
 - P11_RETR1564 : **Retraités Préretraités 15-64 ans en 2011 (princ)**
 - P11_HRETR1564 : **Retraités Préretraités 15-64 ans Hommes en 2011 (princ)**
 - P11_FRETR1564 : **Retraités Préretraités 15-64 ans Femmes en 2011 (princ)**
 - P11_AINACT1564 : **Autres inactifs 15-64 ans en 2011 (princ)**
 - P11_HAINACT1564 : **Autres inactifs 15-64 ans Hommes en 2011 (princ)**
 - P11_FAINACT1564 : **Autres inactifs 15-64 ans Femmes en 2011 (princ)**
 - C11_ACT1564 : **Actifs 15-64 ans en 2011 (compl)**
 - C11_ACT1564_CS1 : **Actifs 15-64 ans Agriculteurs exploitants en 2011 (compl)**
 - C11_ACT1564_CS2 : **Actifs 15-64 ans Artisans, Comm., Chefs entr. en 2011 (compl)**
 - C11_ACT1564_CS3 : **Actifs 15-64 ans Cadres, Prof. intel. sup. en 2011 (compl)**
 - C11_ACT1564_CS4 : **Actifs 15-64 ans Prof. intermédiaires en 2011 (compl)**
 - C11_ACT1564_CS5 : **Actifs 15-64 ans Employés en 2011 (compl)**
 - C11_ACT1564_CS6 : **Actifs 15-64 ans Ouvriers en 2011 (compl)**
 - C11_ACTOCC1564 : **Actifs occupés 15-64 ans en 2011 (compl)**
 - C11_ACTOCC1564_CS1 : **Actifs occ 15-64 ans Agriculteurs exploitants en 2011 (compl)**
 - C11_ACTOCC1564_CS2 : **Actifs occ 15-64 ans Artisans, Comm., Chefs entr. en 2011 (compl)**
 - C11_ACTOCC1564_CS3 : **Actifs occ 15-64 ans Cadres Prof. intel. sup. en 2011 (compl)**
 - C11_ACTOCC1564_CS4 : **Actifs occ 15-64 ans Prof. intermédiaires en 2011 (compl)**
 - C11_ACTOCC1564_CS5 : **Actifs occupés 15-64 ans Employés en 2011 (compl)**
 - C11_ACTOCC1564_CS6 : **Actifs occupés 15-64 ans Ouvriers en 2011 (compl)**
 - P11_ACTOCC15P : **Actifs occupés 15 ans ou plus en 2011 (princ)**
 - P11_HACTOCC15P : **Actifs occupés 15 ans ou plus Hommes en 2011 (princ)**
 - P11_FACTOCC15P : **Actifs occupés 15 ans ou plus Femmes en 2011 (princ)**
 - P11_SAL15P : **Salariés 15 ans ou plus en 2011 (princ)**
 - P11_HSAL15P : **Salariés 15 ans ou plus Hommes en 2011 (princ)**
 - P11_FSAL15P : **Salariés 15 ans ou plus Femmes en 2011 (princ)**
 - P11_NSAL15P : **Non-salariés 15 ans ou plus en 2011 (princ)**
 - P11_HNSAL15P : **Non-salariés 15 ans ou plus Hommes en 2011 (princ)**
 - P11_FNSAL15P : **Non-salariés 15 ans ou plus Femmes en 2011 (princ)**
 - P11_ACTOCC15P_TP : **Actifs occ 15 ans ou plus TP en 2011 (princ)**
 - P11_SAL15P_TP : **Salariés 15 ans ou plus TP en 2011 (princ)**
 - P11_HSAL15P_TP : **Salariés 15 ans ou plus TP Hommes en 2011 (princ)**
 - P11_FSAL15P_TP : **Salariés 15 ans ou plus TP Femmes en 2011 (princ)**
 - P11_NSAL15P_TP : **Non-salariés 15 ans ou plus TP en 2011 (princ)**
 - P11_SAL15P_CDI : **Salariés 15 ans ou plus Fonct publ, CDI en 2011 (princ)**
 - P11_SAL15P_CDD : **Salariés 15 ans ou plus CDD en 2011 (princ)**
 - P11_SAL15P_INTERIM : **Salariés 15 ans ou plus Intérim en 2011 (princ)**
 - P11_SAL15P_EMPAID : **Salariés 15 ans ou plus Emplois aidés en 2011 (princ)**
 - P11_SAL15P_APPR : **Salariés 15 ans ou plus Apprentissage - Stage en 2011 (princ)**
 - P11_NSAL15P_INDEP : **Non-salariés 15 ans ou plus Indépendants en 2011 (princ)**
 - P11_NSAL15P_EMPLOY : **Non-salariés 15 ans ou plus Employeurs en 2011 (princ)**
 - P11_NSAL15P_AIDFAM : **Non-salariés 15 ans ou plus Aides familiaux en 2011 (princ)**
 - P11_ACTOCC15P_ILT1 : **Actif occ 15 ans ou plus travaille commune résidence en 2011 (princ)**
 - P11_ACTOCC15P_ILT2P : **Actif occ 15 ans ou plus travaille autre commune que commune résidence en 2011 (princ)**
 - P11_ACTOCC15P_ILT2 : **Actif occ 15 ans ou plus travaille autre commune même dépt résidence en 2011 (princ)**
 - P11_ACTOCC15P_ILT3 : **Actif occ 15 ans ou plus travaille autre dépt même région résidence en 2011 (princ)**
 - P11_ACTOCC15P_ILT4 : **Actif occ 15 ans ou plus travaille autre région en métropole en 2011 (princ)**
 - P11_ACTOCC15P_ILT5 : **Actif occ 15 ans ou plus travaille autre région hors métropole en 2011 (princ)**
 - C11_ACTOCC15P : **Actif occ 15 ans ou plus en 2011 (compl)**
 - C11_ACTOCC15P_PAS : **Actif occ 15 ans ou plus pas de transport en 2011 (compl)**
 - C11_ACTOCC15P_MAR : **Actif occ 15 ans ou plus marche à pied en 2011 (compl)**
 - C11_ACTOCC15P_DROU : **Actif occ 15 ans ou plus deux roues en 2011 (compl)**
 - C11_ACTOCC15P_VOIT : **Actif occ 15 ans ou plus voiture, camion en 2011 (compl)**
 - C11_ACTOCC15P_TCOM : **Actif occ 15 ans ou plus transport en commun en 2011 (compl)**



