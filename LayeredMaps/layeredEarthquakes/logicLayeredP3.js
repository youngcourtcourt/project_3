//Logic for LayeredFaultLinesMap
//Various Queries for various data types
// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson";
//var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson";
//var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson";

// Perform a GET request to the query URL
d3.json(queryUrl).then(function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {

  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place, magnitude, MagType and time of the earthquake
  function onEachFeature(feature, layer) {
    layer.bindPopup("<h1>" + feature.properties.place + "<h2>" + "Magnitude: " + feature.properties.mag  + "/ MagType: " + feature.properties.magType +
      "</h2><h3>" + new Date(feature.properties.time) + "</p>");
  }

  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature
  });

    // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}
//do i need a mapbox account part here?

function createMap(earthquakes) {

// Define variables for our tile layers

var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
});

var light = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "light-v10",
  accessToken: API_KEY
});

var dark = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "dark-v10",
  accessToken: API_KEY
});

// var ocean = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   maxZoom: 18,
//   id: "10m-bathymetry-81bsvj",
//   // style: 'mapbox://styles/mapbox/streets-v11',
//   accessToken: API_KEY
// });

// var hillshading = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   maxZoom: 18,
//   id: "hillshading",
//   accessToken: API_KEY
// });



// Only one base layer can be shown at a time
var baseMaps = {
 "Street Map": streetmap,
  "Light Map": light,
  "Dark Map": dark,
  // "Ocean Map": ocean,
  // "Hillshading Map": hillshading,
  // Satelite: satelite,
};

// Overlays that may be toggled on or off
var overlayMaps = {
  Earthquakes: earthquakes
}

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      36.09, -117.71
    ],
    zoom: 6,
    layers: [streetmap, earthquakes]
  });

// Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}







// var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   maxZoom: 18,
//   id: "satellite",
//   // style: 'mapbox://styles/mapbox/satellite-v9', // style URL
//   accessToken: API_KEY
// });

// var faultlinedark = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   maxZoom: 18,
//   container: 'map', // you need this
//   style: 'mapbox://styles/mapbox/dark-v9', // you also need this
//   center: [-74.0006213, 40.7229971], // [long, lat] Different than leaflet, different than google maps, same as geojson!
//   zoom: 2,
//   accessToken: API_KEY
// });


// var map = new mapboxgl.Map({
//   container: 'map', // you need this
//   style: 'mapbox://styles/mapbox/dark-v9', // you also need this
//   center: [-74.0006213, 40.7229971], // [long, lat] Different than leaflet, different than google maps, same as geojson!
//   zoom: 2,
// });
// map.addSource('my-data', {
//   type: 'vector',
//   url: 'mapbox://myusername.tilesetid'
// });

// map.addSource('my-data', {
//   "type": "geojson",
//   "data": {
//     "type": "Feature",
//     "geometry": {
//       "type": "Point",
//       "coordinates": [-77.0323, 38.9131]
//     },
//     "properties": {
//       "title": "Mapbox DC",
//       "marker-symbol": "monument"
//     }
//   }
// });
