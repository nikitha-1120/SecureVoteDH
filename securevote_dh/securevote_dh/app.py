from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

voting_open = True

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login_page")
def login_page():
    return render_template("login.html")

@app.route("/dh_page")
def dh_page():
    return render_template("dh.html")

@app.route("/vote_page")
def vote_page():
    return render_template("vote.html")

@app.route("/admin_page")
def admin_page():

    global voting_open

    if voting_open:
        return "Voting still in progress"

    return render_template("admin.html")

@app.route("/login",methods=["POST"])
def login():

    voter=request.form["voter"]

    conn=get_db()
    cur=conn.cursor()

    cur.execute("SELECT * FROM voters WHERE voter_id=?",(voter,))
    user=cur.fetchone()

    if user:
        return jsonify({"status":"ok"})
    else:
        return jsonify({"status":"invalid"})

@app.route("/vote",methods=["POST"])
def vote():

    global voting_open

    if not voting_open:
        return jsonify({"status":"voting_closed"})

    voter=request.form["voter"]
    candidate=request.form["candidate"]

    conn=get_db()
    cur=conn.cursor()

    cur.execute("SELECT voted FROM voters WHERE voter_id=?",(voter,))
    res=cur.fetchone()

    if res[0]==1:
        return jsonify({"status":"already_voted"})

    cur.execute("UPDATE voters SET voted=1 WHERE voter_id=?",(voter,))
    cur.execute("INSERT INTO votes(candidate) VALUES(?)",(candidate,))
    conn.commit()

    return jsonify({"status":"success"})

@app.route("/results")
def results():

    conn=get_db()
    cur=conn.cursor()

    cur.execute("SELECT candidate,COUNT(*) FROM votes GROUP BY candidate")

    data=cur.fetchall()

    return jsonify(data)

@app.route("/end_voting")
def end_voting():

    global voting_open
    voting_open=False

    return "Voting closed. Admin can now view dashboard."

if __name__=="__main__":
    app.run(debug=True)