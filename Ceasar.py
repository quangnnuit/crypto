import os
'''Số lần dịch tối đa là 26 lần tương úng với 26 giá trị của k'''
MAX_KEY = 26
'''Lấy menu'''

def getMenu():
    while True:
        print('Bạn muốn encrypt hay decrypt?')
        print('Nhấn e để "encypt" hoặc d để "decrypt" hoặc b để"Brute Force"')
        mode = input().lower()
        '''Kiểm tra lựa chọn nhập vào, nếu sai bắt người dùng nhập lại'''
        if mode in 'encrypt e decrypt d brute b'.split():
           return mode
        else:
            print('SAI CÚ PHÁP! Nhấn e để "encypt" hoặc d để "decrypt" hoặc b để "Brute Force"')

'''Hàm lấy Message'''

def getMassage():
    print('Nhập message: ')
    return  input()

'''Hàm lấy Khóa'''

def getKey():
    key = 0
    '''Kiểm tra khóa nhập vào giá trị phải từ 1 tới 26 nếu sai bắt nhập lại'''
    while True:
        print('Nhập khóa k (1-%s)' % (MAX_KEY))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY):
            return key

'''Hàm xử lý'''

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMenu()
message = getMassage()
if mode[0] != 'b':
    key = getKey()

print('Kết quả chuyển đổi:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range (1, MAX_KEY + 1):
        print(key, getTranslatedMessage('decrypt', message, key))



