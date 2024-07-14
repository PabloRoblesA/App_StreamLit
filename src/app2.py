''' Streamlit '''
from pickle import load
import streamlit as st

model = load(open("../models/decision_tree_classifier_default_42.sav", "rb"))

class_dict = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}

st.title("Iris - Modelo de Prediccion")

val1 = st.slider("Ancho de Petalo", min_value=0.0, max_value=4.0, step=0.1)
val2 = st.slider("Largo de Petalo", min_value=0.0, max_value=4.0, step=0.1)
val3 = st.slider("Ancho de Sepalo", min_value=0.0, max_value=4.0, step=0.1)
val4 = st.slider("Largo de Sepalo", min_value=0.0, max_value=4.0, step=0.1)

if st.button("Descubre que especie es:"):
    prediction = str(model.predict([[val1, val2, val3, val4]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)
