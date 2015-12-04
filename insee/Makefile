ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: download convert

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
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-2eme-degre
	@wget -O data/equip-serv-ens-2eme-degre-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-ens-2eme-degre/equip-serv-ens-2eme-degre-infra-13.zip
	@unzip data/equip-serv-ens-2eme-degre-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-ens-sup-form-serv
	@wget -O data/equip-serv-ens-sup-form-serv-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-ens-sup-form-serv/equip-serv-ens-sup-form-serv-infra-13.zip
	@unzip data/equip-serv-ens-sup-form-serv-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=structure-distrib-revenus-2011
	# 4 files for this insee'files
	@wget -O data/structure-distrib-revenus-iris-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/structure-distrib-revenus/structure-distrib-revenus-2011/structure-distrib-revenus-iris-2011.zip
	@unzip data/structure-distrib-revenus-iris-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-action-sociale
	@wget -O data/equip-serv-action-sociale-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-action-sociale/equip-serv-action-sociale-infra-13.zip
	@unzip data/equip-serv-action-sociale-infra-13.zip -d data/	
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-sante
	@wget -O data/equip-serv-sante-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-sante/equip-serv-sante-infra-13.zip
	@unzip data/equip-serv-sante-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-medical-para
	@wget -O data/equip-serv-medical-para-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-medical-para/equip-serv-medical-para-infra-13.zip
	@unzip data/equip-serv-medical-para-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-serv-particuliers
	@wget -O data/equip-serv-particuliers-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-serv-particuliers/equip-serv-particuliers-infra-13.zip
	@unzip data/equip-serv-particuliers-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=equip-tour-transp
	@wget -O data/equip-tour-transp-infra-13.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/equip-tour-transp/equip-tour-transp-infra-13.zip
	@unzip data/equip-tour-transp-infra-13.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-logement-11
	@wget -O data/infra-logement-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-logement-11/infra-logement-2011.zip
	@unzip data/infra-logement-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-formation-11
	@wget -O data/infra-formation-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-formation-11/infra-formation-2011.zip
	@unzip data/infra-formation-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-famille-11
	@wget -O data/infra-famille-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-famille-11/infra-famille-2011.zip
	@unzip data/infra-famille-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-population-11
	@wget -O data/infra-population-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-population-11/infra-population-2011.zip
	@unzip data/infra-population-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-activite-resident-11
	@wget -O data/infra-activite-resident-2011.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-activite-resident-11/infra-activite-resident-2011.zip
	@unzip data/infra-activite-resident-2011.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-logement-12
	@wget -O data/infra-logement-2012.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2012/infracommunal/infra-logement-12/infra-logement-2012.zip
	@unzip data/infra-logement-2012.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-formation-12
	@wget -O data/infra-formation-2012.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2012/infracommunal/infra-formation-12/infra-formation-2012.zip
	@unzip data/infra-formation-2012.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-famille-12
	@wget -O data/infra-famille-2012.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2012/infracommunal/infra-famille-12/infra-famille-2012.zip
	@unzip data/infra-famille-2012.zip -d data/
	# http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-population-12
	@wget -O data/infra-population-2012.zip http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2012/infracommunal/infra-population-12/infra-population-2012.zip
	@unzip data/infra-population-2012.zip -d data/

convert:
	python mk_data.py