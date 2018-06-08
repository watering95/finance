    google.charts.load('current', {'packages':['line']});
    google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Day');
    data.addColumn('number', 'KOSPI');
    data.addColumn('number', 'Dollar');
    data.addColumn('number', 'Gold');
    data.addColoum('number', 'CNY');

    data.addRows([
        [1,  37.8, 80.8, 41.8, 1.1],
        [2,  30.9, 69.5, 32.4, 1.1],
        [3,  25.4,   57, 25.7, 1.1]
    ]);

    var options = {
        chart: {
          title: 'Money change',
          subtitle: 'during 3 years'
         },
        width: 900,
        height: 500
    };
    
    var chart = new google.charts.Line(document.getElementById('linechart_material'));
    
    chart.draw(data, google.charts.Line.convertOptions(options));
}