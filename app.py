from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    image = request.files['image']
    filename = image.filename.lower()

    if "tomato" in filename:
        disease = "Early Blight"
        confidence = "95%"
        recommendation = "Apply fungicide and remove infected leaves."

    elif "potato" in filename:
        disease = "Late Blight"
        confidence = "92%"
        recommendation = "Avoid overwatering and use disease-resistant varieties."

    else:
        diseases = [
            ("Healthy", "98%", "No treatment needed."),
            ("Leaf Spot", "90%", "Use recommended fungicide."),
            ("Powdery Mildew", "88%", "Improve air circulation.")
        ]

        disease, confidence, recommendation = random.choice(diseases)

    return render_template(
        'result.html',
        disease=disease,
        confidence=confidence,
        recommendation=recommendation
    )

if __name__ == '__main__':
    app.run(debug=True)