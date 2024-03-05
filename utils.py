import pickle
import numpy as np 
import config

def get_predicted_species(sepal_length, sepal_width, petal_length,petal_width):
    model_file_path =r"logistic.pkl"

 
    with open(model_file_path,"rb") as f:
        model= pickle.load(f)


    test_array=np.array([[sepal_length, sepal_width, petal_length,petal_width]])    
    predicted_species = model.predict(test_array)[0] 

    return predicted_species   
