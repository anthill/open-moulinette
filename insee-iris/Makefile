ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: download

download:
	@rm -rf data
	@mkdir data
	@curl -o data/iris-france.7z https://wxs-telechargement.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-FRANCE-2013-01-01_CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01/file/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01.7z
	@curl -o data/departement_CC_lambert.csv https://gist.githubusercontent.com/armgilles/4f92204ee07df82e2dbd/raw/8e9ee4bdc8d70778e3d5d1bdc17b980c68e5085f/departement_CC_lambert.csv

convert:
	@node index.js