import os
import sys
import subprocess

def uninstall_all_packages():
    """Desinstala todos os pacotes Python instalados."""
    # Listar todos os pacotes instalados
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode().split('\n')
    
    # Remover pacotes instalados
    for package in installed_packages:
        if package:
            package_name = package.split('==')[0]
            subprocess.call([sys.executable, '-m', 'pip', 'uninstall', package_name, '-y'])

def clear_pip_cache():
    """Limpa o cache do pip."""
    subprocess.call([sys.executable, '-m', 'pip', 'cache', 'purge'])

if __name__ == "__main__":
    uninstall_all_packages()
    clear_pip_cache()
    print("Todos os pacotes desinstalados e cache limpo.")
