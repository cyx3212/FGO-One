from interface.interface import *
from recovery.recover import *
from config import recovery_times

times = recovery_times

while times >= 0:
    recognize()
    ap = recover_ap()
    if ap == 1 and times != 0:
        continue
    elif ap == 1 and times == 0:
        break
    elif ap == 2:
        times = times - 1
