
## 1. Análisis
Crea carpetas, .gitignore y README inicial. Commit «Inicializar estructura del proyecto». Copia el análisis y agrega foto real del ejercicio previo. Commit «Agregar análisis y evidencia del problema».
## 2. Especificaciones
Copia las tres especificaciones y revísalas antes de implementar. Commit «Agregar especificaciones de clases y programa principal».
## 3. Implementación
Crea entorno virtual y requirements.txt. Abre Copilot y solicita una clase a la vez:
- «Implementa únicamente clases/fuerza.py siguiendo especificaciones/especificacion_fuerza.md. Explica constructor y producto cruz. No implementes otras clases».
- Comprueba manualmente el ejercicio y haz commit «Implementar clase Fuerza».
- «Implementa únicamente SistemaEstatico según especificacion_sistema.md, usando Fuerza ya revisada».
- Revisa y haz commit «Implementar clase SistemaEstatico».
- «Implementa el menú de main.py según especificacion_main.md, sin cambiar las clases».
- Commit «Implementar menú»; ejecuta e integra; commit «Integrar clases y menú» si hay cambios de integración.
## 4. Pruebas
Ejecuta python pruebas.py y python main.py. Repite cinco casos, guarda capturas reales y actualiza resultados. Commit «Agregar casos de prueba y evidencias». Si corriges errores, commit «Corregir errores identificados en pruebas».
## 5. Entrega
Completa README y la reflexión real de Copilot. Commit «Completar documentacion y entrega del proyecto». Comprueba acceso del profesor y entrega URL del repositorio.
## Git
Si clonaste tu repositorio nuevo, ya tendrás remoto origin. En cada etapa, selecciona solo los archivos de esa etapa con git add RUTA, ejecuta git commit -m "Mensaje de la etapa" y git push. En la primera publicación puede requerirse git push -u origin main (si tu rama es main). No publiques .venv ni credenciales. No inventes commits ni evidencias.
## Defensa oral
__init__ inicializa atributos; self identifica el objeto; una lista almacena fuerzas; los métodos realizan operaciones; while repite el menú; if/elif decide; try/except controla datos inválidos. El signo negativo de My proviene de la regla de la mano derecha: r×F. Si dos fuerzas opuestas actúan en el mismo punto, se cancelan tanto las fuerzas como los momentos.
