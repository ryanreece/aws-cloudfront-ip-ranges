import requests


AWS_IP_RANGES_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"


def fetch_aws_ip_ranges():
    """
    Fetches the AWS IP ranges from the AWS_IP_RANGES_URL and returns them as a
    dictionary.

    This function sends a GET request to the AWS IP ranges URL and parses the
    JSON response into a Python dictionary. The dictionary typically contains
    keys such as 'syncToken', 'createDate', 'prefixes', and 'ipv6_prefixes',
    among others, depending on the API response structure.

    Returns:
        dict: A dictionary containing the parsed JSON payload from the AWS IP
              ranges API response. The structure includes information about
              IPv4 and IPv6 prefixes, regions, and services.

    Raises:
        requests.exceptions.HTTPError: If response status code is 4XX or 5XX.
    """

    response = requests.get(AWS_IP_RANGES_URL)
    response.raise_for_status()  # Raises HTTPError for bad responses

    return response.json()


def parse_cloudfront_ip_ranges(aws_ip_ranges_json):
    """
    Parses the provided JSON payload to extract CloudFront IP ranges,
    including both IPv4 and IPv6 addresses.

    This function filters the AWS IP ranges JSON data to find entries
    that are specifically for the CloudFront service. It separately
    collects IPv4 and IPv6 CloudFront IP ranges based on the 'service'
    key in each entry.

    Args:
        aws_ip_ranges_json (dict): A dictionary representing the JSON payload
        from the AWS IP ranges API. This dictionary should contain keys like
        'prefixes' for IPv4 addresses and 'ipv6_prefixes' for IPv6 addresses,
        each with a list of dictionaries detailing the IP ranges.

    Returns:
        tuple of (list, list): A tuple containing two lists. The first list
        contains dictionaries of CloudFront IPv4 IP ranges, and the second
        list contains dictionaries of CloudFront IPv6 IP ranges. Each
        dictionary in the lists includes details such as the IP prefix, region,
        and service.
    """

    cloudfront_ipv4_ips = [entry for entry in
                           aws_ip_ranges_json['prefixes']
                           if entry['service'] == 'CLOUDFRONT']

    cloudfront_ipv6_ips = [entry for entry in
                           aws_ip_ranges_json['ipv6_prefixes']
                           if entry['service'] == 'CLOUDFRONT']

    return cloudfront_ipv4_ips, cloudfront_ipv6_ips


if __name__ == "__main__":
    aws_ip_ranges_json = fetch_aws_ip_ranges()

    cloudfront_ip_ranges = parse_cloudfront_ip_ranges(aws_ip_ranges_json)
    cloudfront_ipv4_ips, cloudfront_ipv6_ips = cloudfront_ip_ranges

    print(f"Found {len(cloudfront_ipv4_ips)} CloudFront IPv4 ranges.")
    for ip_range in cloudfront_ipv4_ips:
        print(ip_range['ip_prefix'])

    print(f"\nFound {len(cloudfront_ipv6_ips)} CloudFront IPv6 IP ranges.")
    for ip_range in cloudfront_ipv6_ips:
        print(ip_range['ipv6_prefix'])
