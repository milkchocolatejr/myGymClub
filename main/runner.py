import sys, util, constants, util, db, sqlite3
from flask import Flask, request, render_template, session, flash, url_for, redirect

#startup Sequence
util.clear_terminal()
app = Flask(
      import_name= "myGymClub",
          template_folder = constants.TEMPLATE_PATH,
              static_folder = constants.STATIC_PATH)

app.secret_key = 'CS480'
app.config['EXPLAIN_TEMPLATE_LOADING'] = ("-d" in sys.argv)

def run():
  util.print_welcome_message()
  db.init_db()
  app.run(debug=("-d" in sys.argv), port = constants.PORT)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    user = request.args.get("user")
    return render_template('home.html', user=user)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": #get info and display user page
        user = request.form["nm"] #nm is dictionary key for username in html page
        pw = request.form["pw"]

        conn = sqlite3.connect("myGymClub.db")
        cur = conn.cursor()

        cur.execute( #get entry
            "SELECT * FROM User_Records WHERE username=? AND password=?",
            (user, pw)
        )
        record = cur.fetchone()

        conn.close()

        if record: #match found
            return redirect(url_for("home", user=user)) #redirect to user welcome
        else: #no entry found
            flash("Invalid username or password.")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route('/register', methods=["POST", 'GET'])
def register():
    if request.method == "POST": #get info and display user page
        user = request.form["nm"] #nm is dictionary key for username in html page
        pw = request.form["pw"]
        confirmPW = request.form["pw2"]

        if not user or not pw: #Not null username/password
            flash("Username and password cannot be empty.")
            return redirect(url_for("register"))

        elif(pw != confirmPW): #confirm password matches
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))

        try:
            conn = sqlite3.connect("myGymClub.db")
            db.add_user_record(conn, user, pw, 0, 0)  # 0 = not admin
            conn.close()
            flash("Account created successfully.")
            return redirect(url_for("user", usr=user)) #redirect to user welcome
        except sqlite3.IntegrityError:
            flash("Username already exists.")
            return redirect(url_for("register"))

    else:
        return render_template("register.html")



# Finally, run the app
app.run()
