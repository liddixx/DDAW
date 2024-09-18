# Semana 1: Introducción al Despliegue de Aplicaciones Web

## Contenido

### 1. Introducción al Concepto de Despliegue de Aplicaciones
El despliegue de aplicaciones es el proceso mediante el cual una aplicación desarrollada se pone en funcionamiento en un entorno de servidor para que los usuarios puedan acceder y utilizarla. Este proceso abarca desde la preparación del código y la infraestructura hasta la configuración de los entornos en los que la aplicación será ejecutada.

- **Despliegue manual**: Cuando el proceso de instalación, configuración y publicación se realiza de manera manual.
- **Despliegue automatizado**: Cuando se utilizan herramientas o scripts que permiten automatizar el proceso de despliegue para reducir errores y aumentar la eficiencia.

### Ejemplos de Herramientas para Despliegue Automatizado

1. **Jenkins**:  
   Jenkins es una herramienta de **Integración Continua (CI)** que permite automatizar las fases de construcción, prueba y despliegue del software. Se utiliza para ejecutar **pipelines de despliegue** que integran múltiples etapas automatizadas. Jenkins es muy flexible y se puede configurar para trabajar con una amplia variedad de tecnologías y entornos de servidor.  
   - Sitio oficial: [https://www.jenkins.io](https://www.jenkins.io)

2. **Ansible**:  
   Ansible es una herramienta de **automatización de configuración** y **despliegue** que permite gestionar servidores y aplicaciones a través de archivos YAML. Con Ansible, es posible definir configuraciones y procedimientos de despliegue de manera declarativa, lo que hace que los despliegues sean repetibles y consistentes en cualquier entorno.  
   - Sitio oficial: [https://www.ansible.com](https://www.ansible.com)

---

### 2. Revisión del Ciclo de Vida de Desarrollo y Despliegue
El ciclo de vida de desarrollo y despliegue de aplicaciones sigue una serie de etapas que garantizan que una aplicación pasa por diferentes pruebas y ajustes antes de ser accesible al público. Los pasos más comunes incluyen:

1. **Desarrollo**: Donde los desarrolladores escriben el código de la aplicación en un entorno local.
2. **Pruebas (QA)**: Se realizan pruebas funcionales, de rendimiento, seguridad, etc., para asegurar que la aplicación funciona correctamente.
3. **Preproducción**: Una réplica del entorno de producción donde se realizan pruebas finales.
4. **Producción**: La aplicación se despliega en el entorno real donde los usuarios finales la utilizan.

### 3. Diferencias entre Entornos de Desarrollo, Pruebas, Preproducción y Producción
- **Desarrollo**: Ambiente local donde los desarrolladores crean y prueban nuevas funcionalidades. Suele contener datos y configuraciones de prueba.
- **Pruebas**: Ambiente donde se ejecutan pruebas para verificar que los cambios realizados no generan errores en la aplicación.
- **Preproducción**: Una réplica casi exacta del entorno de producción utilizada para realizar pruebas antes de la implementación final.
- **Producción**: El entorno final donde los usuarios acceden a la aplicación. Aquí se requiere la máxima estabilidad y seguridad.

---

## Práctica: Instalación y Configuración de una Máquina Virtual con Ubuntu Server

### Objetivo:
El objetivo de esta práctica es configurar una máquina virtual con **Ubuntu Server** y conectarnos a ella utilizando **SSH** desde **WSL** en Windows o desde una terminal Linux, utilizando autenticación basada en **claves SSH**.

### ¿Qué es SSH?

**SSH** (Secure Shell) es un protocolo de red que permite a los usuarios conectarse de manera segura a un servidor remoto o a otra máquina en una red, utilizando una interfaz de línea de comandos. SSH cifra todo el tráfico entre el cliente y el servidor, garantizando que la comunicación esté protegida contra ataques, intercepciones y manipulaciones de datos.

#### Características principales de SSH:
- **Seguridad**: SSH utiliza técnicas de cifrado para garantizar que la información transmitida entre el cliente y el servidor esté protegida. Esto incluye la autenticación del usuario y la confidencialidad de los datos.
- **Autenticación basada en claves**: Además de las contraseñas, SSH permite el uso de claves criptográficas para autenticar al usuario, lo que mejora la seguridad al evitar la necesidad de ingresar contraseñas en cada sesión.
- **Interfaz de línea de comandos**: SSH proporciona acceso remoto a la línea de comandos del servidor, permitiendo ejecutar comandos, transferir archivos y gestionar el sistema desde cualquier lugar.

#### Cómo funciona:
1. **Cliente SSH**: Es la máquina o dispositivo desde el cual se inicia la conexión. El cliente SSH envía una solicitud de conexión al servidor.
2. **Servidor SSH**: Es la máquina que recibe la solicitud y permite el acceso si las credenciales (contraseña o clave SSH) son válidas.
3. **Autenticación**: El cliente puede autenticarse mediante una contraseña o un par de claves (pública y privada). En el caso de la autenticación basada en claves, la clave pública se almacena en el servidor, mientras que la clave privada permanece en el cliente. Si la clave privada coincide con la clave pública almacenada en el servidor, se permite el acceso.

SSH es ampliamente utilizado para administrar servidores y entornos remotos de forma segura, y es esencial para los desarrolladores, administradores de sistemas y cualquier profesional que gestione servidores en entornos de red.

---

### Pasos:

### 1. Instalación de la Máquina Virtual
1. **Descargar VirtualBox o VMware**:
   - Si aún no lo has hecho, descarga e instala [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/).
   
2. **Descargar Ubuntu Server**:
   - Dirígete al sitio oficial de Ubuntu y descarga la versión **Ubuntu Server** (preferiblemente la más reciente): [Ubuntu Server](https://releases.ubuntu.com/jammy/).
   
3. **Crear una nueva máquina virtual** en VirtualBox o VMware:
   - Abre VirtualBox/VMware.
   - Haz clic en **Nueva máquina**.
   - Asigna un nombre a la máquina y selecciona **Linux** como el tipo de sistema operativo, y **Ubuntu (64-bit)**.
   - Asigna suficiente memoria RAM (al menos 2 GB) y espacio en disco (mínimo 10 GB).
   - En la sección de disco duro, selecciona **Crear un disco duro virtual ahora** y elige un formato compatible como VDI.
   - Completa el asistente y comienza a configurar la máquina.

4. **Instalar Ubuntu Server**:
   - Monta la imagen ISO descargada de Ubuntu Server en la VM.
   - Inicia la VM y sigue los pasos para instalar Ubuntu Server:
     - Selecciona el idioma.
     - Configura las opciones de red (puedes dejarlo en automático).
     - Establece un usuario y contraseña.
     - Instala las utilidades básicas del sistema.
     - Finaliza la instalación y reinicia.

### 2. Configurar SSH en Ubuntu Server

1. **Instalar el servicio OpenSSH**:
   - Inicia sesión en tu máquina virtual con las credenciales configuradas.
   - Abre la terminal y ejecuta el siguiente comando para instalar el servidor SSH:
     ```bash
     sudo apt update
     sudo apt install openssh-server
     ```
   
2. **Verificar el estado del servicio SSH**:
   - Asegúrate de que el servicio SSH está funcionando:
     ```bash
     sudo systemctl status ssh
     ```
   - Si no está en ejecución, puedes iniciarlo con:
     ```bash
     sudo systemctl start ssh
     ```

3. **Obtener la dirección IP de la VM**:
   - Ejecuta el siguiente comando para obtener la dirección IP de tu VM:
     ```bash
     ip a
     ```
   - Localiza la dirección IP bajo la interfaz de red activa (por ejemplo, `enp0s3` o `eth0`).

### 3. Generar y Configurar Claves SSH

En lugar de utilizar una contraseña, generaremos un par de claves SSH (pública y privada) para conectarnos de manera segura.

#### **Generar las claves SSH (en WSL o Linux)**:

1. **Generar un par de claves SSH**:
   - En la terminal de **WSL** o en Linux, ejecuta el siguiente comando para generar un par de claves:
     ```bash
     ssh-keygen -t rsa -b 4096
     ```
   - Este comando creará un par de claves (pública y privada) de 4096 bits.
   - Cuando te pida una ubicación para guardar las claves, puedes usar la ruta predeterminada (`~/.ssh/id_rsa`) o elegir una personalizada.
   - Puedes dejar la contraseña en blanco si prefieres no establecer una.

2. **Copiar la clave pública al servidor Ubuntu**:
   - Para permitir la autenticación con clave pública, copia la clave **pública** a tu servidor Ubuntu utilizando `ssh-copy-id`:
     ```bash
     ssh-copy-id usuario@<IP_de_tu_VM>
     ```
   - Esto añadirá tu clave pública a la lista de claves autorizadas en el servidor.

   Si `ssh-copy-id` no está disponible, puedes copiar la clave manualmente:
   - Muestra el contenido de tu clave pública ejecutando:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Copia el contenido y pégalo en el archivo `~/.ssh/authorized_keys` en tu servidor Ubuntu.

### 4. Conectarse al Servidor Ubuntu mediante SSH

1. **Conectarse desde WSL o Linux**:
   - En la terminal, ejecuta el siguiente comando para conectarte al servidor Ubuntu:
     ```bash
     ssh usuario@<IP_de_tu_VM>
     ```
   - Si la autenticación con clave es exitosa, deberías estar conectado al servidor Ubuntu sin necesidad de una contraseña.

---

## Recursos

- **Documentación de Ubuntu Server**: [Ubuntu Server Guide](https://ubuntu.com/server/docs)
- **Introducción a la arquitectura cliente-servidor**: [Cliente-Servidor en Wikipedia](https://es.wikipedia.org/wiki/Cliente-servidor)
