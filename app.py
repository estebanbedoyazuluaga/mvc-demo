from flask import Flask, redirect, url_for
from routes.tasks_bp import bp

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("tasks.show_index"))

app.register_blueprint(bp, url_prefix='/tasks')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)