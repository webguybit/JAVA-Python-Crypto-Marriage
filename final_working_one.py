from base64 import b64encode, encodebytes
from Crypto.Cipher import AES
import binascii
import hashlib
 
BS = AES.block_size

unpad = lambda data: data[0:-ord(data[-1])]  

def padding_pkcs5(text):
    count = len(text.encode('utf-8'))
    add = BS - (count % BS)
    entext = text + (chr(add) * add)
    return entext


def padding_zero(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)
    
    
def aes_ecb_encrypt_nopad(key, value):
    ''' AES/ECB/NoPadding encrypt '''
    key = bytes.fromhex(key.encode().hex())
    cryptor = AES.new(key, AES.MODE_ECB)
    ciphertext = cryptor.encrypt(bytes.fromhex(value))
    return ''.join(['%02x' % i for i in ciphertext]).upper()
 
def aes_ecb_decrypt(key, value):
    ''' AES/ECB/NoPadding decrypt '''
    key = bytes.fromhex(key)
    cryptor = AES.new(key, AES.MODE_ECB)
    ciphertext = cryptor.decrypt(bytes.fromhex(value))
    # print(ciphertext.decode())
    return unpad(ciphertext.decode())
    # return ''.join(['%02x' % i for i in ciphertext]).upper()
 
def aes_ecb_encrypt_pkcs5(key, value):
    ''' AES/ECB/PKCS5Padding encrypt '''
    cryptor = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    padding_value = padding_pkcs5(value).encode("utf8")
    ciphertext = cryptor.encrypt(padding_value)
    return ''.join(['%02x' % i for i in ciphertext]).upper()
 
def get_sha1prng_key(key):
    '''[summary]
    encrypt key with SHA1PRNG
    same as java AES crypto key generator SHA1PRNG
    Arguments:
        key {[string]} -- [key]
    
    Returns:
        [string] -- [hexstring]
    '''
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).digest()
    return ''.join(['%02x' % i for i in signature]).upper()[:32]



# data = '你好'
# key = 'WHATEVER'
# aes128string = aes_ecb_encrypt_pkcs5(get_sha1prng_key(key), data.encode().decode())
# print('AES:',aes128string)
# devl=aes_ecb_decrypt(get_sha1prng_key(key),aes128string)
# print(devl.strip())
