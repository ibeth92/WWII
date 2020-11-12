let weapon_url = 'http://127.0.0.1:5000/api/v1.0/weapons'
fetch(weapon_url)
    .then(response => response.json())
    .then((weaponData) => {
        console.log(weaponData)
    })
    .catch(err => console.log(err))


let myMap = L.map("map").setView([51.50, -0.09], 5);

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 20,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}).addTo(myMap);
