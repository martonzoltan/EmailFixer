import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route("/get-result", methods=["POST"])
def get_result():
    data = request.get_json()
    email = data['email']
    if request.method == "POST":
        raw_email = email
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(raw_email),
            temperature=0.6,
            max_tokens=250,
        )
        return jsonify({'result': response.choices[0].text})


def generate_prompt(raw_email):
    return """Based on the below email formulate one that is more professional:
        {}""".format(
        raw_email
    )
