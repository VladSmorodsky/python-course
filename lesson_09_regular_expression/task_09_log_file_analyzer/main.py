from IPAddressPicker import IPAddressPicker

if __name__ == '__main__':
    ip_address_picker = IPAddressPicker()
    with open('log.txt', 'r') as file:
        for line in file:
            ip_address_picker.pick_ip_address(line)

    print(ip_address_picker.get_statistics())
