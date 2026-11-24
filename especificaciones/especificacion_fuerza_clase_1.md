# Etapa 2. Clase Fuerza
Responsabilidad: representar una fuerza aplicada en XZ.
Atributos float: magnitud (N), angulo (grados), x y z (m). Inicializados con los argumentos de __init__(magnitud, angulo, x, z). El constructor rechaza valores no finitos, magnitud negativa o ángulo fuera de 0–360.
| Método | Entradas | Atributos | Algoritmo y retorno |
|---|---|---|---|
| componentes | Ninguna | magnitud, angulo | Convertir a radianes, calcular coseno y seno; regresar tupla Fx,Fz |
| momento | Ninguna | x,z y componentes | Regresar z*Fx-x*Fz, en N·m |
Reglas: conservar signo de My según producto cruz, no redondear internamente. Los datos se validan en el constructor.
