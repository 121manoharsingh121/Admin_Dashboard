

// line code

new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
      labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
      datasets: [{ 
          data: [86,114,106,106,107,111,133,221,783,2478],
          label: "india",
          borderColor: "#3e95cd",
          fill: false
        }, { 
          data: [282,350,411,502,635,809,947,1402,3700,5267],
          label: "America",
          borderColor: "#8e5ea2",
          fill: false
        }, { 
          data: [168,170,178,190,203,276,408,547,675,734],
          label: "Europe",
          borderColor: "#3cba9f",
          fill: false
        }, { 
          data: [40,20,10,16,24,38,74,167,508,784],
          label: "Latin America",
          borderColor: "#e8c3b9",
          fill: false
        }, { 
          data: [6,3,2,2,7,26,82,172,312,433],
          label: "North America",
          borderColor: "#c45850",
          fill: false
        }
      ]
    },
    options: {
        responsive: true,
      title: {
        display: true,
        text: 'World population per region (in millions)'
      }
    }
  });

  // pie


  new Chart(document.getElementById('mycht'),{
    type:'pie',
    data:{
        labels:['Assigned','NotAssigned','Ressigned'],
        datasets:[{
            data:[40,50,10],
            borderWidth:2,
            backgroundColor:['red','green','yellow'],
        }]
    },
    options:{
        scale:{
            y:{
                beganAtZero:true
            }
        }
    }
    
    });


// Bar chart
new Chart(document.getElementById("mybar"), {
  type: 'bar',
  data: {
    labels: ["delhi", "Noida", "Agra", "Bombay", "Banglore"],
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: [2478,5267,734,784,433]
      }
    ]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});

// area
new Chart(document.getElementById('area-cht'),{
  type:'polarArea',
  data:{
      labels:['india','usa','kanada','franch'],
      datasets:[

          {
              label: 'poputation',
              backgroundColor:['red','yellow',"green",'pink'],
              data:[30,20,40,10]
          }
      ]
  },
  options:{
      tittle:{
          display:true,
          text:'mayank raghav'
      }
  }

});


// bubble

new Chart(document.getElementById("bubble"), {
  type: 'bubble',
  data: {
    labels: "India",
    datasets: [
      {
        label: ["Delhi"],
        backgroundColor: "rgba(255,221,50,0.2)",
        borderColor: "rgba(255,221,50,1)",
        data: [{
          x: 21269017,
          y: 5.245,
          r: 15
        }]
      }, {
        label: ["Noida"],
        backgroundColor: "rgba(60,186,159,0.2)",
        borderColor: "rgba(60,186,159,1)",
        data: [{
          x: 258702,
          y: 7.526,
          r: 10
        }]
      }, {
        label: ["Banglore"],
        backgroundColor: "rgba(0,0,0,0.2)",
        borderColor: "#000",
        data: [{
          x: 3979083,
          y: 6.994,
          r: 15
        }]
      }, {
        label: ["Agra"],
        backgroundColor: "rgba(193,46,12,0.2)",
        borderColor: "rgba(193,46,12,1)",
        data: [{
          x: 4931877,
          y: 5.921,
          r: 15
        }]
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Predicted world population (millions) in 2050'
    }, scales: {
      yAxes: [{ 
        scaleLabel: {
          display: true,
          labelString: "Happiness"
        }
      }],
      xAxes: [{ 
        scaleLabel: {
          display: true,
          labelString: "GDP (PPP)"
        }
      }]
    }
  }
});


// radar chart


new Chart(document.getElementById("radar-chart"), {
  type: 'radar',
  data: {
    labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
    datasets: [
      {
        label: "1950",
        fill: true,
        backgroundColor: "rgba(179,181,198,0.2)",
        borderColor: "rgba(179,181,198,1)",
        pointBorderColor: "#fff",
        pointBackgroundColor: "rgba(179,181,198,1)",
        data: [8.77,55.61,21.69,6.62,6.82]
      }, {
        label: "2050",
        fill: true,
        backgroundColor: "rgba(255,99,132,0.2)",
        borderColor: "rgba(255,99,132,1)",
        pointBorderColor: "#fff",
        pointBackgroundColor: "rgba(255,99,132,1)",
        pointBorderColor: "#fff",
        data: [25.48,54.16,7.61,8.06,4.45]
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Distribution in % of world population'
    }
  }
});