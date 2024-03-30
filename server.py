
from flask import Flask, request,jsonify, render_template
from recommender import recommender

app = Flask(__name__, template_folder='web',static_folder='web/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Invalid request. Content-Type must be 'application/json'."}), 400

    data = request.json

    # Check if 'topic' and 'difficulty_level' are present in the request
    if 'topic' not in data or 'difficulty_level' not in data:
        return jsonify({"error": "Invalid request. 'topic' and 'difficulty_level' are required."}), 400

    topic = data['topic']
    difficulty_level = data['difficulty_level']
    # Call the recommender system functio
    recommended_solutions = recommender(topic, difficulty_level)
    return jsonify({"solutions": recommended_solutions})

if __name__ == '__main__':
    app.run(debug=True)