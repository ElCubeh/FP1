# Escriba aquí su código
def evaluate(expression):
    if isinstance(expression, int) or isinstance(expression, float):
        return expression
    elif isinstance(expression, tuple) and len(expression) == 3:
        operand1 = evaluate(expression[0])
        operand2 = evaluate(expression[2])
        operator = expression[1]
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("División por cero")
            return operand1 / operand2
        else:
            raise ValueError("Operador desconocido")
    else:
        raise ValueError("Expresión inválida")
    return
