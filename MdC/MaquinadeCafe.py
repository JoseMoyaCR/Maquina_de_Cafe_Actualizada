
from time import sleep
from recetas import recetas

# Declaración de la Clase Máquina de Cafe
class MaquinadeCafe:

    # Consutructor de Clase: Código que se ejecuta cuando se "crea" la máquina de cafe
    # Método Incializar
    def __init__(self, nombre : str = "Máquina de Café", version__sistema: float = 1.0):
        self.nombre                     = nombre
        self.version_sistema            = version__sistema
        self._tanque_de_agua            = 10000 # mililitros de agua
        self._recipiente_de_leche       = 4000  # gramos de leche en polvo
        self._recipiente_de_cafe        = 6000  # gramos de café
        self._recipiente_de_chocolate   = 4000  # gramos de chocolate
        self._tazas_servidas            = 0     # cantidad de tazas procesadas

        # Variables Internas
        self._encendido                 = False
        self._temperatura_caldera       = 24

        # Recetas
        self.bebidas                    = recetas
        
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
        self._temperatura_caldera = 98

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
        self._tanque_de_agua            = agua
        self._recipiente_de_leche       = leche
        self._recipiente_de_cafe        = cafe
        self._recipiente_de_chocolate   = chocolate
        self._temperatura_caldera       = 24 #Se llena con agua a temperatura ambiente
        return {"Code": 1, "Message": "Mantenimiento completo"}
    
    def preparar_bebida(self, receta):
        # Actualizar reservas si todo está bien
        actualizacion = self.actualizar_reservas(receta)
        if actualizacion["Code"] == -1:
            return actualizacion

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
