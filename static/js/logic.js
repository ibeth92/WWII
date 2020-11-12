let weapon_url = 'http://127.0.0.1:5000/api/v1.0/wwii_map'
fetch(weapon_url)
    .then(response => response.json())
    .then((mapData) => {
        // console.log(mapData)
        data = JSON.parse(mapData);

        for (let d = 0; d < data.length; d ++) {

            const coords = []
            let lat = data[d].LATITUDE
            let lon = data[d].LONGITUDE

            
            coords.push(lat, lon)

            console.log(coords)
            // console.log('Date:', data[d].DATE)
            const mymap = L.map('map-id').setView([0, 0], 5);

            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1,
                accessToken: API_KEY
            }).addTo(mymap);

            var marker = L.marker(coords).addTo(mymap);
        }
    }).catch(err => console.log(err));