#!/usr/bin/python3
"""
This is a script that reads stdin
line by line and computes metrics
"""
import sys
import re

line_num = 0
statuscode_dic = {}
total_size = 0

try:
    for line in sys.stdin:
        rq = "GET /projects/260 HTTP/1.1"
        pattern = rf'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "{rq}" (\d+) (\d+)$'
        match = re.match(pattern, line)

        if match:
            # track number of lines
            line_num += 1
            # necessary data
            ip_address = match.group(1)
            date = match.group(2)
            try:
                status_code = int(match.group(3))
            except ValueError:
                status_code = ""
            file_size = int(match.group(4))

            # compute number of occurrences of status codes
            if status_code in statuscode_dic:
                statuscode_dic[status_code] += 1
            else:
                statuscode_dic[status_code] = 1

            # compute total file size per line
            total_size += file_size

        if line_num % 10 == 0:
            print(f"File size: {total_size}")
            sorted_dic = dict(sorted(statuscode_dic.items()))
            for key, value in sorted_dic.items():
                print(f"{key}: {value}")

            # reset values back for the next log group
            line_num = 0

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    sorted_dic = dict(sorted(statuscode_dic.items()))
    for key, value in sorted_dic.items():
        print(f"{key}: {value}")
