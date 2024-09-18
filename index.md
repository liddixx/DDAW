# Semana 1: Introducción al Despliegue de Aplicaciones Web

## Contenido

### 1. Introducción al Concepto de Despliegue de Aplicaciones
El despliegue de aplicaciones es el proceso mediante el cual una aplicación desarrollada se pone en funcionamiento en un entorno de servidor para que los usuarios puedan acceder y utilizarla. Este proceso abarca desde la preparación del código y la infraestructura hasta la configuración de los entornos en los que la aplicación será ejecutada.

- **Despliegue manual**: Cuando el proceso de instalación, configuración y publicación se realiza de manera manual.
- **Despliegue automatizado**: Cuando se utilizan herramientas o scripts que permiten automatizar el proceso de despliegue para reducir errores y aumentar la eficiencia.

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
El objetivo de esta práctica es que los estudiantes configuren una máquina virtual con **Ubuntu Server** y se conecten a ella utilizando **SSH** desde **WSL** en Windows o desde una terminal Linux, utilizando autenticación basada en **claves SSH**.

### Pasos:

### 1. Instalación de la Máquina Virtual
1. **Descargar VirtualBox o VMware**:
   - Si aún no lo has hecho, descarga e instala [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/).
   
2. **Descargar Ubuntu Server**:
   - Dirígete al sitio oficial de Ubuntu y descarga la versión **Ubuntu Server** (preferiblemente la más reciente): [Ubuntu Server](https://ubuntu.com/download/server).
   
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
   - Copia el contenido y pégalo en el archivo `~/.ssh/authorized_keys` de tu servidor Ubuntu. Para ello, conéctate al servidor y ejecuta:
     ```bash
     mkdir -p ~/.ssh
     echo "tu_clave_publica" >> ~/.ssh/authorized_keys
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **Verificar la conexión con clave SSH**:
   - Ahora puedes conectarte a tu servidor Ubuntu sin necesidad de usar una contraseña:
     ```bash
     ssh usuario@<IP_de_tu_VM>
     ```
   - Si todo está configurado correctamente, la conexión se realizará automáticamente usando la clave privada.

### 4. Conectarse por SSH desde Windows (usando WSL) o Linux

#### Desde **Windows (WSL)**:
1. **Instalar WSL** (si no lo tienes instalado):
   - Abre PowerShell como administrador y ejecuta el siguiente comando para habilitar WSL:
     ```powershell
     wsl --install
     ```

2. **Conectarse por SSH**:
   - Abre la terminal de WSL.
   - Ejecuta el siguiente comando para conectarte a tu máquina virtual:
     ```bash
     ssh usuario@<IP_de_tu_VM>
     ```

#### Desde **Linux**:
1. Abre la terminal.
2. Ejecuta el comando SSH:
   ```bash
   ssh usuario@<IP_de_tu_VM>
