from this import d
from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game
import random

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

    data, ret, items, alive = game.move(dx,dy)
    print(data)
    if ret:
        print('ret ok man')
        socketio.emit("response", data)
        socketio.emit("response1", items)
    if not alive:
        print('player1 is dead')
        socketio.emit("death p1")
        socketio.emit("response1", items)
        
@socketio.on("move player2")
def on_move_msg2(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret, items, alive = game.move2(dx,dy)
    print(data)
    if ret:
        socketio.emit("response", data)
        socketio.emit("response2", items)
    if not alive:
        print('player2 is dead')
        socketio.emit("death p2")
        socketio.emit("response2", items)

@socketio.on("move_monster")
def on_move_monster(methods=["GET", "POST"]):
    dict = {'dx':0, 'dy':0}
    d = random.choice(['dx', 'dy'])
    r = random.choice([-1, 1])
    dict[d] = r
    dx = dict['dx']
    dy = dict['dy']

    data, ret = game.move_monster(dx, dy)
    print(data)
    if ret:
        socketio.emit("response", data)

if __name__=="__main__":
    socketio.run(app, port=5001) #debug=True



