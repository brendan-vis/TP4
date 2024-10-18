# I. Simple bs program

## 1. First steps

🌞 bs_server_I1.py

[bs_server_I1.py](./bs_server_I1.py)
```

```

🌞 bs_client_I1.py

[bs_client_I1.py](./bs_client_I1.py)
```

```

🌞 Commandes...

```
[brendan@server ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[brendan@server ~]$ sudo firewall-cmd --reload



[brendan@server ~]$ python bs_server_I1.py
Connected by ('10.1.1.12', 52712)
Données reçues du client : b'Meoooo !'

[brendan@client ~]$ python bs_client_I1.py
Le serveur a répondu b'Hi mate !'


[brendan@server ~]$ ss -lnpt | grep 13337
LISTEN 0      1          10.1.1.11:13337      0.0.0.0:*    users:(("python",pid=13083,fd=3))
```


## 2. User friendly

🌞 bs_client_I2.py

[bs_client_I1.py](./bs_client_I1.py)

```
[brendan@client ~]$ python bs_client_I1.py
Connecté avec succès au serveur 10.1.1.11 sur le port 13337
Que veux-tu envoyer au serveur : meo
Le serveur a répondu b'Meo a toi confrere.'

[brendan@client ~]$ python bs_client_I1.py
Connecté avec succès au serveur 10.1.1.11 sur le port 13337
Que veux-tu envoyer au serveur : waf
Le serveur a répondu b'ptdr t ki'

[brendan@client ~]$ python bs_client_I1.py
Connecté avec succès au serveur 10.1.1.11 sur le port 13337
Que veux-tu envoyer au serveur : yo
Le serveur a répondu b'Mes respects humble humain.'
```

## 3. You say client I hear control

🌞 bs_client_I3.py

[bs_client_I1.py](./bs_client_I1.py)

```
[brendan@server TP4]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('10.1.1.12', 57380).
Données reçues du client : b'meo'

[brendan@client TP4]$ python bs_client_I1.py
Connecté avec succès au serveur 10.1.1.11 sur le port 13337
Que veux-tu envoyer au serveur : meo
Le serveur a répondu b'Meo a toi confrere.'


[brendan@server TP4]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('10.1.1.12', 54318).

[brendan@client TP4]$ python bs_client_I1.py
Connecté avec succès au serveur 10.1.1.11 sur le port 13337
Que veux-tu envoyer au serveur : erfd
Il manque le mot waf ou meo
```

# II. You say dev I say good practices

## 1. Args

🌞 bs_server_II1.py

[bs_client_I1.py](./bs_server_I1.py)

```

```