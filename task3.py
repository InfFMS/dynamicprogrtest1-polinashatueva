"""
Алгоритм вычисления значения функции F(n) и G(n), где n - целое число, задан следующими соотношениями:
F(n) = 2 * (G(n - 3) + 8);
G(n) = 2 * n, если n < 10;
G(n) = G(n - 2) + 1, если n >= 10.
Чему равно значение выражения F(15548)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
sys.setrecursionlimit(1000000000)
f = {}
g = {}
def Fibs(n):
    if n in g:
        return g[n]
    if n < 10:
        g[n] = 2 * n
        return g[n]
    g[n] = Fibs(n-2) + 1
    return g[n]

def F(n):
    if n in f:
        return f[n]
    f[n] = 2 * (Fibs(n-3) + 8)
    return f[n]

print(15548)