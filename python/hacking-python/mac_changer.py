import subprocess

# Cambia la dirección MAC de la interfaz de red llamada "Ethernet"
subprocess.call('powershell "Set-NetAdapter -Name \'Ethernet\' -MacAddress \'00:11:22:33:44:66\'"', shell=True)
print("Mac cambiada.")
