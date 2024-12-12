#!/bin/bash

# Caminhos do hook
HOOK_NAME="commit-msg"
HOOK_SRC="hooks/$HOOK_NAME"
HOOK_DEST=".git/hooks/$HOOK_NAME"

# Verifica se estamos em um repositório Git
if [ ! -d ".git" ]; then
    echo "❌ Diretório .git não encontrado! Você está dentro de um repositório Git?"
    exit 1
fi

# Verifica se o hook existe
if [ ! -f "$HOOK_SRC" ]; then
    echo "❌ Hook $HOOK_SRC não encontrado!"
    exit 1
fi

# Copia o hook para o diretório do Git
echo "🔧 Instalando o hook $HOOK_NAME..."
cp "$HOOK_SRC" "$HOOK_DEST"

# Garante que o hook seja executável
chmod +x "$HOOK_DEST"

echo "✅ Hook $HOOK_NAME configurado com sucesso no diretório .git/hooks!"


chmod +x setup-hooks.sh
