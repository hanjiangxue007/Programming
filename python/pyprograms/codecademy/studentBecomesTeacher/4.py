# topic: for loop within dictionaries

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],       # average = 88.5 * 0.1 = 8.85
    "quizzes": [ 88.0, 40.0, 94.0],             # average = 74   * 0.3 = 22.2
    "tests": [75.0, 90.0]                       # average = 82.5 * 0.6 = 49.5
}                                                              # sum   = 80.55
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
print
for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]

# Function average
print
def average(numbers):
    total = sum(numbers)
    total = float (total)
    return total/len(numbers)

print average(lloyd["homework"])

def get_average(student):   # argument student is dictionary
    homework = average(student["homework"]) # student is dictionary and homework is its key
    quizzes  = average(student["quizzes"])
    tests    = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

print get_average(lloyd)        # output: 80.55

def get_letter_grade(score):    # score should be a number
    if type(score) == type(1) or type(score) == type(1.2):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
print
print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

