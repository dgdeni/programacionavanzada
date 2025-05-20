#Definiendo la clase persona con los atributos nombre, edad y propiedad que muestre la información de la persona
from datetime import datetime, date

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def info(self):
        print(f'Nombre: {self.nombre} , Edad: {self.edad}')

#Creando clase Huesped que se construye a partir de la clase Persona, heredando sus propiedades y métodos
#Agregando propiedades adicionales de la clase Huesped

class Huesped(Persona):
  def __init__(self, nombre, edad, habitacion, rfc, numero_cuenta, fecha_ingreso, hospedado_actualmente, servicio_habitacion):
    super().__init__(nombre,edad)
    self.habitacion = habitacion
    self.rfc = rfc
    self.numero_cuenta = numero_cuenta
    self.fecha_ingreso = fecha_ingreso
    self.hospedado_actualmente = hospedado_actualmente
    self.servicio_habitacion = servicio_habitacion

#Métodos clase Huesped
#1. Información básica del huesped
  def mostrar_info(self):
    self.info()  # Nombre y edad son heredadas de la clase Persona
    print (
            f"Habitación: {self.habitacion}\n"
            f"RFC: {self.rfc}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Fecha de ingreso: {self.fecha_ingreso}\n"
            f"Hospedado actualmente: {self.hospedado_actualmente}\n"
            f"Servicios a la habitación: {self.servicio_habitacion}"
        )

#2. Saldo hasta el día de hoy
#Costo de la renta de la habitación * por los días que lleva hospedado + gastos servicio a la habitación
  def saldo(self,costo_noche):
    fecha_ingreso = datetime.strptime(self.fecha_ingreso, "%Y-%m-%d").date()
    hoy = date.today()
    dias_hospedado = (hoy - fecha_ingreso).days
    if dias_hospedado < 0:
      dias_hospedado = 0
    renta = dias_hospedado * costo_noche
    consumo = sum(self.servicio_habitacion.values())
    saldo = renta + consumo
    return saldo
  

#Ejemplo de validación
servicios = {
    "Desayuno": 350,
    "Comida": 450,
    "Cena":400
}

huesped_1 = Huesped(
    nombre="Deni",
    edad=29,
    habitacion=126,
    rfc="DGF00112513",
    numero_cuenta=1234590,
    fecha_ingreso="2025-05-18",
    hospedado_actualmente=True,
    servicio_habitacion=servicios
)

huesped_1.mostrar_info()
huesped_1.saldo(500)