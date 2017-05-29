# Etienne BOESPFLUG - 2017
#
# ScanResult.py - https://github.com/EBoespflug/port-scanner-scapy
#
# This project is part of the public domain.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE.

Unknown = 0xfff # fff is used to have the correct behavior with & masks.
Open = 0x1
Closed = 0x2
Filtered = 0x4
Error = 0x800

def to_str(value):
    '''Return the string corresponding to the passed port-result flag.'''
    if value == Unknown: return "Unknown"
    if value & Error != 0: return "Error"
    if value & Open != 0: return "Open"
    if value & Closed != 0: return "Closed"
    if value & Filtered != 0: return "Filtered"
    return "Error"

def get_result_str(value):
    '''Returns the string corresponding to the specified port-result port.'''
    result_list = []
    # Create result list.
    if value == Unknown: return to_str(Unknown)

    if value & Open != 0: result_list.append(Open)
    if value & Closed != 0: result_list.append(Closed)
    if value & Filtered != 0: result_list.append(Filtered)

    # Generate string.
    if(len(result_list) == 0):
        return "Error"
    if(len(result_list) == 1):
        return to_str(result_list[0])

    result_str = to_str(result_list[0])
    for i in range(1, len(result_list)):
        result_str += " | " + to_str(result_list[i])

    return result_str
