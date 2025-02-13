import re


def search_ip_address(text: str) -> list[str]:
    """
    Search ip addresses in text.
    :param text:
    :return:
    """
    pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
    valid_ip_addresses = []
    ip_address_list = re.findall(pattern, text)
    for ip_address in ip_address_list:
        ip_address_groups = re.split(r"\D", ip_address)
        try:
            for ip_address_group in ip_address_groups:
                if int(ip_address_group) > 255:
                    raise ValueError
            valid_ip_addresses.append(ip_address)
        except ValueError:
            continue
    return valid_ip_addresses


if __name__ == '__main__':
    print(search_ip_address('Test Ip address 172.16.31.10 and other wrong: 172.777.31.10'))  # ['172.16.31.10]
