n = int(input("Введите количество элементов первого множества N: "))
m = int(input("Введите количество элементов второго множества M: "))
multitude1=[]
multitude2=[]
result = []
for i in range(0,n):
    multitude1.append(int(input(f"Введите {i+1}-й элемент первого множества: ")))
for i in range(0,m):
    multitude2.append(int(input(f"Введите {i+1}-й элемент второго множества: ")))    
    if multitude2[i] in multitude1:
        result.append(multitude2[i])
        
print(f"Итоговое множество: {set(result)}")        

    
