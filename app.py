from flask import Flask, render_template
from routes.task_bp import bp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)