

cantidadBT = 1000.5

dias = 31

print("dia: ", 0, "\t cantidad: ", cantidadBT)
for x in range(0, dias):

	increaseBT = cantidadBT * 0.05
	cantidadBT = increaseBT + cantidadBT

	print("dia: ", x + 1, "\t cantidad: ", cantidadBT)
