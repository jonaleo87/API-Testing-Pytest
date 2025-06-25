# Pruebas Automatizadas con Pytest + POM 

## Descripción
Este proyecto automatiza pruebas para un endpoint de API usando:
- Pytest como framework de testing
- Modelo POM adaptado a APIs
- Campo `personId` dinámico y parametrizado
- Manejo básico de errores
- **Validación en base de datos:** Se consulta la base de datos para verificar que el `personId` enviado por la API haya sido correctamente insertado.

## Problema encontrado
El endpoint proporcionado (`https://api.test.worldsys.ar/import `) **no es accesible públicamente**. Tras validar desde Postman y consola:
- El dominio no resuelve (`DNS_PROBE_FINISHED_NXDOMAIN`)
- No es posible conectarse al servidor

## Conclusión
- El código está correctamente estructurado y listo para funcionar contra un endpoint real.
- Se han implementado buenas prácticas de testing.
- Se ha manejado adecuadamente el caso en que el servicio no esté disponible.
- Se incluye una validación automática contra la base de datos para asegurar la correcta inserción de los