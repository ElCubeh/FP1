import string_utils


if __name__ == "__main__":
    formula = "H2O"

    if string_utils.validate_formula(formula):
        print("Estructura válida")
    else:
        print("Estructura no válida")
