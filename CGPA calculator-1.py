List_Courses = [] 
unit_courses = []
score_courses = []
Score_grades = []
score_unit = []
GPA_Courses = []

while True:
    courses = input("\nEnter the course code u did in this semester (when done type done): ").upper().strip()
    if courses.lower() == "done":
      correcting_input = input("Did you enter a wrong input when calculating your CGPA 'yes' or 'no': ")
      if correcting_input == "yes":
       # do corrections
        correcting_options = input("where did u make the mistake \n Type 1 for course code \n Type 2 for units \n Type 3 for score\n: ")
        if correcting_options == "1":
           for course in List_Courses:
              correcting_course = input("Which course code do u want to change: ")
              if correcting_course in List_Courses:
               new_course = input("Enter the correct course code: ").strip().upper()
               index = List_Courses.index(correcting_course)
               List_Courses[index] = new_course
               print("✅ Course updated successfully.")
               print(f"\n")

        elif correcting_options == "2":
           correcting_unit = input("What the unit of the course do u want to change: ")
           if correcting_unit in List_Courses:
               new_unit = input("Enter the correct unit code: ").strip().upper()
               index = unit_courses.index(correcting_unit)
               List_Courses[index] = new_unit
               print("✅ Course updated successfully.")
               print(f"\n")
               
        elif correcting_options == "3":
           course_to_change = input("Which course code's score do you want to change? ").strip().upper()
           if course_to_change in List_Courses:
            new_score = int(input("Enter the correct score: "))
            idx = List_Courses.index(course_to_change)
            score_courses[idx] = new_score
            print("✅ Score updated successfully")
        else:
            print("⚠ Course not found.")
            break
      else:
          break
      break   # 🚨 stops the outer loop fully
    else:
       List_Courses.append(courses)
   # then ask for units and score
       
    while True:
       unit_course = input("Enter the unit of the course: ")

       if unit_course.isdigit():  # check if input is a number
        UNITS = int(unit_course)

        if UNITS < 0:  # check if it's less than zero
            print("\nUnits cannot be less than zero. Type your correct course unit.")
            continue  # ask again
        else:
            if len(unit_course) > 1:
               print("\nUnits can only be in tens, Try again")
               continue
            else:
               unit_courses.append(UNITS)
               break  # valid input, exit loop
       else:
        print("\nPlease enter a valid number for course unit.")
        continue

# Now collect the score
    while True:
       score_course = input("Enter what you scored: ")

       if score_course.isdigit():  # check if input is a number
        SCORES = int(score_course)

        if SCORES < 0:  # check if it's less than zero
            print("Your score cannot be less than zero. Type your correct score.")
            continue  # ask again
        else:
            if SCORES > 100:
               print("\nScore can not be more than 100, Try again")
               continue
            else:
               score_courses.append(SCORES)
               break  # valid input, exit loop
       else:
        print("\nPlease enter a valid number for score.")

for course, score in zip(List_Courses,score_courses):
   print (f" Your scored {score} in {course}")
print(f"\n")

for score in score_courses:
   if score < 100 and score >= 70:
      alph = "A"
      Score_grades.append(alph)
      score_unit.append(5)
   elif score< 70 and score >= 60:
      alph = "B"
      Score_grades.append(alph)
      score_unit.append(4)
   elif score < 60 and score >= 50:
      alph = "C"
      Score_grades.append(alph)
      score_unit.append(3)
   elif score < 50 and score >= 45:
      alph = "D"
      Score_grades.append(alph)
      score_unit.append(2)
   elif score < 45 and score >= 40:
      alph = "E"
      Score_grades.append(alph)
      score_unit.append(1)
   else:
      alph = "E"
      Score_grades.append(alph)
      score_unit.append(0)

for grades, course in zip(Score_grades, List_Courses):
   print (f"you grade for {course} is {grades}")
print(f"\n")

for unit, units, Course in zip(score_unit,unit_courses,List_Courses):
   GPA_Course = unit * units
   GPA_Courses.append(GPA_Course)
   print(F"Your GPA of {Course} is {GPA_Course}")
print(f"\n")

sum_units = sum([unit*units for unit,units in zip(score_unit,unit_courses)])
sum_units_courses = sum(unit_courses)
CGPA =  round(sum_units/sum_units_courses,2)
if sum_units_courses != 0:
   print(f"\nYour CGPA is {CGPA}")
   if CGPA >= 4.5:
      print(f"\nCongratulations🥳🎉, you are on a First Class🥳🎉")
   elif CGPA < 4.5 and CGPA>= 3.5 :
      print(f"\nCongratulations🥳🎉, you are on a Second Class Upper🥳🎉")
   elif CGPA < 3.5 and CGPA>= 2.4 :
      print(f"\nCongratulations, you are on a Second Class Lower")
   elif CGPA < 2.4 and CGPA>= 1.5 :
      print(f"\nCongratulations, you are on a Third Class/Pass")
   else:
      print("\nADVICE TO REDRAW")
else: 
   print("\nThe sum of your unit cannot be 0")



