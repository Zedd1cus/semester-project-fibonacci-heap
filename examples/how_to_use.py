from src.fibonacci_heap import FibonacciHeap

# Создание пустой Фибоначчиевой кучи
new_heap = FibonacciHeap()

# Пример заполнения кучи 1
new_heap.insert(6)
new_heap.insert(10)

# Пример заполнения кучи 2
for i in range(12):
    new_heap.insert(i)

# Пример извлечения минимального элемента
minim = new_heap.extract_min()
print(minim)

# Создаем и заполняем вторую кучу
new_heap2 = FibonacciHeap()
for i in range(12, 20):
    new_heap2.insert(i)

# Пример объединения двух куч - оно же расширение первой кучи с помощью второй
new_heap.union(new_heap2)