n = int(input("Введите количество кустов N (не менее 3-х): "))
while n <3:
    n = int(input("Вы ввели некорректное число. Введите количество кустов N (не менее 3-х): "))
    continue
bush = []  
harvest = []   
for i in range (0,n):
    bush.append(int(input(f"Введите количество ягод на {i+1}-м кусте: ")))
h_max = bush[1]
for i in range (0,n):
    if i == 0:
        harvest.append(bush[0] + bush[1] + bush[n-1])
    else:
        if i != n-1:
            harvest.append(bush[i-1] + bush[i] + bush[i+1])
        else:
            harvest.append(bush[n-2] + bush[n-1] + bush[0])
    if harvest[i] > h_max:
        h_max = harvest[i]

print(f"Наибольшее количество ягод: {h_max}")
