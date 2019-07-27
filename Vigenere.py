import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = "Vietnam National University Ho Chi Minh City, University of Information Technology"
    myKey = 'UITNUMBERONE'
    myMode = 'encrypt' # chọn là 'encrypt' hoặc 'decrypt'
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('%sed message:' % (myMode.title()))
    print(translated)

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] # lưu két quả
    keyIndex = 0
    key = key.upper()

    for symbol in message: # duyệt symbol
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 có nghĩa là hàm symbol.upper() không tìm thấy trong LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # cộng vào nếu là encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # trừ vào neu1 là decrypting
            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1 # duy chuyễn đến symbol tiếp theo của khóa
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)


if __name__ == '__main__':
    main()