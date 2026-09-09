// mapa.js - Inicialización del mapa en el concesionario principal

// Coordenadas del Showroom Principal (Ejemplo: Bogotá)
const latitudShowroom = 4.6510;
const longitudShowroom = -74.0510;

// Instanciar el mapa apuntando al contenedor HTML con id="mapa"
const mapa = L.map('mapa').setView([latitudShowroom, longitudShowroom], 13);

// Capa de mapa base usando OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap - Deportivos Guadalupe'
}).addTo(mapa);

// Marcador principal con ventana emergente
const marcadorPrincipal = L.marker([latitudShowroom, longitudShowroom]).addTo(mapa);
marcadorPrincipal.bindPopup(`
    <div style="text-align: center;">
        <h4 style="margin: 0;">Deportivos Guadalupe</h4>
        <p style="margin: 5px 0 0 0;">Showroom Principal & Vitrina VIP</p>
    </div>
`).openPopup();