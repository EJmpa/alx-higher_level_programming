#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            if len(split_line) > 2:
                try:
                    status_code = int(split_line[-2])
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    total_size += int(split_line[-1])
                except ValueError:
                    pass

            if count % 10 == 0:
                print("File size: {}".format(total_size))
                for key in sorted(status_codes.keys()):
                    if status_codes[key] > 0:
                        print("{}: {}".format(key, status_codes[key]))

    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key] > 0:
                print("{}: {}".format(key, status_codes[key]))
        sys.exit(0)
