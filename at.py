"""
Filename: at.py
Author: Open Risk
Date: 11 09 2025
Version: 0.2
Description: This script converts a bluesky follow list into an OPML file for use with an RSS reader
License: GPL
Contact: info@openriskmanagement.com
"""

from atproto import CAR, IdResolver
import xml.etree.ElementTree as ET

# Load and parse the saved CAR file
# https://atproto.blue/en/latest/atproto_core/car.html
# https://davepeck.org/notes/bluesky/converting-between-dids-and-bluesky-handles-with-python/

with open('data/repo.car', 'rb') as f:
    car = CAR.from_bytes(f.read())

print('repo.car parsed ok')

# Convert the "follow" records into RSS urls
follows = {}
resolver = IdResolver()
count = 0
for cid in car.blocks:
    record = car.blocks.get(cid)
    if '$type' in record.keys():
        if record['$type'] == 'app.bsky.graph.follow':
            did = record['subject']
            did_doc = resolver.did.resolve(did)
            name = did_doc.model_dump()['also_known_as'][0][5:]
            rss = 'https://bsky.app/profile/' + record['subject'] + '/rss'
            follows[name] = rss
            count += 1

print('Found ', count, ' follows')

# Write out the list as OPML
title = "AtProto Follow RSS List"
description = "For use in any standard RSS reader"
opml = ET.Element("opml", version="2.0")
head = ET.SubElement(opml, "head")
ET.SubElement(head, "description").text = description
ET.SubElement(head, "title").text = title
body = ET.SubElement(opml, "body")

for key, value in follows.items():
    outline = ET.SubElement(body, "outline", text=key, xmlUrl=value, htmlUrl=value, description=key)

tree = ET.ElementTree(opml)
with open("data/bluesky_feeds.opml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)
