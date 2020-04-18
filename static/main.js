//Default country, sets dropdown, animation isn't started, initalises elections variable, counter reset
country = "United Kingdom";
date = "";
$('#countries').val(country.replace(" ", ""));
elections = [];
animation = false;
count = 0;
dates = [];

//Gets the data to create the chart from x, y and z properties
Sijax.request('init');

function init(x,y,z,description) {
    console.log(description)
    description = description;
    //Writes html for all the other factors 
    //points.factor[description] is equal to it's value in the data
    items = "";
    for (i=0; i< description.factors.length; i++) {
        factors = description.factors[i];
        items += '<tr><th>'+factors[1]+'</th><td>'+'{point.'+factors[1]+'}</td></tr>';
    }
    console.log(items)

    //Initalises the chart, using previous properties, sets some fairly standard attributes
    chart = Highcharts.chart('container', {
        chart: {
            type: 'bubble',
            plotBorderWidth: 1,
            zoomType: 'xy'
        },
        legend: {
            enabled: false
        },
        xAxis: {
        	min: description['xScale'][0],
        	max: description['xScale'][1],
            gridLineWidth: 1,
            title: {
                text: description['xDescription']
            },
            labels: {
                format: '{value}'
            }
        },
        yAxis: {
        	min: description['yScale'][0],
        	max: description['yScale'][1],
            startOnTick: false,
            endOnTick: false,
            title: {
                text: description['yDescription']
            },
            labels: {
                format: '{value}'
            }
        },
        tooltip: {
            useHTML: true,
            headerFormat: '<table>',
            pointFormat: '<tr><th colspan="2">{point.name}</th></tr>' +
                '<tr><th>'+description['xDescription']+':</th><td>{point.x}</td></tr>' +
                '<tr><th>'+description['yDescription']+':</th><td>{point.y}</td></tr>' +
                items,
            footerFormat: '</table>',
            followPointer: true
        },

        plotOptions: {
        	bubble: {
            	minSize:'5%',
        	},
            series: {
                dataLabels: {
                    enabled: true,
                    format: '{point.abbrev}',
                    allowOverlap: true,
                    padding: 0,
                }
            }
        },
        series: [{
            data: []
        }]
    });

    Sijax.request('getElections', [country, count])
}


//Add elections to the chart
function draw() {
    //Sets the title
	chart.setTitle({text: country + ": " + date});

	//if the party on the screen is not on the list, remove it 
	for (a=0; a<chart.series[0].data.length; a++) {
		allowed_on_screen = false;
		for (b=0; b<parties.length; b++) {
			if (parties[b].id == chart.series[0].data[a].id) {
				//else, if the party on the screen is on the list, update it 
				allowed_on_screen = true;
				chart.series[0].data[a].update(parties[b]);
			}
		}
		if (allowed_on_screen == false) {
			chart.series[0].data[a].remove(false);
		}
	}

	//if the party on the list is not on the screen, add it 
	for (i=0; i<parties.length; i++) {
		on_screen = false
		for (z=0; z<chart.series[0].data.length; z++) {
			if (chart.series[0].data[z].id == parties[i].id) {
				on_screen = true;
			}
		}
		if (on_screen == false) {
			chart.series[0].addPoint(parties[i]);
		}
	}

    //If something doesn't work, just update anything not working
    chart.series[0].setData(parties);
}

//Handler for animation
setInterval(function() {
   if (animation == true) {
        count +=1; 
        Sijax.request('getElections', [country, count]);
   }
}, 1000);

//Handler for dropdown
$('#countries').on('change', function() {
    animated = false;
    chart.series[0].setData([]);
    country = $('#countries option:selected').text();
    count = 0;
    Sijax.request('getElections', [country, count]);
});

