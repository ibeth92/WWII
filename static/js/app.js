// let url = 'http://127.0.0.1:5000/api/v1.0/bombings'

// async function getData() {
//     const response = await fetch(url);
//     const data = await response.json();
//     console.log(data);
// }

// getData();
// 'data' = data.js list of objects
let tableData = data;
// d3.csv, d3.json
let tbody = d3.select('tbody');

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
// 'datetime' should be changed to our 'date' field
    let filteredData = tableData.filter(bombings => bombings.datetime === inputValue);

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
