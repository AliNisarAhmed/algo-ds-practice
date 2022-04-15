class CaesarCipher:

    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

        self._forward = ''.join(chr((k + shift) % 26 + ord('A')) for k in range(26))
        self._backward = ''.join(chr((k - shift) % 26 + ord('A')) for k in range(26))

    def encrypt(self, message):
        return self._tranform(message, self._forward)

    def decrypt(self, message):
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        msg = list(original)  # convert to character array
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 - 25
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = 'Ali Samrah Azlan'
    coded = cipher.encrypt(message)
    print(coded)
    answer = cipher.decrypt(coded)
    print(answer)
