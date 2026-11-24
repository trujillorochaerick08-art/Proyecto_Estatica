# Etapa 4. Pruebas y validación
Pruebas automatizadas ejecutadas con Python durante la preparación de esta versión de referencia. Consultar pruebas.py y evidencias/ejecuciones/pruebas.txt.
| ID | Objetivo | Entradas (F,θ,x,z) | Esperado | Obtenido | Estado / observación |
|---|---|---|---|---|---|
| 01 | Ejercicio previo reconstruido | 700,20,4,0 | Fx=657.78; Fz=239.41; My=-957.66 | Coincide | Correcto; falta evidencia original |
| 02 | Normal | 100,90,2,0 | My=-200 | Coincide | Correcto |
| 03 | Límite | 0,360,0,0 | My=0 | Coincide | Correcto |
| 04 | Inválido | -100,90,2,0 | ValueError | ValueError | Correcto |
| 05 | Equilibrio y eliminación | (100,90,2,0), (100,270,2,0) | R=0; equilibrio; al eliminar segunda, no equilibrio | Coincide | Correcto |
Repetir en VS Code y guardar capturas reales del menú, caso original y pruebas adicionales. Los archivos TXT son registros de ejecución, no capturas de pantalla.
