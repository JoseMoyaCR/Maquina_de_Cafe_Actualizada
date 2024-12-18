import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestSensorTemperatura(unittest.TestCase):
    """Tests para validar la lectura del sensor de temperatura (REQ9)."""

    def setUp(self):
        """Configura la instancia de la maquina de cafe."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_temperatura_despues_de_mantenimiento(self):
        """CP-009-1: Validar que la temperatura se mantiene estable en valores normales tras inicializar."""
        self.mc._inicializar_caldera()

        # Validar que la temperatura esta dentro del rango permitido despues del mantenimiento
        self.assertGreaterEqual(self.mc._temperatura_caldera, 0, "La temperatura esta por debajo de 0C despues de mantenimiento.")
        self.assertLessEqual(self.mc._temperatura_caldera, 110, "La temperatura supera 110C despues de mantenimiento.")

    def test_temperatura_mantenimiento_normal(self):
        """CP-009-2: Validar que la temperatura se ajusta tras llamar a mantenimiento."""
        # Simula temperatura normal antes de mantenimiento
        self.mc._temperatura_caldera = 95
        self.mc.mantenimiento()  # Llamada a mantenimiento
        # Validar que la temperatura esta dentro del rango permitido despues del mantenimiento
        self.assertGreaterEqual(self.mc._temperatura_caldera, 0, "La temperatura esta por debajo de 0C despues de mantenimiento.")
        self.assertLessEqual(self.mc._temperatura_caldera, 110, "La temperatura supera 110C despues de mantenimiento.")

    def test_temperatura_limite_inferior_despues_mantenimiento(self):
        """CP-009-3: Validar limite inferior despues del mantenimiento."""
        # Simula temperatura por debajo del limite
        self.mc._temperatura_caldera = -5
        self.mc.mantenimiento()
        # Validar que la temperatura esta dentro del rango permitido despues del mantenimiento
        self.assertGreaterEqual(self.mc._temperatura_caldera, 0, "La temperatura esta por debajo de 0C despues de mantenimiento.")
        self.assertLessEqual(self.mc._temperatura_caldera, 110, "La temperatura supera 110C despues de mantenimiento.")

if __name__ == "__main__":
    unittest.main()

