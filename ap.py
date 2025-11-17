#!/usr/bin/env python3

"""
Filename: ap.py
Author: Open Risk
Date: 11 09 2025
Version: 0.2
Description: This script converts a mastodon follow list into an OPML file for use with an RSS reader
License: GPL
Contact: info@openriskmanagement.com
"""

import csv
import datetime
import xml.etree.ElementTree as ET

# Load and parse the saved CSV file
follows = {}
with open('data/following_accounts.csv') as f:
    next(f, None)
    reader = csv.reader(f)
    for row in reader:
        name = row[0].split('@')[0]
        server = row[0].split('@')[1]
        rss = 'https://' + server + '/@' + name + '.rss'
        follows[name] = [server, rss]

# Write out the list as OPML
title = "Mastodon Follow RSS List"
description = "For use in any standard RSS reader"
opml = ET.Element("opml", version="2.0")
head = ET.SubElement(opml, "head")
ET.SubElement(head, "title").text = title
ET.SubElement(head, "description").text = description
now = datetime.datetime.now()
ET.SubElement(head, "dateCreated").text = now.isoformat()
ET.SubElement(head, "ownerName").text = "Private"
body = ET.SubElement(opml, "body")

for key, value in follows.items():
    outline = ET.SubElement(body, "outline", text=key, xmlUrl=value[1], htmlUrl=value[1], description=value[0])

tree = ET.ElementTree(opml)
with open("data/mastodon_feeds.opml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)