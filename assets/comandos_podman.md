# Cheat Sheet: Podman y Podman Compose

---

### Gestión de Imágenes

* **Listar imágenes locales**

  ```bash
  podman images
  ```

* **Buscar imagen en registries (Docker Hub por defecto)**

  ```bash
  podman search <nombre_imagen>
  ```

* **Descargar (pull) una imagen**

  ```bash
  podman pull <registro>/imagen:etiqueta
  ```

* **Eliminar imagen**

  ```bash
  podman rmi <imagen>  # o ID de imagen
  ```

* **Etiquetar imagen**

  ```bash
  podman tag <imagen> <registro>/imagen:etiqueta
  ```

* **Exportar imagen a un archivo tar**

  ```bash
  podman save -o imagen.tar <imagen>
  ```

* **Importar imagen desde tar**

  ```bash
  podman load -i imagen.tar
  ```

---

### Gestión de Contenedores

* **Listar contenedores**

  ```bash
  podman ps        # solo activos
  podman ps -a     # todos, incluso detenidos
  ```

* **Crear y arrancar contenedor**

  ```bash
  podman run -d --name <nombre> <imagen>
  ```

  * `-d`: modo detach (segundo plano)
  * `-p <host>:<contenedor>`: mapear puertos
  * `-v <host>:<contenedor>`: montar volúmenes

* **Iniciar/Detener contenedor**

  ```bash
  podman start <nombre|ID>
  podman stop <nombre|ID>
  ```

* **Reiniciar contenedor**

  ```bash
  podman restart <nombre|ID>
  ```

* **Eliminar contenedor**

  ```bash
  podman rm <nombre|ID>
  # agregar -f para forzar
  ```

* **Mostrar logs**

  ```bash
  podman logs <nombre|ID>
  ```

* **Ejecutar comando dentro de un contenedor en ejecución**

  ```bash
  podman exec -it <nombre|ID> bash
  ```

* **Ver estadísticas de uso (recursos)**

  ```bash
  podman stats <nombre|ID>
  ```

---

### Volúmenes y Almacenamiento

* **Listar volúmenes**

  ```bash
  podman volume ls
  ```

* **Crear volumen**

  ```bash
  podman volume create <nombre_volumen>
  ```

* **Eliminar volumen**

  ```bash
  podman volume rm <nombre_volumen>
  ```

* **Inspeccionar volumen**

  ```bash
  podman volume inspect <nombre_volumen>
  ```

---

### Redes

* **Listar redes**

  ```bash
  podman network ls
  ```

* **Crear red**

  ```bash
  podman network create <nombre_red>
  ```

* **Eliminar red**

  ```bash
  podman network rm <nombre_red>
  ```

* **Inspeccionar red**

  ```bash
  podman network inspect <nombre_red>
  ```

---

### Sistema

* **Ver versión de Podman**

  ```bash
  podman --version
  ```

* **Mostrar info del sistema**

  ```bash
  podman info
  ```

* **Limpiar recursos no usados**

  ```bash
  podman system prune
  ```

---

## Podman Compose

CLI similar a Docker Compose, usa archivos `docker-compose.yml`.

* **Levantar servicios**

  ```bash
  podman-compose up      # interactivamente
  podman-compose up -d   # detach
  ```

* **Detener servicios y eliminar contenedores**

  ```bash
  podman-compose down
  ```

* **Listar contenedores gestionados**

  ```bash
  podman-compose ps
  ```

* **Ver logs de servicios**

  ```bash
  podman-compose logs    # todos
  podman-compose logs -f <servicio>
  ```

* **Construir imágenes**

  ```bash
  podman-compose build
  ```

* **Eliminar imágenes creadas por Compose**

  ```bash
  podman-compose down --rmi all
  ```

* **Ejecutar comando en un servicio**

  ```bash
  podman-compose exec <servicio> bash
  ```

* **Recrear contenedores**

  ```bash
  podman-compose up -d --force-recreate
  ```

* **Escalar servicios**

  ```bash
  podman-compose up -d --scale <servicio>=<número>
  ```

---

> By CISO oswaldo.diaz
