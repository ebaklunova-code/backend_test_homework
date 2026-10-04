print('Привет! Я - твой личный помощник. Давай знакомиться:')
user_name = input('Как тебя зовут?')
user_age = input('Сколько тебе лет?')
user__age = int(user_age)      

print('Теперь рассчитаем твой ИМТ и норму воды. Для этого:')
user_height = input('Введи свой рост(в местрах, например, 1.7)')
user_weight = input('Введи свой вес (в кг, например,55.6)')
user__height = float(user_height)   
user__weight = float(user_weight)    
bmi=user__weight / (user__height ** 2)
bmi_rounded = round(bmi, 1)
water_ml = user__weight * 30
water_l = water_ml / 1000
 
print('Отчет для пользователя:', user_name, user__age)
print('Твой индек массы тела:', bmi_rounded)
print('Рекомендуемая норма воды:', water_l, 'л в день')
print('')
print('Расчет окончен. Будьте здоровы!')
