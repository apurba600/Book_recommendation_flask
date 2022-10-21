from flask import Flask, render_template, request
from predict import similar_books, b_weights
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = True
    recommended_books = list()
    bookname = str()
    if request.method == 'POST':
        bookname = request.form.get('bookname')
        recommended_books = similar_books(bookname,b_weights)[1:]
        result = False if not recommended_books else True
    return render_template('index.html', recommended_books=recommended_books, bookname=bookname, result=result)


if __name__ == '__main__':
    app.run()
