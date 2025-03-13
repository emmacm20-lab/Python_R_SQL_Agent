# 📂 tests/test_execute_model.py - Pruebas en Python para validación de ejecución

import unittest
from src.execute_model import run_model

class TestModelExecution(unittest.TestCase):
    def test_run_model(self):
        try:
            run_model()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()