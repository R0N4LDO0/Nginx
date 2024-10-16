import os
from datetime import datetime

# Definindo variáveis
service = "nginx"
online_file = "/home/ronaldo/service_status/online.txt"
offline_file = "/home/ronaldo/service_status/offline.txt"
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Verificar se o serviço está em execução
status = os.system(f'systemctl is-active --quiet {service}')

if status == 0:
    with open(online_file, 'w') as file:
        file.write(f"{date_time} - {service} - active - ONLINE")
else:
    with open(offline_file, 'w') as file:
        file.write(f"{date_time} - {service} - inactive - OFFLINE")





