from flask import Flask,render_template,session

app = Flask(__name__)
app.config['SECRET_KEY']='ASASD92192JF32U4532FKJFDS'

@app.route("/welcomee/")
def welcomepage():
    session["username"]="xxxxx"
    if session["username"]:
        unm=session["username"]
    return render_template('abc.html',username=unm)


@app.route("/samplee/")
def samplepage():
    if session["username"]:
        unm=session["username"]
    return render_template('abc.html',username=unm)


if __name__ == '__main__':
    app.run(debug=True)