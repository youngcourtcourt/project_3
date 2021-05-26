// Create a map object
var myMap = L.map("map", {
  center: [37.4946, -120.8460],
  zoom: 6
});

// Create tile later
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 8,
  minZoom:5,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// Initialize a county list in case we need one
var countyList=[]

function onClick(event){

  var county=(this._popup._content).split(',')[0]
  var numEvents=(this._popup._content).split(',')[1]
  var rate=(this._popup._content).split(',')[2]

  // ######## Uncomment in case probability calculator boots up ########

  // var probability=(this._popup._content).split(',')[3]
  // d3.select("#probability")
  // .text(`${probability}`)


  // console.log((this._popup._content).split(','))
  d3.select("#county")
  .text(`${county}`)

  d3.select("#numEvents")
  .text(`${numEvents}`)

  d3.select("#rate")
  .text(`${rate}`)

  var lat=this._latlng.lat
  var lng=this._latlng.lng
  
  center=[lat, lng]
  
  myMap.setView(center, 7)
}

function closePopup(event){
  myMap.closePopup()
}

d3.json("/api/v1.0/county_data").then(function(data){

    for (var i=0;i<data.length;i++){

      // Set key metrics to variables
        var numEvents=Math.round(data[i]['total_damaging_events'])
        var latitude=data[i]['latitude']
        var longitude=data[i]['longitude']
        var rate=Math.round(data[i]['rate_of_damaging_events'])
        var countyName=(data[i]['county']).replaceAll('_', ' ')
        countyList.push(countyName)

        // ######## Uncomment in case probability calculator boots up ########

        // var probability=data[i]['Probability']

        // Attach palm tree to every marker

        var marker= new L.Marker([latitude, longitude], {
          icon: new L.DivIcon({
              className: 'my-div-icon',
              html: '<img class="palmTree" src="../static/styleElements/palmTree.svg"/>'
                      })
        }).on("click", onClick)

      // Add to map

        marker.addTo(myMap)

        // Bind popup to each marker

        // Add ${probability} to popup in case probability calculator comes up

        marker.bindPopup(`${countyName},${numEvents},${rate}` ).on("click", closePopup)

      
    }

})
