from flask import Flask, request, jsonify, render_template, url_for
import math
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/About_Us")
def about_page():
    return render_template("About_Us.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == 'POST':
        body = request.get_json()
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')
    return render_template("contact.html")

@app.route("/newsletter-subscribe", methods=["POST"])
def subscribe_to_newsletter():
        if request.method == 'POST':
            body = request.get_json()
            email = body.get('email')        
            subject = 'You Have Sucessfully Subscribed to our Newsletter'
            body = "Hello from CoDragons Team,\n\n"\
            "Thank you for subscribing to our monthly newsletter"+'.\n\n'\
            "Regards,"

@app.route("/faq")
def faq_page():
        return render_template("faq.html")

@app.route("/information_covid19")
def faq_ar_page():
    return render_template("information_covid19.html")

@app.route("/prevention")
def prevention_page():
    return render_template("prevention.html")

@app.route("/information_cancer")
def prevention_ar_page():
    return render_template("information_cancer.html")

@app.route("/search")
def search_page():
    return render_template("search.html")

@app.route("/information_heartattacks")
def search_ar_page():
    return render_template("information_heartattacks.html")

@app.route("/symptom")
def symptom_page():
    return render_template("symptom.html")

@app.route("/videos_covid19")
def symptom_ar_page():
    return render_template("videos_covid19.html")

@app.route("/symptom-checker-lung")
def symptom_checker_lung_page():
    return render_template("symptom-checker-lung.html")

@app.route("/videos_cancer")
def symptom_checker_lung_ar_page():
    return render_template("videos_cancer.html")

@app.route("/symptom-checker-covid")
def symptom_checker_covid_page():
    return render_template("symptom-checker-covid.html")

@app.route("/videos_heartattacks")
def symptom_checker_covid_ar_page():
    return render_template("videos_heartattacks.html")

@app.route("/symptom-checker-pneumonia")
def symptom_checker__pneumonia_page():
    return render_template("symptom-checker-pneumonia.html")

@app.route("/Forum_covid19")
def symptom_checker__pneumonia_ar_page():
    return render_template("Forum_covid19.html")

@app.route("/virus-checker")
def virus_checker_page():
    return render_template("pages/virus-checker.html")

@app.route("/Forum_cancer")
def virus_checker_ar_page():
    return render_template("Forum_cancer.html")

@app.route("/tracker")
def tracker_page():
    return render_template("pages/tracker.html")

@app.route("/Forum_heartattacks")
def tracker_ar_page():
    return render_template("Forum_heartattacks.html")

# **************************************** #

#            covid-19 prediction           #

# **************************************** #

def index():
    if request.method == 'POST':
        answers = {
            'fever': request.form.get('fever'),
            'cough': request.form.get('cough'),
            'breathlessness': request.form.get('breathlessness'),
            'fatigue': request.form.get('fatigue'),
            'loss_of_taste_smell': request.form.get('loss_of_taste_smell'),
            'sore_throat': request.form.get('sore_throat'),
            'muscle_pain': request.form.get('muscle_pain'),
            'diarrhea': request.form.get('diarrhea'),
            'headache': request.form.get('headache'),
            'contact': request.form.get('contact'),
            'bathroom_frequency': request.form.get('bathroom_frequency')
        }
        result = assess_covid_risk(answers)
        return render_template('Covied_19.html', result=result)
    return render_template('Covied_19.html')

def assess_covid_risk(answers):
    total_questions = 11 
    yes_count = 0
    
    if answers.get('fever') == 'yes':
        yes_count += 1
    if answers.get('cough') == 'yes':
        yes_count += 1
    if answers.get('breathlessness') == 'yes':
        yes_count += 1
    if answers.get('fatigue') == 'yes':
        yes_count += 1
    if answers.get('loss_of_taste_smell') == 'yes':
        yes_count += 1
    if answers.get('sore_throat') == 'yes':
        yes_count += 1
    if answers.get('muscle_pain') == 'yes':
        yes_count += 1
    if answers.get('diarrhea') == 'yes':
        yes_count += 1
    if answers.get('headache') == 'yes':
        yes_count += 1
    if answers.get('contact') == 'yes':
        yes_count += 1

    try:
        bathroom_visits = int(answers.get('bathroom_frequency', 0))
        if bathroom_visits > 5:
            yes_count += 1
    except ValueError:
        pass 
    
    risk_percentage = (yes_count / total_questions) * 100
    
    if risk_percentage >= 70:
        return f"High Risk ({risk_percentage:.1f}% chance of COVID-19. Seek medical advice!)"
    else:
        return f"Low Risk ({risk_percentage:.1f}% chance of COVID-19. Monitor symptoms.)"



# **************************************** #

#          Lung Cancer prediction          #

# **************************************** #

def assess_lung_cancer_risk(answers):
    total_questions = 11
    yes_count = 0
    
    if answers.get('smoking') == 'yes':
        yes_count += 1
    if answers.get('age') == 'yes':
        yes_count += 1
    if answers.get('family_history') == 'yes':
        yes_count += 1
    if answers.get('cough_blood') == 'yes':
        yes_count += 1
    if answers.get('chronic_cough') == 'yes':
        yes_count += 1
    if answers.get('chest_pain') == 'yes':
        yes_count += 1
    if answers.get('weight_loss') == 'yes':
        yes_count += 1
    if answers.get('shortness_breath') == 'yes':
        yes_count += 1
    if answers.get('asbestos_exposure') == 'yes':
        yes_count += 1
    if answers.get('radiation_exposure') == 'yes':
        yes_count += 1
    
    try:
        cough_frequency = int(answers.get('cough_frequency', 0))
        if cough_frequency > 10:
            yes_count += 1
    except ValueError:
        pass
    
    risk_percentage = (yes_count / total_questions) * 100
    
    if risk_percentage >= 70:
        return f"High Risk ({risk_percentage:.1f}% chance of lung cancer. Consult a doctor immediately!)"
    elif risk_percentage >= 40:
        return f"Moderate Risk ({risk_percentage:.1f}% chance. Consider screening.)"
    else:
        return f"Low Risk ({risk_percentage:.1f}% chance. Monitor symptoms if concerned.)"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answers = {
            'smoking': request.form.get('smoking'),
            'age': request.form.get('age'),
            'family_history': request.form.get('family_history'),
            'cough_blood': request.form.get('cough_blood'),
            'chronic_cough': request.form.get('chronic_cough'),
            'chest_pain': request.form.get('chest_pain'),
            'weight_loss': request.form.get('weight_loss'),
            'shortness_breath': request.form.get('shortness_breath'),
            'asbestos_exposure': request.form.get('asbestos_exposure'),
            'radiation_exposure': request.form.get('radiation_exposure'),
            'cough_frequency': request.form.get('cough_frequency')
        }
        result = assess_lung_cancer_risk(answers)
        return render_template('result.html', result=result)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
