from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/random_forest_classifier_default_42.sav", "rb"))
