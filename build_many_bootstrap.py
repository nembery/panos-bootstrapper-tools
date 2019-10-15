#!/usr/bin/env python3
# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Nathan Embery nembery@paloaltonetworks.com
#
#  Read a comma separated value file and create any number of bootstrap archives
#  Currently, the following format is expected
#
#  # hostname, tpl_name, dg_name, auth_code
#
#  adding more fields is easy to do. See here for more examples of how to build the API payload:
#  https://panos-bootstrapper.readthedocs.io/en/latest/usage.html
#
#
import os

# open the datafile for reading
with open('bootstrap_data.csv', 'r') as data_file:
    # iterate over each line in the file
    for d in data_file:
        # ignore comments
        if '#' in d:
            print('Skipping comment')
            continue
        # remove trailing newlines and split into an array on the ','
        d_fields = d.strip().split(',')
        # customize these fields based on your csv layout
        hostname = d_fields[0]
        tpl_name = d_fields[1]
        dg_name = d_fields[2]
        auth_code = d_fields[3]
        # build the payload appropriately
        payload = f'{{"archive_type": "iso", "hostname": "{hostname}", "tpl_name":"{tpl_name}",' \
                  f'"dg_namne":"{dg_name}", "panorama_server": "10.10.10.10", "auth_code": "{auth_code}"}}'
        # print it out just to show what is gonna happen
        print(
            f"curl -X POST -d '{payload}'  -H \"Content-Type: application/json\" "
            f" http://localhost:5001/generate_bootstrap_package -o {hostname}.iso")
        # now shell out the command and issue the command
        os.system(
            f"curl -X POST -d '{payload}'  -H \"Content-Type: application/json\"  "
            f"http://localhost:5001/generate_bootstrap_package -o {hostname}.iso")
