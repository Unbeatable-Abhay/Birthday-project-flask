from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        user = request.form["nm"]
        bdate = request.form["bdt"]

        if bdate == "2006-02-04":
            return render_template("b1.html", name = user)
        else:
            return render_template("b2.html")
    else:
        return render_template("wlcm.html")



if __name__ == '__main__':
    app.run(host="0.0.0.0")
