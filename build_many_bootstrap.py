#!/usr/bin/env python3
import os

with open('bootstrap_data.csv', 'r') as data_file:
    for d in data_file:
        if '#' in d:
            print('Skipping comment')
            continue
        d_fields = d.strip().split(',')
        hostname = d_fields[0]
        tpl_name = d_fields[1]
        dg_name = d_fields[2]
        auth_code = d_fields[3]
        payload = f'{{"archive_type": "iso", "hostname": "{hostname}", "tpl_name":"{tpl_name}",' \
                  f'"dg_namne":"{dg_name}", "panorama_server": "10.10.10.10", "auth_code": "{auth_code}"}}'
        print(
            f"curl -X POST -d '{payload}'  -H \"Content-Type: application/json\" "
            f" http://localhost:5001/generate_bootstrap_package -o {hostname}.iso")
        os.system(
            f"curl -X POST -d '{payload}'  -H \"Content-Type: application/json\"  "
            f"http://localhost:5001/generate_bootstrap_package -o {hostname}.iso")
