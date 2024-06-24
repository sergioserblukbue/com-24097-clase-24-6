import datetime
hoy = datetime.date.today()
fechainicio ="2021-01-01"
diferencia = hoy - datetime.date.fromisoformat(fechainicio) #la funcion fromisoformat convierte una cadena en una fecha
print(f"diferencia: {diferencia}")