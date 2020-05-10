#!/usr/bin/env python3

# New file
# added new comment
import sys
import os

def check_reboot():
    """ Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    else:
        print("All ok, oh nee toch niet")
        sys.exit(0)

main()
