$(document).ready(function(){
  initMap();
});
var lat = 37.176817;
var lon = -3.589867;

function initMap(){

    var map_street=L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        minZoom: 2,
        id: 'mapbox.run-bike-hike',
        accessToken: 'pk.eyJ1IjoibWFsb2JyYSIsImEiOiJjamxnaDczbnAxNDBoM2txZ2RzdWIyOTVpIn0.oqAEb6w6WtjWEmh6Zuqb4w'
    }).addTo(map);
    var latlng = L.latLng(lat, lon);
    var marker = L.marker(latlng).addTo(map);
    var zoom = 16;
    map.setView(latlng, zoom);
}