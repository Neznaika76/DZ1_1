
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def transformation_elements(x, y):
    m = int(x)
    z = int(float(x) * (10**y)) % (10**y)
    z = m + z/(10**y)
    return z


n = float(input('Введите число: '))
d = int(input('Введите точность d: '))
if n > 0:
    print(transformation_elements(n, d))
else:
    n = abs(n)
    print(transformation_elements(n, d)*(-1))