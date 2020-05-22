const URL = "http://127.0.0.1:8000/appProduccion/produccion/equipos/api/";

let ver = document.getElementById('ver');
ver.addEventListener('click', event => {
    event.preventDefault();
    loadData();
})

function loadData(){
    console.log(URL);
    fetch(URL)
        .then((response) => response.json())
        .then((json) => {
            introducirTabla(json);
        });
}

function crearTabla(json){
    let tabla = `
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Marca</td>
                    <td>Modelo</td>
                </tr>
            </thead>
            <tbody>`;

    for (let dato of json){
        tabla += crearFila(dato.id, dato.marca, dato.modelo);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(id, marca, modelo){
    return `
        <tr>
            <td>${id}</td>
            <td>${marca}</td>
            <td>${modelo}</td>
        </tr>`;
}

function introducirTabla(json){
    let tabla = crearTabla(json);
    document.getElementById('cont').innerHTML = tabla;
}