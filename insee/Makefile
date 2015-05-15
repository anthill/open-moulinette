ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: download

download:
	@rm -rf data
	@mkdir data
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-commerce
	@wget -O data/equip-serv-commerce-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-commerce/equip-serv-commerce-infra-13.zip
	@unzip data/equip-serv-commerce-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-sport-loisir-socio
	@wget -O data/equip-sport-loisir-socio-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-sport-loisir-socio/equip-sport-loisir-socio-infra-13.zip
	@unzip data/equip-sport-loisir-socio-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-1er-degre
	@wget -O data/equip-serv-ens-1er-degre-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-ens-1er-degre/equip-serv-ens-1er-degre-infra-13.zip
	@unzip data/equip-serv-ens-1er-degre-infra-13.zip -d data/
		

convert:
	#@node index.js