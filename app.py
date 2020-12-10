import json

from flask import Flask, Response, request

from tools import get_appearence


app = Flask(__name__)


@app.route("/api/appearence/", methods=["POST"])
def appearence():
    data = request.get_json()

    if data is None or not all(
        key in {"lesson", "tutor", "pupil"} for key in data
    ):
        return Response(status=400, mimetype="application/json")

    appearence = get_appearence(data)

    return Response(
        json.dumps({"appearence": appearence}), 
        status=200, 
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
