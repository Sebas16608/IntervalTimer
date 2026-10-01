import time

def timer(rondas, inicio, descanso):
    if descanso:
        descanso = int(descanso)

    print("Preparado ")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    while rondas > 0:
        print("Inicio\n")
        for t in range(inicio, 0, -1):
            print(t)
            time.sleep(1)

        if descanso:
            print("DESCANSO")
            for t in range(descanso, 0, -1):
                print(t)
                time.sleep(1)

        print(f"Fin de la ronda\n")
        rondas -= 1
