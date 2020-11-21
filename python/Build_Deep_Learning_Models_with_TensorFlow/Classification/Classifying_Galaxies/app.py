import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def plot_graph():
  return render_template(
    'plt_tmpl.html', 
    name = "Visualizations Created in Task 12", 
    url1 ='static/images/Galaxy_0Conv0.png', 
    url2='static/images/Galaxy_0Conv1.png', 
    url3='static/images/Galaxy_0.png', 
    url4 ='static/images/Galaxy_1Conv0.png', 
    url5='static/images/Galaxy_1Conv1.png', 
    url6='static/images/Galaxy_1.png',
    url7 ='static/images/Galaxy_2Conv0.png', 
    url8='static/images/Galaxy_2Conv1.png', 
    url9='static/images/Galaxy_2.png', 
    url10 ='static/images/Galaxy_3Conv0.png', 
    url11='static/images/Galaxy_3Conv1.png', 
    url12='static/images/Galaxy_3.png', 
    url13 ='static/images/Galaxy_4Conv0.png', 
    url14='static/images/Galaxy_4Conv1.png', 
    url15='static/images/Galaxy_4.png'
  )
