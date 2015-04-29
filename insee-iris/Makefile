ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: python-scripts

download:
	@rm -rf data
	@mkdir data
	@cd data
	curl -o iris-france.zip https://wxs-telechargement.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-FRANCE-2013-01-01_CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01/file/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01.7z
	mv iris-france.zip data/iris-france.zip