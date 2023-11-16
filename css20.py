<!doctype html>
<html>
   <head>
   <title>demo</title>
<style>
     table, th, td {
       border: 1px solid black;
       border-collapse: collapse;
     }
    th, td {
      padding: 10px;
    }
    table#alter tr:nth-child(even) {
        background-color: red;
    }
    table#alter tr:nth-child(odd) {
       background-color: blue;
    }
    table#alter th {
       color: white;
       background-color: green;
   }
   </style>
   </head>
<body>
  <table id="alter">
       <tr><th>ENO</th><th>ENAME</th><th>ESAL</th><th>EGRADE</th></tr>
       <tr><td>101</td><td>VARSHITHA</td><td>7500</td><td>A</td></tr>
       <tr><td>102</td><td>CHAITANYA</td><td>7000</td><td>A</td></tr>
       <tr><td>103</td><td>DEVI</td><td>7500</td><td>A</td></tr>
       <tr><td>104</td><td>RANI</td><td>7500</td><td>B</td></tr>
       <tr><td>105</td><td>MOHITHA</td><td>7500</td><td>B</td></tr>
  </table>
</body>
</html>

     
     