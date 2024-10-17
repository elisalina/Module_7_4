first_team_name = 'Мастера кода'
second_team_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'




print('В команде %(name)s участников: %(count)s ! ' % {'name' : first_team_name, 'count': team1_num})

print("Итого сегодня в командах участников: %(count1)s и %(count2)s !" % {'count1' : team1_num, 'count2': team2_num})


print("Команда {} решила задач: {} !" .format(second_team_name, score_2))

print("{} решили задачи за {} с !".format (second_team_name, team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)
print(f'Результат битвы: победа команды {first_team_name} !')

print(f'Команды решили  задач.')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')