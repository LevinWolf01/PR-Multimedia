// puntos_encuentro.js - Ubicación de sucursales y puntos clave de pruebas

const puntosGuadalupe = [
    {
        nombre: "Punto de Inico: Test Drive V8",
        coords: [4.6550, -74.0550],
        descripcion: "Pista habilitada para pruebas de 0 a 100 km/h."
    },
    {
        nombre: "Taller Express & Tuning Guadalupe",
        coords: [4.6450, -74.0450],
        descripcion: "Mantenimiento preventivo y reprogramación de ECU."
    },
    {
        nombre: "Centro de Entregas Oficial",
        coords: [4.6600, -74.0600],
        descripcion: "Zona VIP para la entrega de superdeportivos importados."
    }
];

// Dibujar cada marcador en el mapa previamente inicializado
puntosGuadalupe.forEach(punto => {
    L.marker(punto.coords).addTo(mapa)
        .bindPopup(`
            <b>${punto.nombre}</b><br>
            <small>${punto.descripcion}</small>
        `);
});