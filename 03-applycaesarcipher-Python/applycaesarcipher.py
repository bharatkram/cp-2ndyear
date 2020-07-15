# A Caesar Cipher is a simple cipher that works by shifting each letter in
# the given message by a certain number. For example, if we shift the message
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given
# message by shift letters. You are guaranteed that message is a string, and
# that shift is an integer between -25 and 25. Capital letters should stay capital
# and lowercase letters should stay lowercase, and non-letter characters should not be changed.
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def applyCaesarCipher(char, shift):
    ele = ord(char)
    if 65 <= ele <= 90:
        ele += shift
        return chr(ele + 26) if ele < 65 else chr(ele - 26) if ele > 90 else chr(ele)
    elif 97 <= ele <= 122:
        ele += shift
        return chr(ele + 26) if ele < 97 else chr(ele - 26) if ele > 122 else chr(ele)
    else:
        return chr(char)


def fun_applycaesarcipher(msg, shift):
    # your code goes here
    return "".join([applyCaesarCipher(char, shift) for char in msg])
