#Проверка и поиск синтаксически корректных СНИЛС
#Формат СНИЛС: «ХХХ-ХХХ-ХХХ YY», где X,Y — цифры, причём первые девять цифр 'X' — это любые цифры, а последние две 'Y' фактически являются контрольной суммой, вычисляемой по особому алгоритму из последовательности первых 9 цифр
#Контрольное число СНИЛС рассчитывается следующим образом:
#Каждая цифра СНИЛС умножается на номер своей позиции (позиции отсчитываются с конца, то есть, справа)
#Полученные произведения суммируются
#Получить остаток от деления на 101.
#Если получилось 100, контрольное число равно 0.