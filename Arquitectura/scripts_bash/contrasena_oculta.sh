#!/bin/bash
# Script para solicitar la contraseña oculta (-s)

read -sp "Ingresa tu contraseña: " clave
echo "" # Este echo lo puse porque si no muestra todo en la misma linea por el -s

echo "Contraseña ingresada correctamente."
