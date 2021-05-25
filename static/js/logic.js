// Creating map object
var myMap = L.map("map", {
  center: [33.68, -117.82],
  zoom: 11
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

d3.json("/api/v1.0/earthquake_data").then(function(eqdata){
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();

  // Loop through data
  for (var i = 0; i < eqdata.length; i++) {

    var latitude=eqdata[i].Latitude
    var longitude=eqdata[i].Longitude
    var depth=eqdata[i].Depth
    var magnitude=eqdata[i].Magnitude
    var waveForm=eqdata[i].Waveform
    var place=eqdata[i].Place
    var time=eqdata[i].Time
    var type=eqdata[i].Type

    
    // console.log(eqdata[i].Magnitude)
    // console.log(Math.round(depth*100)/100)

    // var magElement=d3.select("#magnitude")
    // var depthElement=d3.select("#depth")

    // Set the data location property to a variable
    
    // var formatTime=d3.parseTime("%B $d, %Y")
    // console.log(formatTime(time))

    // Check for location property
    // if (location) {

      // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer((L.marker([latitude, longitude])
        .bindPopup(`<h4>${place}</h4><hr><p>Depth: ${Math.round(depth*100)/100} ft<br>WaveForm: ${waveForm}</p>`)
        .on("click", function(){
        // d3.select("#magnitude").text(`${magnitude}`)
        // var depth2= (Math.round(depth*100)/100)
        // d3.select("#depth").text(`${depth2}`)
        // d3.select("#form").text(`${waveForm.toUpperCase()}`)
        $( "#map" ).effect( "shake" )
      
 
    })))
        
    }
    d3.selectAll("#europe").on("click", function(){
      var center=[54.5260, 15.25510]
      myMap.setView(center, 3)
   })
   d3.selectAll("#asia").on("click", function(){
     center=[34.0479, 100.6197]
     myMap.setView(center, 3)
   })
   d3.selectAll("#northAmerica").on("click", function(){
     center=[54.5260, -105.2551]
     myMap.setView(center, 3)
   })
   d3.selectAll("#southAmerica").on("click", function(){
     center=[8.7832, -55.4915]
     myMap.setView(center, 3)
   })
   d3.selectAll("#africa").on("click", function(){
     center=[8.7832, 34.5085]
     myMap.setView(center, 3)
   })
   d3.selectAll("#antarctica").on("click", function(){
     center=[82.8628, 135.0000]
     myMap.setView(center, 3)
   })
   d3.selectAll("#oceania").on("click", function(){
     center=[22.7359, 140.0188]
     myMap.setView(center, 3)
   })


  // Add our marker cluster layer to the map
  myMap.addLayer(markers);
  
});
