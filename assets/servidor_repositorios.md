

Guía de Implementación de una Plataforma Centralizada de Repositorios para Entornos de Ciencia de Datos e IA con Acceso Restringido a Internet

Versión: 1.0
 Fecha: Agosto 2026
 Autor: Dirección de Investigación en Ciencia de Datos e Inteligencia Artificial

1. Introducción

Las estaciones de trabajo y servidores con GPU NVIDIA utilizados para proyectos de Ciencia de Datos, Inteligencia Artificial Generativa e Inteligencia Artificial Agéntica requieren actualizaciones frecuentes de sistemas operativos, controladores, bibliotecas, imágenes de contenedores y modelos de lenguaje.

Sin embargo, debido a las políticas institucionales de seguridad de la información, estos equipos no pueden acceder directamente a Internet ni a repositorios externos.

Para resolver esta situación, se propone la implementación de una Plataforma Centralizada de Repositorios Empresariales para IA, cuya función será actuar como único punto autorizado para la sincronización, validación, almacenamiento y distribución de componentes tecnológicos requeridos por el ecosistema de IA institucional.

2. Objetivos
Objetivo General

Implementar una infraestructura centralizada que permita distribuir actualizaciones y artefactos tecnológicos a servidores y estaciones de trabajo Ubuntu con GPU NVIDIA sin requerir conectividad directa a Internet.

Objetivos Específicos
Centralizar la administración de repositorios.
Reducir la superficie de ataque asociada al acceso directo a Internet.
Garantizar trazabilidad y auditoría de componentes instalados.
Incorporar mecanismos de validación de vulnerabilidades.
Facilitar el despliegue de modelos de IA generativa y agéntica.
Estandarizar las versiones de software utilizadas institucionalmente.
3. Alcance

La solución cubre la distribución interna de:

Sistema Operativo Ubuntu.
Drivers NVIDIA.
CUDA Toolkit.
cuDNN.
TensorRT.
NCCL.
Docker.
Podman.
NVIDIA Container Toolkit.
Bibliotecas Python.
Ollama.
vLLM.
Imágenes de contenedores.
Modelos de IA de código abierto.
Actualizaciones de seguridad.
4. Arquitectura de Referencia
                               INTERNET
                                   │
                                   │
                    ┌──────────────┴──────────────┐
                    │ Firewall / Proxy Seguridad │
                    └──────────────┬──────────────┘
                                   │
                                   ▼

                 ┌─────────────────────────────────┐
                 │ Enterprise Repository Hub       │
                 │                                 │
                 │ Ubuntu Mirror                   │
                 │ NVIDIA Repository               │
                 │ Harbor Registry                 │
                 │ DevPI Repository                │
                 │ MinIO Object Storage            │
                 │ Trivy Security Scanner          │
                 └───────────────┬─────────────────┘
                                 │
                     Firewall Interno
                                 │
         ┌───────────────────────┼───────────────────────┐
         │                       │                       │
         ▼                       ▼                       ▼

   Workstation IA          Servidor GPU          Servidor IA
      Ubuntu                 Ubuntu                Ubuntu

              SIN CONECTIVIDAD DIRECTA A INTERNET

5. Especificaciones del Servidor Central
Infraestructura recomendada
Hardware
Componente	RecomendaciónCPU	16 a 32 vCPU
RAM	64 GB mínimo
Almacenamiento SO	500 GB SSD
Repositorios	5 TB a 20 TB
Red	10 Gbps
Sistema Operativo
Ubuntu Server 26.04 LTS

6. Fase 1. Preparación de la Infraestructura
Paso 1. Aprovisionar el servidor

Instalar:

Ubuntu Server 26.04 LTS


Configurar:

Dirección IP fija.
Nombre DNS institucional.
Certificados TLS.
Integración con Active Directory o LDAP.

Ejemplo:

repo-ia.interno.gob.mx

Paso 2. Configurar almacenamiento

Crear volúmenes independientes:

/opt/repos/ubuntu
/opt/repos/nvidia
/opt/repos/pypi
/opt/repos/containers
/opt/repos/models

7. Fase 2. Implementación del Repositorio Ubuntu
Paso 1. Instalar Aptly
sudo apt update
sudo apt install aptly

Paso 2. Sincronizar repositorios oficiales
aptly mirror create ubuntu-main \
https://archive.ubuntu.com/ubuntu noble main


Sincronizar:

aptly mirror update ubuntu-main

Paso 3. Publicar repositorio interno
aptly publish mirror ubuntu-main

Paso 4. Configurar clientes

Editar:

/etc/apt/sources.list


Ejemplo:

deb https://repo-ia.interno/ubuntu noble main


Actualizar:

sudo apt update

8. Fase 3. Implementación del Repositorio NVIDIA
Componentes a almacenar
NVIDIA Drivers
CUDA
cuDNN
TensorRT
NCCL
Fabric Manager
Container Toolkit

Paso 1. Crear espejo institucional

Sincronizar:

developer.download.nvidia.com


Hacia:

repo-ia.interno/nvidia

Paso 2. Publicar mediante NGINX

Instalar:

sudo apt install nginx


Configurar:

https://repo-ia.interno/nvidia

Paso 3. Configurar clientes

Agregar:

deb https://repo-ia.interno/nvidia stable main

9. Fase 4. Implementación de Registro de Contenedores
Solución recomendada
Harbor

Paso 1. Instalar Harbor

Desplegar utilizando:

docker compose up -d

Paso 2. Integrar escaneo de vulnerabilidades

Habilitar:

Trivy

Paso 3. Crear proyectos

Ejemplos:

ia-base
ollama
vllm
pytorch
tensorflow

Paso 4. Replicación de imágenes

Sincronizar:

Docker Hub
GitHub Container Registry
NVIDIA NGC
Quay.io

Paso 5. Configurar los clientes
docker login harbor.interno

docker pull harbor.interno/ollama/ollama:latest

10. Fase 5. Implementación de Repositorio Python
Herramienta recomendada
DevPI

Paso 1. Instalación
pip install devpi-server

Paso 2. Inicialización
devpi-init

Paso 3. Arranque del servicio
devpi-server --host 0.0.0.0

Paso 4. Configuración corporativa
pip config set global.index-url \
https://repo-ia.interno/pypi

Bibliotecas sugeridas
numpy
pandas
scipy
matplotlib
scikit-learn
torch
tensorflow
transformers
langchain
llama-index
vllm
peft
trl
accelerate

11. Fase 6. Implementación de Repositorio de Modelos de IA
Solución recomendada
MinIO

Paso 1. Instalación
docker run -d \
--name minio \
-p 9000:9000 \
-p 9001:9001 \
minio/minio server /data

Paso 2. Crear buckets
llama
qwen
phi
gemma
deepseek
mistral

Paso 3. Definir proceso de aprobación

Flujo:

Descarga
     ↓
Análisis
     ↓
Aprobación
     ↓
Publicación
     ↓
Consumo interno

12. Fase 7. Implementación de Servicios de IA
Ollama

Instalar:

ollama pull llama3

ollama pull qwen3


Publicar en repositorio interno.

vLLM

Crear imágenes certificadas:

vllm-cuda-12.x
vllm-cuda-13.x


Distribuir mediante Harbor.

13. Fase 8. Gestión de Seguridad
Escaneo de paquetes

Implementar:

Trivy
Grype

Escaneo de contenedores

Validar:

CVE críticas.
Dependencias vulnerables.
Imágenes obsoletas.
Flujo de liberación
Internet
    ↓
Descarga
    ↓
Escaneo
    ↓
Validación Seguridad
    ↓
Liberación
    ↓
Consumo institucional

14. Fase 9. Controles de Red
Segmentación propuesta
Zona DMZ

Contiene:

Enterprise Repository Hub


Acceso permitido:

HTTPS 443

Zona IA

Contiene:

Servidores GPU
Workstations
Plataformas IA

Reglas recomendadas
DMZ → Internet
Permitir HTTPS (443)

Zona IA → DMZ
HTTPS
APT
Docker Registry
PyPI
MinIO

Zona IA → Internet
DENY ALL

15. Fase 10. Alta Disponibilidad

Implementar dos nodos:

RepoHub01
RepoHub02


Servicios:

HAProxy
Keepalived


Nombre virtual:

repo-ia.interno

16. Operación y Gobierno Tecnológico
Actividades del Administrador
Diarias
Monitoreo de sincronizaciones.
Validación de errores.
Revisión de vulnerabilidades.
Semanales
Actualización de imágenes.
Actualización de modelos.
Publicación de versiones aprobadas.
Mensuales
Revisión de cumplimiento.
Auditoría de accesos.
Revisión de capacidad.
17. Beneficios Institucionales

La implementación de esta arquitectura permite:

Eliminar la necesidad de acceso directo a Internet desde servidores y estaciones de trabajo.
Mantener repositorios homologados institucionalmente.
Incrementar el control de ciberseguridad.
Reducir riesgos de cadena de suministro de software.
Mejorar la trazabilidad y auditoría de componentes.
Facilitar la operación de plataformas de IA generativa y agéntica.
Reducir los tiempos de despliegue y actualización tecnológica.
Asegurar la reproducibilidad de entornos de investigación y producción.
Referencias Bibliográficas (Formato APA 7.ª Edición)

Canonical Ltd. (2024). Ubuntu Server documentation. Ubuntu Documentation. https://ubuntu.com/server/docs

Harbor Authors. (2025). Harbor documentation: Open source container registry. CNCF Harbor Project. https://goharbor.io/docs/

NVIDIA Corporation. (2025). NVIDIA AI Enterprise and CUDA installation guides. NVIDIA Documentation. https://docs.nvidia.com

The Linux Foundation. (2025). Cloud native security with container registries and software supply chain protection. Cloud Native Computing Foundation. https://www.cncf.io

VMware, Inc. (2024). DevPI and enterprise Python package management best practices. Python Packaging Authority Ecosystem Reference Materials. https://packaging.python.org

Documento orientado a su presentación ante un Comité de Arquitectura Empresarial, Seguridad de la Información y Gobierno de TI para habilitar una plataforma institucional de Ciencia de Datos, IA Generativa e IA Agéntica bajo un esquema de acceso controlado a repositorios externos.

___________

Tu escenario es muy común en entornos gubernamentales, financieros y de infraestructura crítica donde los equipos de IA requieren aceleradores NVIDIA pero no tienen acceso directo a Internet por temas de ciberseguridad. La mejor práctica no es permitir que cada estación o servidor acceda a Internet, sino crear una Plataforma de Repositorios Empresariales Controlados (Enterprise Repository Hub) que funcione como punto único de actualización y distribución de software.

Objetivo

Implementar un host intermedio (Jump Repository Host o AI Software Hub) que:

Tenga conectividad controlada hacia Internet.
Sea auditado por Seguridad.
Sincronice únicamente repositorios autorizados.
Distribuya actualizaciones a servidores y estaciones Ubuntu dentro de la red interna.
Funcione como repositorio central para:
Ubuntu
NVIDIA Drivers
NVIDIA CUDA
NVIDIA Container Toolkit
Docker
Podman
Ollama
vLLM
Python Packages (PyPI)
Modelos de IA autorizados
Imágenes de contenedores
Arquitectura propuesta
                    INTERNET
                         │
                         │
          ┌──────────────┴──────────────┐
          │ Firewall / Proxy Seguridad  │
          └──────────────┬──────────────┘
                         │
                         ▼

        ┌──────────────────────────────────┐
        │ Enterprise AI Repository Hub     │
        │                                  │
        │ Ubuntu Mirror                    │
        │ NVIDIA Mirror                    │
        │ Docker Registry                  │
        │ Podman Registry                  │
        │ PyPI Mirror                      │
        │ Ollama Models                    │
        │ vLLM Components                  │
        │ Vulnerability Scanner            │
        └──────────────┬───────────────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼

    Workstation    GPU Server    AI Server
    Ubuntu 26      Ubuntu 26     Ubuntu 26

         SIN ACCESO DIRECTO A INTERNET

Componente 1. Ubuntu Repository Mirror

La finalidad es evitar que los equipos se conecten a los repositorios oficiales.

Herramientas recomendadas:

apt-mirror
debmirror
aptly
Pulp

Mi recomendación:

Aptly

Ventajas:

Gestión granular de paquetes.
Firma GPG propia.
Snapshots.
Promoción entre ambientes.

Repositorios a sincronizar:

Ubuntu Base
Ubuntu Security
Ubuntu Updates
Ubuntu Backports


Los equipos internos usarían:

deb http://repo-ia.interno/ubuntu noble main restricted universe multiverse

Componente 2. Repositorio NVIDIA

Es uno de los elementos más importantes.

Debe contener:

NVIDIA Drivers
CUDA
cuDNN
TensorRT
NVIDIA Container Toolkit
NVIDIA Fabric Manager
NCCL


Repositorio espejo:

repo-ia.interno/nvidia


Beneficios:

Control de versiones.
Validación previa.
Certificación por Seguridad.
Componente 3. Registro Privado de Contenedores

Para Docker y Podman.

No es recomendable permitir acceso a:

docker.io
quay.io
ghcr.io
nvcr.io


desde las estaciones finales.

Se recomienda:

Harbor

Es actualmente una de las mejores opciones.

Funciones:

Pull desde Internet.
Cache.
Replicación.
Escaneo de vulnerabilidades.
Control RBAC.
Firma de imágenes.

Arquitectura:

DockerHub
GHCR
NVIDIA NGC
Quay

      ↓

 Harbor Registry

      ↓

 Workstations
 Servidores GPU


Ejemplos:

docker pull harbor.interno/ollama/ollama:latest

podman pull harbor.interno/vllm/vllm:latest

Componente 4. PyPI Mirror

Uno de los mayores problemas en entornos de Ciencia de Datos es la descarga permanente de bibliotecas Python.

Herramienta recomendada:

DevPI

Alternativas:

Bandersnatch
Nexus Repository
Artifactory

Repositorio:

repo-ia.interno/pypi


Instalación de paquetes:

pip install pandas


Configurado automáticamente hacia:

https://repo-ia.interno/pypi


Paquetes importantes:

numpy
pandas
scipy
scikit-learn
transformers
langchain
llama-index
pytorch
tensorflow
ray
vllm
accelerate
peft
trl

Componente 5. Repositorio de Modelos de IA

Actualmente suele ser el elemento olvidado.

Los equipos descargan modelos desde:

Hugging Face
Ollama Library
GitHub


La recomendación es crear un repositorio interno.

Opciones:

MinIO

o

Nexus

Contenido:

Llama
Mistral
Phi
Gemma
DeepSeek
Qwen


Ejemplo:

minio://modelos-ia/llama3.3


Los modelos son previamente aprobados por Seguridad.

Componente 6. Repositorio Ollama

Mantener una estación sincronizadora.

Servidor Hub:

ollama pull llama3
ollama pull qwen3
ollama pull mistral


Posteriormente:

ollama push interno/llama3


o mediante exportación:

ollama create


Los servidores internos descargan desde el Hub.

Componente 7. Repositorio de Vulnerabilidades

Integrar:

Trivy

y/o

Grype

Para validar:

Contenedores.
Paquetes.
Dependencias Python.
Drivers.

Antes de publicar actualizaciones.

Flujo:

Internet
   ↓
Descarga
   ↓
Escaneo
   ↓
Aprobación Seguridad
   ↓
Publicación
   ↓
Consumo Interno

Segmentación de Red Recomendada

Propongo al área de Seguridad una estructura de tres zonas.

                INTERNET
                    │
            Firewall Externo
                    │
        ┌───────────┴───────────┐
        │        DMZ IA         │
        │ Enterprise Hub        │
        └───────────┬───────────┘
                    │
            Firewall Interno
                    │

          Zona IA Corporativa

    Workstations
    Servidores GPU
    Servidores vLLM
    Servidores Ollama


Reglas:

DMZ → Internet

Permitido
HTTPS 443
HTTP 80 (si se requiere)


Zona IA → DMZ

HTTPS 443
Docker Registry
APT Repository
PyPI Repository


Zona IA → Internet

DENY ALL

Alta Disponibilidad Recomendada

Si el presupuesto lo permite:

RepoHub01
RepoHub02

Keepalived
HAProxy


Disponibilidad:

repo-ia.interno


sin importar qué nodo esté activo.

Solución empresarial integral recomendada

Si buscas una plataforma madura para presentar a Seguridad y Arquitectura Tecnológica, mi recomendación sería:

Ubuntu 26.04 LTS

+
Harbor (Imágenes)
+
Aptly (Ubuntu y NVIDIA)
+
DevPI (Python)
+
MinIO (Modelos IA)
+
Trivy (Seguridad)
+
HAProxy
+
LDAP/AD


Con esta arquitectura consigues:

Cero acceso directo a Internet desde las estaciones de trabajo.
Trazabilidad completa de actualizaciones.
Control de versiones de controladores NVIDIA.
Distribución centralizada de CUDA, Docker, Podman, Ollama y vLLM.
Escaneo de vulnerabilidades previo a la liberación.
Cumplimiento de políticas de ciberseguridad.
Escalabilidad para proyectos de IA generativa y agéntica a nivel institucional.

Esta propuesta es suficientemente robusta para presentarse ante un Comité de Arquitectura Empresarial o un área de Seguridad de la Información como patrón de referencia para una plataforma de IA aislada (Air-Gapped o Semi Air-Gapped).
