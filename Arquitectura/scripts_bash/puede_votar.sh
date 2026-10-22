#!/bin/bash
# Script que solicita los datos al usuario y dice si puede votar

read -p "Ingresa tu nombre: " nombre
read -p "Ingresa tu edad: " edad

if [ "$edad" -ge 16 ]; then
    echo "Hola, $nombre. Si estás habilitado para votar."
else
    echo "Hola, $nombre. No estás habilitado para votar (debes tener mas de 16 años)."
fi
