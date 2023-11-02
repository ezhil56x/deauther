import csv
import subprocess

def list_clients():
    command = 'ls /tmp | grep "scan_ap" | grep "[0-9].csv" | tail -n 1'
    file = subprocess.getoutput(command)
    file_path = "/tmp/" + file

    with open(file_path) as my_file:
        reader = csv.reader(my_file, delimiter=',')

        # Print the column names BSSID, Channel, ESSID
        print("\n\t\tAvailable Clients\n")
        print(55 * "-")
        print("No.\t\tBSSID\t\t\tESSID")
        print(55 * "-")

        rowcount = 1

        # for row in reader: start from row 6
        for _ in range(5):
            next(reader)

        for row in reader:
            if len(row) == 7:
                print(f"{rowcount}\t{row[5]}\t{row[0]}")
                rowcount += 1
