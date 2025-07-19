fecha = input("Introduce una fecha en formato `dd-mm-aaaa': ")
dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:]
fecha_nueva = mes + '-' + dia +'-'+ año
print("La nueva fecha es: ",fecha_nueva)