

window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move player1", {dx:-1, dy:0});
                break;
            case 38:
                socket.emit("move player1", {dx:0, dy:-1});
                break;
            case 39:
                socket.emit("move player1", {dx:1, dy:0});
                break;
            case 40:
                socket.emit("move player1", {dx:0, dy:1});
                break;
    
            case 81:
                socket.emit("move player2", {dx:-1, dy:0});
                break;
            case 90:
                socket.emit("move player2", {dx:0, dy:-1});
                break;
            case 68:
                socket.emit("move player2", {dx:1, dy:0});
                break;
            case 83:
                socket.emit("move player2", {dx:0, dy:1});
                break;
        }


    };
    
    //bouton déplacement premier joueur.
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move player1", {dx:0, dy:-1});
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move player1", {dx:0, dy:1});
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move player1", {dx:-1, dy:0});
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move player1", {dx:1, dy:0});
    };

    //bouton déplacement deuxième joueur
    var btn_n2 = document.getElementById("go_2n2");
    btn_n2.onclick = function(e) {
        console.log("Clicked on button north2");
        socket.emit("move player2", {dx:0, dy:-1});
    };

    var btn_s2 = document.getElementById("go_s2");
    btn_s2.onclick = function(e) {
        console.log("Clicked on button south2");
        socket.emit("move player2", {dx:0, dy:1});
    };

    var btn_w2 = document.getElementById("go_w2");
    btn_w2.onclick = function(e) {
        console.log("Clicked on button w2");
        socket.emit("move player2", {dx:-1, dy:0});
    };

    var btn_e2 = document.getElementById("go_e2");
    btn_e2.onclick = function(e) {
        console.log("Clicked on button e2");
        socket.emit("move player2", {dx:1, dy:0});
    };

    socket.on("response", function(data){       //en créer 2?
        console.log(data);
        for( var i=0; i<2; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.textContent = data[i].content;
        }
    });

    








});