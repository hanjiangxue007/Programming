# example of dictionary ( gradebook )

print

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
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

# function average which takes list as a argument
def average(numbers):	# numbers = [1,2,3,4] is a list
    total = sum(numbers)
    total = float (total)
    return total/len(numbers)
    
print average([2,3,4])
print average(lloyd["homework"])

#################################################  
print "\nAverage marks of a student"  
def get_average(student):	# student is a dictionary ( not a string)
    homework = average(student["homework"])
    quizzes  = average(student["quizzes"])
    tests    = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests 
print get_average(lloyd)		# 80.55

######################################################
print"\nLetter Grades"    
def get_letter_grade(score):	# score is a number
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
print get_letter_grade(get_average(lloyd))
print get_letter_grade(90)

################################################33
print ("\nClass Average")
def get_class_average(students):	# students = [lloyd,alice] is a list of dictionary
    results = []					# empty list
    for student in students:
    	results.append(get_average(student))
    return average(results)	# results is list of numbers
    
print get_class_average([alice])  # [alice] is a list
print get_average(alice)		  # alice   is a dictionary
print get_class_average([lloyd,alice,tyler])
students = [lloyd,alice,tyler]
print get_class_average(students)

class_avg = get_class_average([lloyd,alice,tyler])

print get_letter_grade(class_avg)

print    
    
        
