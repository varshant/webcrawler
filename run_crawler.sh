#!/bin/bash

# Read domains from the file and run Scrapy
domains=$(paste -s -d, data/domains.txt)

# Use full Python and Scrapy paths to avoid issues
/usr/bin/env python3 -m scrapy runspider crawler/spiders/product_spider.py -a domains="$domains" -o data/output.json

# Convert output to CSV
/usr/bin/env python3 scripts/convert_to_csv.py
