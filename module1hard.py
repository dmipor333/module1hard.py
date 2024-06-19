grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) #преобразую множество в список
students_alf = sorted(students) #сортирую список в алфавитном порядке
#вычисляю среднюю оценку
grades_a = (sum(grades[0])/len(grades[0]))
grades_b = (sum(grades[1])/len(grades[1]))
grades_c = (sum(grades[2])/len(grades[2]))
grades_d = (sum(grades[3])/len(grades[3]))
grades_e = (sum(grades[4])/len(grades[4]))
result = {students_alf[0] : grades_a, students_alf[1] : grades_b, students_alf[2] : grades_c, students_alf[3] : grades_d, students_alf[4] : grades_e}
print(result)