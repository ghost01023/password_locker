UPPER_LIMIT: int = 126
LOWER_LIMIT: int = 32


# ASCII TABLE FOR PRINTABLE CHARACTERS STARTS FROM 33 TO 126
# SO, FOR EACH DIGIT, INCREMENT BY RELATIVE INDEX IN CIPHER
# THEN, MODULO BY (126 - 33) AND FINALLY, ADD BY 33
# FIND ASCII-CHAR FOR THIS NEW ASCII INDEX, AND STORE IT INSTEAD

def encrypt(pText: str, cText: str) -> str:
    plainText: str = pText
    # print("original plain text is: " + plainText)
    plainTextArray: list = [*plainText]
    cipherText: str = cText
    cipherTextArray: list = [*cipherText]
    plainTextCount: int = 0
    cipherCount: int = 0
    plainTextLen: int = len(plainTextArray)
    cipherTextLen: int = len(cipherTextArray)
    encryptedText: str = ""
    while plainTextCount < plainTextLen:
        origChar: str = plainTextArray[plainTextCount]
        cipherChar: str = cipherTextArray[cipherCount]
        asciiOrigChar: int = ord(origChar)
        asciiCipherChar: int = ord(cipherChar)
        displacement: int = asciiOrigChar + asciiCipherChar
        modulo: int = displacement % (UPPER_LIMIT - LOWER_LIMIT)
        asciiFinal: int = modulo + LOWER_LIMIT
        newChar: str = chr(asciiFinal)
        # print("Displacement: %s\tModulo Value: %s\t Final ASCII Value: %s\t\tNew Char: %s\t" % (
        #     str(displacement).zfill(3), str(modulo).zfill(3), str(asciiFinal).zfill(3), str(newChar)))
        encryptedText += newChar
        plainTextCount += 1
        cipherCount = (cipherCount + 1) % cipherTextLen
    return encryptedText


# ITERATE OVER EVERY CHARACTER IN ENCRYPTED_TEXT
# DECREMENT BY THE LOWER_LIMIT
# INCREMENT BY UPPER_LIMIT - LOWER_LIMIT


def decrypt(eText: str, cText: str) -> str:
    # print(eText)
    encryptedText: str = eText
    cipherText: str = cText
    cipherTextArray: list = [*cipherText]
    cipherTextLen: int = len(cipherTextArray)
    cipherCount = 0
    encryptedTextCount: int = 0
    encryptedTextLen: int = len(encryptedText)
    encryptedTextArray: list = [*encryptedText]
    decryptedText: str = ""
    while encryptedTextCount < encryptedTextLen:
        cipherChar: str = cipherTextArray[cipherCount]
        asciiCipherChar: int = ord(cipherChar)
        asciiFinal: int = ord(encryptedTextArray[encryptedTextCount])
        modulo: int = asciiFinal - LOWER_LIMIT
        displacement = modulo + (UPPER_LIMIT - LOWER_LIMIT)
        # fDis: str = str(displacement)
        decryptedAscii: int = -1
        if displacement <= UPPER_LIMIT:
            displacement += (UPPER_LIMIT - LOWER_LIMIT)
            decryptedAscii = displacement - asciiCipherChar
        if decryptedAscii < 0:
            decryptedAscii = displacement - asciiCipherChar
        if decryptedAscii < LOWER_LIMIT:
            decryptedAscii += (UPPER_LIMIT - LOWER_LIMIT)
        elif decryptedAscii > UPPER_LIMIT:
            decryptedAscii -= (UPPER_LIMIT - LOWER_LIMIT)
        newChar: str = chr(decryptedAscii)
        # print("R-M: %s\tFsR-Dis: %s\tFlR-Dis: %s\tDecrypted ASCII:%s\t\tDecryptedText:%s\t" % (
        #     str(modulo).zfill(3), fDis.zfill(3), str(displacement).zfill(3), str(decryptedAscii).zfill(3), newChar))
        decryptedText += newChar
        encryptedTextCount += 1
        cipherCount = (cipherCount + 1) % cipherTextLen
    # print("IT IS: " + decryptedText)
    return decryptedText


# print(encrypt('{"http://www.google.com/account/mainmate":"helloWorld!"}', "JohnnyBeGood!"))
