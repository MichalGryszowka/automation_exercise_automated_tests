from dataclasses import dataclass


@dataclass
class User:
    name: str = 'Tomasz'
    surname: str = 'Kowalski'
    email: str = 'mytestemail10@gmail.com'
    existing_email:  str = 'existingemail@gmail.com'
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
    subject: str = 'technical error'
    message: str = '''I can't add one of the product to the basket'''
    screenshot_path: str = 'C:/Users/HP/PycharmProjects/AutomationExercise/files/error_screenshot.png'
    product_name: str = 'Blue Top'
    card_number: str = '6666 0000 9999 1111'
    cvc: str = '567'
    exp_month: str = '12'
    exp_year: str = '2023'

