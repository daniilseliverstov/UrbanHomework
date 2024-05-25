grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ABC = sorted(students)
aver = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
result = {ABC[0]:aver[0], ABC[1]:aver[1], ABC[2]:aver[2], ABC[3]:aver[3], ABC[4]:aver[4]}
print(result)