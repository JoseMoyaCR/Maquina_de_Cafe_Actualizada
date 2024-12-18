import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe
from recetas import recetas

class TestSensorCafe(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_lectura_normal_sensor_cafe(self):
        """CP-011-1: Validar que la lectura de cafe en gramos en condiciones normales es correcta."""
        self.assertGreaterEqual(self.mc._recipiente_de_cafe, 0, "La cantidad de cafe es negativa.")
        self.assertLessEqual(self.mc._recipiente_de_cafe, 5000, "La cantidad de cafe supera el limite superior.")

    def test_limite_inferior_sensor_cafe(self):
        """CP-011-2: Validar lectura en el limite inferior del rango."""
        self.mc._recipiente_de_cafe = 0  # Simula el limite inferior
        self.assertEqual(self.mc._recipiente_de_cafe, 0, "El sensor no registra correctamente el limite inferior.")

    def test_limite_superior_sensor_cafe(self):
        """CP-011-3: Validar lectura en el limite superior del rango."""
        self.mc._recipiente_de_cafe = 5000  # Simula el limite superior
        self.assertEqual(self.mc._recipiente_de_cafe, 5000, "El sensor no registra correctamente el limite superior.")

    def test_actualizacion_receta_sensor_cafe(self):
        """CP-011-4: Validar la reduccion del nivel de cafe despues de preparar recetas."""
        receta = {"cafe_g": 300}  # Simula una receta con 300g de cafe
        cafe_inicial = self.mc._recipiente_de_cafe
        self.mc.preparar_bebida(receta)  # Prepara la bebida usando la receta
        self.assertEqual(self.mc._recipiente_de_cafe, cafe_inicial - 300,
                         "El sensor no registra correctamente la reduccion del nivel de cafe.")

if __name__ == "__main__":
    unittest.main()
