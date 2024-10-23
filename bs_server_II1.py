import socket
import argparse
import psutil
from socket import AddressFamily
from sys import exit as sysexit
from re import compile as recompile


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', help="port utilisé",type=int, default=13337)
parser.add_argument('-l', '--listen', help="ip sur laquelle écoute",type=str, default="127.0.0.1")
args = parser.parse_args()

port = args.port
if port < 0 or port > 65535:
    print(f"ERROR -p argument invalide. Le port spécifié {port} n'est pas un port valide (de 0 à 65535).")
    sysexit(1)
if port >= 0 and port <= 1024:
    print(f"ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.")
    sysexit(2)

host = args.listen
ip_regex = recompile(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$')
if not ip_regex.match(host):
    print(f"ERROR -l argument invalide. L'adresse {host} n'est pas une adresse IP valide.")
    sysexit(3)

res = psutil.net_if_addrs()['Wi-Fi']
for infos in res:
    if infos.family == AddressFamily.AF_INET:
        ip = infos.address
        print(f"{ip}")
        if host != ip:
            print(f"ERROR -l argument invalide. L'adresse {host} n'est pas l'une des adresses IP de cette machine.")
            sysexit(4)
