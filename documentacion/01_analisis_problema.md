# Etapa 1. Análisis del problema
## 1. Nombre y asignatura
Calculadora de fuerzas, momentos y equilibrio en el plano XZ. Asignatura: Estática.
## 2. Descripción, introducción y justificación
En ingeniería civil, la estática permite estudiar las fuerzas que actúan sobre elementos estructurales. El proyecto automatiza la descomposición de fuerzas y el cálculo de momentos para facilitar la revisión de ejercicios académicos. No sustituye un análisis estructural profesional.
## 3. Entradas
| Dato | Tipo | Restricción | Significado |
|---|---|---|---|
| Magnitud | float | Finita, >= 0 | Fuerza en N |
| Ángulo | float | 0 a 360 grados | Desde +X hacia +Z |
| x, z | float | Finitos | Coordenadas en metros respecto al origen |
| Opción | str | 1 a 8 | Acción del menú |
| Índice | int | 1 a cantidad de fuerzas | Registro a eliminar |
## 4. Procesos
Fx=F cos(θ); Fz=F sin(θ). Se convierten grados a radianes. Para r=(x,0,z) y F=(Fx,0,Fz), r×F=(0,z Fx-x Fz,0). Se suman componentes y momentos. R=sqrt((ΣFx)^2+(ΣFz)^2). Equilibrio cuando las tres sumas tienen valor absoluto <= 0.000001 (N para fuerzas y N·m para momentos), con al menos una fuerza. Se rechazan entradas inválidas.
## 5. Salidas
Componentes, momento individual y total, resultante, estado de equilibrio y lista de registros.
## 6. Ejercicio previo reconstruido
Barra sobre X de 4 m; fuerza de 700 N en el plano XZ a 20° respecto de +X, suponiendo que apunta hacia +Z. r=(4,0,0) m. Fx=657.78 N; Fz=239.41 N; Mx=0; My=-957.66 N·m; Mz=0. Magnitud del momento=957.66 N·m. R=700 N; no hay equilibrio con esa única fuerza. El enunciado corresponde al ejercicio trabajado anteriormente; el alumno debe adjuntar su evidencia original y confirmar el sentido de la fuerza.
## 7. Alcance
Registrar varias fuerzas, consultar resultados, comprobar equilibrio y eliminar registros durante la sesión. No calcula reacciones automáticamente ni guarda datos al cerrar.
## 8. Cumplimiento técnico
Dos clases con constructores, atributos y métodos; objetos; lista; menú; funciones; ciclos; condiciones; operaciones y validación. Módulos separados y cinco casos de prueba. Evidencias originales, Copilot y publicación quedan a cargo del alumno.
