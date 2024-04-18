capacidad = float(input('Introduzca la capacidad de su disco (en GB): '))

print(f'''Su capacidad es {1024*capacidad} Megabytes
Su capacidad es {(1024**2)*capacidad} Kilobytes
Su capacidad es {(1024**3)*capacidad} Bytes''')