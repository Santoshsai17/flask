from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India'
}, {
    'id': 2,
    'title': 'Softwarw engineer',
    'location': 'mumbai'
}, {
    'id': 3,
    'title': 'Teting',
    'location': 'delhi, India'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
