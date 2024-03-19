from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template(
        "base.html", 
        title='Jinja2 is free',
    )

@app.route("/results")
def results():
    max_score = 100
    test_name = "Python Challenge"
    students = [
        {
            "name": "Yaromyr",
            "score": 99,
        },{
            "name": "Maxim",
            "score": 95,
        },        {
            "name": "Leonid",
            "score": 79,
        },        {
            "name": "Bohdan",
            "score": 100,
        },        {
            "name": "Nikita",
            "score": 100,
        },        {
            "name": "Nazar",
            "score": 99,
        },
        {
            "name": "Daniil",
            "score": 80,
        },
    ]
    
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }

    return render_template("results.html", **context)

@app.route("/myprojects")
def myprojects():
    projects = [
        ("Old", "Телеграм бот 2023",),
        ("New", "Веб-сайт 2024",),
        ("Old", "Гра в шахи 2023",),
    ]
    students = [
        {
            "name": "Yaromyr",
            "score": 99,
        },{
            "name": "Maxim",
            "score": 95,
        },        {
            "name": "Leonid",
            "score": 79,
        },        {
            "name": "Bohdan",
            "score": 100,
        },        {
            "name": "Nikita",
            "score": 100,
        },        {
            "name": "Nazar",
            "score": 99,
        },
        {
            "name": "Daniil",
            "score": 80,
        },
    ]
    
    context = {
        "projects": projects,
        "students": students,
    }

    return render_template("portfolio.html", **context)


@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        print(f"{request.form=}")
        name = request.form.get("name")
        print(f"{name=}")
    return render_template("auth.html")

@app.route("/hobbies")
def hobbie():
    hobbies = {"name": "Nikita",
               "hobbies": ["Football", 
                           "Basketball", 
                           "Ping-pong",
                           "Swimming",
                           "Listening music", 
                           "Playing computer games"]}
    return render_template("hobbies.html", context= hobbies)
@app.route("/advantages")
def advantage():
    advantages_and_disadvantages = {"name": "Nikita",
                                    "advantages": ["fit",
                                                   "smart",
                                                   "can solve a hard problem",
                                                   "can do something for long time and not getting bored",
                                                   "can talk about a lot of diffrent topics"],
                                    "disadvantages": ["shy",
                                                      "sometimes scared to make new friends"]
                                    }
    return render_template("advantages.html", context = advantages_and_disadvantages)
