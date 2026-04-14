import numpy as np

def get_student_details():
  n=int(input("enter number of students to add : "))
  names=[]
  marks=[]
  for i in range (n):
    name_=input(f"enter name of student {i+1} : ")
    subjects=int(input(f"enter number of subjects of {name_} : "))
    marks_=[]
    for j in range (subjects):
      m = float(input(f"  Marks for subject {j+1}: "))
      marks_.append(m)
    names.append(name_)
    marks.append(marks_)
  return names,marks

def store_numpy(marks):
  marks2= np.array(marks)
  return marks2

def calculate(marks2):
  total=np.sum(marks2,axis=1)
  average=np.mean(marks2, axis=1)
  max_=np.max(marks2, axis=1)
  min_=np.min(marks2, axis=1)
  return total,average,max_,min_

def grade(average):
  if average >= 85:
        return "A"
  elif average >= 70:
        return "B"
  elif average >= 50:
        return "C"
  else:
        return "Fail"

def display(names, totals, averages, highest, lowest):
    print('STUDENT MARKS REPORT : ')
    for i in range(len(names)):
        print(f"Student  : {names[i]}")
        print(f"Total    : {totals[i]:}")
        print(f"Average  : {averages[i]:}")
        print(f"Highest  : {highest[i]:}")
        print(f"Lowest   : {lowest[i]:}")
        print(f"Grade    : {grade(averages[i])}")
        print("-"*55)

names,marks = get_student_details()
marks_ =store_numpy(marks)
total,average,max_,min_=calculate(marks_)
display(names,total,average,max_,min_)

