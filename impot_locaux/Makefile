ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: download process

download:
	@rm -rf data
	@mkdir data
	# Download 2013 data
	@wget -O data/rei_2013.zip https://www.impots.gouv.fr/portail/www2/fichiers/statistiques/temp_rei/rei_2013.zip
	@unzip data/rei_2013.zip -d data/
	# Download 2014 data
	@wget -O data/rei_2014.zip https://www.impots.gouv.fr/portail/www2/fichiers/statistiques/temp_rei/rei_2014.zip
	@unzip data/rei_2014.zip -d data/
	# Download 2015 data
	@wget -O data/rei_2015.zip https://www.impots.gouv.fr/portail/www2/fichiers/statistiques/temp_rei/rei_2015.zip
	@unzip data/rei_2015.zip -d data/

process:
	python mk_data.py