from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder="Templates")

@app.route('/')
def requestdata():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)

@app.route('/books/<genre>')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Nacist'
    return res

if __name__ == "__main__":
    app.run(debug=True)