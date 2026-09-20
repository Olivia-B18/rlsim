import functools
from flask_login import current_user
from flask_socketio import disconnect
from .extensions import socketio

# DEV: socket auth is commented out to match views.py where "# @login_required"
# is disabled while pages are being built. Re-enable "# @authenticated_only"
# lines below at the same time as the decorators in views.py.

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on("connect")
# @authenticated_only
def handle_connect():
    print("client connected")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"user {username} joined")

@socketio.on("train")
# @authenticated_only
def handle_train(food, alive, die):
    if(food != "" and alive != "" and die != ""):
        from .agent import start
        start(food, alive, die)
    else:
        print("error")