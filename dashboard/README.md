# Docker as dev environement


```
docker build --rm -t="openmoulinette_loader_1" dashboard
docker run -ti -v $PWD:/open-moulinette openmoulinette_loader_1
```


```
# telecharge les donnees geographiques iris et les nettoie
cd /open-moulinette/insee-iris
make
node index.js

# telecharge les donnees insee et les agrège
cd /open-moulinette/insee
make download
python mk_data.py

# build les dépendances du dashboard
cd /open-moulinette/dashboard
npm install
```

# Docker for deployment

```
docker-compose up
```

use `docker-machine ls`  to get the ip and go to `http://192.168.99.100:5601/`


