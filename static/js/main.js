

window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move player2", {dx:-1, dy:0});
                socket.emit("move_monster");
                break;
            case 38:
                socket.emit("move player2", {dx:0, dy:-1});
                socket.emit("move_monster");
                break;
            case 39:
                socket.emit("move player2", {dx:1, dy:0});
                socket.emit("move_monster");
                break;
            case 40:
                socket.emit("move player2", {dx:0, dy:1});
                socket.emit("move_monster");
                break;
    
            case 81:
                socket.emit("move player1", {dx:-1, dy:0});
                socket.emit("move_monster");
                break;
            case 90:
                socket.emit("move player1", {dx:0, dy:-1});
                socket.emit("move_monster");
                break;
            case 68:
                socket.emit("move player1", {dx:1, dy:0});
                socket.emit("move_monster");
                break;
            case 83:
                socket.emit("move player1", {dx:0, dy:1});
                socket.emit("move_monster");
                break;
        }


    };
    
    //bouton déplacement premier joueur.
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move player1", {dx:0, dy:-1});
        socket.emit("move_monster");
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move player1", {dx:0, dy:1});
        socket.emit("move_monster");
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move player1", {dx:-1, dy:0});
        socket.emit("move_monster");
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move player1", {dx:1, dy:0});
        socket.emit("move_monster");
    };

    //bouton déplacement deuxième joueur
    var btn_n2 = document.getElementById("go_n2");
    btn_n2.onclick = function(e) {
        console.log("Clicked on button north2");
        socket.emit("move player2", {dx:0, dy:-1});
        socket.emit("move_monster");
    };

    var btn_s2 = document.getElementById("go_s2");
    btn_s2.onclick = function(e) {
        console.log("Clicked on button south2");
        socket.emit("move player2", {dx:0, dy:1});
        socket.emit("move_monster");
    };

    var btn_w2 = document.getElementById("go_w2");
    btn_w2.onclick = function(e) {
        console.log("Clicked on button w2");
        socket.emit("move player2", {dx:-1, dy:0});
        socket.emit("move_monster");
    };

    var btn_e2 = document.getElementById("go_e2");
    btn_e2.onclick = function(e) {
        console.log("Clicked on button e2");
        socket.emit("move player2", {dx:1, dy:0});
        socket.emit("move_monster");
    };

    socket.on("response", function(data){
        console.log("helllooooo")      //en créer 2?
        console.log(data);
        for( var i=0; i<2; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.textContent = data[i].content;
        }
    });

    socket.on("response1", function(items){
        console.log(items);
        for( var i=0; i<2; i++){
            document.getElementById("life").textContent = `Life : ${items[i].life}`;
            document.getElementById("potion").textContent = `Potion : ${items[i].potion}`;
            document.getElementById("weapon").textContent = `Weapon : ${items[i].weapon}`;
            document.getElementById("money").textContent = `Money : ${items[i].money}`;
        }
    });

    socket.on("response2", function(items){
        console.log(items);
        for( var i=0; i<2; i++){
            document.getElementById("life2").textContent = `Life : ${items[i].life}`;
            document.getElementById("potion2").textContent = `Potion : ${items[i].potion}`;
            document.getElementById("weapon2").textContent = `Weapon : ${items[i].weapon}`;
            document.getElementById("money2").textContent = `Money : ${items[i].money}`;
        }
    });

    /*function movement(){
        var dict = {dx:0, dy:0};
        var x = math.floor(math.random()*2);
        var y = math.floor(math.random()*2);
        if (x>0) {
            if (y>0) {
                dict.dy = 1
            } else {
                dict.dy = -1
            }
        } else {
            if (y>0) {
                dict.dx = 1
            } else {
                dict.dx = -1
            }
        }
        return dict
    };

    socket.emit("move monster", movement)*/







});