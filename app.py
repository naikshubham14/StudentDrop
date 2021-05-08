from flask import Flask, render_template, request, Markup
import numpy as np
#import sys
#sys.path.insert(1, r"C:\Users\shubh\OneDrive\Documents\DS Web apps\Untitled Folder")
import pickle
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading crop recommendation model


crop_damge_model = pickle.load(open('models/RandomForest.pkl', 'rb'))

# =========================================================================================

# Custom functions for calculations


# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

# render crop recommendation form page




# render fertilizer recommendation form page



# render damage prediction input page


@ app.route('/crop-damage')
def crop_damage():
    title = 'Student Dropout Prediction'

    return render_template('crop-damage.html', title=title)

#@ app.route('/team')
#def team():
 #   title = 'AgriSmart - Team'

  #  return render_template('team.html', title=title)





# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page


#Crop Damage Prediction render
@app.route('/predict', methods=['POST'])
def dam_pred():
    data1= request.form['Residence_city']
    data2= request.form['Socioeconomic_level']
    data3= request.form['Age']
    data4= request.form['Province']
    data5= request.form['Family_income']
    data6= request.form['Father_level']
    data7= request.form['Mother_level']
    data8= request.form['STEM_subjects']
    data9= request.form['H_subjects']
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9]])
    pred_c = crop_damge_model.predict(arr)
    if pred_c==0:
        prediction="Not a Dropout"
    elif pred_c==1:
        prediction="Dropout"
    
    
    return render_template('crop-damage-result.html', data=prediction)

# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
