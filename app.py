

from flask import Flask, render_template

app = Flask(__name__)


data = [
    {
        'web developer': 761
    },
    {
        'graphic design': 306
    },
    {
        'web design': 600
    },
    {
        'typography': 102
    },
{
        'branding': 201
    },
]


@app.route('/')
def hello_world():
    return render_template('views/home.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)









