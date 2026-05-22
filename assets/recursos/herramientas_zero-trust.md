## Herramientas para Zero Trust 

El concepto de "Zero Trust" (Confianza Cero, en español) es un enfoque de seguridad informática que se basa en la premisa de que no se debe confiar en ninguna entidad, ya sea interna o externa, por defecto. En lugar de asumir que ciertas partes de una red o sistema son de confianza, el enfoque Zero Trust asume que todas las personas, dispositivos y aplicaciones son potencialmente no confiables y, por lo tanto, deben ser verificados antes de permitir el acceso a recursos o datos sensibles.


OSSEC (Open Source Security Information and Event Management) contenedor 

        podman pull atomicorp/ossec-docker
        podman run -d -p 1514:1514/udp -p 1515:1515/tcp --name ossec-server <image>

OSSEC Repositorio

        https://github.com/ossec/ossec-hids.git

Nota: otras herramientas open source Suricata, Wazuh, Snort, Fail2Ban, Bro (ahora Zeek), Security Onion.


**Firewalls de Aplicación Web (WAF)**: Ayudan a proteger las aplicaciones web y los servicios contra ataques comunes, como inyecciones SQL y ataques de cross-site scripting (XSS).

ModSecurity contenedor

        podman pull owasp/modsecurity # contenedor

ModSecurity repositorio

        https://github.com/SpiderLabs/ModSecurity.git # repositorio

**Soluciones de Gestión de Identidad y Acceso (IAM)**: Estas herramientas se utilizan para autenticar y autorizar a los usuarios y sistemas, y para gestionar los privilegios de acceso.

KEYCLOAK contenedor

        podman run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:23.0.3 start-dev

KEYCLOAK repositorio

        https://www.keycloak.org/documentation

Authelia contenedor

        podman pull authelia/authelia:latest

Authelia Repositorio

        https://www.authelia.com/integration/deployment/docker/

Ory Hydra contenedor

        podman pull oryd/hydra:v2.2.0-rc.3
        podman run --rm -it oryd/hydra:v2.2.0-rc.3 help

Ory Hydra Repositorio

        https://github.com/ory/hydra.git


**Seguridad de Punto de Acceso (NAC)**: Las soluciones NAC garantizan que solo los dispositivos autorizados tengan acceso a la red. Verifican y hacen cumplir las políticas de seguridad antes de permitir la conexión.

OpenHab contenedor

        podman pull openhab/openhab

OpenHab Repositorio

        https://github.com/openhab/openhab1-addons.git


Nota: otras soluciones comerciales 

- Cisco NAC Appliance & Fortinet NAC: son sistemas administrados que se puede implementar en una variedad de entornos, incluido la autenticación, la autorización y la detección de dispositivos.

**Microsegmentación de Red**: Esta tecnología divide la red en segmentos más pequeños y aísla el tráfico entre ellos. Soluciones como VMware NSX y Cisco ACI pueden ayudar a implementar la microsegmentación.

Calico repositorio Kubernetes

        https://github.com/projectcalico/calico.git

Flannel repositorio Kubernetes

        https://github.com/flannel-io/flannel.git

Weave NET repositorio Kuebernetes

        https://www.weave.works/docs/net/latest/kubernetes/

**Soluciones de Gestión de Amenazas y Seguridad de Endpoints**: Herramientas de seguridad de endpoints, como antivirus y soluciones EDR (Detección y Respuesta a Amenazas), ayudan a proteger los dispositivos y sistemas finales.

Vmware Carbon Black 

        https://carbonblack.vmware.com/carbon-black-demonstrations

CylancePROTECT repositorio Kubernetes

        https://github.com/zer0Trac3/cylanceprotect.git


**Soluciones de Análisis de Comportamiento y Anomalías**: Utilizan el aprendizaje automático y la analítica para detectar patrones de comportamiento inusuales o amenazas en tiempo real.

Seldon Core repositorio kubernetes

        https://docs.seldon.io/projects/seldon-core/en/latest/workflow/install.html

Feast repositorio Kubernetes

        https://docs.feast.dev/v/v0.21-branch/getting-started/feast-workshop

Anomaly Detection Toolkit (ADTK) repositorio Kubernetes

        https://github.com/arundo/adtk.git


**Soluciones de Gestión de Privilegios**: Permiten gestionar de manera más granular los privilegios de los usuarios y sistemas, asegurando que solo tengan acceso a los recursos necesarios, las plataformas para el control de acceso basado en roles (RBAC), son  

Red Hat Privileged Access Manager, CyberArk Conjur, Microsoft Azure Privileged Identity Management.

CyberArk Conjur Contenedor

        podman pull cyberark/conjur

CyberArk Conjur Repositorio

        https://github.com/cyberark/conjur.git


**Soluciones de Gestión de Acceso Condicional**: Estas soluciones aseguran que el acceso a recursos y datos sensibles esté condicionado a factores como la autenticación multifactor (MFA) y la ubicación del usuario.

Open Policy Agent (OPA) contenedor

        podman pull openpolicyagent/opa

Open Policy Agent (OPA) 

        https://github.com/open-policy-agent/opa.git

Athens repositorio para Kubernetes 

        curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash

**Herramientas de Gestión de Políticas de Seguridad**: Ayudan a definir y hacer cumplir políticas de seguridad coherentes en toda la infraestructura.

Regal antes Rego repositorio

        https://github.com/StyraInc/regal.git


**Plataformas de Orquestación y Automatización de Seguridad**: Estas herramientas permiten la automatización de procesos de seguridad, lo que ayuda a responder rápidamente a las amenazas.

Ansible contenedor

        podman pull ansible/ansible

Ansible repositorio

        https://github.com/ansible/ansible-docker-base.git

Chef contenedor

        podman pull chef/chef

Chef repositorio

        https://github.com/chef/chef.git

Nota: para utilizar Puppet considerar "This project is deprecated".

### Normas internacionales

- Zero Trust Architecture (ZTA): Aunque no es una norma internacional, el Grupo de Trabajo de Zero Trust del Instituto de Estándares de Internet (IETF) está trabajando en un conjunto de documentos y estándares relacionados con la arquitectura Zero Trust.

- ISO 27001: La norma ISO 27001 es un estándar internacional para la gestión de la seguridad de la información. Aunque no define Zero Trust en sí, proporciona un marco sólido para establecer políticas y procedimientos de seguridad que pueden ser integrados en un enfoque Zero Trust.

- NIST Cybersecurity Framework: El Marco de Ciberseguridad del Instituto Nacional de Estándares y Tecnología (NIST) de EE. UU. ofrece pautas y mejores prácticas para la gestión de la seguridad cibernética. Si bien no se enfoca específicamente en Zero Trust, puede ser útil para desarrollar una estrategia de seguridad alineada con los principios de confianza cero.

- GDPR (Reglamento General de Protección de Datos): Para organizaciones que manejan datos personales de ciudadanos de la Unión Europea, el GDPR establece requisitos específicos de protección de datos y privacidad. La implementación de Zero Trust puede ayudar a cumplir con los principios de privacidad y protección de datos.

- PCI DSS (Estándar de Seguridad de Datos de la Industria de Tarjetas de Pago): Para las organizaciones que manejan información de tarjetas de pago, el PCI DSS establece estándares de seguridad. La implementación de Zero Trust puede ayudar a cumplir con los requisitos de seguridad de PCI.

______________

> Rose, S. , Borchert, O. , Mitchell, S. and Connelly, S. (2020), Zero Trust Architecture, Special Publication (NIST SP), National Institute of Standards and Technology, Gaithersburg, MD, [online], 10.6028/NIST.SP.800-207

> Cusick, James. (2018). The General Data Protection Regulation (GDPR): What Organizations Need to Know. CT Corporation Resource Center. 

> Seaman, Jim. (2023). Zero Trust Security Strategies and Guideline. 10.1007/978-3-031-09691-4_9. 

> Garbis, Jason & Chapman, Jerry. (2021). Zero Trust Security: An Enterprise Guide. 10.1007/978-1-4842-6702-8. 

> Sarkar, Sirshak & Choudhary, Gaurav & Shandilya, Shishir K & Hussain, Azath & Kim, Hwankuk. (2022). Security of Zero Trust Networks in Cloud Computing: A Comparative Review. Sustainability. 14. 11213. 10.3390/su141811213. 

> Alawneh, Muntaha & Abbadi, Imad. (2023). Approaches for Zero Trust Adoption Based upon Organization Security Level. 10.1007/978-981-99-0272-9_36. 

> Cheng, Ruizhi & Chen, Songqing & Han, Bo. (2023). Towards Zero-trust Security for the Metaverse. 
