import phonenumbers
from phonenumbers import geocoder


num1 = phonenumbers.parse( input(" Enter Phone Number :   "))
print(geocoder.description_for_number(num1, 'en'))
