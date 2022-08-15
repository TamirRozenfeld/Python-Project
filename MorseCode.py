
def to_morse_code(text):
    code = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}

    morse_code = ""
    for x in text:
        morse_code += code[x.upper()]
    return morse_code

text = input("Enter text to conver to Mose Code: ")
print(to_morse_code(text))
