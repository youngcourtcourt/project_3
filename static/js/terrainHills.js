mapboxgl.accessToken = 'pk.eyJ1Ijoicmhpbm9iYWNrIiwiYSI6ImNrbjIwMWZmYzBlYXQyb21yaDg1MjBscG4ifQ.hU5CRI2iUlmr9igTrw5zUA';
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/cjaudgl840gn32rnrepcb9b9g', // the outdoors-v10 style but without Hillshade layers
        center: [-119.5591, 37.715],
        zoom: 6
    });

    map.on('load', function () {
        map.addSource('dem', {
            'type': 'raster-dem',
            'url': 'mapbox://mapbox.mapbox-terrain-dem-v1'
        });
        map.addLayer(
            {
                'id': 'hillshading',
                'source': 'dem',
                'type': 'hillshade'
                // insert below waterway-river-canal-shadow;
                // where hillshading sits in the Mapbox Outdoors style
            },
            'waterway-river-canal-shadow'
        );
    });