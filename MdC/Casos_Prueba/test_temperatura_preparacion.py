import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestTemperaturaCaldera(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_temperatura_durante_preparacion(self):
        """CP-034-1: Validar que la temperatura se mantiene en el rango durante la preparacion de una bebida."""
        # Preparar una receta estandar (Ejemplo: Americano de 8 oz)
        receta = {"agua_ml": 236, "cafe_g": 7, "leche_g": 0, "chocolate_g": 0}
        self.mc._temperatura_caldera = 95  # Simular temperatura inicial dentro del rango
        self.mc.preparar_bebida(receta, "Americano", 8)

        # Validar que la temperatura permanece en el rango
        self.assertGreaterEqual(self.mc._temperatura_caldera, 94, "La temperatura es inferior a 94C.")
        self.assertLessEqual(self.mc._temperatura_caldera, 96, "La temperatura supera 96C.")

    def test_temperatura_estable_multiples_preparaciones(self):
        """CP-034-2: Validar la estabilidad de la temperatura con multiples preparaciones."""
        # Simular multiples preparaciones consecutivas
        recetas = [
            {"agua_ml": 236, "cafe_g": 7, "leche_g": 0, "chocolate_g": 0},  # Americano 8 oz
            {"agua_ml": 355, "cafe_g": 14, "leche_g": 10, "chocolate_g": 0},  # Cappuccino 12 oz
            {"agua_ml": 473, "cafe_g": 14, "leche_g": 0, "chocolate_g": 30}  # Chocolate caliente 16 oz
        ]

        for receta in recetas:
            self.mc._temperatura_caldera = 95  # Simular temperatura inicial
            self.mc.preparar_bebida(receta, "Test", 0)

            # Verificar la temperatura despues de cada preparacion
            self.assertGreaterEqual(self.mc._temperatura_caldera, 94, "La temperatura es inferior a 94C.")
            self.assertLessEqual(self.mc._temperatura_caldera, 96, "La temperatura supera 96C.")

if __name__ == "__main__":
    unittest.main()
