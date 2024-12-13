import os
import yaml
from pathlib import Path
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Gera a documentação dos apps e atualiza o mkdocs.yml'

    def handle(self, *args, **kwargs):
        # Caminho para a pasta modules
        modules_dir = Path('modules')
        docs_dir = Path('docs/api')
        mkdocs_yml = Path('mkdocs.yml')

        # Carregar o mkdocs.yml existente
        if mkdocs_yml.exists():
            with open(mkdocs_yml, 'r') as file:
                mkdocs_config = yaml.safe_load(file)
        else:
            mkdocs_config = {}

        # Inicializar a navegação no mkdocs.yml
        nav = mkdocs_config.get('nav', [])

        # Adicionar as seções de apps no mkdocs.yml
        apps_nav = []

        # Criar documentação para cada app dentro de modules/
        for module in modules_dir.iterdir():
            if module.is_dir():
                # Gerar o arquivo markdown para o app
                app_name = module.name
                app_docs = self.generate_docs_for_module(module)
                app_readme = docs_dir / app_name / 'index.md'
                app_readme.parent.mkdir(parents=True, exist_ok=True)

                # Escrever o conteúdo no arquivo README.md
                with open(app_readme, 'w') as f:
                    f.write(app_docs)

                # Adicionar o app à navegação no mkdocs.yml
                apps_nav.append({app_name: f'modules/{app_name}/index.md'})

        # Atualizar o mkdocs.yml com a nova navegação
        if apps_nav:
            if 'Apps' in mkdocs_config.get('nav', []):
                mkdocs_config['nav'].remove('API')

            mkdocs_config['nav'].append(('API', apps_nav))

            with open(mkdocs_yml, 'w') as file:
                yaml.dump(mkdocs_config, file, default_flow_style=False)

        self.stdout.write(self.style.SUCCESS('Documentação gerada e mkdocs.yml atualizado com sucesso!'))

    def generate_docs_for_module(self, module_path):
        """
        Gera a documentação para um módulo Django, incluindo models, schemas, etc.
        """
        docs = ""

        # Percorrer os arquivos Python do módulo
        for file_path in Path(module_path).rglob('*.py'):
            # Excluir arquivos desnecessários como views.py
            if 'views.py' in str(file_path):
                continue

            # Gerar título com base no nome do arquivo
            file_name = file_path.stem
            docs += f"## {file_name.capitalize()}\n\n"

            # Ler e adicionar o conteúdo do arquivo Python
            with open(file_path, 'r') as file:
                docs += "```python\n" + file.read() + "\n```\n\n"

        return docs
