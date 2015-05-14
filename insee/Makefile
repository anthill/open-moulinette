ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: download

download:
	@rm -rf data
	@mkdir data
	@wget -O data/equip-serv-commerce-infra-13.7z http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-commerce/equip-serv-commerce-infra-13.zip
	@wget -O data/equip-sport-loisir-socio-infra-13.7z http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-sport-loisir-socio/equip-sport-loisir-socio-infra-13.zip
		

convert:
	@node index.js