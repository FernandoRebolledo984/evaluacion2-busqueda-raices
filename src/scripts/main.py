import numpy as np
import os
import sys
import subprocess

if __name__ == "__main__":

    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    DIR_ASSETS = os.path.abspath(os.path.join(DIR_SCRIPTS, '..', 'assets'))
    DIR_DATA = os.path.abspath(os.path.join(DIR_SCRIPTS, '..', 'data'))
    os.makedirs(DIR_ASSETS, exist_ok=True)
    os.makedirs(DIR_DATA, exist_ok=True)

    SCRIPTS_INDIVIDUALES = ["biseccion.py","falsa_posicion.py","punto_fijo.py","secante.py","Newthon-Raphson.py","Newthon-Raphson_upgraded.py",]
    
    entorno = os.environ.copy()
    entorno["MPLBACKEND"] = "Agg"
    for nombre in SCRIPTS_INDIVIDUALES:
        ruta = os.path.join(DIR_SCRIPTS, nombre)
        print(f"\n{'=' * 70}\n=== Ejecutando {nombre}\n{'=' * 70}")
        if not os.path.exists(ruta):
            print(f"  [!] No se encontró {nombre}, se omite.")
            continue
        resultado = subprocess.run([sys.executable, ruta], cwd=DIR_SCRIPTS, env=entorno)
        if resultado.returncode != 0:
            print(f"  [!] {nombre} terminó con errores (código {resultado.returncode}).")