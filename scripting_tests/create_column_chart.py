import csv

# final desired data format
# - Charts [["Test Name", <NumberOfAsserts>, <NumberOfFailedAsserts>]]

# Read in the data from file
data_list = []
with open("scripting_tests/TestAnalysisData.csv") as csv_file:
    # Read in data using csv reader
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        data_list.append(row)

# New list is initialized with headers
chart_data = [data_list[0]]
for row in data_list[1:]:
    num_asserts = int(row[1])
    num_failed_asserts = int(row[2])
    chart_data.append([row[0], num_asserts, num_failed_asserts])

# Create the html for the chart
from string import Template
# First substitution is the header, the rest is the data
html_string = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart(){
      var data = google.visualization.arrayToDataTable([
           $labels,
           $data
          ],
          false); // 'false' means that the first row contains labels, not data.
      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
    <div id="chart_div" style="width:800; height:600"></div>
</body>
</html>
""")

chart_data_str = ''

for row in chart_data[1:]:
    # Create the data string
    chart_data_str += '%s,\n'%row

# Substitute the data into the template
completed_html = html_string.substitute(labels=chart_data[0], data=chart_data_str)

with open('scripting_tests/create_column_chart.html', 'w') as f:
    # Write the html string you've create to a file
    f.write(completed_html)
