# Kenn Thomas, Jr.
# kwt61
# BMI WEB App

from flask import Flask, jsonify, request, render_template
from bmi_app import calculate_bmi, classify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.get_json()
    weight = float(data['weight'])  # Convert string to float
    height_ft = int(data['height_ft'])  # Convert string to int
    height_in = int(data['height_in'])  # Convert string to int
    bmi = calculate_bmi(weight, height_ft, height_in)
    classification = classify(bmi)
    return jsonify(BMI=bmi, Classification=classification)

if __name__ == '__main__':
    app.run(debug=True)

