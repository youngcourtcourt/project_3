// Create a map object
var myMap = L.map("map", {
  center: [37.4946, -120.8460],
  zoom: 6
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

var countyList=[]

function onClick(e){

  var split1=(this._popup._content).split('County: ')[1]
  var county=split1.split(' Total')[0]
  d3.select("#county")
  .text(`${county}`)
  
  
}

d3.csv("../data/aggregateCountyData.csv").then(function(data){
    
    // console.log(data)

    for (var i=0;i<data.length;i++){

        numEvents=Math.round(data[i]['Total Damaging Events'])
        latitude=data[i]['Latitude']
        longitude=data[i]['Longitude']
        countyName=(data[i]['County Name']).replaceAll('_', ' ')
        countyList.push(countyName)

        var marker= new L.Marker([latitude, longitude], {
          icon: new L.DivIcon({
              className: 'my-div-icon',
              html: '<img class="palmTree" src="../static/styleElements/palmTree.svg"/>'
                      })
        }).on("click", onClick)

        marker.addTo(myMap)

        marker.bindPopup(`County: ${countyName} Total Events: ${numEvents}` )

        // marker.on("click", function(){
        //   d3.select("#test")
        //     .selectAll("h1")
        //     .text(`${marker._latlng}`)
            
        //   console.log(marker._latlng)
        // })
    }


})

// new L.Marker([37.4946, -120.8460], {
//   icon: new L.DivIcon({
//       className: 'my-div-icon',
//       html: '<img class="palmTree" src="../static/styleElements/palmTree.svg"/>'
//   })
// }).addTo(myMap)