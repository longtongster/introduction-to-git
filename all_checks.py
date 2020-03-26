#!/usr/bin/env python3

# New file

def check_reboot():
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
    else:
        print("All ok")

main()
