from characters import character

def caesar(start_text, shift_amount, cipher_direction):
  shift_amount = shift_amount % 26
  end_text = ""
  if cipher_direction == "seeker": 
    print("Hello seeker what truth we seeking today\n")
    shift_amount *= -1
    
  for char in start_text:

    if char in character:
      position = character.index(char)
      new_position = (position + shift_amount) % 27
      end_text += character[new_position]
  if cipher_direction == "seeker":
    print(f"symon says:{end_text}")
  else: print(end_text)
