var map = new atlas.Map("map", {
    center: [-122.33, 47.64],
    zoom: 13,
    view: "Auto",
    authOptions: {
        authType: "anonymous",
        clientId: "35267128-0f1e-41de-aa97-f7a7ec8c2dbd",
        getToken: function(resolve, reject, map) {
            var tokenServiceUrl = "https://adtokens.azurewebsites.net/api/HttpTrigger1?code=dv9Xz4tZQthdufbocOV9RLaaUhQoegXQJSeQQckm6DZyG/1ymppSoQ==";

            fetch(tokenServiceUrl).then(r => r.text()).then(token => resolve(token));
        }
    }
});


map.events.add('ready', function() {

    var dataSource = new atlas.source.DataSource();
    map.sources.add(dataSource);
    var point = new atlas.Shape(new atlas.data.Point([-122.33, 47.64]));

    dataSource.add([point]);

    map.events.add('click', function(e) {
        point.setCoordinates(e.position);
        alert("The location you pinned is " + e.position + ". Please use this location while filing up the form.");
    });


    map.layers.add(new atlas.layer.SymbolLayer(dataSource, null));
});