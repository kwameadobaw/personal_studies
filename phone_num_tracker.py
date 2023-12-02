#!/usr/bin/python3

import phonenumbers
from phonenumbers import geocoder

phone_number_str = input("Enter the phone number with country code: ")
phone_number = phonenumbers.parse(phone_number_str)

print(geocoder.description_for_number(phone_number, 'en'))
