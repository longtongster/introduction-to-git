
# added new comment
import sys
import os

def check_reboot():
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    else:
        print("All ok, oh nee toch niet")
        sys.exit(0)

main()
