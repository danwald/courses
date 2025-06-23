from flask import Flask, render_template, request, jsonify

from ice_breaker import ice_break_with

from typing import Any

app = Flask(__name__)


@app.route("/")  # type: ignore
def index() -> Any:
    return render_template("index.html")


@app.route("/process", methods=["POST"])  # type: ignore
def process() -> Any:
    name = request.form["name"]
    summary_and_facts, profile_pic_url = ice_break_with(name=name)
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": {},  # interests.to_dict(),
            "ice_breakers": {},  # ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
