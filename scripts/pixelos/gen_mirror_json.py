#!/usr/bin/env python3

#
# Copyright (C) 2017-2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from __future__ import print_function
import errno
import hashlib
import json
import os
import re
import sys
import zipfile

from datetime import datetime
from time import mktime

def gen_json(FILE_BASE: str, URL_BASE: str):
    builds = {}

    for f in [os.path.join(dp, f) for dp, dn, fn in os.walk(FILE_BASE) for f in fn]:
        data = open(f, 'rb')
        filename = f.split('/')[-1]
        # PixelOS_joan-15.0-20250218-1047.zip
        device, version, builddate, buildtime, *_ = os.path.splitext(filename)[0].replace("PixelOS_", "").split('-')
        version = version.split('.')[0]
        print('hashing sha256 for {}'.format(filename), file=sys.stderr)
        sha256 = hashlib.sha256()
        for buf in iter(lambda: data.read(128 * 1024), b''):
            sha256.update(buf)

            try:
                with zipfile.ZipFile(f'{FILE_BASE}/{filename}', 'r') as update_zip:
                    build_prop = update_zip.read('META-INF/com/android/metadata').decode('utf-8')
                    timestamp = (re.findall('post-timestamp=([0-9]+)', build_prop)[0])
            except Exception as e:
                print(e)
                timestamp = int(mktime(datetime.strptime(builddate, '%Y%m%d').timetuple()))

        builds.setdefault("response", []).append({
            'id': sha256.hexdigest(),
            'size': os.path.getsize(f),
            'datetime': timestamp,
            'filename': filename,
            'url': f.replace(FILE_BASE, URL_BASE),
            'version': version
        })
    if builds:
        builds["response"] = sorted(builds["response"], key=lambda x: x['datetime'])
    return builds


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage python3 {sys.argv[0]} /path/to/mirror/base/url [URL of mirror]")
        sys.exit(errno.EINVAL)

    FILE_BASE = sys.argv[1]
    URL_BASE = sys.argv[2] if len(sys.argv) >= 3 else ''

    for device in os.listdir(FILE_BASE):
        otaData = gen_json(f"{FILE_BASE}/{device}", f"{URL_BASE}/{device}" if URL_BASE else '')
        if otaData:
            try:
                os.mkdir("ota/pixelos")
            except FileExistsError:
                pass
            with open(f"ota/pixelos/{device}", 'w') as otafile:
                json.dump(otaData, otafile, sort_keys=True, indent=4)
