from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'e6c730e68c495515da8b6a6d0d0d6f16'

@app.route("/", methods=["GET", "POST"])
def home():
    if "score" not in session:
        session['score'] = {"wins": 0, "losses": 0, "draws": 0}

    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(["rock", "paper", "scissor"])

        if user_choice == computer_choice:
            result = "It's a draw!"
            session["score"]["draws"] += 1
        elif (
            (user_choice == "rock" and computer_choice == "scissor") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissor" and computer_choice == "paper")
        ):
            result = "You win!"
            session["score"]["wins"] += 1
        else:
            result = "You lose!"
            session["score"]["losses"] += 1

        session.modified = True

    return render_template("home.html",
                           result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice,
                           score=session["score"])

@app.route("/reset")
def reset():
    session.pop("score", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=10000)
