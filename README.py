#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o `Warsaw` do `Itaú Personnalité` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar o `Warsaw` do `Itaú Personnalité` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for installing/configuring `Warsaw` from `Itaú Personnalité` on `Linux Ubuntu`._
# 

# ## 1. Instalar o `Warsaw` do `Itaú Personnalité` no `Linux Ubuntu` [1]
# 
# Para instalar o `Warsaw` do `Itaú Personnalité`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# In[ ]:


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    


# 3. Para instalar um arquivo `.deb` no Ubuntu, você pode usar o comando `dpkg`. Siga as etapas abaixo para instalar o arquivo `warsaw_setup_64.deb`:
# 
# 4. Navegue até o diretório onde o arquivo `warsaw_setup_64.deb` está localizado. Por exemplo, se ele estiver na sua pasta de downloads, você pode usar o comando cd para entrar nesse diretório: `cd ~/Downloads`
# 
# 5. Agora, você pode usar o comando `dpkg` para instalar o arquivo `.deb`. Substitua `warsaw_setup_64.deb` pelo nome correto do arquivo, se for diferente: `sudo dpkg -i warsaw_setup_64.deb`
# 
# 6. O comando `sudo` é usado para executar a instalação com privilégios de superusuário, pois a instalação de pacotes requer permissões especiais.
# 
# Após a execução do comando acima, o sistema tentará instalar o pacote. Se houver dependências não atendidas, você receberá uma mensagem de erro informando quais pacotes são necessários. Você pode usar o comando `sudo apt-get install -f` para tentar resolver essas dependências: `sudo apt-get install -f`
# 
# Depois que todas as dependências forem resolvidas e a instalação for concluída com sucesso, o Warsaw deve estar instalado em seu sistema.
# 
# Lembre-se de que o Warsaw é um software específico e pode ser usado para fins bancários. Certifique-se de que está instalando-o de uma fonte confiável.

# In[ ]:


### 1.1 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `Warsaw` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÃO há.
    ```


# ## Referências
# 
# [1] OPENAI. Instalar arquivo .deb no ubuntu: https://chat.openai.com/c/178353d8-4823-4ccc-8aa6-f3e4b010f20e (texto adaptado). Acessado em: 04/10/2023 20:02.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 18/03/2024 17:10.
