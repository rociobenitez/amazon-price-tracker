# Amazon Price Tracker

Automatiza el monitoreo de precios en Amazon con un script desarrollado en Python. Este proyecto utiliza [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para realizar web scraping y `smtplib` para enviar alertas por correo electrónico cuando el precio de un producto cae por debajo de un umbral predefinido.

Ideal para rastrear descuentos automáticamente y nunca perder una buena oferta.

---

## 📖 Tabla de Contenido

1. [Descripción](#descripción)
2. [Características Principales](#características-principales)
3. [Prerrequisitos Técnicos](#prerrequisitos-técnicos)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Instalación](#instalación)
6. [Configuración](#configuración)
7. [Demostración Visual](#demostración-visual)
8. [Ejecución Automática](#ejecución-automática)
9. [Notas de Seguridad](#notas-de-seguridad)
10. [Contribuciones](#contribuciones)

---

## 📜 Descripción

Este script de **Amazon Price Tracker** está diseñado para automatizar el monitoreo de precios en Amazon. Usa **web scraping** para extraer dinámicamente los precios y envía notificaciones por correo electrónico si el precio de un producto es inferior al valor objetivo definido. 

Este proyecto es ideal para:
- Usuarios que buscan rastrear precios y aprovechar descuentos.
- Desarrolladores interesados en aprender técnicas de web scraping y notificaciones automáticas en Python.

---

## 🚀 Características Principales

- **Web Scraping con BeautifulSoup:** Extrae dinámicamente el precio de productos desde Amazon.
- **Notificaciones Automáticas:** Envía alertas por correo electrónico con el título del producto, precio actual y enlace.
- **Encabezados HTTP Personalizados:** Simula solicitudes humanas para evitar bloqueos del servidor.

---

## 🔧 Prerrequisitos Técnicos

- **Python 3.9** o superior.
- Dependencias listadas en el archivo `requirements.txt`.
- Una cuenta de correo electrónico (se recomienda Gmail) con acceso SMTP.

---

## 📂 Estructura del Proyecto

```plaintext
amazon-price-tracker/
├── main.py             # Script principal
├── requirements.txt    # Dependencias del proyecto
├── .env.example        # Ejemplo del archivo .env
├── README.md           # Documentación del proyecto
```

---

## ⚙️ Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/rociobenitez/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tus credenciales:**

   Crea un archivo `.env` en la raíz del proyecto y define las siguientes variables:

   ```plaintext
   EMAIL=tuemail@gmail.com
   PASSWORD=tucontraseña
   SMTP_ADDRESS=smtp.gmail.com
   SMTP_PORT=587
   ```

4. **Configura el precio objetivo y la URL del producto:**

   Edita las variables en `main.py`:

   ```python
   BUY_PRICE = 550  # Precio objetivo en euros
   URL = 'https://www.amazon.es/tu-producto'
   ```

---

## 📸 Demostración Visual

<p align="center">
  <img src="/img/product.jpeg" alt="Producto en Amazon" width="70%">
</p>

<p align="center">
  <img src="/img/email-alert.jpeg" alt="Alerta de correo" width="70%">
</p>

---

## 🔄 Ejecución Automática

Puedes configurar este script para que se ejecute automáticamente en **PythonAnywhere** o servicios como **AWS Lambda**.

### Ejecución en PythonAnywhere

1. **Sube tu proyecto:**
   - Inicia sesión en [PythonAnywhere](https://www.pythonanywhere.com/).
   - Ve a la pestaña **Files** y sube los archivos del proyecto.

2. **Instala las dependencias:**
   - Abre una consola Bash en PythonAnywhere.
   - Ve al directorio de tu proyecto y ejecuta:
     ```bash
     pip3 install --user -r requirements.txt
     ```

3. **Configura la ejecución automática:**
   - Ve a la pestaña **Tasks**.
   - Haz clic en **Add a new scheduled task** y agrega el siguiente comando:
     ```bash
     python3 /home/tu_usuario/amazon-price-tracker/main.py
     ```
   - Define la periodicidad (por ejemplo, cada hora).

4. **Revisa los logs:**
   - Ve a **Tasks > Log files** para verificar la salida del script.

---

## 🛡️ Notas de Seguridad

- **No compartas tus credenciales:** Usa un archivo `.env` para almacenar datos sensibles y asegúrate de excluirlo del repositorio agregándolo al archivo `.gitignore`.
- **Usa contraseñas específicas para aplicaciones:** Si tu proveedor de correo lo requiere (por ejemplo, Gmail con autenticación de dos factores).

---

## 🤝 Contribuciones

¿Tienes ideas para mejorar este proyecto? Abre un **issue** o envía un **pull request**. ¡Todas las contribuciones son bienvenidas!

---