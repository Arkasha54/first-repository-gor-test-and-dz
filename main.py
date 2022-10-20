first_element = 1
second_element = 1
n = input("Номер элемента последовательнocти ")
n = int(n)

print(first_element, second_element, end=' ')
while n > 2:
    sum = first_element + second_element
    first_element = second_element
    second_element = sum
    print (sum, end=' ')
    n -= 1

print("Значение этого элемента:", second_element)