def game_core_v3(number: int = 1) -> int:
    """Сначала задаем начальное random число (predict), затем зная диапазон в котором загадано число, определяем его границы start и finish. 
    Создаем цикл, условием выхода из цикла будет равенство переданного в функцию числа (number) с подобранным числом (predict).
    В качестве условий сравниваем числа predict и number, и в зависимости от знака равенства < или > сдвигаем границы, 
    презаписывая значения переменных start или finish.
    Затем производим расчет нового значения для (predict) и снова сравниваем, до тех пор пока не угадаем (number), 
    т.е. когда выполнится условие number == predict

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    start = 0
    finish = 101

    while number != predict:
        count += 1
        if predict < number:
            start = predict
        elif predict > number:
            finish = predict
        predict = (start + finish) // 2 

    return count
game_core_v3()