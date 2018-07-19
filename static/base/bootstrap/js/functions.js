/*workers*/

/*INICIO DEL SCRIPT DE workers*/

function verIndicador(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function verIncidencia(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function verInforActi(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function indicador() {
    var randomnumber = Math.random() * 11;
    $.get("Indicadores?rn=" + randomnumber + "", {}, function (data) {
        $("#indicador").html(data);
    });
}

function indicadorCreate() {
    var randomnumber = Math.random() * 11;
    $.get("IndicadorCreate" + "", {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function verInforme(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11;
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function informe() {
    var randomnumber = Math.random() * 11;
    $.get("Informes?rn=" + randomnumber + "", {}, function (data) {
        $("#informe").html(data);
    });
}


function verMotivo(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11;
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function motivo() {
    var randomnumber = Math.random() * 11;
    $.get("Motivos?rn=" + randomnumber + "", {}, function (data) {
        $("#motivo").html(data);
    });
}

function motivoCreate() {
    var randomnumber = Math.random() * 11;
    $.get("MotivoCreate" + "", {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function verPersonal(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11;
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function personal() {
    var randomnumber = Math.random() * 11;
    $.get("Personales?rn=" + randomnumber + "", {}, function (data) {
        $("#personal").html(data);
    });
}

function personalCreate() {
    var randomnumber = Math.random() * 11;
    $.get("PersonalCreate" + "", {}, function (data) {
        $("#contenidotable").html(data);
    });
}


function verCargo(url) {
    var randomnumber = url + "?rn=" + Math.random() * 11;
    $.get(randomnumber, {}, function (data) {
        $("#contenidotable").html(data);
    });
}

function cargo() {
    var randomnumber = Math.random() * 11;
    $.get("Cargos?rn=" + randomnumber + "", {}, function (data) {
        $("#cargo").html(data);
    });
}

function cargoCreate() {
    var randomnumber = Math.random() * 11;
    $.get("CargoCreate" + "", {}, function (data) {
        $("#contenidotable").html(data);
    });
}