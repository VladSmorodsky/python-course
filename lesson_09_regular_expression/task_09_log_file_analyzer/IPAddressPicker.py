import re


class IPAddressPicker:
    """
    Used for retrieving storing IPv4 addresses from text.
    """
    __ip_addresses: dict[str, int] = {}

    def pick_ip_address(self, text_line: str) -> None:
        """
        Pick IP address from text line.
        :param text_line:
        :return:
        """
        pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
        ip_address_list = re.findall(pattern, text_line)
        for ip_address in ip_address_list:
            ip_address_groups = re.split(r"\D", ip_address)
            try:
                for ip_address_group in ip_address_groups:
                    if int(ip_address_group) > 255:
                        raise ValueError
                if ip_address in self.__ip_addresses:
                    self.__ip_addresses[ip_address] += 1
                    continue
                self.__ip_addresses[ip_address] = 1
            except ValueError:
                continue

    def get_statistics(self) -> str:
        """
        Get dictionary of IP addresses as a key and number of occurrences as value.
        :return:
        """
        statistics_message = 'IP addresses requests count: \n'
        for ip_address in self.__ip_addresses:
            statistics_message += f'IP: {ip_address}, Count: {self.__ip_addresses[ip_address]}\n'
        return statistics_message
