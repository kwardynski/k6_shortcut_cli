#!/usr/bin/env python3
import sys
from shortcut_mappings import shortcut_mappings as sm

# Minimum buffer between shortcut function and key mapping
disp_buffer = 3

# Displays ALL Keychron K6 shortcut mappings
def display_all():
    longest_key_length = len(max(sm.keys(), key=len))

    for kvp in sm:
        buffer = longest_key_length - len(kvp) + disp_buffer
        print(f"   {kvp}{'.'*buffer}{sm[kvp]}")


# Displays an individual Keychron K6 shortcut mapping based on function name
# Will warn if function does not exist 
def display_indiv(shortcut):
    if shortcut in sm.keys():
        print(f"   {shortcut}: {sm[shortcut]}")
    else:
        print(f"   !! Shortcut \"{shortcut}\" not found !!")


if __name__ == '__main__':
    print("== Keychron K6 Shortcut Mappings ==\n")

    args = sys.argv
    if len(args) > 2:
        print("Just one argument is fine, thanks...")
    elif len(args) == 1:
        display_all()
    else:
        display_indiv(args[1])

    print("")

