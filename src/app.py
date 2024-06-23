from pickle import load
import streamlit as st

model = load(open("../models/logistic_regression_default.sav", "rb"))

class_dict = {
    "True": "Es un pokemon LEGENDARIO, atrapalo!",
    "False": "Mejor suerte la proxima, no es LEGENDARIO.",
}

st.title("Prediccion de legendarios")

val = st.slider("Total", min_value=0, max_value=750, step=1)

if st.button("Quien es ese pokeon?"):

    prediction = str(model.predict([[val]])[0])
    pred_class = class_dict[prediction]
    st.write("Quien es ese pokeon?:", pred_class)
