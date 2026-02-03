import sys, util, constants, util, db
from flask import Flask, request, render_template

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


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")



# Finally, run the app
run()
