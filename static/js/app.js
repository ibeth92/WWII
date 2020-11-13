const bombing_url = '/api/v1.0/wwii_data'
fetch(bombing_url)
    .then(response => response.json())
    .then((data) => {
      let tableData = JSON.parse(data);
      let tbody =d3.select('tbody');
      tableData.forEach(function (bombingevent) {
        console.log(bombingevent);
        let row = tbody.append('tr');
        Object.entries(bombingevent).forEach(function([key, value]) {
          console.log(key, value);
          let cell = row.append('td');
          cell.text(value);
        });
      });
      let button = d3.select('#filter-btn');
      function runEnter() {
        tbody.html('');
        let inputElement = d3.select('#datetime');
        let inputValue = inputElement.property('value');
        console.log(inputValue);
        let filteredData = tableData.filter(bombing => bombing.DATE === inputValue);
        console.log(filteredData);
        filteredData.forEach(function(results) {
          console.log(results);
          let row = tbody.append('tr');
          Object.entries(results).forEach(function([key, value]) {
            console.log(key, value);
            let cell = row.append('td');
            cell.text(value);
          });
      });
    };
    button.on('click', runEnter);
})
.catch(err => console.log(err));