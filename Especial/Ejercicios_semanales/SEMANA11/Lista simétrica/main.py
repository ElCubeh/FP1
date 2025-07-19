import math_utils

l1 = [12, 23, 34, 45, 67, 89]
l2 = [10, 12, 35, 12, 10]
r1 = "SÍ ES" if math_utils.is_sym(l1) else "NO ES"
print(l1, r1, "SIMÉTRICA")
r2 = "SÍ ES" if math_utils.is_sym(l2) else "NO ES"
print(l2, r2, "SIMÉTRICA")
