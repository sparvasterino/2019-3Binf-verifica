from flask import Flask 

from teti import books

import json

app = Flask("marconi")

@app.route("/")
def data_book():
    return json.dumps(
        [book.__dict__ for book in books]
        )