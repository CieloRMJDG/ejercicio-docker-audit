# Entrega — Ejercicio Docker (082)

## Enlaces de acceso (públicos, con certificado HTTPS)

| Servicio | URL |
|---|---|
| API | https://api.dockercamaron.duckdns.org/ |
| Logs (Dozzle) | https://dozzle.dockercamaron.duckdns.org/ |
| Monitoreo (Uptime Kuma) | https://uptime.dockercamaron.duckdns.org/ |

- **Uptime Kuma** (dashboard de monitoreo de los 3 servicios): usuario `sky`, contraseña `JINamor2712`.
- **Endpoints extra de la API:**
  - `https://api.dockercamaron.duckdns.org/health` → estado OK
  - `https://api.dockercamaron.duckdns.org/buscar?id=5` → consulta parametrizada (ejemplo)

## Repositorio

- GitHub: https://github.com/CieloRMJDG/ejercicio-docker-audit

## Arquitectura del servidor

- **Puertos expuestos (Security Group):** 22 (SSH), 80 (HTTP), 443 (HTTPS).
- **Proxy reverso:** Nginx Proxy Manager (única puerta de entrada en 80/443).
- **Contenedores (perfil de Docker):**

| Contenedor | Rol | Puerto interno |
|---|---|---|
| proxy-manager | Nginx Proxy Manager | 80 / 81 (admin) / 443 |
| api-082 | API Flask | 5050 |
| bd-082 | Base de datos MySQL | 3306 |
| uptime-kuma | Monitoreo | 3001 |
| dozzle | Visualizador de logs | 8080 |

- Todos los servicios internos se comunican en una red privada Docker; solo el proxy maneja el tráfico externo (443).

## Despliegue

- Docker + Docker Compose v5 en EC2, con certificados Let's Encrypt generados y renovados automáticamente por Nginx Proxy Manager.
- Pipeline CI/CD (GitHub Actions): análisis estático (Bandit), escaneo de vulnerabilidades (Trivy), tests (pytest), build + push de imagen y deploy automático al servidor.

## Acceso a Nginx Proxy Manager (panel)

- Solo por túnel SSH (puerto 81 no es público):
  - `ssh -L 8080:localhost:81 -i <llave>.pem ubuntu@16.59.56.6`
  - Abrir `http://localhost:8080` — usuario `skylbr2712@gmail.com`, contraseña `Cambiar123!`.