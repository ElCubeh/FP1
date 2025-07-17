# Escriba, en el archivo funciones.py una función, inicial_o_final(primer_texto, segundo_texto), donde primer_texto y segundo_texto
# son strings. La función debe devolver True si los caracteres iniciales de ambas strings son iguales, o si lo son sus caracteres
# finales. En los demás casos, debe devolver False.

# Escriba también, en el archivo main.py, un programa que, para ilustrar el uso de la función, la llame primero con dos strings
# que empiezan, pero no terminan, con el mismo carácter; luego con dos strings que terminan, pero no empiezan, con el mismo
# carácter; luego con dos strings que empiezan con el mismo carácter y terminan con el mismo carácter; y luego con dos strings que
# no empiezan con el mismo carácter ni terminan con el mismo carácter. Para cada llamada a la función debe mostrar el resultado en
# pantalla.

#==============================================================================================================================

from funciones import inicial_o_final
print(inicial_o_final("Hola sergio guapo", "Hola vidal dental"))
print(inicial_o_final("Hola colgate", "Me gusta el chocolate"))
print(inicial_o_final("Aurora esta cansada", "Amanda esta flaca"))
print(inicial_o_final("Prefiero la pizza", "No me gusta las aceitunas"))