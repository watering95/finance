    google.charts.load('current', {'packages':['line']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

    var data = new google.visualization.DataTable();
        data.addColumn('date', 'Day');
        data.addColumn('number', 'KOSPI');
        data.addColumn('number', 'Dollar');
        data.addColumn('number', 'Gold');
        data.addColumn('number', 'CNY');

        data.addRows([
         [new Date('2018-05-08'), 0.99, 1.00, 1.00, 1.00][new Date('2018-05-09'), 0.99, 1.00, 1.00, 1.00][new Date('2018-05-10'), 1.00, 0.99, 1.00, 1.00][new Date('2018-05-14'), 1.00, 1.00, 1.00, 1.00][new Date('2018-05-15'), 0.99, 1.01, 0.98, 1.00][new Date('2018-05-16'), 0.99, 1.00, 0.98, 1.00][new Date('2018-05-17'), 0.98, 1.01, 0.98, 1.00][new Date('2018-05-21'), 0.99, 1.00, 0.98, 1.00][new Date('2018-05-23'), 1.01, 1.00, 0.98, 1.00][new Date('2018-05-24'), 1.00, 1.01, 0.99, 1.00]
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