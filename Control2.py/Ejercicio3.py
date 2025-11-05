"""Indicaciones
Ya casi termina el 2025 y la ESEN está preparando toda la gestión para los estudiantes de nuevo ingreso que comenzarán sus estudios en 2026. Con el fin de ahorrar algo de tiempo, decidieron desarrollar un generador automático de correos electrónicos que crea el correo de cada alumno.

Tristemente, no realizaron pruebas para verificar si funcionaba correctamente y generaron todos los correos sin probarlos. Algunos de ellos podrían tener errores de formato, como:

Falta del @
El @ está ubicado en una posición indebida
Tu misión es crear un programa que verifique cuáles correos son válidos y cuáles no, para que la ESEN pueda enviar la información de los estudiantes de manera correcta. Un correo eléctronico se considera válido si se cumplen las siguientes condiciones:

Contiene exactamente un @
El @ no está ubicado al inicio del correo
El @ no está ubicado al final del correo
El programa recibirá un correo a validar y deberá confirmar si cumple con cada condición.

Entrada
Una sola línea con un correo electrónico a validar.

Salida
Tres líneas, cada línea confirmando si cumple o no con cada una de las condiciones:

 True/False
 True/False
El @ no está ubicado al final del correo: True/False"""
correo = input()

un_arroba = correo.count("@") == 1
inicio = correo[0] != "@"
fin = correo [17] != "@"

print(f"Contiene exactamente un @: {un_arroba}")
print(f"El @ no está ubicado al inicio del correo: {inicio}")
print(f"El @ no está ubicado al final del correo: {fin}")