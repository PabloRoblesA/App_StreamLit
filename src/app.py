from pickle import load
import streamlit as st

model = load(open("../models/logistic_regression_default_42.sav", "rb"))

class_dict = {
    "True": "Es",
    "False": "No es",
}

st.title("Prediccion de legendarios")
val1 = st.slider("Total", min_value=180, max_value=780, step=1)
val2 = st.slider("Speed", min_value=1, max_value=255, step=1)

if st.button("Quien es ese pokemon?"):
    prediction = str(model.predict(
        [[val1, val2]])[0])
    pred_class = class_dict[prediction]
    st.write("Quien es ese pokemon?:", pred_class)
