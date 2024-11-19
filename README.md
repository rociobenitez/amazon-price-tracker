# Amazon Price Tracker

Un script desarrollado en Python que utiliza [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para **rastrear el precio de un producto en Amazon** y envía una alerta por correo electrónico cuando el precio cae por debajo de un valor predefinido. Ideal para monitorear productos y aprovechar descuentos automáticamente.

### 📋 Funcionalidades

- **Extracción de precios con BeautifulSoup:** Extrae dinámicamente el precio de un producto desde la página de Amazon.
- **Notificación por correo electrónico:** Envía un correo con los detalles del producto (título, precio actual y enlace) si el precio está por debajo de tu valor objetivo.
- **Encabezados HTTP personalizados:** Utiliza encabezados HTTP para simular una solicitud más humana y evitar bloqueos del servidor.

### 🛠️ Requisitos Previos

- Python 3.9 o superior.
- Una cuenta de correo (se recomienda Gmail) para enviar notificaciones.
- Instalación de librerías necesarias:
    ```bash
    pip install -r requirement

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/usuario/amazon-price-tracker.git
    cd amazon-price-tracker
    ```

2. **Crea un archivo `.env` en la raíz del proyecto:**
   - Define las siguientes variables de entorno:
       ```plaintext
       EMAIL=tuemail@gmail.com
       PASSWORD=tucontraseña
       SMTP_ADDRESS=smtp.gmail.com
       SMTP_PORT=587
       ```
   - Si usas autenticación de dos factores, genera una contraseña específica para aplicaciones desde tu cuenta de Gmail. 

![Verificación en dos pasos](/img/verificacion-dos-pasos.jpeg)

3. **Configura el precio objetivo y la URL del producto:** Edita las variables en `main.py`:

    ```python
    BUY_PRICE = 550  # Precio objetivo en euros
    URL = 'https://www.amazon.es/tu-producto'
    ```

### 📚 Estructura del Proyecto

```plaintext
amazon-price-tracker/
├── main.py             # Script principal
├── requirements.txt    # Dependencias del proyecto
├── .env.example        # Ejemplo del archivo .env
├── README.md           # Documentación del proyecto
```

### 🛠️ Detalles Técnicos

**Paso 1: Usar BeautifulSoup para obtener el precio del producto**

Se utiliza la biblioteca BeautifulSoup para extraer el precio del producto directamente desde su página web. El precio se convierte a un número de punto flotante para facilitar las comparaciones.

```python
price = soup.find(class_="priceToPay").get_text()
clean_price = price.strip().replace("€", "").replace(",", ".")
price_float = float(clean_price)
```
**Paso 2: Enviar notificaciones por correo**

Cuando el precio cae por debajo del valor objetivo, se utiliza el módulo [smtplib](https://docs.python.org/es/3/library/smtplib.html) para enviar un correo electrónico con los detalles del producto.

**Paso 3: Agregar encabezados a la solicitud HTTP**
Para evitar que la solicitud sea bloqueada, se añaden encabezados HTTP personalizados utilizando la biblioteca ***requests***.

**Encabezados mínimos necesarios:**
- Accept-Language: Idioma preferido.
- User-Agent: Identifica el tipo de navegador.

```python
headers = {
    "Accept-Language": "es-ES,es;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)
```

🔗[myttpheader](https://myhttpheader.com/)

### 🔍 Cómo Personalizar

- **Cambiar el precio objetivo:** Modifica la variable `BUY_PRICE` en `main.py` según tus necesidades.
- **Actualizar encabezados:** Copia los encabezados personalizados desde [httpbin.org/headers](https://httpbin.org/headers) para simular solicitudes más humanas.
- **Añadir un nuevo producto:** Reemplaza la URL del producto en la variable URL.

### 📸 Ejemplo Visual

![Producto de Amazon elegido](/img/product.jpeg)
![Ejemplo de Alerta de Correo](/img/email-alert.jpeg)

### 🛡️ Notas de Seguridad

- **No compartas tus credenciales:** Almacena las credenciales en el archivo .env y exclúyelo del repositorio añadiendo `.env` a `.gitignore`.
- **Usa contraseñas específicas para aplicaciones** si utilizas autenticación de dos factores en Gmail.

### 🧪 Pruebas

- **Prueba de conexión al servidor SMTP:** Ejecuta el siguiente script para verificar tu configuración:

    ```python
    import smtplib
    with smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT) as connection:
        connection.starttls()
        print("Conexión exitosa al servidor SMTP")
    ```
- **Simula un precio bajo:** Cambia temporalmente el precio del producto en el código para comprobar si se envía la notificación.

### 🔄 Ejecución Automática

Puedes configurar el script para que se ejecute automáticamente en un servidor, asegurándote de que rastrea los precios sin necesidad de intervención manual. Este proyecto es compatible con [PythonAnywhere](https://www.pythonanywhere.com/) y servicios como [AWS Lambda](https://aws.amazon.com/es/lambda/).

**Ejecución Automática en PythonAnywhere**
1. **Sube tu proyecto a PythonAnywhere:**
   - Inicia sesión en tu cuenta en [PythonAnywhere](https://www.pythonanywhere.com/).
   - Ve a la pestaña **Files** y sube los archivos del proyecto (o clónalo desde GitHub si ya está alojado).
2. **Instala las dependencias:**
   - Abre una consola Bash en PythonAnywhere. 
   - Ve al directorio donde está tu proyecto y ejecuta:
   ```bash
   pip3 install --user -r requirements.txt
   ```
3. **Configura la ejecución automática:**
   - Ve a la pestaña **Tasks** en PythonAnywhere. 
   - Haz clic en **Add a new scheduled task**. 
   - Introduce el siguiente comando para ejecutar el script automáticamente:
   ```bash
   python3 /home/tu_usuario/amazon-price-tracker/main.py
   ```
   - Define la periodicidad (por ejemplo, cada hora o una vez al día). 
4. **Revisa los logs:**
   - Accede a **Tasks > Log files** para verificar la salida del script y asegurarte de que se ejecuta correctamente.

### 🤝 Contribuciones

Si deseas contribuir al proyecto, abre un issue o realiza un pull request. ¡Toda ayuda es bienvenida!