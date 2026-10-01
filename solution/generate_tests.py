"""
Generar casos de prueba, en formato JSON, para el ejercicio.
"""

import json
from pathlib import Path
from random import randint

PROG = "convertir_a_binario.py"

base_dir = Path(".")
tests_file = base_dir / "solution" / "test_cases.json"

cases = [0, 1, 2, 3, 4, 5, 10, 15, 151, 255, 1000]

output = {}
tests = []

for decimal in cases:
    binario = f"{decimal:b}"
    
    inp = f"{decimal}"
    outp = f"(\\b{decimal}\\b)?0*{binario}\\b"
    name = f"{decimal}"
    entry = {
        "name": name,
        "type": "io",
        "run": "python3 " + PROG,
        "points": 1,
        "comparison": "regex",
        "input": inp,
        "expected": outp,
        }
    tests.append(entry)

# Añadir sangrías extra para copiar en archivo de Classroom 50
clsrm50 = {"assignments": [{"tests": tests}]}

with tests_file.open("w", encoding="utf-8") as f:
    json.dump(clsrm50, f, indent=2, ensure_ascii=False)
