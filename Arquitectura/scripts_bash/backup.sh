#!/bin/bash
# Crea el directorio backup y copiar en el todos los archivos txt

mkdir -p backup
cp *.txt backup/

echo "Todos los archivos txt se copiaron a backup"
