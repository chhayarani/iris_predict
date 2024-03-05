from flask import Flask,render_template, url_for, request
from flask import jsonify
from utils import get_predicted_species
# Initialize Flask Application
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
 
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Make a prediction using the  function
    predicted_species = get_predicted_species(sepal_length, sepal_width, petal_length, petal_width)
    print("predicted_species:",predicted_species)
    species = {0:'Iris-setosa', 1 : 'Iris-versicolor',2:'Iris-virginica'}

    return render_template('index.html', predicted_species= f"{species[predicted_species]}")


if __name__ == "__main__":

    app.run(host='0.0.0.0',port=8080,debug=False)