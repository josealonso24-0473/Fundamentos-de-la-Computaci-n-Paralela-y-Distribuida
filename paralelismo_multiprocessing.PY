# Ejemplo practico: suma de cuadrados en paralelo

from multiprocessing import Process, current_process
import time
import random

def calcular_cuadrados(nombre: str, inicio: int, fin: int):
    proc = current_process()
    print(f"[{nombre}] PID={proc.pid} | Calculando {inicio}..{fin}")
    
    resultado = sum(i ** 2 for i in range(inicio, fin + 1))
    time.sleep(random.uniform(0.5, 1.5))  # simula carga variable
    
    print(f"[{nombre}] Suma de cuadrados [{inicio}-{fin}] = {resultado:,}")

if __name__ == "__main__":
    t_inicio = time.time()

    procesos = [
        Process(target=calcular_cuadrados, args=("Proceso-A", 1,    1000)),
        Process(target=calcular_cuadrados, args=("Proceso-B", 1001, 2000)),
        Process(target=calcular_cuadrados, args=("Proceso-C", 2001, 3000)),
    ]

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    t_fin = time.time()
    print(f"\nTodos finalizados en {t_fin - t_inicio:.2f}s")