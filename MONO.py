mono = {
    "a":"N",
    "b":"O",
    "c":"P",
    "d":"Q",
    "e":"R",
    "f":"S",
    "g":"T",
    "h":"U",
    "i":"V",
    "j":"W",
    "k":"X",
    "l":"Y",
    "m":"Z",
    "n":"A",
    "o":"B",
    "p":"C",
    "q":"D",
    "r":"E",
    "s":"F",
    "t":"G",
    "u":"H",
    "v":"I",
    "w":"J",
    "x":"K",
    "y":"L",
    "z":"M",
    " ":" "
}
plain_text = input("Enter a plain text in small: ").lower()
mono_cipher = [ ]
for x in plain_text:
    if x in mono:
        mono_cipher.append(mono[x])
    else:
        mono_cipher.append("?")

cipher_text ="".join(mono_cipher)
print("Monoalphabetic Cipher is: ", cipher_text)
