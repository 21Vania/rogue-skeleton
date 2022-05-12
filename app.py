from this import d
from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game

app = Flask(__name__)
socketio = SocketIO(app)    
game = Game()


@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move player1")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret = game.move(dx,dy)
    print(data)
    if ret:
        print('ret ok man')
        socketio.emit("response", data)
        
@socketio.on("move player2")
def on_move_msg2(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret = game.move2(dx,dy)
    print(data)
    if ret:
        socketio.emit("response", data)


if __name__=="__main__":
    socketio.run(app, port=5001, debug=True)



