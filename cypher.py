from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def encrypt(t, s,d):
    blank = ''
    if d == 'decode':
        s = -s
    for i in t:
        if i in t:
            new = alphabet.index(i)
            new1 = new+s
            new_str = alphabet[new1]
            blank += new_str
        else:
            pass
    print(f"encrypted msg {blank}")
condition = True
while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 25
    encrypt(t=text, s=shift, d=direction)
    again=input('type "yes", if you want to do again. otherwise type "no"\n').lower()
    if again=='no':
        condition=False
    print('Goodbye')


