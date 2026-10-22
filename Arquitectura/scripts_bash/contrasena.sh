#!/bin/bash
# Script que pide la contrasena hasta que ingrese la correcta

clave=""

until [ "$clave" = "secreto" ]; do
    read -p "Ingresa la contraseña: " clave
    
    if [ "$clave" != "secreto" ]; then
        echo "Contraseña incorrecta. Inténtalo de nuevo."
    fi
done

echo "¡Acceso concedido!"
