from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api/projects')
def projects():
    return {"projects": ["Project 1", "Project 2", "Project 3"]}

if __name__ == '__main__':
    app.run(debug=True)
