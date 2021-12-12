alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
def caesar(cipher_direction, input_text, shift_amount):
  output = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in input_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_pos = position + shift_amount
      output += alphabet[new_pos]
    else:
      output += char
  print(f"The {cipher_direction}d text is: {output}")


continue_cipher = True

while continue_cipher:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  caesar(direction,text,shift)
  
  restart = input("Would you like to try again? [y/n]\n")
  if restart == "n":
    continue_cipher = False
    print("Bye.")
  
