#!/usr/bin/env python3

import json
import os
import yaml


def gen_page(device: str):
    with open(f"_data/devices/{device}.yml", 'r') as deviceYaml:
        deviceData = yaml.safe_load(deviceYaml)

    with open(f"ota/{device}", 'r') as buildJson:
        buildData = json.load(buildJson)

    # Initialize downloads section
    deviceData['downloads'] = {}

    for build in buildData["response"]:
        # Initialize download item
        deviceData['downloads'][build['filename']] = {}
        deviceData['downloads'][build['filename']]['url'] = build['url']

    # Reverse sort this so that the latest link is the first one
    deviceData['downloads'] = dict(sorted(deviceData['downloads'].items(), reverse=True))

    # Rewrite page front matter
    # That's the only thing on this file anyway
    with open(f'_device/{device}.md', 'w') as devicePage:
        devicePage.write('---\n')
        yaml.dump(deviceData, devicePage, sort_keys=False)
        devicePage.write('---')


if __name__ == "__main__":
    for i in os.listdir('_data/devices/'):
        device = i.replace('.yml', '')
        print(f"Generating {device} page...")
        gen_page(device)
