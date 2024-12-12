#!/bin/bash

HOOK_NAME="commit-msg"
HOOK_SRC="hooks/$HOOK_NAME"
HOOK_DEST=".git/hooks/$HOOK_NAME"

if [ ! -d ".git" ]; then
    echo "⚠️ Diretório .git não encontrado. Inicializando repositório Git..."
    git init
    if [ $? -ne 0 ]; then
        echo "❌ Falha ao inicializar o repositório Git."
        exit 1
    fi
    echo "✅ Repositório Git inicializado com sucesso!"
fi


if [ ! -f "$HOOK_SRC" ]; then
    echo "❌ Hook $HOOK_SRC não encontrado!"
    exit 1
fi

echo "🔧 Instalando o hook $HOOK_NAME..."
cp "$HOOK_SRC" "$HOOK_DEST"

if [ $? -ne 0 ]; then
    echo "❌ Falha ao instalar o hook $HOOK_NAME."
    exit 1
fi

chmod +x "$HOOK_DEST"

echo "✅ Hook $HOOK_NAME configurado com sucesso no diretório .git/hooks!"


chmod +x setup-hooks.sh
