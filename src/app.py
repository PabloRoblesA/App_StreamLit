from pickle import load
import streamlit as st

model = load(open("../models/logistic_regression_default_42.sav", "rb"))

class_dict = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}

st.title("Prediccion de legendarios")
val1 = st.slider("Total", min_value=180, max_value=780, step=1)
val2 = st.slider("HP", min_value=1, max_value=255, step=1)
val3 = st.slider("Attack", min_value=1, max_value=255, step=1)
val4 = st.slider("Defense", min_value=1, max_value=255, step=1)
val5 = st.slider("Sp. Atk", min_value=1, max_value=255, step=1)
val6 = st.slider("Sp. Def", min_value=1, max_value=255, step=1)
val7 = st.slider("Speed", min_value=1, max_value=255, step=1)

if st.button("Quien es ese pokemon?"):
    prediction = str(model.predict(
        [[val1, val2, val3, val4, val5, val6, val7]])[0])
    pred_class = class_dict[prediction]
    st.write("Quien es ese pokemon?:", pred_class)
