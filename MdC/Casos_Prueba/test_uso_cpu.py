import unittest
import psutil
import time
from concurrent.futures import ThreadPoolExecutor
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestUsoCPU(unittest.TestCase):
    def setUp(self):
        """Configurar la instancia de la maquina de cafe."""
        self.mc = MaquinadeCafe("Maquina de Cafe", version__sistema=1.0)

    def test_cpu_preparacion_bebida(self):
        """CP-005-1: Monitorear el uso de CPU durante la preparacion de una bebida estandar."""
        receta = {"agua_ml": 60, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0}

        cpu_inicial = psutil.cpu_percent(interval=1)
        inicio = time.time()
        resultado = self.mc.preparar_bebida(receta)
        cpu_durante = psutil.cpu_percent(interval=1)
        fin = time.time()

        self.assertEqual(resultado["Code"], 1, "La preparacion de la bebida fallo.")
        self.assertLess(cpu_durante, 100, "El uso de CPU alcanzo el 100% durante la preparacion.")

        print(f"CP-005-1: CPU antes: {cpu_inicial}%, CPU durante: {cpu_durante}%, Tiempo: {fin - inicio:.2f}s")

    def test_cpu_cargas_simultaneas(self):
        """CP-005-2: Verificar el uso de CPU con cargas simultaneas."""
        recetas = [{"agua_ml": 60, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0} for _ in range(5)]

        def preparar():
            resultado = self.mc.preparar_bebida(recetas[0])
            self.assertEqual(resultado["Code"], 1, "La preparacion de una bebida fallo.")

        cpu_inicial = psutil.cpu_percent(interval=1)
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(lambda _: preparar(), range(5))

        cpu_durante = psutil.cpu_percent(interval=1)
        self.assertLess(cpu_durante, 100, "El uso de CPU alcanzo el 100% durante la carga simultanea.")

        print(f"CP-005-2: CPU antes: {cpu_inicial}%, CPU durante: {cpu_durante}% bajo cargas simultaneas")

    def test_cpu_impacto_tamano(self):
        """CP-005-3: Analizar el impacto del tiempo de preparacion en el uso de CPU."""
        tamanos = [
            {"agua_ml": 240, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0},  # 8 oz
            {"agua_ml": 360, "cafe_g": 18, "leche_g": 0, "chocolate_g": 0},  # 12 oz
            {"agua_ml": 480, "cafe_g": 22, "leche_g": 0, "chocolate_g": 0}   # 16 oz
        ]

        for i, receta in enumerate(tamanos, start=1):
            cpu_inicial = psutil.cpu_percent(interval=1)
            inicio = time.time()
            resultado = self.mc.preparar_bebida(receta)
            cpu_durante = psutil.cpu_percent(interval=1)
            fin = time.time()

            self.assertEqual(resultado["Code"], 1, f"La preparacion de la bebida tamanio {i} fallo.")
            self.assertLess(cpu_durante, 100, f"Uso de CPU excesivo para bebida {i}.")

            print(f"CP-005-3: Tamanio {i}, CPU antes: {cpu_inicial}%, CPU durante: {cpu_durante}%, Tiempo: {fin - inicio:.2f}s")

if __name__ == "__main__":
    unittest.main()

