
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_continue = True

def encrypt(org_text, shift_no):
    result = []
    for i in range(0,len(org_text),1):
        for j in range(0, len(alphabet),1):
            if alphabet[j] == org_text[i]:
                first_value = j
                new_value = (first_value + shift_no) % len(alphabet)
                result.append(alphabet[new_value])
                break
        else:
            result.append(org_text[i])
    return "".join(result)

def decrypt(org_text, shift_no):
    result = []
    for i in range(0, len(org_text), 1):
        for j in range(0, len(alphabet), 1):
            if alphabet[j] == org_text[i]:
                first_value = j
                new_value = (first_value - shift_no) % len(alphabet)
                result.append(alphabet[new_value])
                break
        else:
            result.append(org_text[i])
    return "".join(result)



while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(f"Your encoded message is: {encrypt(text, shift)}")
    elif direction == "decode":
        print(f"Your decoded message is: {decrypt(text, shift)}")
    else:
        print("Invalid value.")
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
