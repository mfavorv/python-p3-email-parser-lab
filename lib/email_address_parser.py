# your code goes here!
import re 
class EmailAddressParser:

    def __init__(self, addresses):
        self.addresses = addresses
    
    def parse(self):
        emails = []
        pattern = r"[,\s]+"
        individual_addresses = re.split(pattern, self.addresses)
        individual_addresses = [address for address in individual_addresses if address]
        email_address = r"^[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        for email in individual_addresses:
            if re.fullmatch(email_address, email):
                emails.append(email)
        unique_addresses = set(emails)
        sorted_addresses = sorted(unique_addresses)
        return sorted_addresses
