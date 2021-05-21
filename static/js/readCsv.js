d3.csv("../data/aggregateCountyData.csv").then(function(data){
    
    console.log(data)

    for (var i=0;i<data.length;i++){
        // console.log((data[i]['County Name']).replaceAll('_', ' '))

        county=(data[i]['County Name']).replaceAll('_', ' ')
    }

})
