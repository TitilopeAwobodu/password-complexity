def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any (char.islower() for char in password):
            score += 1
        if any (char.isdigit() for char in password):
            score += 1
        if any (not char.isalnum() for char in password):
            score += 1


    feedback = "" 

    if score == 0:
        feedback = "very weak"  
    elif score == 1:
        feedback = "weak" 
    elif score == 2:
        feedback = "medium" 
    elif score == 3:
        feedback = "strong" 
    elif score == 4:
        feedback = "very strong"  
    elif score == 5:
        feedback = "Excellent" 

    return feedback
password = "#vU2_%SHbyl"
strength = password_strength(password) 

print("password strength:", strength)