'''
Это мой кузнечик, и он играет по моим правилам! Прыгать можно на одну или две клетки
'''

def magic(path_length):
    n = path_length
    A = [0]*n
    A[1], A[2] = 1, 1
    n = 2
    while n != path_length:
        A[n] = A[n-1] + A[n-2]  # Фибби, ты ли это?
        n += 1
    return A[-1]

print(magic(5))
