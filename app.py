from flask import Flask, request, render_template, send_from_directory
from main.main import main_page
from loader.loader import load_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_page)
app.register_blueprint(load_post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
