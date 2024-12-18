import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestGenerarReporteSistema(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_generar_reporte_normal(self):
        """CP-024-1: Validar reporte en condiciones normales."""
        # Simula condiciones normales
        self.mc._tanque_de_agua = 9000
        self.mc._recipiente_de_leche = 2000
        self.mc._recipiente_de_cafe = 4000
        self.mc._recipiente_de_chocolate = 2000
        self.mc._tazas_servidas = 10
        
        reporte = self.mc.generar_reporte_sistema()

        # Validar el estado general
        self.assertEqual(reporte["Estado General"], "OK", 
						"El estado general deberia ser OK en condiciones normales.")
        
        # Validar detalles
        self.assertEqual(reporte["Detalles"]["Agua"], "OK")
        self.assertEqual(reporte["Detalles"]["Leche"], "OK")
        self.assertEqual(reporte["Detalles"]["Cafe"], "OK")
        self.assertEqual(reporte["Detalles"]["Chocolate"], "OK")
        self.assertEqual(reporte["Detalles"]["Temperatura Caldera"], "OK")
        
        # Validar niveles de materia prima
        self.assertEqual(reporte["Cantidad de Materia Prima"]["Agua (ml)"], 9000)
        self.assertEqual(reporte["Cantidad de Materia Prima"]["Leche (g)"], 2000)
        self.assertEqual(reporte["Cantidad de Materia Prima"]["Cafe (g)"], 4000)
        self.assertEqual(reporte["Cantidad de Materia Prima"]["Chocolate (g)"], 2000)
        
        # Validar bebidas procesadas
        self.assertEqual(reporte["Bebidas Procesadas"], 10)

    def test_generar_reporte_con_fallas(self):
        """CP-024-2: Simular fallas y validar el reporte."""
        # Simula fallas en sensores
        self.mc._tanque_de_agua = -100  # Falla
        self.mc._recipiente_de_leche = 3000  # Falla
        self.mc._recipiente_de_cafe = 4000
        self.mc._recipiente_de_chocolate = 2500
        self.mc._temperatura_caldera = 120  # Falla
        self.mc._tazas_servidas = 5

        reporte = self.mc.generar_reporte_sistema()

        # Validar el estado general
        self.assertEqual(reporte["Estado General"], "FALLA", 
						"El estado general deberia ser FALLA con sensores incorrectos.")
        
        # Validar detalles con fallas
        self.assertEqual(reporte["Detalles"]["Agua"], "FALLA", 
						"El sensor de agua deberia reportar FALLA.")
        self.assertEqual(reporte["Detalles"]["Leche"], "FALLA", "
						El sensor de leche deberia reportar FALLA.")
        self.assertEqual(reporte["Detalles"]["Temperatura Caldera"], "FALLA", 
						"La temperatura de la caldera deberia reportar FALLA.")
        
        # Validar detalles correctos
        self.assertEqual(reporte["Detalles"]["Cafe"], "OK")
        self.assertEqual(reporte["Detalles"]["Chocolate"], "OK")
        
        # Validar bebidas procesadas
        self.assertEqual(reporte["Bebidas Procesadas"], 5)

if __name__ == "__main__":
    unittest.main()
