Instalação do Linux no Windows Subsystem for Linux (WSL)


#Habilitar o WSL
Abra o PowerShell como administrador. Você pode procurar por "PowerShell" no menu iniciar, clicar com o botão direito e selecionar "Executar como administrador".

Execute o seguinte comando para habilitar o WSL:

wsl --install
Isso irá instalar a versão mais recente do WSL e a distribuição padrão do Ubuntu.

Reiniciar o Computador Após a instalação, reinicie o computador para aplicar as mudanças.

Instalar uma Distribuição Linux Após reiniciar, abra o Microsoft Store. Procure por "Ubuntu" e selecione a versão que você deseja instalar (como Ubuntu 20.04 ou 22.04). Clique em "Instalar" para baixar e instalar a distribuição.

Configurar o Linux Após a instalação, inicie o Ubuntu através do menu iniciar. A primeira execução pode levar alguns minutos. Você será solicitado a criar um nome de usuário e uma senha para sua nova instalação do Ubuntu.

Atualizar o Sistema Depois que o Ubuntu estiver instalado, é uma boa prática atualizar o sistema:

sudo apt update
sudo apt upgrade 
Instalar Dependências Necessárias Para o projeto de monitoramento do Nginx, instale as dependências necessárias:
sudo apt install nginx curl cron
