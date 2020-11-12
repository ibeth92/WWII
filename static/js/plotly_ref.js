// Create function for data plotting
function dataPlots(id) {
// Read in samples.json and call function to populate dropdown menu
// Create object for filtering and populate it with data from samples.json
    d3.json("Data/samples.json").then((data) => {
        console.log(data)
        let testData = data;
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
// Retrieve top 10 OTU ids for plot OTU and reverse them
        let idsampleValues = cleanData[0].sample_values.slice(0,10).reverse();
//console.log(idsampleValues);
        let topOTU = cleanData[0].otu_ids.slice(0, 10).reverse();
// Transform OTUs for plotting
// let otu_id = topOTU.map(d => "OTU " + d)
        let labels = cleanData[0].otu_labels.slice(0,10).reverse();
// Create label array
        let labelArray = []
// For loop
        for(let i=0; i<10; i++) {
            labelArray.push("OTU" + cleanData[0].otu_ids[i])
        }
// Create trace variable for plotting
        let trace = {
            x: idsampleValues,
            y: labelArray,
            text: labels,
            marker: { 
                size: 16, 
                color: 'blue'
            },
            type: "bar",
            orientation: "h",
            mode: 'markers',
         };
// Create the data variable
        let barInfo = [trace];
// Create layout variable to set plots layout
        let layout = {
            title: "Top 10 OTU vs Sample Values",
            yaxis: {
                //tickmode: "linear", 
                title: "OTU IDs"
            },
            xaxis: {title: "Sample Values"},
            showlegend: false,
        };
// Create the bar plot
        Plotly.newPlot("bar", barInfo, layout);
        //console.log???
// Create the bubble plot
        let newtrace = {
            y: sampleValues,
            x: topOTU,
            mode: "markers",
            marker: {
                size: sampleValues,
                color: topOTU,
            },
            text: labels
        };
 // Create the layout for the bubble plot
        let layoutB = {
            title: "Marker Size",
            xaxis: { title: "Top 10 OTU" },
            yaxis: { title: "Top 10 Values"},
            height: 600,
            width: 1000,
            showlegend: false
        };
 // Create the data variable 
        let dataB = [newtrace];
 // Create the bubble plot
        Plotly.newPlot("bubble", dataB, layoutB);
    });
 };
 // Create function for the change event
function optionChanged(id) {
        dataPlots(id);
        dataInfo(id);
 };
// Read in samples.json and create function to render plots with data
    function init() {
// Select dropdown menu 
        let dropdownMenu = d3.select("#selDataset");
// Read in sample data 
        d3.json("Data/samples.json").then((data) => {
            console.log(data);
// Populate name id data to the dropdwown menu
        let testid = data.names;
// Append values 
        testid.forEach(name=> {
            dropdownMenu.append("option")
                .text(name)
                .property("value");
            });
            data.samples.forEach(sampleValues => 
            console.log(sampleValues));
            // Demographic info
            let demoData = data.metadata.filter(sample => sample.id)[0];
            console.log(demoData);
// Append to bring in key and value data from dempgraphics info
            Object.entries(demoData).forEach(
            ([key, value]) => d3.select("#sample-metadata")
            .append("p")
            .text(`${key}: ${value}`)
            );
// Call functions to display the data plots to the page
            dataPlots(data.names[0]);
            dataInfo(data.names[0]);
            });
};
init();