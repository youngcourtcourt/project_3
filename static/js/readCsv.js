// Create a map object
var myMap = L.map("map", {
  center: [37.4946, -120.8460],
  zoom: 7
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

d3.csv("../data/aggregateCountyData.csv").then(function(data){
    
    console.log(data)

    for (var i=0;i<data.length;i++){

        numEvents=Math.round(data[i]['Total Damaging Events'])
        latitude=data[i]['Latitude']
        longitude=data[i]['Longitude']
        countyName=(data[i]['County Name']).replaceAll('_', ' ')
    }


})

new L.Marker([37.4946, -120.8460], {
  icon: new L.DivIcon({
      className: 'my-div-icon',
      html: '<img class="my-div-image" src="../static/styleElements/palmTree.svg"/>'+
            '<span class="my-div-span">RAF Banff Airfield</span>'
  })
}).addTo(myMap)