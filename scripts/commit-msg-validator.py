#!/usr/bin/env python
import sys
import re
import subprocess


# Regex para validar Conventional Commits
PATTERN = r"^(feat|fix|chore|refactor|test|docs|style|ci|perf)(\([\w\-]+\))?: .{1,72}$"

def get_git_user():
    """Obtém o nome de usuário configurado no Git."""
    try:
        username = subprocess.check_output(
            ["git", "config", "user.name"], text=True
        ).strip()
        if not username:
            raise ValueError("Nome de usuário não configurado")
        return username
    except subprocess.CalledProcessError:
        return None
    except ValueError:
        return None

def add_user_to_commit(commit_msg, git_user):
    """Adiciona o nome do usuário à mensagem de commit"""
    return f"{commit_msg} (Usuário: {git_user})"

def main():
    # Primeiro argumento é o caminho para o arquivo da mensagem de commit
    commit_msg_path = sys.argv[1]

    # Lê a mensagem de commit
    with open(commit_msg_path, 'r', encoding='utf-8') as file:
        commit_msg = file.read().strip()

    # Obtém o nome do usuário
    git_user = get_git_user()

    # Se o nome do usuário não for encontrado, exibe erro
    if git_user is None:
        print("❌ Erro: Nome de usuário do Git não configurado!")
        print("Por favor, configure seu nome de usuário no Git usando os seguintes comandos:")
        print("\ngit config --global user.name 'Seu Nome'")
        print("git config --global user.email 'seu.email@dominio.com'")
        sys.exit(1)

    # Valida a mensagem de commit
    if not re.match(PATTERN, commit_msg):
        print(f"❌ Mensagem de commit inválida! (Usuário: {git_user})")
        print("A mensagem deve seguir o padrão:")
        print("<tipo>(<escopo opcional>): <descrição breve>")
        print("\nExemplo: feat(core): adiciona configurações no settings")
        sys.exit(1)

    # Se a mensagem for válida, adiciona o nome do usuário
    updated_commit_msg = add_user_to_commit(commit_msg, git_user)

    # Sobrescreve a mensagem de commit com o nome do usuário adicionado
    with open(commit_msg_path, 'w', encoding='utf-8') as file:
        file.write(updated_commit_msg)

    print(f"✅ Mensagem de commit válida e atualizada! (Usuário: {git_user})")
    sys.exit(0)

if __name__ == "__main__":
    main()
