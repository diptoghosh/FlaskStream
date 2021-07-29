from application import app, socketio

if __name__ == "__main__":
    socketio.run(app, use_reloader=True, debug=True)