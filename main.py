# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for
from flask.helpers import make_response
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    if request.args.get('e') == None:
        return render_template("login.html")
    else:
        return render_template("login.html",loginerror="ユーザー名またはパスワードが違います")

@app.route("/mypage", methods=["POST"])
def login_manager():
    RequestUserName = request.form["name"]
    RequestPassword = request.form["pass"]
    json_open = open('UserData.json', 'r', encoding="utf-8_sig")
    json_load = json.load(json_open)
    Registration = json_load["0"]["Registration"]
    Registration = int(Registration)
    for i in range(Registration):
        j = i + 1
        j = str(j)
        try:
            UserName = json_load[j]["name"]
            Password = json_load[j]["pass"]
        except KeyError:
            pass
        if RequestUserName == UserName:
            if RequestPassword == Password:
                # 認証完了
                session["login"] = RequestUserName
                return render_template("move.html")
    return render_template("move2.html")

@app.route("/mypage", methods=["GET"])
def mypage():
    if 'login' in session:
        return render_template("mypage.html",name=session['login'])
    else:
        return redirect(url_for('login'))

@app.route("/register", methods=["POST"])
def register_manager():
    RequestUserName = request.form["newname"]
    RequestPassword = request.form["newpass"]
    json_open = open('UserData.json', 'r', encoding="utf-8_sig")
    json_load = json.load(json_open)
    Registration = json_load["0"]["Registration"]
    Registration = int(Registration)
    for i in range(Registration):
        j = i + 1
        j = str(j)
        UserName = json_load[j]["name"]
        Password = json_load[j]["pass"]
        if RequestUserName == UserName:
            return render_template("registererror.html")
    json_open.close()
    Registration = json_load["0"]["Registration"]
    Registration = int(Registration)
    Registration = Registration + 1
    Registration = str(Registration)
    json_load[Registration] = {"name": RequestUserName, "pass": RequestPassword}
    json_load["0"] = {"Registration":Registration}
    with open('UserData.json', mode='w', encoding='utf-8_sig') as file:
        json.dump(json_load, file, indent=1)
    session["login"] = RequestUserName
    return redirect(url_for('mypage'))

@app.route("/logout")
def logout():
    session.pop("login",None)
    return redirect(url_for('login'))

@app.route("/chatroom")
def chatroom():
    if 'login' in session:
        return render_template("chat.html",name=session['login'])
    else:
        return redirect(url_for('login'))

@app.route("/delete")
def delete():
    return "この機能は、まだ未対応です"

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(debug=False, host='0.0.0.0', port=80)