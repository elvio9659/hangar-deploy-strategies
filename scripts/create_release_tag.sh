#!/bin/bash

# Script de Automação de Emissão de Certificados de Voo (Tags Anotadas)
VERSION=$1
DESCRICAO=$2

if [ -z "$VERSION" ] || [ -z "$DESCRICAO" ]; then
    echo "Erro: Forneça a versão e a descrição técnica do deploy."
    echo "Uso: ./create_release_tag.sh v1.0.0 'Homologado sem falhas'"
    exit 1
fi

echo "Gerando Tag Anotada para a versão $VERSION..."
# -a cria tag anotada, -m insere os metadados permanentes de auditoria
git tag -a "$VERSION" -m "$DESCRICAO - Emitido por: $USER em $(date)"

echo "Enviando Tag com segurança para a esteira de nuvem..."
git push origin "$VERSION"
echo "Tag $VERSION implantada com sucesso!"
