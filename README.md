# AWS CloudFront IP Ranges

A simple Python script for fetching and parsing AWS IP ranges, specifically focusing on CloudFront services. It leverages the AWS `ip-ranges.json` data to extract IPv4 and IPv6 ranges associated with CloudFront, helping users to programmatically access and utilize this information for various purposes such as updating firewall rules, network monitoring, and security configurations

## Features

- Fetch AWS IP ranges from the official AWS `ip-ranges.json` URL.
- Filter and extract CloudFront-related IP ranges (both IPv4 and IPv6).
- Easy to integrate with other Python scripts or projects.

## Installation

This project uses Poetry for dependency management. If you do not have Poetry installed, please follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install it.

```bash
poetry install
```

## Running the Script

```bash
poetry run python aws_cloudfront_ip_ranges/aws_cloudfront_ip_ranges.py
```

## One liner with curl + jq

If you want a quick and easy way to retrieve the CloudFront or any other service ip address, simply use curl to download the file and then parse the data using `jq`.

### Get IPv4 CloudFront Addresses

```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | select(.service == "CLOUDFRONT") | .ip_prefix'
```

### Get IPv6 CloudFront Addresses

```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.ipv6_prefixes[] | select(.service == "CLOUDFRONT") | .ipv6_prefix'
```
