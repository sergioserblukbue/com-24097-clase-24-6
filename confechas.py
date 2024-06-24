#------------------------------------------------------------
import datetime
#creamos un objeto de la clase datetime que es util para manejar fechas y horas
hoy = datetime.datetime.now() #fecha y hora actual
print(f"hoy: {hoy}") #imprime la fecha y hora actual
print(f"año: {hoy.year}") #imprime el año
print(f"mes-: {hoy.month}") #imprime el mes
print(f"dia: {hoy.day}") #imprime el dia
print(f"hora: {hoy.hour}") #imprime la hora
print(f"minutos: {hoy.minute}") #imprime los minutos
print(f"segundos: {hoy.second}") #imprime los segundos
print(f"microsegundos: {hoy.microsecond}") #imprime los microsegundos
print(f"zona horaria: {hoy.tzinfo}") #imprime la zona horaria, devuelve None porque no se ha definido
#defino la zona horaria
zona = datetime.timezone(datetime.timedelta(hours=-3)) #zona horaria de Argentina
print(f"zona horaria: {zona}") #imprime la zona horaria
#creamos un objeto de la clase date que es util para manejar fechas
hoy = datetime.date.today() #fecha actual
print(f"hoy: {hoy}") #imprime la fecha actual
print(f"año: {hoy.year}") #imprime el año
print(f"mes: {hoy.month}") #imprime el mes
print(f"dia: {hoy.day}") #imprime el dia
#creamos un objeto de la clase time que es util para manejar horas
hora = datetime.time(10,30,20) #hora:minuto:segundo
print(f"hora: {hora}") #imprime la hora
print(f"hora: {hora.hour}") #imprime la hora
print(f"minutos: {hora.minute}") #imprime los minutos
print(f"segundos: {hora.second}") #imprime los segundos
print(f"microsegundos: {hora.microsecond}") #imprime los microsegundos
#creamos un objeto de la clase timedelta que es util para manejar diferencias de tiempo
dias = datetime.timedelta(days=10) #10 dias
print(f"dias: {dias}") #imprime los 10 dias
print(f"fecha actual: {datetime.date.today()}") #fecha actual
print(f"fecha actual + 10 dias: {datetime.date.today() + dias}") #fecha actual + 10 dias
#creamos un objeto de la clase timedelta que es util para manejar diferencias de tiempo
horas = datetime.timedelta(hours=10) #10 horas
print(f"horas: {horas}") #imprime las 10 horas
print(f"fecha y hora actual: {datetime.datetime.now()}") #fecha y hora actual
print(f"fecha y hora actual + 10 horas: {datetime.datetime.now() + horas}") #fecha y hora actual + 10 horas
#creamos un objeto de la clase timedelta que es util para manejar diferencias de tiempo
minutos = datetime.timedelta(minutes=10) #10 minutos
print(f"minutos: {minutos}") #imprime los 10 minutos
print(f"fecha y hora actual: {datetime.datetime.now()}") #fecha y hora actual
print(f"fecha y hora actual + 10 minutos: {datetime.datetime.now() + minutos}") #fecha y hora actual + 10 minutos
#creamos un objeto de la clase timedelta
segundos = datetime.timedelta(seconds=10) #10 segundos
print(f"segundos: {segundos}") #imprime los 10 segundos
print(f"fecha y hora actual: {datetime.datetime.now()}") #fecha y hora actual
print(f"fecha y hora actual + 10 segundos: {datetime.datetime.now() + segundos}") #fecha y hora actual + 10 segundos
#creamos un objeto de la clase timedelta
microsegundos = datetime.timedelta(microseconds=10) #10 microsegundos
print(f"microsegundos: {microsegundos}") #imprime los 10 microsegundos
print(f"fecha y hora actual: {datetime.datetime.now()}") #fecha y hora actual
print(f"fecha y hora actual + 10 microsegundos: {datetime.datetime.now() + microsegundos}") #fecha y hora actual + 10 microsegundos
#creamos un objeto de la clase timedelta
semanas = datetime.timedelta(weeks=10) #10 semanas
print(semanas) #imprime las 10 semanas
print(datetime.date.today()) #fecha actual
print(datetime.date.today() + semanas) #fecha actual + 10 semanas
#creamos un objeto de la clase timedelta
meses = datetime.timedelta(days=30) #30 dias
print(meses) #imprime los 30 dias
print(datetime.date.today()) #fecha actual
print(datetime.date.today() + meses) #fecha actual + 30 dias
#creamos un objeto de la clase timedelta
anios = datetime.timedelta(days=365) #365 dias
print(anios) #imprime los 365 dias
print(datetime.date.today()) #fecha actual
print(datetime.date.today() + anios) #fecha actual + 365 dias
#creamos un objeto de la clase timedelta
bisiesto = datetime.timedelta(days=366) #366 dias
print(bisiesto) #imprime los 366 dias
print(datetime.date.today()) #fecha actual
print(datetime.date.today() + bisiesto) #fecha actual + 366 dias
