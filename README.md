# Calculadora de Estática — Proyecto Integrador Programación II
Asignatura original: Estática. Objetivo: calcular componentes, momentos, resultante y equilibrio de fuerzas en el plano XZ mediante programación orientada a objetos.
## Requisitos e instalación
Python 3, VS Code, Git, GitHub y Copilot. Sin dependencias externas.
En terminal de Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python main.py
python pruebas.py
```
También se puede ejecutar con `python main.py` sin entorno virtual al no requerir paquetes externos.
## Funcionalidades y clases
Fuerza calcula componentes y momento. SistemaEstatico administra una lista y evalúa resultante y equilibrio. El menú permite registrar, consultar y eliminar fuerzas.
## Ejemplo
700 N a 20 grados desde +X hacia +Z, posición (4,0) m: Fx=657.78 N, Fz=239.41 N, My=-957.66 N·m.
## Documentación
Consultar documentacion/01_analisis_problema.md, especificaciones/, documentacion/02_pruebas.md y documentacion/03_uso_copilot.md. Consultar GUIA_ENTREGA.md para reproducir las etapas obligatorias. Esta es una versión de referencia educativa; faltan las evidencias personales y publicación por etapas.
