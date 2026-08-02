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
