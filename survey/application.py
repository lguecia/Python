import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # validates a form’s submission, alerting users with a message via error.html if they have not completed 1+ fields (if JS code let something through or was disabled)
    First = request.form.get("First")
    Last = request.form.get("Last")
    Gender = request.form.get("Gender")
    Meal = request.form.get("Meal")
    Age = request.form.get("Age")
    Level = request.form.get("Level")
    if not First or not Last or not Gender or not Meal or not Age or not Level:
        return render_template("error.html", message="Please complete all fields")

    # writes the form’s values to a new row in survey.csv using csv.writer or csv.DictWriter
    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("First"), request.form.get("Last"), request.form.get("Gender"),
                         request.form.get("Meal"), request.form.get("Age"), request.form.get("Level")))

    # redirects the user to /sheet
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # return render_template("error.html", message="TODO")

    # reads past submissions from survey.csv using csv.reader or csv.DictReader
    with open("survey.csv", "r") as file:
        reader = csv.reader(file)
        submissions = list(reader)

    # displays those submissions in an HTML table via a new template
    return render_template("submissions.html", submissions=submissions)