name = input("Как тебя зовут? ")
age_str = input("Сколько тебе лет? ")
age = int(age_str)
if age < 18:
    print(f"Привет, {name}! Ты еще слишком молод для этого.")  
elif age >= 18 and age < 30:
    print(f"Отличный возраст для старта в IT, {name}!")
else:
    print(f"Привет, {name}! У тебя уже есть жизненный опыт, который поможет в IT.")