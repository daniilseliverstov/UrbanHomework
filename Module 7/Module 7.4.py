
team1 = '"Мастера кода"'
team1_num = 5

print('В команде %(team1)s участников: %(team1_num)s' % {'team1': team1, 'team1_num': team1_num})

team2 = '"Волшебники данных"'
team2_num = 6

print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s'
      % {'team1_num': team1_num, 'team2_num': team2_num})

score_1 = 40
score_2 = 42

print('Команда {} решила задач: {} !'.format(team2, score_2))

team1_time = 18015.2
team2_time = 2153.31451

print('{} решили задачи за {} с !'.format(team1, team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {team1}!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {team2}!'

else:
    result = f'Ничья!'

print(f'Результат битвы: победа команды {result}')

time_avg = (team1_time + team2_time) / (score_1 + score_2)

print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!')




