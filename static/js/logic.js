let weapon_url = 'http://127.0.0.1:5000/api/v1.0/wwii_map'
fetch(weapon_url)
    .then(response => response.json())
    .then((mapData) => {
        // console.log(mapData)
        data = JSON.parse(mapData);
        // console.log(data)

        data.forEach(function (mapevent) {
            mapDates = []
            mapDate = mapevent.DATE;
            mapLat = mapevent.LATITUDE;
            mapLon = mapevent.LONGITUDE;
            mapDates.push({
                DATE: mapDate,
                COORDS: [mapLat, mapLon],
            });
            console.log(mapevent);

            function createMap(mapevent);

            let myMap = L.map("map").setView([51.50, -0.09], 5);

            let streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
                attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
                tileSize: 512,
                maxZoom: 20,
                zoomOffset: -1,
                id: "mapbox/streets-v11",
                accessToken: API_KEY
            }).addTo(myMap);


            console.log(mapevent.DATE);
            console.log(mapevent.LATITUDE);
            console.log(mapevent.LONGITUDE)
        })
    }).catch(err => console.log(err))
