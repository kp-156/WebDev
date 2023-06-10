from flask import Flask, render_template, jsonify

app = Flask(__name__)
QUIZZES = [
  {
    'id': 1,
    'title': 'What kind of potato are you?'
    
  },
  {
    'id': 2,
    'title': 'What your favorait potato dish thinks of you'
    
  },
  {
    'id': 3,
    'title': 'How many potatos do you think it cost to build a potato castle'
    
  },
  {
    'id': 4,
    'title': 'How many potatoes will it take to defeat The Rock'
    
  }
]

@app.route("/")
def hello_potatoes():
  return render_template('home.html', quizzes = QUIZZES)

@app.route("/api/quizzes")
def list_quiz():
  return jsonify(QUIZZES)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)