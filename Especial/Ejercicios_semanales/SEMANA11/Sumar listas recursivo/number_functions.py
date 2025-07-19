# Escriba aquí su código
def sum_lists(l1, l2):
    if not l1 and not l2:
        return []
    if len(l1) != len(l2):
        return None
    total = l1[0] + l2[0]
    return [total] + sum_lists(l1[1:], l2[1:])
