import netifaces
import collections

def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = float(f.read()) / 1000.0
    return temp

def meminfo():
    meminfo=collections.OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

def partition():
    procfile = open("/proc/partitions")
    parts = [p.split() for p in procfile.readlines()[2:]]
    procfile.close()
    return parts

def guet_ip():
    gateways = netifaces.gateways()
    try:
        ifnet = gateways['default'][netifaces.AF_INET][1]
        return netifaces.ifaddresses(ifnet)[netifaces.AF_INET][0]['addr']
    except (KeyError, IndexError):
        return