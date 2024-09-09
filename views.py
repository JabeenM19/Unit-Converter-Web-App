from flask import Blueprint, render_template,request,jsonify,redirect,url_for
views= Blueprint(__name__,"views")

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/json")
def json_file():
    return jsonify({})

@views.route("/data")
def data():
    data =request.json
    return jsonify(data)