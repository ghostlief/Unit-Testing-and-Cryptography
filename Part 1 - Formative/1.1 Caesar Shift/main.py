# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_str = ""
    for let in text:
        index = alpha.index(let)
        new_str += alpha[(index + n) % 26]
        #new_str += alpha[5] #new_str = let + new_str
    return new_str


def caesar_decode(text, n):
    old_str = text
    for let in text:
        index = alpha.index(let)
        old_str += alpha[(index - n) % 26]
    return old_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
