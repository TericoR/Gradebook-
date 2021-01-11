last_semester_gradebook = [("Politics", 80), ("Latin", 96), ("Dance", 97), ("Architecture", 65)]

subjects = ['Physics', 'Calculus', 'Poetry', 'History']
grades = [98, 97, 85, 88]
gradebook = zip(subjects, grades)
subjects.append('Computer Science')
grades.append(100)
subjects.append('Visual Arts')
grades.append(93)
full_gradebook = zip(gradebook, last_semester_gradebook)
print(list(full_gradebook))
