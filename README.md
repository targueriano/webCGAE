# webCGAE
Serviço web com intuito técnico administrativo a fim de otimizar o serviço público no IFC (CGAE).


Procedimento para por o projeto em produção com apache2 em sistema Ubuntu¹
*****************************************
GERAL
*****************************************
1. Fazer download do projeto. 
2. Escolher local para armazenâ-lo, pode ser "/var/www/" ou em algum diretório do usuário comun.


*****************************************
INSTALAR
*****************************************
# sudo apt install apache2 libapache2-mod-wsgi python-virtualenv python-tk python-pip


*****************************************
CRIAR VIRTUALENV, ACESSAR-LO E INSTALAR PACOTES NECESSÁRIOS 
*****************************************
(local do webCGAE-master[pode modificar nome, por exemplo elimar master]) 

$ virtualenv .env_webcgae

$ source .env_webcgae/bin/activate

(.env_webcgae) $ pip install -r requirements.txt


Se apresentar erro, tentar manualmente, por exempo "pip install pacote"
******************************************
CONFIGURAR PROJETO
******************************************

(.env_webcgae)$ python manage.py migrate

(.env_webcgae)$ python manage.py makemigrations

(.env_webcgae)$ python manage.py collectstatic

(.env_webcgae)$ python manage.py createsuperuser

Editar arquivo settings.py de webCGAE_1_11

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.249', 'localhost', 'webcgae.com'] (endereço que hospederá o projeto)


**************************************************
PERMISSÕES AOS ARQUIVOS
**************************************************

# chmod 777 -R webCGAE 

# chown :www-data webCGAE

# chown :www-data db.sqlite3


*****************************************
CONFIGURAR HOSTS
*****************************************

Em /etc/hosts

127.0.0.1   webcgae.com


*****************************************
CONFIGURAR APACHE2
*****************************************

Em /etc/apache2/sites-available/ criar um arquivo "webcgae.conf"

# touch webcgae.conf

1. Escrever no arquivo as seguintes instruções sem os parenteses: 

<VirtualHost *:80>
	ServerAdmin seuemail@gmail.com
	ServerName webcgae.com
        ServerAlias www.webcgae.com
	DocumentRoot /home/user/Documentos/webCGAE (Caminho completo onde está salvo o projeto)
	
	
	<Directory /home/user/Documentos/webCGAE/webCGAE_1_11>
	<Files wsgi.py>
	Require all granted
	</Files>
	</Directory>

        Alias /static /home/user/Documentos/webCGAE/static
	<Directory /home/user/Documentos/webCGAE/static>
	Require all granted
	</Directory>

	Alias /media /home/user/Documentos/webCGAE/media
	<Directory /home/user/Documentos/webCGAE/media>
	Require all granted
	</Directory>

        WSGIDaemonProcess webCGAE python-home=/home/user/Documentos/webCGAE/.env_webcgae python-path=/home/user/Documentos/webCGAE
        WSGIProcessGroup webCGAE
        WSGIScriptAlias / /home/user/Documentos/webCGAE/webCGAE_1_11/wsgi.py

	ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined


</VirtualHost>

Salvar e fechar

2. Ativar o site: 
# a2ensite webcgae.conf

3. Desativar default:
# a2dissite 000-default.conf

4. Reiniciar o serviço do apache2
# systemctl restart apache2

Se não retornar nenhum erro, sucesso, caso contrário dor de cabeça.


  

¹ Testado em Ubuntu 18.04
