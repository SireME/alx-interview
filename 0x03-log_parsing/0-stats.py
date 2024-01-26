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
    while True:
        line = input()
        ip = r"\d+\.\d+\.\d+\.\d+|\w+"
        rq = "GET /projects/260 HTTP/1.1"
        p = rf'^({ip})\s?-\s?\[([^\]]+)\] "{rq}" (\d+|\w+) (\d+)$'
        pattern = p
        match = re.match(pattern, line)

        if match:
            # track number of lines
            line_num += 1
            # necessary data
            try:
                status_code = int(match.group(3))
            except ValueError:
                status_code = ""
            try:
                file_size = int(match.group(4))
            except Exception:
                file_size = 0

            # compute umber of occurrences of status codes
            if status_code in statuscode_dic and type(status_code) == int:
                statuscode_dic[status_code] += 1
            elif type(status_code) == int:
                statuscode_dic[status_code] = 1

            # compute total file size per line
            total_size += file_size

            if line_num % 10 == 0:
                print(f"File size: {total_size}", flush=True)
                sorted_dic = dict(sorted(statuscode_dic.items()))
                for key, value in sorted_dic.items():
                    try:
                        print(f"{int(key)}: {value}")
                    except Exception:
                        pass

except Exception:
    print(f"File size: {total_size}", flush=True)
    sorted_dic = dict(sorted(statuscode_dic.items()))
    for key, value in sorted_dic.items():
        print(f"{key}: {value}")
