from flask import Flask, request, render_template

app = Flask(__name__, template_folder='public')

previous_word = "しりとり"
words = [] 
start_word = "しりとり"
len_words = 0

@app.route('/')
def index():
    previous_word = "しりとり"
    return render_template('index.html', previous_word=previous_word, start_word=start_word)

@app.route('/reset')
def reset():
    global previous_word
    global words
    previous_word  = "しりとり"
    words = []
    miss = ''
    return render_template('index.html', previous_word=previous_word, miss=miss, start_word=start_word, )

@app.route('/enter', methods=['POST'])
def enter():
    global previous_word
    global words
    global len_words
    enter_word = request.form['word']

    if enter_word == '' :
        miss = "前の単語に続いていません"
        return render_template('index.html', previous_word=previous_word, miss=miss, word=enter_word, words=words, start_word=start_word)
    
    pre_end_value = previous_word[-1]
    ent_head_value = enter_word[0]

    if pre_end_value == ent_head_value:
        miss = ''

        if enter_word[-1] == "ん" :
            return render_template('end.html', word = enter_word, len_words=len_words, words=words, start_word=start_word)
        
        elif enter_word in words:
            return render_template('same_word.html', word = enter_word, len_words=len_words, words=words, start_word=start_word)
        
        else :
            previous_word = enter_word
            words.append(previous_word)
            len_words = len(words)
            return render_template('index.html', previous_word=previous_word, miss=miss, words=words, start_word=start_word)
        
    else :
        miss = "前の単語に続いていません"
        return render_template('index.html', previous_word=previous_word, miss=miss, word=enter_word, words=words, start_word=start_word)

if __name__ == '__main__' :
    app.run(debug=True, port=8000)
