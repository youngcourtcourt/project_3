d3.json("/api/v1.0/relief_data").then(function(data){
    var countries=[]
    var dollars=[]
    for (var i=0;i<data.length;i++){
        var dollar=data[i]["Total_relief"]
        // dollar= parseInt(dollar.replace(/,/g, ""))
        countries.push(data[i].Country)
        dollars.push(dollar)
        
    }
    

    var topTenCountries=countries.slice(0, 20)
    var topTenDollars=dollars.slice(0, 20)
    var bottomTenCountries=countries.slice((countries.length-20), countries.length)
    var bottomTenDollars=dollars.slice((dollars.length-20), dollars.length)
    var countryList=topTenCountries.concat(bottomTenCountries)
    var dollarList=topTenDollars.concat(bottomTenDollars)

var ctx1 = document.getElementById('myChart');
var myChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: countryList,
        datasets: [{
            label: "Disaster Relief Funds in Dollars",
            data: dollarList,
            backgroundColor: [
                "#DFFF00",
                "#FFBF00",
                "#FF7F50",
                "#DE3163",
                "#9FE2BF",
                "#40E0D0",
                "#6495ED",
                "#CCCCFF"
            ],
            borderColor: [
                "#DFFF00",
                "#FFBF00",
                "#FF7F50",
                "#DE3163",
                "#9FE2BF",
                "#40E0D0",
                "#6495ED",
                "#CCCCFF"
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        maintainAspectRatio: false
    }
})})

d3.json("/api/v1.0/earthquake_data").then(function(data){
    var waveForm=["ML","MD", "MB", "MMW", "MB_LG", "Other"]
    var mLCount=0
    var mdCount=0
    var mbCount=0
    var mmwCount=0
    var mbLgCount=0
    var otherCount=0
    var counts=[]
    for (var i=0;i<data.length;i++){
        if(data[i].Waveform==="ML"){
            mLCount+=1
        }else if(data[i].Waveform==="MD"){
            mdCount+=1
        }else if(data[i].Waveform==="MB"){
            mbCount+=1
        }else if(data[i].Waveform==="MMW"){
            mmwCount+=1
        }else if(data[i].Waveform==="MB_LG"){
            mbLgCount+=1
        }else{
            otherCount+=1
        }
        
        
}counts.push(mLCount, mdCount, mbCount, mmwCount, mbLgCount, otherCount)

var ctx2 = document.getElementById('myPieChart');

var myChart2 = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels:waveForm,
        datasets: [{
            data: counts,
            backgroundColor: [
                '#40E0D0',
                '#DAF7A6',
                '#FFC300',
                '#FF5733',
                '#F8C471',
                '#F7DC6F'
            ],
            hoverOffset:5
        }]
},options: {
    plugins:{
        title:{
            display:false,
            text:"Wave Form by Percentage"
        }
    },
    
    maintainAspectRatio: false
}
})


})

