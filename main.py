from flask import Flask, send_from_directory
from flask_cors import CORS
import routes

app = Flask(__name__)
CORS(app)
#app.config.update(flask_config)

def static_files(filename, ext):
    file = f"{filename}.{ext}"
    
    return send_from_directory("static", file)


rules = [("/", routes.routes, ["GET"]), 
         ("/<path:route>", routes.routes, ["GET"]),
         ("/<path:filename>.<ext>", static_files, ["GET"]),
         ("/add", routes.add, ['POST']),
         ("/hello", routes.hello, ['POST'])
        ]

for rule in rules:
    app.add_url_rule(rule[0], view_func=rule[1], methods=rule[2])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)

