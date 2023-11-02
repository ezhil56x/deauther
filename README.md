# Deauther

## Disclaimer ⚠️

This tool is provided for educational purposes only. It should not be used for illegal activities. Only use it for legitimate penetration testing and security research purposes and network devices that you own or have permission to test. By using this tool, you agree that you will not engage in any unauthorized or illegal activities with it. You understand that the misuse of this tool may violate laws and regulations and can lead to severe legal consequences, including criminal charges and penalties. The author of this tool shall not be held responsible for any damages or liabilities caused by the use or misuse of this tool. Use this tool at your own risk and with proper authorization. Ensure compliance with applicable laws and obtain necessary permissions before using it.

## Introduction

Deauther is a command-line utility designed for educational purposes, allowing you to perform various actions related to Wi-Fi networks. This tool is intended for legitimate penetration testing, security research purposes, and network devices that you own or have permission to test.

## Pre-requisites

- Linux Environment
- [Python 3](https://www.python.org/downloads/)
- [Aircrack-ng](https://www.aircrack-ng.org/downloads.html)

## Installation

1. Clone the repository

```
git clone https://github.com/ezhil56x/deauther.git
```

2. Move the repository

```
sudo mv deauther /opt
```

3. Create a symbolic link

```
sudo ln -s /opt/deauther/deauther /usr/local/bin/deauther
```

4. Make the tool executable

```
sudo chmod +x /opt/deauther/deauther
```

## Options

| Option                          | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| `-h` or `--help`                | Show help message and exit                      |
| `--mode=<mode> `                | Specify the mode to use                         |
| `--interface=<interface>`       | Specify the Wi-Fi interface                     |
| `--time=<time>`                 | Specify the time you want to scan               |
| `--channel=<channel>`           | Specify the channel number of the Wi-Fi network |
| `--access-point=<access-point>` | Specify the access point MAC to use             |
| `--client=<client>`             | Specify the client MAC to use                   |
| `--number=<number>`             | Specify the number to packets to send           |

## Modes of Operation

| Mode            | Description                                           |
| --------------- | ----------------------------------------------------- |
| `scan_wns`      | Scan for Wi-Fi networks                               |
| `list_aps`      | List available Wi-Fi networks                         |
| `scan_ap`       | Scan for clients connected to a Wi-Fi network         |
| `list_clients`  | List clients connected to a Wi-Fi network             |
| `deauth_all`    | Deauthenticate all clients from a Wi-Fi network       |
| `deauth_client` | Deauthenticate a specific client from a Wi-Fi network |

## Usage

### Scan Wi-Fi networks

```
sudo deauther --mode=scan_wns --interface=wlan0 --time=120
```

### List available Wi-Fi networks

```
sudo deauther --mode=list_aps
```

### Scan a Wi-Fi network for clients

```
sudo deauther --mode=scan_ap --interface=wlan0 --channel=6 --access-point=FF:FF:FF:FF:FF:FF --time=120
```

### List clients connected to a Wi-Fi network

```
sudo deauther --mode=list_clients
```

### Deauthenticate all clients from a Wi-Fi network

```
sudo deauther --mode=deauth_all --interface=wlan0 --access-point=FF:FF:FF:FF:FF:FF --number=10000
```

### Deauthenticate a specific client from a Wi-Fi network

```
sudo deauther --mode=deauth_client --interface=wlan0 --access-point=FF:FF:FF:FF:FF:FF --client=FF:FF:FF:FF:FF:FF --number=10000
```

## License

This tool is licensed under the [MIT License](https://github.com/ezhil56x/deauther/blob/main/LICENSE)
