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

## Results Example

```
Found ### CloudFront IPv4 ranges.
120.52.22.96/27
205.251.249.0/24
180.163.57.128/26
204.246.168.0/22
111.13.171.128/26
18.160.0.0/15
205.251.252.0/23
54.192.0.0/16
204.246.173.0/24
54.230.200.0/21
120.253.240.192/26
116.129.226.128/26
130.176.0.0/17
108.156.0.0/14
44.234.90.252/30
-- More --

Found ## CloudFront IPv6 IP ranges.
2600:9000:3000::/36
2600:9000:f600::/39
2600:9000:f540::/42
2409:8c00:2421:300::/56
2600:9000:f000::/38
2600:9000:f500::/43
-- More --
```
