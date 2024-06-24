from pickle import load
import streamlit as st

model = load(open("../models/logistic_regression_default_42.sav", "rb"))
scaler = load(open("../models/scaler.sav", "rb"))

class_dict = {
    "True": "Es un pokemon LEGENDARIO, atrapalo si puedes!",
    "False": "No es un LEGENDARIO, buena suerte la proxima vez.",
}

st.title("Prediccion de legendarios")
val1 = st.slider("Total", min_value=50, max_value=780, step=1)
val2 = st.slider("HP", min_value=1, max_value=255, step=1)

if st.button("Quien es ese pokemon?"):
    prediction = str(model.predict([[val1, val2])[0])
    pred_class=class_dict[prediction]
    st.write("Quien es ese pokemon?:", pred_class)
