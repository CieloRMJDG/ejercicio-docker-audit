# Auditoría de seguridad — API Legacy TechNova

Fecha: 04/09/2026
Herramienta: Bandit 1.9.4

## Resultados

| # | ID Bandit | Severidad | CWE | Archivo:línea | Descripción | Remediación | Prioridad |
|---|-----------|-----------|-----|---------------|-------------|-------------|-----------|
| 1 | B105 | Medium | CWE-259 | `app.py:10` | Contraseña de BD `DB_PASS` hardcodeada en el código | Mover a variables de entorno / gestor de secretos | Alta |
| 2 | B608 | Medium | CWE-89 | `app.py:25` | SQL injection: el parámetro `id` se concatena en la consulta | Usar consultas parametrizadas | Alta |
| 3 | B201 | High | CWE-94 | `app.py:35` | Flask con `debug=True` expone el debugger de Werkzeug | Deshabilitar debug en producción | Alta |
| 4 | B104 | Medium | CWE-605 | `app.py:35` | Bind a `0.0.0.0` sin restricción | Configurar host/puerto por entorno, usar proxy inverso | Media |
| 5 | B311 | Low | CWE-330 | `app.py:30` | `random.random()` no es criptográficamente seguro | Usar `secrets` o eliminar la aleatoriedad del health check | Baja |
| 6 | B101 | Low | CWE-703 | `test_app.py:7` | `assert` en test (común en pruebas) | Aceptado para tests | Baja |

## Notas
- El health check (`/health`) es inestable: 30% de las veces lanza `1/0` → problema de disponibilidad, se corrige en la Fase 2.
- El endpoint `/buscar` devuelve la query cruda en el HTML → riesgo de fuga de información.