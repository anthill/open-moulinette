# Docker as a dev environement


```
docker build --rm -t="openmoulinette_loader_1" dashboard
docker run -ti -v $PWD:/open-moulinette openmoulinette_loader_1
```

```
# download and clean iris geographical grid
cd /open-moulinette/insee-iris
make
npm install
node index.js

# download and agglomerate insee data
cd /open-moulinette/insee
make download
python mk_data.py

# build dashboard dependencies
cd /open-moulinette/dashboard
npm install
```

```
# start Docker containers for deployment
docker-compose up
```

use `docker-machine ls`  to get the ip and go to `http://192.168.99.100:5601/`


Find more details on this [tutorial](https://medium.com/code-feelings/construire-un-dashboard-open-data-avec-docker-elasticsearch-et-kibana-11984e5a15fb)


