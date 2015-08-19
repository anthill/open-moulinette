## Iris dataset

This script will dowload and convert Insee's datafile concerning IRIS zones in France and create a single json.

## Prerequisites

You need to have `wget` and `p7zip` installed. On mac:
```
brew install wget p7zip
```

## Usage

After `npm install` to get the dependencies, use `make download` to automatically save the files on your computer. Then launch the conversion using `make convert`.

## Format

This will create a single geojson file with the following structure:

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "DEPCOM": "97701",
        "NOM_COM": "SAINT-BARTHELEMY",
        "IRIS": "0102",
        "DCOMIRIS": "977010102",
        "NOM_IRIS": "CENTRE",
        "TYP_IRIS": "H",
        "ORIGINE": "2"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              1.637095937960687,
              7.610503016150719
            ],
            ...
          ]
        ]
      }
    },
    ...
  ]
}
```

Then you can use it like this in node, if you like:


```
var data = require("./data/iris.json");
data.features.forEach(function(iris){
	console.log(iris.properties.IRIS)
})

```

to list all iris ids.


