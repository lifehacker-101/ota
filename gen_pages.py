#!/usr/bin/env python3

import json
import os
import yaml


def byteCount(bytes: int) -> str:
	"""Converts an int number of bytes to a str with the largest appropriate unit"""

	if bytes == 1:
		return "1 Byte"
	elif bytes < (1 << 10):
		return f"{bytes} Bytes"
	elif bytes < (1 << 20):
		return f"{bytes // (1 << 10)} KiB"
	elif bytes < (1 << 30):
		return f"{bytes // (1 << 20)} MiB"
	else:
		return f"{bytes // (1 << 30)} GiB"


def gen_page(device: str):
    deviceData = {}
    with open(f"_data/devices/{device}.yml", 'r') as deviceYaml:
        deviceData = yaml.safe_load(deviceYaml)

    buildData = {}
    try:
        with open(f"ota/{device}", 'r') as buildJson:
            buildData = json.load(buildJson)
    except FileNotFoundError:
        pass

    # Initialize downloads section
    deviceData['downloads'] = {}

    if buildData:
        for build in buildData["response"]:
            # Initialize download item
            deviceData['downloads'][build['filename']] = {}
            deviceData['downloads'][build['filename']]['url'] = build['url']
            deviceData['downloads'][build['filename']]['size'] = build['size']
            deviceData['downloads'][build['filename']]['size_str'] = byteCount(build['size'])

    if deviceData['downloads']:
        # Reverse sort this so that the latest link is the first one
        deviceData['downloads'] = dict(sorted(deviceData['downloads'].items(), reverse=True))
    else:
        deviceData.pop('downloads')

    # Rewrite page front matter
    # That's the only thing on this file anyway
    with open(f'_device/{device}.md', 'w') as devicePage:
        devicePage.write('---\n')
        yaml.dump(deviceData, devicePage, sort_keys=False)
        devicePage.write('---')
        devicePage.write('\n\n')
        try:
            with open(f'_instructions/{device}.md', 'r') as deviceInstructions:
                devicePage.write('## Installation Instrutions\n\n')
                devicePage.write(deviceInstructions.read())
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    for i in os.listdir('_data/devices/'):
        device = i.replace('.yml', '')
        print(f"Generating {device} page...")
        gen_page(device)
