from Crypto.Cipher import ARC4 as RC4


class CryptoRc4:

    def __init__(self):

        self.key = b'FROGMINDTODO'
        self.nonce = b'nonce'
        self.RC4_Stream = RC4.new(self.key + self.nonce)
        self.RC4_Stream.encrypt(self.key + self.nonce)
        self.RC4_Stream2 = RC4.new(self.key + self.nonce)
        self.RC4_Stream2.encrypt(self.key + self.nonce)

    def decrypt(self, data):

        decryptedData = self.RC4_Stream.encrypt(data)
        return decryptedData

    def encrypt(self, data):

        encryptedData = self.RC4_Stream2.encrypt(data)
        return encryptedData
