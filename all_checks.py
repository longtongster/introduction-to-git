#!/usr/bin/env python3

# New file

import sys

def check_reboot():
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    else:
        print("All ok")
        sys.exit(0)

main()
