#!/usr/bin/python3

"""
this script reads <stdin> line by line and computes metrics
"""
import sys
import signal

total_size = 0
status_codes = {}


def print_stats(signum=None, frame=None):
    """
    method definition to print metrics
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


signal.signal(signal.SIGINT, print_stats)

count = 0
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9 or parts[-2] not in [
                "200",
                "301",
                "400",
                "401",
                "403",
                "404",
                "405",
                "500"
                ]:
            continue
        count += 1
        total_size += int(parts[-1])
        status_codes[parts[-2]] = status_codes.get(parts[-2], 0) + 1

        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
