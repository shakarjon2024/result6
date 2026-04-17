from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result6():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        age = request.form.get("age")

        return render_template("result6.html", name=name, phone=phone, age=age)


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
