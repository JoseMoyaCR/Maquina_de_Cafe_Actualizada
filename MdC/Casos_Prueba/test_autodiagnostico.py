import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestAutodiagnostico(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_autodiagnostico_sensores_funcionales(self):
        """CP-023-1: Verificar rutina con sensores funcionales."""
        reporte = self.mc.rutina_autodiagnostico()
        self.assertEqual(reporte["Estado General"], "OK", "El autodiagnostico reporta fallas con sensores funcionales.")

    def test_autodiagnostico_falla_sensores(self):
        """CP-023-2: Simular fallas en los sensores y validar el reporte."""
        # Simular fallas en los valores de los sensores
        self.mc._tanque_de_agua = -1  # Agua fuera de rango
        self.mc._recipiente_de_leche = 3000  # Leche fuera de rango
        self.mc._temperatura_caldera = 120  # Temperatura fuera de rango

        reporte = self.mc.rutina_autodiagnostico()
        self.assertEqual(reporte["Estado General"], "FALLA", "El autodiagnostico no detect0 las fallas correctamente.")
        self.assertEqual(reporte["Detalles"]["Agua"], "FALLA")
        self.assertEqual(reporte["Detalles"]["Leche"], "FALLA")
        self.assertEqual(reporte["Detalles"]["Temperatura Caldera"], "FALLA")

if __name__ == "__main__":
    unittest.main()
