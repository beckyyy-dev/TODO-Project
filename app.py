from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todos = ["vkbdsnlblknd", "kabv uejduk"]


# Display todos
@app.route("/")
def home():
    return render_template("home.html", todos=todos)


# Create todo
@app.route("/add", methods=["POST"])
def add_todo():

    todo = request.form["add"]

    if todo:
        todos.append(todo)

    return redirect(url_for("home"))


# Update todo
@app.route("/update/<i>", methods=["POST"])
def update(i):

    new_todo = request.form["update"]

    if new_todo:
        index = todos.index(i)
        todos[index] = new_todo

    return redirect(url_for("home"))


# Delete todo
@app.route("/delete/<i>", methods=["POST"])
def delete(i):

    index = todos.index(i)

    if len(i) != 0:
        todos.pop(index)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)