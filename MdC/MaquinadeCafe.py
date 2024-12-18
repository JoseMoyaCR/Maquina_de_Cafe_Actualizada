
from time import sleep
from recetas import recetas

import os
import json
from datetime import datetime

import csv

# Declaración de la Clase Máquina de Cafe
class MaquinadeCafe:

    # Consutructor de Clase: Código que se ejecuta cuando se "crea" la máquina de cafe
    # Método Incializar
    def __init__(self, nombre : str = "Máquina de Café", version__sistema: float = 1.0):
        self.nombre                     = nombre
        self.version_sistema            = version__sistema
        self._tanque_de_agua            = 10000 # mililitros de agua
        self._recipiente_de_leche       = 2500  # gramos de leche en polvo
        self._recipiente_de_cafe        = 5000  # gramos de café
        self._recipiente_de_chocolate   = 2500  # gramos de chocolate
        self._tazas_servidas            = 0     # cantidad de tazas procesadas

        # Variables Internas
        self._encendido                 = False
        self._temperatura_caldera       = 24

        # Recetas
        self.bebidas                    = recetas
        
        # Reporte de bebidas
        self.reporte_bebidas = []
        
    # Destructor de Clase: Código que se ejecuta cuando se "apaga" la máquinada de café
    def __del__(self,):
        print("La máquinde cafe %s está terminando su operación", self.nombre)

    def obtener_receta(self, bebida: str, tamano: int) -> dict:
        if bebida not in self.bebidas:
            return {"error": "La bebida no está disponible"}

        if bebida == "Expreso":
            if tamano == 0:  # Expreso simple
                return self.bebidas[bebida]["simple"]
            elif tamano == 1:  # Expreso doble
                return self.bebidas[bebida]["doble"]
            else:
                return {"error": "El tamaño no es válido \n para Expreso"}

        # Manejo general para bebidas con tamaños específicos
        receta = self.bebidas[bebida].get(tamano)
        if receta:
            return receta 
        else:
            return {"error": "El tamaño especificado \n no está disponible para \n esta bebida"}
        
    # Verificar Encendido de Máquina
    def verificar_encendido(self) -> bool:
        return self._encendido

    # Encender Máquina
    def encender_máquina(self) -> dict:
        if not self._encendido:
            self._encendido = True
            self._inicializar_caldera()
            return {"Code": 1, "Message": "La Máquina se encendió \n Incializando Caldera", "Tiempo_Proceso" : 10000}
        else:
            return {"Code": 0, "Message": "La Máquina ya está encendida", "Tiempo_Proceso" : 0}

    def _inicializar_caldera(self):
        self._temperatura_caldera = 95

    # Estado de Máquina de cafe
    def estado(self) -> dict:
        return {"Agua disponible": self._tanque_de_agua, "Leche disponible": self._recipiente_de_leche, 
                "Cafe disponible": self._recipiente_de_cafe, "Chocolate disponible": self._recipiente_de_chocolate, 
                "Cantidad de tazas procesadas": self._tazas_servidas, "Temperatura de la caldera": self._temperatura_caldera}
    
    def mostrar_reporte(self):
        return (
            f"Reporte de materiales:\n"
            f"- Agua: {self._tanque_de_agua} ml\n"
            f"- Leche: {self._recipiente_de_leche} g\n"
            f"- Café: {self._recipiente_de_cafe} g\n"
            f"- Chocolate: {self._recipiente_de_chocolate} g\n"
            f"- Tazas servidas: {self._tazas_servidas}\n"
            f"- Temperatura de la caldera: {self._temperatura_caldera} °C"
        )

    # Matenimiento de Máaquina para recarga de Materia Prima
    def mantenimiento(self, agua : int = 0, leche : int = 0, cafe : int = 0, chocolate : int = 0) -> dict:
        self.registrar_mantenimiento(agua, leche, cafe, chocolate)  # Guardar valores previos y nuevos
        self._tanque_de_agua            = agua
        self._recipiente_de_leche       = leche
        self._recipiente_de_cafe        = cafe
        self._recipiente_de_chocolate   = chocolate
        self._temperatura_caldera       = 24 #Se llena con agua a temperatura ambiente
        return {"Code": 1, "Message": "Mantenimiento completo"}
    
    def preparar_bebida(self, receta, bebida: str, tamano):
        # Actualizar reservas si todo está bien
        actualizacion = self.actualizar_reservas(receta)
        if actualizacion["Code"] == -1:
            return actualizacion
            
        if bebida == "Expreso":
            if tamano == 0:  # Expreso simple
                tamano = "simple"
            elif tamano == 1:  # Expreso doble
                tamano = "doble"
        else:
            tamano = str(tamano) + "oz"
                
        self.registrar_bebida(bebida, tamano)
        # Retornar éxito al preparar la bebida
        return {"Code": 1, "Message": "Bebida preparada exitosamente"}
    
    def verificar_reservas(self, receta: dict) -> dict:

        # Obtener las cantidades necesarias de la receta
        agua_necesaria = receta.get("agua_ml", 0)
        cafe_necesario = receta.get("cafe_g", 0)
        leche_necesaria = receta.get("leche_g", 0)
        chocolate_necesario = receta.get("chocolate_g", 0)

        # Verificar reservas
        if (self._tanque_de_agua < agua_necesaria or
            self._recipiente_de_cafe < cafe_necesario or
            self._recipiente_de_leche < leche_necesaria or
            self._recipiente_de_chocolate < chocolate_necesario):
            return {"Code": 0, "Message": "Bebida no preparada, no hay \n suficiente materia prima, \n por favor recargue el sistema"}
        # Si todo está bien
        else: 
            return {"Code": 1, "Message": "Suficiente materia prima"}
    
    
    def actualizar_reservas(self, receta: dict) -> dict:

        # Verificar reservas antes de actualizar
        resultado_verificacion = self.verificar_reservas(receta)
        if resultado_verificacion["Code"] == -1:
            # Si no hay suficiente materia prima, retornar el mensaje de error
            return resultado_verificacion

        # Actualizar reservas si hay suficiente materia prima
        self._tanque_de_agua -= receta.get("agua_ml", 0)
        self._recipiente_de_cafe -= receta.get("cafe_g", 0)
        self._recipiente_de_leche -= receta.get("leche_g", 0)
        self._recipiente_de_chocolate -= receta.get("chocolate_g", 0)

        return {"Code": 1, "Message": "Reservas actualizadas \n correctamente"}
        
    def rutina_autodiagnostico(self):
        reporte = {
            "Agua": "OK" if 0 <= self._tanque_de_agua <= 10000 else "FALLA",
            "Leche": "OK" if 0 <= self._recipiente_de_leche <= 2500 else "FALLA",
            "Cafe": "OK" if 0 <= self._recipiente_de_cafe <= 5000 else "FALLA",
            "Chocolate": "OK" if 0 <= self._recipiente_de_chocolate <= 2500 else "FALLA",
            "Temperatura Caldera": "OK" if 0 <= self._temperatura_caldera <= 110 else "FALLA",
        }

        estado_general = "OK"
        # Revisar si existe alguna falla
        for sensor, estado in reporte.items():
            if estado == "FALLA":
                estado_general = "FALLA"
                break

        reporte_final = {
            "Estado General": estado_general,
            "Detalles": reporte
        }
        
        return reporte_final

    def generar_reporte_sistema(self):
        reporte_diagnostico = self.rutina_autodiagnostico()
        
        reporte_final = {
            "Estado General": reporte_diagnostico["Estado General"],
            "Detalles": reporte_diagnostico["Detalles"],
            "Cantidad de Materia Prima": {
                "Agua (ml)": self._tanque_de_agua,
                "Leche (g)": self._recipiente_de_leche,
                "Cafe (g)": self._recipiente_de_cafe,
                "Chocolate (g)": self._recipiente_de_chocolate
            },
            "Bebidas Procesadas": self._tazas_servidas
        }
        return reporte_final

    def guardar_reporte(self):
        # Crear carpeta 'logs' si no existe
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Generar reporte
        reporte = {
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Reporte": self.generar_reporte_sistema()
        }

        # Guardar reporte como JSON en la carpeta 'logs'
        nombre_archivo = f"logs/reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(nombre_archivo, "w") as file:
            json.dump(reporte, file, indent=4)

        return {"Code": 1, "Message": f"Reporte guardado en: {nombre_archivo}"}
        
    def registrar_bebida(self, bebida: str, tamano):
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.reporte_bebidas.append({"Hora": hora_actual, "Bebida": bebida + " " + str(tamano)})
        self.guardar_reporte_bebidas()

    def guardar_reporte_bebidas(self, nombre_archivo="reporte_bebidas.csv"):
        with open(nombre_archivo, mode="w", newline="") as archivo_csv:
            campos = ["Hora", "Bebida"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(self.reporte_bebidas)
            
    def registrar_mantenimiento(self, agua : int = 0, leche : int = 0, cafe : int = 0, chocolate : int = 0):
        # Ruta y nombre del archivo
        ruta_reporte = "reporte_mantenimiento.csv"
        # Obtener la fecha y hora actual
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Crear el registro con valores previos
        registro = {
            "Fecha y Hora"            : fecha_hora,
            "Agua Antes (ml)"         : self._tanque_de_agua,
            "Leche Antes (g)"         : self._recipiente_de_leche,
            "Cafe Antes (g)"          : self._recipiente_de_cafe,
            "Chocolate Antes (g)"     : self._recipiente_de_chocolate,
            "Temp Caldera Antes (C)"  : self._temperatura_caldera,
            "Agua Despues (ml)"       : agua,  # Nuevos valores
            "Leche Despues (g)"       : leche,
            "Cafe Despues (g)"        : cafe,
            "Chocolate Despues (g)"   : chocolate,
            "Temp Caldera Despues (C)": 24
        }

        # Verificar si el archivo existe
        archivo_nuevo = not os.path.exists(ruta_reporte)

        # Guardar el registro en el archivo CSV
        with open(ruta_reporte, mode="a", newline="") as file:
            escritor = csv.DictWriter(file, fieldnames=registro.keys())

            # Escribir el encabezado si el archivo es nuevo
            if archivo_nuevo:
                escritor.writeheader()

            escritor.writerow(registro)

        print(f"Evento de mantenimiento registrado en {ruta_reporte}.")



































