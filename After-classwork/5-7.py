t = ""
def fenge(a = 75):
        print("-" * a)
while t != 3:
        fenge()
        t = input("1 加密\n2 解密\n3 退出\n")
        fenge()
        key =int(input("请输入密钥(1-25)"))
        fenge()
        message = input("请输入要加密/解密的内容：")
        message = message.upper()
        output = ""
        for letter in message:
            if letter.isupper():
                if(t=='1'):
                    value = ord(letter) + key
                if(t=='2'):
                    value = ord(letter) + (26-key)
                letter = chr(value)
                if not letter.isupper():
                    value = value - 26
                    letter = chr(value)
            output += letter
        fenge()
        print("最后的结果：",output)
