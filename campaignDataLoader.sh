#!/bin/bash

# Color codes for prompts
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No color

# Check if input.csv exists in current directory
if [ ! -f ./input.csv ]; then
    echo -e "${RED}Error: No se encontró el archivo 'input.csv' en el directorio actual.${NC}"
    exit 1
fi

echo -e "${GREEN}Procesando input.csv y distribuyendo en archivos separados...${NC}"
# Execute the Python script in the same directory as this bash script
python "$(dirname "$0")/splitter.py"

# Prompt the user to verify files
echo -e "${YELLOW}Puede verificar los archivos manualmente ingresando a la carpeta 'output' o verificarlos ahora mismo desde la terminal.${NC}"
echo -n -e "${YELLOW}¿Desea verificar en la terminal los archivos a subir antes de continuar? (s/n): ${NC}"
read verify_input

if [ "$verify_input" == "s" ]; then
  # Execute the verify.py script in the same directory as this bash script
  python "$(dirname "$0")/verify.py"
fi

# Prompt the user for a string input or cancel
echo -n -e "${YELLOW}Ingrese target org o presione enter para cancelar: ${NC}"
read input_string

if [ -z "$input_string" ]; then
    echo -e "${RED}Subida de datos cancelada.${NC}"
    exit 1
fi

# Execute the Salesforce CLI command with the input string

echo -e "${GREEN}Subiendo archivos a la org $input_string...${NC}"
