import random

notas = [random.randint(0, 10) for _ in range(100)]

print("En mi lista tengo", notas.count(0), "ceros.")

notas = [nota for nota in notas if nota != 0]

print(len(notas), notas)