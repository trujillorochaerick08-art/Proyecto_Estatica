# Etapa 2. Clase SistemaEstatico
Responsabilidad: gestionar objetos Fuerza y calcular resultados globales. Constructor __init__ sin argumentos: self.fuerzas inicia como lista vacía.
| Método | Entrada | Atributos | Algoritmo y resultado |
|---|---|---|---|
| agregar | Objeto Fuerza previamente validado | fuerzas | append, sin retorno |
| resultante | Ninguna | fuerzas | Recorrer lista, sumar Fx y Fz, regresar ambas sumas y magnitud |
| momento_total | Ninguna | fuerzas | Sumar momentos My; regresar float |
| equilibrio | Ninguna | fuerzas | Comparar sumas con tolerancia 1e-6; regresar bool; vacío no es equilibrio evaluable |
| eliminar | Índice entero desde 1 | fuerzas | Validar rango y eliminar; ValueError si no existe |
Reglas: no redondear antes de comparar, no cambiar las fórmulas de Fuerza.
