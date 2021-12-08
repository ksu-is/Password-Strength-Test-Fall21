import os



from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']

    #split password inputed into a list and set variable for password strength score
    inputName.split(",")
    strength_score = 0
    
    #gathers points based on what the password is comprised of. Tests for characters, numerics, and special characters
    for character in inputName:
        if character.isalpha():
            if character.isupper():
                strength_score += 5
            else:   
                strength_score += 2
        elif character.isdigit():
            strength_score += 5
        else:
            strength_score += 6

    #gathers points on how long password is
    if len(inputName) < 5:
        strength_score += 10
    elif len(inputName) >= 5 and len(inputName) < 8:
        strength_score += 20
    elif len(inputName) >= 8 and len(inputName) < 11:
        strength_score += 30
    else:
        strength_score += 40

    #gathers score for password based on points collected
    if strength_score < 25:
        final_score = "Weak! Add more upper case characters, digits, or special characters!"
    elif strength_score >=25 and strength_score < 50:
        final_score = "Under Average! Keep adding more characters and digits!"
    elif strength_score >=50 and strength_score < 75:
        final_score = "Above Average! Password is strong but could be stronger with more characters/digits!"
    else:    
        final_score = "Excellent! Password is strong! Remember to copy and save your password in a secure location"
    
    #prints password given, points score, and final evaluation. Reminds user to save passcode in a secure location
    inputName ="\n" + inputName + "\n is the password you inputed, and it has a strength of " + str(strength_score) + "! " + final_score
    return render_template("home.html",myName=inputName)

@app.route('/') 
def home():
    return render_template("home.html",myName="")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    
