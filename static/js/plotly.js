<<<<<<< HEAD
// let weapon_url = 'http://127.0.0.1:5000/api/v1.0/wwii_data'
// fetch(weapon_url)
//     .then(response => response.json())
//     .then((mapData) => {
//         // console.log(mapData)
//         data = JSON.parse(mapData);
//         // console.log(data)
//         data.forEach(function (mapevent) {
//             console.log(mapevent);
//         })
// })
// .catch(err => console.log(err))


let dropItems = ['Target Country','Target Location', 'Country Flying Mission']
let points = {'Target Country':'TGT_COUNTRY','Target Location':'TGT_LOCATION', 'Country Flying Mission':'COUNTRY_FLYING_MISSION'}
let selectID
dropItems.forEach(dropDownMenu => {
    d3.select("#selDataset")
    // option is the html element
    .append("option")
    .text(dropDownMenu)
    .property("value", dropDownMenu)
});
// listens for when there is a change to the selDataset, when there is a change then it runs function updateDisplay
d3.selectAll('#selDataset').on("change", handleSubmit); 
function handleSubmit() {
    // use this to prevent the page from refreshing... may or may not be necessary.
    d3.event.preventDefault();
    // select the value from the dropdown
    selectedId = d3.select('#selDataset').node().value;
    let selectedObj = whatever[selectedId] 
    console.log(selectedObj);
    // build your plots
    buildMap(selectedObj);
};

function dataPlots(id) {
// import data with d3 and json and set dropdown menu to names array
    const url = "/api/v1.0/wwii_data";
    d3.json(url).then(function(response) {
            let allData= response;
=======
let weapon_url = 'http://127.0.0.1:5000/api/v1.0/wwii_data'
fetch(weapon_url)
    .then(response => response.json())
    .then((mapData) => {
        // console.log(mapData)
        data = JSON.parse(mapData);
        // console.log(data)
        data.forEach(function (mapevent) {
            console.log(mapevent);
        })
})
.catch(err => console.log(err))


function dataPlots(id) {
>>>>>>> andrew
    let testData = mapevent;
    let filteredData = testData.metadata.filter(meta => meta.id ==id);
    // Bring in sample data by id 
            let cleanData = data.samples.filter(sample => sample.id === id);
            //console.log(cleanData);
    // Clear html in order to popoulate with next sample data
            let index = d3.select("#sample-metadata");
            index.html("")
    // Append to bring in key and value data from dempgraphics info
            Object.entries(filteredData[0]).forEach(
                ([key, value]) => 
                d3.select("#sample-metadata")
                .append("p")
                .text(`${key}: ${value}`)
            );

<<<<<<< HEAD
// // Retrieve top 10 OTU ids for plot OTU and reverse them
//     let idsampleValues = cleanData[0].sample_values.slice(0,10).reverse();
// //console.log(idsampleValues);
//     let topOTU = cleanData[0].otu_ids.slice(0, 10).reverse();
// // Transform OTUs for plotting
// // let otu_id = topOTU.map(d => "OTU " + d)
//     let labels = cleanData[0].otu_labels.slice(0,10).reverse();
// // Create label array
//     let labelArray = []
// // For loop
//     for(let i=0; i<10; i++) {
//             labelArray.push("OTU" + cleanData[0].otu_ids[i])
//         }
=======
>>>>>>> andrew
/**
 * Helper function to select stock data
//  * Returns an array of values
// //  * @param {array} rows
// //  * @param {integer} index
//  * index 0 - Date
//  * index 1 - Open
//  * index 2 - High
//  * index 3 - Low
//  * index 4 - Close
//  * index 5 - Volume
//  */
// function unpack(rows, index) {
//   return rows.map(function(row) {
//     return row[index];
//   });
// }


// // the unpacking function in a nutshell
// let list1 = [['a', 1], ['b', 2]]
// // unpacking will take list1 and run this
// list1.map(element => element[0]) // returns ['a', 'b']



/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {
  // @TODO: YOUR CODE HERE
  d3.json(url).then(function(apiData) {
    let name = apiData.dataset.name;
    let stock = apiData.dataset.dataset_code;
    let startDate = apiData.dataset.start_date;
    let endDate = apiData.dataset.end_date;
    let dates = unpack(apiData.dataset.data, 0);
    let closingPrices = unpack(apiData.dataset.data, 1);

    // DO THIS SO YOU KNOW YOUR DATA IS COMING!
    // console.log('result from api:', apiData);
    // console.log('name: ', name);
    // console.log('stock: ', stock);
    // console.log("Dates: ", dates);
    // console.log('Closing Prices: ', closingPrices);

    let trace1 = {
      x: dates,
      y: closingPrices,
      type: 'scatter',
      mode: 'lines',
      name: name,
      line: {color: '#17BECF'}
    }

    let dataTrace = [trace1];
    let layout = {
      title: `${stock} closing prices`,
      xaxis: {
        range: [startDate, endDate],
        type: 'date'
      },
      yaxis: {
        autorange: true,
        type: 'linear'
      }
    };

    Plotly.newPlot('plot', dataTrace, layout);

  });
}

buildPlot();
