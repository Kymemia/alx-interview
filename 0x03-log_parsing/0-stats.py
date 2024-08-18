#!/usr/bin/env python3

"""
This script reads <stdin> line by line and computes metrics
"""
import sys
import signal


total_size = 0
status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

count = 0


def print_stats(signum=None, frame=None):
    """
    method definition
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

    if signum is not None:
        sys.exit(0)


signal.signal(signal.SIGINT, print_stats)

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        if len(parts) < 7:
            continue

        file_size = int(parts[-1])
        total_size += file_size

        status_code = parts[-2]

        if status_code in status_codes:
            status_codes[status_code] += 1

        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
