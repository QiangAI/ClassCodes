# coding=utf-8
from psutil import net_if_addrs
from psutil import net_if_stats
from psutil import net_io_counters

result = net_if_addrs().items()
for key, value in result:
    print(key)
    for v in value:
        print('\t', v.family)
        print('\t', v.address)
        print('\t', v.netmask)
        print('\t', v.broadcast)

for key, value in net_if_stats().items():
    print(key)
    print("\t", value)

print(net_io_counters().bytes_sent)
print(net_io_counters().bytes_recv)
