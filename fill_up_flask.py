from flask import Flask

fill_up = Flask(__name__)

@fill_up.route("/")
def homepage():
    return("Hello! This is '/', route 1 of 3")

@fill_up.route("/two")
def two():
    return("Hello! This is '/two', route 2 of 3")

@fill_up.route("/three")
def three():
    return("Hello! This is '/three', route 3 of 3")

if __name__ == "__main__":
    fill_up.debug = True
    fill_up.run()
