from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Accra, Ghana",
  "Salary": "1,000 GHS",
}, {
  "id": 2,
  "title": "Data Scientist",
  "location": "Dakar, Senegal",
  "Salary": "1,000 francs"
}, {
  "id": 3,
  "title": "Front-end Engineer",
  "location": "Lome, Togo",
  "Salary": "1,000 cfa"
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
