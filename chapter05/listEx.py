#리스트 선언
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

print(numbers)
print(fruits)

#리스트 추가, 삭제, 수정
fruits = ["apple", "banana"]
fruits.append("cherry")  
fruits.insert(1, "orange")  

fruits.remove("banana")  
del fruits[0]  
fruits[0] = "grape"  

print(fruits)  