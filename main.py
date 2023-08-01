# Script para calcular NETWORK BALANCING en pfSense
import os
import math

os.system("clear")
print("==============================================================")
print("---       CALCULADORA WAN WEIGHT PARA LOAD BALANCING       ---")
print("==============================================================")

# Consultamos el ancho de banda contratado
ispWAN1Mbps = int(input("Ingrese el valor en Mbps para la WAN1: "))
ispWAN2Mbps = int(input("Ingrese el valor en Mbps para la WAN2: "))

# Calculamos el Weight de cada enlace con el máximo común divisor de los anchos de banda contratados
ispWAN1Weight = ispWAN1Mbps / math.gcd(ispWAN1Mbps, ispWAN2Mbps)
ispWAN2Weight = ispWAN2Mbps / math.gcd(ispWAN1Mbps, ispWAN2Mbps)

# Los valores para declarar en el LoadBalance de pfSense
print("--------------------------------------------------------------")
print("Valores para ser declarados en pfSense para Load Balance:")
print(f"Ancho de banda contratado: [WAN1 = {ispWAN1Mbps} Mbps] [WAN2 = {ispWAN2Mbps} Mbps]")
print("RUTA: System / Routing / Gateways / Edit -> Advanced -> Weight")
print("--------------------------------------------------------------")
print(f"WAN Weight: [WAN1 = {ispWAN1Weight}] & [WAN2 = {ispWAN2Weight}]")
print("--------------------------------------------------------------")

# Informacion sobre porcentajes de distribucion de cargas
sumWANWeight = ispWAN1Weight + ispWAN2Weight
avgWAN1Weight = ispWAN1Weight / sumWANWeight
avgWAN2Weight = ispWAN2Weight / sumWANWeight
print("INFORMACION: Porcentajes de carga segun Weight declarado: ")
print(f"WAN Weight: [WAN1 = {avgWAN1Weight:.0%}] & [WAN2 = {avgWAN2Weight:.0%}]")
