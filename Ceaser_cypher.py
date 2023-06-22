from characters import character, char_lenght
 
from encode import caesar

from art import logo
print(logo)
print("Hello adventurer\n")

keep_playing = True
while keep_playing :

  direction = input("Type 'symon' to encode 'seeker' to decode:\n")
  text = input("Message:\n").lower()
  shift = int(input("secret code??\n"))
  
  print(shift)

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    keep_playing = False
    print("Goodbye")
