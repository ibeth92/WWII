let bombings = "http://127.0.0.1:5000/api/v1.0/weapons";
let date = "$where=MSNDATE between'8/15/1943' and '10/20/1944";
let aircraft = "&AircraftName=B17";
let location = "$"
let limit = "&$limit=1000";

let url = bombings + date + aircraft + limit;

d3.json(url, function (response) {
    let markers = L.markerClusterGroup();

    for (let i = 0; i < response.length; i++) {


    }

})


function createMap(bombings) {
    let streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
    });

    let lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        accessToken: API_KEY
    });

    let darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        zoomOffset: -1,
        id: "dark-v10",
        accessToken: API_KEY
    });
    // Defining baseMaps to hold our base layers
    let baseMaps = {
        "Light Map": lightmap,
        "Street Map": streetmap,
        "Dark Map": darkmap
    };

    // Create overlay object to hold our overlay layer
    let overlayMaps = {
        Bombings: bombings

    };

    let myMap = L.map("map", {
        center: [51.505, -0.09],
        zoom: 100
    });

