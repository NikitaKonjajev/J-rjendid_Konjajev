




spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmerimine"
slovo_list=list(slovo) 
print(slovo)
print(slovo_list)
while True:
    print("1 - добавить букву в список ")
    print("2 - склеить списки\n3- Добавить букву на i - позицию ")
    print("4 - удалить букву ")
    print("5 - очистить список ")
    print("6 - развернуть список ")
    print("7 - Считает количество элементов со значением x ")
    print("8 - Изменяет на нижний регистр весь лист ")
    print("9 - Изменяет на верхний регистр весь лист ")
    print("10 - Введите позицию, которую удалить")
    valik=int(input())
    if valik==1:
        a=input("Введи букву ")
        slovo_list.append(a)
        print(f"Добавили {a} новый списко", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=(input("Введи букву, которую хочешь добавить "))
        i=int(input("Введи номер позии, куда хочешь добавить букву 0,"))
        slovo_list.insert(i-1,a) #0,1,2,3...
        print(slovo_list)
    elif valik==4:
        a=(input("Введи букву, которую хочешь удалить "))
        a=a.lower()
        listcopy_list=[]
        for t in (slovo_list):
            listcopy_list.append(t.lower())
        n=listcopy_list.count(a)
        if n>0:
            for i in range(n):
                listcopy_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(listcopy_list)
    elif valik==5:
        slovo_list.clear()
    elif valik==6:
        slovo_list.reverse()
    elif valik==7:
        h=input("Введите искомую букву ")
        g=slovo_list.count(h)
        print(g)
    elif valik==8:
        listcopy1_list=[]
        for t in (slovo_list):
            listcopy1_list.append(t.lower())
        print(listcopy1_list)
    elif valik==9:
        listcopy2_list=[]
        for t in (slovo_list):
            listcopy2_list.append(t.upper())
        print(listcopy2_list)
    elif valik==10:
        a=int(input("Введите позицию, которую удалить "))
        listcopy3_list=slovo_list.copy()
        if a>=0 and a<len(listcopy3_list):
            listcopy3_list.pop(a-1)
        print(listcopy3_list)
    print(slovo_list)
