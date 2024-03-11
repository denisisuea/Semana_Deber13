# SEMANA 13
# Definición y uso de funciones en programación
# Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.

# Función para calcular el promedio de temperaturas de una ciudad en un intervalo de tiempo

def calculo_temperatura(datos, ciudad, semana_inicio, semana_final):
	num_items = 0 #total de items leídos
	suma_temp = 0 # la sumatoria de las temperaturas
	for i in range(len(datos[ciudad])):
		if i>=semana_inicio and i<=semana_final:
			for j in range(len(datos[ciudad][i])):
				suma_temp = suma_temp + datos[ciudad][i][j]['temp']
				num_items = num_items + 1

				print(datos[ciudad][i][j])

	promedios = suma_temp/num_items
	return promedios

# DATOS DE TEMPERATURAS
temperaturas = [
    [   # Ciudad 1 El Coca
        # Semana 1 
		[
			{"Día": "Lunes", "temp": 92}, # lUNES
			{"Día": "Martes", "temp": 88}, # MARTES
			{"Día": "Miércoles", "temp": 85}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 79}, # JUEVES
			{"Día": "Viernes", "temp": 82}, # VIERNES
			{"Día": "Sábado", "temp": 80}, # SÁBADO
			{"Día": "Domingo", "temp": 78} # DOMINGO
		],
		# Semana 2
		[
			{"Día": "Lunes", "temp": 83}, # lUNES
			{"Día": "Martes", "temp": 89}, # MARTES
			{"Día": "Miércoles", "temp": 87}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 81}, # JUEVES
			{"Día": "Viernes", "temp": 83}, # VIERNES
			{"Día": "Sábado", "temp": 79}, # SÁBADO
			{"Día": "Domingo", "temp": 76} # DOMINGO
		],
		# Semana 3
		[
			{"Día": "Lunes", "temp": 95}, # lUNES
			{"Día": "Martes", "temp": 91}, # MARTES
			{"Día": "Miércoles", "temp": 88}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 82}, # JUEVES
			{"Día": "Viernes", "temp": 85}, # VIERNES
			{"Día": "Sábado", "temp": 81}, # SÁBADO
			{"Día": "Domingo", "temp": 78} # DOMINGO
		],
		# Semana 4
		[
			{"Día": "Lunes", "temp": 91}, # lUNES
			{"Día": "Martes", "temp": 87}, # MARTES
			{"Día": "Miércoles", "temp": 84}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 79}, # JUEVES
			{"Día": "Viernes", "temp": 80}, # VIERNES
			{"Día": "Sábado", "temp": 78}, # SÁBADO
			{"Día": "Domingo", "temp": 75} # DOMINGO
		]
    ],
    [   # Ciudad 2 Quito
        # Semana 1 
		[
			{"Día": "Lunes", "temp": 79}, # lUNES
			{"Día": "Martes", "temp": 75}, # MARTES
			{"Día": "Miércoles", "temp": 73}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 70}, # JUEVES
			{"Día": "Viernes", "temp": 68}, # VIERNES
			{"Día": "Sábado", "temp": 64}, # SÁBADO
			{"Día": "Domingo", "temp": 62} # DOMINGO
		],
		# Semana 2
		[
			{"Día": "Lunes", "temp": 81}, # lUNES
			{"Día": "Martes", "temp": 77}, # MARTES
			{"Día": "Miércoles", "temp": 75}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 72}, # JUEVES
			{"Día": "Viernes", "temp": 70}, # VIERNES
			{"Día": "Sábado", "temp": 66}, # SÁBADO
			{"Día": "Domingo", "temp": 63} # DOMINGO
		],
		# Semana 3
		[
			{"Día": "Lunes", "temp": 80}, # lUNES
			{"Día": "Martes", "temp": 76}, # MARTES
			{"Día": "Miércoles", "temp": 72}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 70}, # JUEVES
			{"Día": "Viernes", "temp": 68}, # VIERNES
			{"Día": "Sábado", "temp": 65}, # SÁBADO
			{"Día": "Domingo", "temp": 61} # DOMINGO
		],
		# Semana 4
		[
			{"Día": "Lunes", "temp": 80}, # lUNES
			{"Día": "Martes", "temp": 77}, # MARTES
			{"Día": "Miércoles", "temp": 74}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 71}, # JUEVES
			{"Día": "Viernes", "temp": 69}, # VIERNES
			{"Día": "Sábado", "temp": 67}, # SÁBADO
			{"Día": "Domingo", "temp": 64} # DOMINGO
		]
    ],
    [   # Ciudad 3 Loja
        # Semana 1 
		[
			{"Día": "Lunes", "temp": 80}, # lUNES
			{"Día": "Martes", "temp": 83}, # MARTES
			{"Día": "Miércoles", "temp": 86}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 89}, # JUEVES
			{"Día": "Viernes", "temp": 92}, # VIERNES
			{"Día": "Sábado", "temp": 90}, # SÁBADO
			{"Día": "Domingo", "temp": 88} # DOMINGO
		],
		# Semana 2
		[
			{"Día": "Lunes", "temp": 83}, # lUNES
			{"Día": "Martes", "temp": 86}, # MARTES
			{"Día": "Miércoles", "temp": 89}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 92}, # JUEVES
			{"Día": "Viernes", "temp": 95}, # VIERNES
			{"Día": "Sábado", "temp": 93}, # SÁBADO
			{"Día": "Domingo", "temp": 91} # DOMINGO
		],
		# Semana 3
		[
			{"Día": "Lunes", "temp": 81}, # lUNES
			{"Día": "Martes", "temp": 84}, # MARTES
			{"Día": "Miércoles", "temp": 87}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 90}, # JUEVES
			{"Día": "Viernes", "temp": 93}, # VIERNES
			{"Día": "Sábado", "temp": 91}, # SÁBADO
			{"Día": "Domingo", "temp": 89} # DOMINGO
		],
		# Semana 4
		[
			{"Día": "Lunes", "temp": 82}, # lUNES
			{"Día": "Martes", "temp": 85}, # MARTES
			{"Día": "Miércoles", "temp": 88}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 91}, # JUEVES
			{"Día": "Viernes", "temp": 94}, # VIERNES
			{"Día": "Sábado", "temp": 92}, # SÁBADO
			{"Día": "Domingo", "temp": 90} # DOMINGO
		]
    ]
]



promedio_calc = calculo_temperatura(temperaturas, 1, 1,2)

print(f"Promedio {promedio_calc:.2f}")