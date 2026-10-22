#!/bin/bash
# Script que lee un archivo con nombres y los saluda 

archivo="nombres.txt"

if [ ! -f "$archivo" ]; then
    echo "Error: El archivo $archivo no existe."
    exit 1
fi

# Leer el archivo línea por línea
while IFS= read -r nombre; do
    # Omitir líneas vacías
    if [ -n "$nombre" ]; then
        echo "¡Hola, $nombre! Bienvenido/a."
    fi
done < "$archivo"
