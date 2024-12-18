import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe
from recetas import recetas

class TestSensorNivelAgua(unittest.TestCase):
    def setUp(self):
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_lectura_nivel_agua(self):
        """CP-007-1: Verificar la lectura inicial del nivel de agua en mililitros."""
        self.assertEqual(self.mc._tanque_de_agua, 10000, "El nivel inicial de agua no es correcto (debe ser 10000 ml).")

    def test_alerta_nivel_critico(self):
        """CP-007-2: Validar que se genere alerta cuando el nivel de agua es critico."""
        self.mc._tanque_de_agua = 500  # Simula un nivel critico en mililitros
        alerta = self.mc.verificar_reservas({"agua_ml": 1000})["Message"]
        self.assertIn("Bebida no preparada, no hay \n suficiente materia prima, \n por favor recargue el sistema", alerta, "No se genero la alerta de nivel critico de agua.")

    def test_consumo_agua_durante_operacion(self):
        """CP-007-3: Validar reduccion del nivel de agua despues de preparar una bebida."""
        receta = {"agua_ml": 250, "cafe_g": 0, "leche_g": 0, "chocolate_g": 0}
        nivel_agua_inicial = self.mc._tanque_de_agua
        self.mc.preparar_bebida(receta)
        self.assertEqual(
            self.mc._tanque_de_agua, nivel_agua_inicial - 250, 
            "El nivel de agua no se redujo correctamente despues de preparar la bebida."
        )

if __name__ == "__main__":
    unittest.main()
