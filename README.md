# Pruebas Automatizadas con Pytest + POM

## Descripción
Este proyecto implementa pruebas automatizadas para una API utilizando las siguientes tecnologías y buenas prácticas:

- **Pytest** como framework de testing.
- **Modelo POM (Page Object Model)** adaptado a APIs para modularizar y reutilizar lógica.
- Campo `personId` **dinámico y parametrizado**, permitiendo su uso flexible en cada ejecución.
- **Manejo básico de errores** durante las llamadas HTTP.
- **Validación opcional contra base de datos**: Se incluye una consulta sugerida para verificar que el `personId` haya sido correctamente insertado por la API.

## Objetivo del Challenge Técnico

Automatizar:
- ✅ **Happy Path**: Respuesta exitosa de la API.
- ✅ **Sad Path**: Casos de error esperados (por ejemplo, `personId` inválido o ausente).

## Problema encontrado

El endpoint proporcionado (`https://api.test.worldsys.ar/import `) **no es accesible públicamente**. Tras validar desde Postman y consola:
- El dominio no resuelve (`DNS_PROBE_FINISHED_NXDOMAIN`)
- No es posible conectarse al servidor.

> ⚠️ Este problema no afecta la calidad del código ni la arquitectura implementada.

## Conclusión

- ✅ El proyecto tiene una **estructura limpia, modular y escalable** siguiendo buenas prácticas.
- ✅ Las pruebas están **parametrizadas y organizadas** con fixtures de Pytest.
- ✅ Se ha manejado adecuadamente el caso en que el servicio no esté disponible.
- ✅ Incluye comentarios y validaciones que facilitan futuras extensiones o ajustes.

## Cómo correr las pruebas

### Requisitos previos:
- Python 3.x instalado
- `pytest` y `requests` instalados

### Pasos:

1. Clona el repositorio:
   ```bash
   git clone git@github.com:jonaleo87/API-Testing-Pytest.git

2. Navega hasta la carpeta del proyecto: 
    ```bash
    cd API-Testing-Pytest

3. Crea y activa el entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate    # En macOS/Linux
    venv\Scripts\activate       # En Windows

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

5. Ejecuta las pruebas:
    ```bash
    pytest tests/test_person_api.py -v
