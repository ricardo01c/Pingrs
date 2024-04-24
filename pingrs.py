from scapy.all import IP, ICMP, send

def send_custom_ping(ip_address, payload):
    # Construir el paquete ICMP personalizado con el contenido especificado
    packet = IP(dst=ip_address) / ICMP() / payload

    # Enviar el paquete ICMP personalizado
    send(packet)

# Solicitar la dirección IP de destino al usuario
ip_address = input("Ingrese la dirección IP de destino: ")

# Solicitar el contenido personalizado del paquete al usuario
payload = input("Ingrese el contenido del payload: ")

# Llamada a la función para enviar el paquete ping personalizado
send_custom_ping(ip_address, payload)