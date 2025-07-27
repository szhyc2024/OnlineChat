from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg':data['username'] + "加入了聊天室" + data['room']}, room=data['room'])

@socketio.on('text')
def text(data):
    send({'msg':data['username'] + ": " + data['msg']}, room=data['room'])

@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({'msg':data['username'] + "退出了聊天室" + data['room']}, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
