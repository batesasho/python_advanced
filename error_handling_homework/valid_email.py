class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == 'End':
        break
    mail_address_list = command.split("@")
    if len(mail_address_list) == 1:
        raise MustContainAtSymbolError("Email must contain @")
    email_name = mail_address_list[0]
    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if not len(mail_address_list[-1]) < 2:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    domain = "."+mail_address_list[1].split('.')[-1]
    if domain not in ('.com', '.bg' '.net', '.org'):
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')

