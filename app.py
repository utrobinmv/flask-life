from flask import Flask, render_template

from game_of_life import GameOfLife

app = Flask(__name__)

game=GameOfLife(width=25, height=25)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    #game=GameOfLife(width=25, height=25)
    game.form_new_generation()
    print(game.counter)
    return render_template('live.html', life = game)

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=5000, debug=True)