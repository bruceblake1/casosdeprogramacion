#ESCTRUCTURA SECUENCIAL

print("Venta de producto")
print("Ingresar el nombre del producto:")
nomprod=input()
print("Ingresar precio del producto")
puprod=input()
puprod=int(puprod)
print("Ingresar cantidad del producto:")
cantprod=input()
cantprod=int(cantprod)
imp=puprod*cantprod
dscto=imp*0.05
total=imp-dscto
print("El nombre del producto es:",nomprod)
print("El precio del producto es:",puprod)
print("El cantidad del producto es:",cantprod)
print("El importe es:",imp)
print("El descuento es:",dscto)
print("El total a pagar es:", total)