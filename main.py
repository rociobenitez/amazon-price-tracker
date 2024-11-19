from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Acceder a las variables de entorno
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

BUY_PRICE = 550 # Precio objetivo

URL = 'https://www.amazon.es/Garmin-010-02809-01-Forerunner-965-Whitestone/dp/B0BS1TN8QL/ref=sr_1_7?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2DPPN6OE8NLJG&dib=eyJ2IjoiMSJ9.w7baCCMnJrT-WnBEmt5DOsZccZTzwRH8-wbnyqRenNPe04k-f23okGkeMQ4iO9Bn35eAK59OfJq4DfnM_HE6YKR89j5O0kSUxUBQqfkFWqaC2j59Km1VWPrnmzejl4OfLdx296or7dAWSGb3iPHu9Id3RsH0qTl5XRc6NpsXtkyBzFONtDWdjzdtPMdBHIS6f757HdXsTJqPpXNnTW6Jja8_AWJVVh7n34R3vuYDV5p5AHezERSLsWiZU8ZQShVAyfPOK16tA_Z-6vsgYGBaZcYSEa7HinByQICU7ANDk7A.LcAKZCWXGnSzMAKuRMmdK4eARrMP2rWjEqnleQ3ZBJU&dib_tag=se&keywords=garmin%2Bforerunner%2B965&nsdOptOutParam=true&qid=1731995921&sprefix=garmin%2Bforerunner%2B965%2Caps%2C89&sr=8-7&ufe=app_do%3Aamzn1.fos.5e544547-1f8e-4072-8c08-ed563e39fc7d&th='
response = requests.get(URL, headers= {
   "Accept-Language": "es-ES,es;q=0.9",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
})

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())

# Encontrar el elemento HTML que contiene el precio
price = soup.find(class_="priceToPay").get_text()

# Quitar espacios en blanco y el símbolo €
clean_price = price.strip().replace("€", "").replace(",", ".")

# Convertir a float
price_float = float(clean_price)
#price_float = 500 # Simulación de correo
#print(price_float)

# ============ Enviar email ============
title = soup.find(class_="product-title-word-break").get_text().strip()
print(title)

if price_float < BUY_PRICE:
   message = f"¡El producto '{title}' está en oferta por {price_float}€!"

   try:
      with smtplib.SMTP(SMTP_ADDRESS, port=SMTP_PORT) as connection:
         print(f"Conectando a {SMTP_ADDRESS}:{SMTP_PORT}")
         connection.starttls()  # Encriptar conexión
         connection.login(EMAIL, PASSWORD)  # Autenticarse
         connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,  # Enviar al mismo email
            msg = f"Subject:Alerta de Precio\n\n{message}".encode("utf-8")  # Codificar el mensaje
         )
      print("Correo enviado.")
   except smtplib.SMTPAuthenticationError as e:
      print("Error de autenticación: Verifica tu email y contraseña.")
   except Exception as e:
      print(f"Error al conectar: {e}")

