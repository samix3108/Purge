# purge.py

`purge.py` é um script Python projetado para desinstalar todos os pacotes Python instalados e limpar o cache do `pip`. Ele é especialmente útil quando você precisa redefinir seu ambiente Python, liberar espaço ou resolver problemas relacionados a pacotes.

## Funcionalidades

- **Desinstala todos os pacotes Python instalados**: O script lista todos os pacotes presentes no ambiente atual usando `pip freeze` e desinstala cada um deles.
- **Limpa o cache do pip**: Remove todos os arquivos do cache do `pip`, garantindo que o espaço em disco seja liberado e que futuros downloads de pacotes sejam feitos a partir de fontes limpas.

## Requisitos

- Python 3.x
- `pip` deve estar instalado e configurado no seu ambiente Python.

## Instalação

Não há necessidade de instalação adicional, mas é importante garantir que você tenha o Python e o `pip` corretamente configurados. 

1. **Certifique-se de que o Python e o pip estão instalados:**

   Verifique a instalação do Python:
   ```bash
   python --version
   ```

   Verifique a instalação do pip:
   ```bash
   pip --version
   ```

2. **Baixe o script:**

   Clone o repositório ou baixe o arquivo `purge.py` diretamente para seu ambiente de trabalho.

## Uso

1. **Navegue até o diretório onde o `purge.py` está localizado:**

   ```bash
   cd /caminho/para/o/diretório
   ```

2. **Execute o script:**

   ```bash
   python purge.py
   ```

   O script irá desinstalar todos os pacotes Python instalados e limpar o cache do `pip`. Após a execução, uma mensagem de confirmação será exibida.

## Como Funciona

- **Desinstalação de Pacotes**: O script usa `subprocess.check_output` para capturar a lista de pacotes instalados através de `pip freeze`. Em seguida, utiliza `subprocess.call` para executar o comando de desinstalação para cada pacote listado.
  
- **Limpeza do Cache**: Após desinstalar os pacotes, o script executa `pip cache purge` para remover todos os arquivos de cache do `pip`.

## Exemplos de Uso

Para garantir que o script funcione conforme o esperado, execute-o em um ambiente virtual Python para evitar efeitos colaterais no seu ambiente de sistema global.

## Contribuições

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
