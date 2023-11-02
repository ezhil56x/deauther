import subprocess
import time
import sys


def scan_n(interface, ttime):
    subprocess.Popen("timeout "+str(ttime)+"s airodump-ng " + interface + " -w /tmp/scan_n &",
                     shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for i in range(ttime, -1, -1):
        print("Scanning for Wi-Fi networks... " +
              str(i) + " seconds remaining", end="\r")
        time.sleep(1)
    sys.stdout.write("\033[K")
    print("Scan completed")


def scan_ap(interface, ttime, channel, access_point):
    # timeout <ttime>s airodump-ng <interface> --channel <channel> --bssid <access point> -w /tmp/scan_ap
    subprocess.Popen("timeout "+str(ttime)+"s airodump-ng " + interface + " --channel " + channel + " --bssid " +
                     access_point + " -w /tmp/scan_ap &", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for i in range(ttime, -1, -1):
        print("Scanning for Wi-Fi networks... " +
              str(i) + " seconds remaining", end="\r")
        time.sleep(1)
    sys.stdout.write("\033[K")
    print("Scan completed")
