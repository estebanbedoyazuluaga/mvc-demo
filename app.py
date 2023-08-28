from flask import Flask, render_template, url_for
from routes.task_bp import bp

app = Flask(__name__)

app.register_blueprint(bp, url_prefix='/tasks')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
