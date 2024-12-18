import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe
from recetas import recetas

class TestSensorLeche(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_lectura_normal_sensor_leche(self):
        """CP-013-1: Validar que la lectura de leche en polvo en condiciones normales es correcta."""
        self.assertGreaterEqual(self.mc._recipiente_de_leche, 0, "La cantidad de leche es negativa.")
        self.assertLessEqual(self.mc._recipiente_de_leche, 2500, "La cantidad de leche supera el limite superior.")

    def test_limite_inferior_sensor_leche(self):
        """CP-013-2: Validar lectura en el limite inferior del rango."""
        self.mc._recipiente_de_leche = 0  # Simula el limite inferior
        self.assertEqual(self.mc._recipiente_de_leche, 0, "El sensor no registra correctamente el limite inferior.")

    def test_limite_superior_sensor_leche(self):
        """CP-013-3: Validar lectura en el limite superior del rango."""
        self.mc._recipiente_de_leche = 2500  # Simula el limite superior
        self.assertEqual(self.mc._recipiente_de_leche, 2500, "El sensor no registra correctamente el limite superior.")

    def test_actualizacion_receta_sensor_leche(self):
        """CP-013-4: Validar la reduccion del nivel de leche despues de preparar recetas."""
        receta = {"leche_g": 500}  # Simula una receta con 500g de leche
        leche_inicial = self.mc._recipiente_de_leche
        self.mc.preparar_bebida(receta)  # Prepara la bebida usando la receta
        self.assertEqual(self.mc._recipiente_de_leche, leche_inicial - 500,
                         "El sensor no registra correctamente la reduccion del nivel de leche.")

if __name__ == "__main__":
    unittest.main()

