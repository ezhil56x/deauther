import csv
import subprocess

def list_aps():
  command = 'ls /tmp | grep "scan_n" | grep "[0-9].csv" | tail -n 1'
  file = subprocess.getoutput(command)
  file_path = "/tmp/" + file

  with open(file_path) as my_file:
    reader = csv.reader(my_file, delimiter=',')
        # print the column names BSSID, Channel, ESSID
    print("")
    print("\t\tAvailable Wi-Fi Networks")
    print("")
    print(60 * "-")
    print("No.\t\tBSSID\t\tChannel\t\tName")
    print(60 * "-")

    for _ in range(3):
      next(reader)

    row_number = 1

    for row in reader:
      if not any(row):
        break
      if len(row) >= 14:
        print(f"{row_number}\t{row[0]}\t{row[3]}\t{row[13]}")
        row_number += 1