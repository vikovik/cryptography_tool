"""
  The function `decoder_viginere` takes a message and a key as input and decodes the message using the
  Vigenere cipher.
  
  :param message: The `message` parameter is the encoded message that you want to decode using the
  Vigenere cipher
  :param key: The key parameter is a string that represents the keyword used for encoding and decoding
  the message
  :return: the decoded message.
"""
def decoder_viginere(message, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  key = key.lower()
  key_length = len(key)
  decoded_message = ""
  key_index = 0

  for char in message:
    decoded_char = char

    if char.isalpha():
      is_upper = char.isupper()
      char = char.lower()
      keyword_shift = alphabet.index(key[key_index % key_length])
      shift = (alphabet.index(char) + keyword_shift) % 26
      decoded_char = alphabet[shift]

      if is_upper:
        decoded_char = decoded_char.upper()

      key_index += 1

    decoded_message += decoded_char

  return decoded_message

"""
  The function `encoder_viginere` takes a message and a key as input and encodes the message using the
  Vigenere cipher.
  
  :param message: The message parameter is the text that you want to encode using the Vigenere cipher.
  It can be any string of characters
  :param key: The key parameter is a string that represents the keyword used for encoding the message
  :return: the encoded message.
"""
def encoder_viginere(message, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  key = key.lower()
  key_length = len(key)
  encoded_message = ""
  key_index = 0

  for char in message:
    encoded_char = char

    if char.isalpha():
      is_upper = char.isupper()
      char = char.lower()
      keyword_shift = alphabet.index(key[key_index % key_length])
      shift = (alphabet.index(char) - keyword_shift) % 26
      encoded_char = alphabet[shift]

      if is_upper:
        encoded_char = encoded_char.upper()

      key_index += 1

    encoded_message += encoded_char

  return encoded_message