import re

PATTERN = re.compile(r'(?P<remote_addr>[0-9.\S]+)'
                     r'\s-\s-\s\['
                     r'(?P<request_datetime>[0-9a-zA-Z/:+\s]+)'
                     r'\]\s"'
                     r'(?P<request_type>[A-Z]+)\s'
                     r'(?P<requested_resource>[a-zA-Z0-9/_]+)'
                     r'\s\w+/[\d.]+"\s'
                     r'(?P<response_code>[\d]+)\s'
                     r'(?P<response_size>[\d]+)')

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        result = PATTERN.findall(line)
        if result:
            print(tuple(result)[0])
