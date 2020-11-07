let tableData = data;

let tbody =d3.select('tbody');

tableData.forEach(function (ufosightings) {
    console.log(ufosightings);

    let row = tbody.append('tr');

    Object.entries(ufosightings).forEach(function([key, value]) {
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

    let filteredData = tableData.filter(sightings => sightings.datetime === inputValue);

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
