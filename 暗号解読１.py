# strInputText	: シーザー暗号の暗号化/復号の対象文字列。英語小文字。
# intKey	: 暗号化キー。英語小文字アルファベットのみの場合は1-25の範囲の数値。
#暗号	: rtytwhdhqj
rtytwhdhqj = input('暗号を入力 : ')
def caesar(strInputText, intKey):
    strResultList = []
    for char in strInputText:
        if (ord(char) + intKey) <= ord('z'):
            strResultList.append(chr(ord(char) + intKey))
        else:
            strResultList.append(chr((ord('a') - 1) + (ord(char) + intKey - ord('z'))))

    print('key:' + str(intKey) + ' > ' + ''.join(strResultList))

if __name__ == '__main__':
    for i in range(1, 26):
        caesar(rtytwhdhqj, i)

