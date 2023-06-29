from dataclasses import dataclass


@dataclass
class User:
    name: str = 'Jan'
    surname: str = 'Kowalski'
    email: str = 'mytestemail9@gmail.com'
    password: str = 'haslo'
    day: str = '1'
    month: str = '6'
    year: str = '1994'
    company: str = 'SpaceX'
    address1: str = 'Musk Street 1'
    address2: str = 'New York'
    country: str = 'United States'
    zipcode: str = '31404'
    mobile: str = '507689301'







# @dataclass
# class Password:
#     pwd: str = "secret_sauce"