# Documentation

Open-moulinette insee is an open data cleaner who concatene each Insee's files in one csv. Beacause Insee's file are often in xls format and not easy to reuse. Actualy we have more than 330 features, but they are not friendly-user :

`NB_B314` is the number of gas station by iris.

The goal of this documentation is to enumerate each feature and explain it. Decription is in French as all the data concerne French'city.


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


**Note :** Pour chacune des installations sportives, on dispose de plusieurs informations : 
exemple pour les bassins de natation de la commune de Marseille  

- NB_F101           : 38  bassins de natation (installations pour la natation)
- NB_F101_NB_BASNAT : 47  cumul des bassins de natation dénombrés dans les 38 installations localisées
- NB_F101_NB_COU    : 25  installations sur les 38 disposent d'au moins un bassin couvert 
- NB_F101_NB_ECL    : 27  installations sur les 38 possèdant un éclairage

Il en va de même pour les autres installations sportive **NB_F1..**
