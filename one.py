from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world. This is my first page."

if __name__ == "__main__":
	app.run(debug=True)

print("Hello")