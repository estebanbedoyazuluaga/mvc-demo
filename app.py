from flask import Flask, render_template, url_for
from routes.tasks_bp import bp

app = Flask(__name__)

app.register_blueprint(bp, url_prefix='/tasks')
