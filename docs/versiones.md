# Versiones

## 0.1

Timer de intervalos por consola con interfaz gráfica en Tkinter.

### Funcionamiento

1. `main.py` crea la ventana (600x400, fondo `lightblue`) mediante `window.py`.
2. El usuario introduce tres datos: rondas, tiempo de trabajo y tiempo de descanso.
3. Al pulsar **Empezar**, `data()` lee los campos y llama a `timer(rondas, work, rest)`.
4. `timer.py` muestra una cuenta atrás de 3 segundos ("Preparado").
5. Luego repite el ciclo `rondas` veces:
   - Cuenta atrás del tiempo de trabajo ("Inicio").
   - Cuenta atrás del tiempo de descanso ("DESCANSO"), si es mayor que 0.
   - Mensaje "Fin de la ronda" y decrementa el contador de rondas.

### Archivos

| Archivo | Contenido |
| --- | --- |
| `main.py` | Interfaz gráfica y lectura de datos |
| `window.py` | Configuración de la ventana |
| `timer.py` | Lógica del temporizador y las rondas |