from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load projects from JSON file
def load_projects():
    with open("data/projects.json") as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port='8080')
