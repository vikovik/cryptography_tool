"""
  The function `decoder_cesar` takes a message and an offset as input and returns the decoded message
  by shifting each letter in the message by the given offset using the Caesar cipher.
  
  :param message: The "message" parameter is a string that represents the message that needs to be
  decoded. It can contain both letters and non-letter characters
  :param offset: The offset parameter in the decoder_cesar function is an integer that represents the
  number of positions to shift each character in the message
  :return: the decoded message.
"""
def decoder_cesar(message, offset):
  decoded_message = ""

  for char in message:
    decoded_char = ''

    if char.isalpha():
      is_uppercase = char.isupper()
      char = char.lower()
      decoded_char = chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))

      if is_uppercase:
        decoded_char = decoded_char.upper()

    else:
      decoded_char = char

    decoded_message += decoded_char

  return decoded_message

"""
  The function `encoder_cesar` takes a message and an offset as input and returns the message encoded
  using the Caesar cipher with the given offset.
  
  :param message: The message parameter is a string that represents the message that you want to
  encode using the Caesar cipher
  :param offset: The offset parameter is an integer that determines how much each character in the
  message should be shifted in the Caesar cipher. A positive offset value will shift the characters to
  the right, while a negative offset value will shift the characters to the left
  :return: the encoded message.
"""
def encoder_cesar(message, offset):
  encoded_message = ""

  for char in message:
    encoded_char = ''

    if char.isalpha():
      is_uppercase = char.isupper()
      char = char.lower()
      encoded_char = chr(((ord(char) - ord('a') - offset) % 26) + ord('a'))

      if is_uppercase:
        encoded_char = encoded_char.upper()

    else:
      encoded_char = char

    encoded_message += encoded_char

  return encoded_message