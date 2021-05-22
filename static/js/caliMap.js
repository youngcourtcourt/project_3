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
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// Initialize a county list in case we need one
var countyList=[]

function onClick(event){

  var county=(this._popup._content).split(',')[0]
  var numEvents=(this._popup._content).split(',')[1]

  d3.select("#county")
  .text(`${county}`)

  d3.select("#numEvents")
  .text(`${numEvents}`)
  
  // console.log(split2)
}

function closePopup(event){
  myMap.closePopup()
}

d3.csv("../data/aggregateCountyData.csv").then(function(data){
    

    for (var i=0;i<data.length;i++){

      // Set key metrics to variables
        numEvents=Math.round(data[i]['Total Damaging Events'])
        latitude=data[i]['Latitude']
        longitude=data[i]['Longitude']
        countyName=(data[i]['County Name']).replaceAll('_', ' ')
        countyList.push(countyName)

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

        marker.bindPopup(`${countyName},${numEvents}` ).on("click", closePopup)

      
    }


})

