import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('scripting_tests/client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('TestRunPythonData').sheet1

# Read in the data from the spreadsheet
spreadsheet_data = sheet.get_all_values()

run_times = []
for row in spreadsheet_data:
    # We remove the first 2 items from the row since we are not
    # interested in the Test Name or Avg Run time
    del row[0]
    del row[1]

    run_times.append(row)

# Read in CSV data
csv_data = []
with open("scripting_tests/LatestTestRunData.csv") as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        csv_data.append(row)

# Get the run date from the third item of the second row of the csv_data
run_date = csv_data[1][2]
spreadsheet_header_row = run_times[0]
spreadsheet_header_row.append(run_date)
del spreadsheet_header_row[0]

# Add the data from each run to the end of the same row in the spreadsheet data
for spreadsheet_row, csv_row in zip(run_times[1:], csv_data[1:]):
    # Second column in the csv data is the new run time
    new_value = csv_row[1]
    spreadsheet_row.append(new_value)
    del spreadsheet_row[0]

# Write the new spreadsheet data back into the spreadsheet
for row_index, row in enumerate(run_times):
    for col_index, cell in enumerate(row):
        sheet.update_cell(row_index + 1,col_index + 3, cell)

# Create a chart

# Read in the average data from the spreadsheet
avg_data = sheet.col_values(2)

chart_data = [["Test Name", "Diff from Avg"]]
for avg, current in zip(avg_data[1:], csv_data[1:]):
    diff = float(avg) - float(current[1])
    chart_data.append([current[0], diff])

from string import Template

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
    chart_data_str += '%s,\n'%row

completed_html = html_string.substitute(labels=chart_data[0], data=chart_data_str)

with open('scripting_tests/chart.html', 'w') as f:
    f.write(completed_html)
