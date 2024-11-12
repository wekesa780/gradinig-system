def grade_system(score):
    """
    This function takes a score as input and returns the corresponding grade.
    """
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score <= 69:
        return 'B'
    elif score >= 50 and score <= 59:
        return 'C'
    elif score >= 40 and score <= 49:
        return 'D'
    elif score <= 39:
        return 'E (Fail) - Supplementary Examination Required'
    else:
        return 'Invalid Score'

# Test the function
score = int(input("Enter the student's score: "))
grade = grade_system(score)
print(f"The student's grade is {grade}.")