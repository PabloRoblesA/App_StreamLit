from pickle import load
import streamlit as st

model = load(open("../models/random_forest_boosting_42.sav", "rb"))

class_dict = {

    "Erratic": "Crecimiento erratico",
    "Fast": "Crecimiento rapido",
    "Fluctuating":"Crecimiento fluctuante",
    "Medium Fast": "Crecimiento medio rapido",
    "Medium Slow": "Crecimiento medio lento",
    "Slow": 'Crecimiento lento'
}

st.title("Tasa de crecimiento de Pokemon")

val1 = st.slider("total", min_value=175, max_value=720, step=1)
val2 = st.slider("catch_rate", min_value=3, max_value=255, step=1)

if st.button("¿A que velocidad crece tu pokemon?"):

    prediction = str(model.predict([[val1,val2]])[0])
    pred_class = class_dict[prediction]
    st.write("Pokemon de:", pred_class)
