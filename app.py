from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_update')
def handle_text_update(data):
    # Broadcast the text to everyone EXCEPT the person who just typed
    emit('text_update', data, broadcast=True, include_self=False)

@socketio.on('cursor_move')
def handle_cursor_move(data):
    # Broadcast cursor position, color, and user ID to everyone else
    emit('cursor_move', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    # Use eventlet in production, fallback to default in local
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)