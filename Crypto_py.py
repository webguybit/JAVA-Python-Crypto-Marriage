from base64 import b64encode, encodebytes
from Crypto.Cipher import AES
import binascii
import hashlib
 
BS = AES.block_size
 
 
def padding_pkcs5(value):
    return str.encode(value + (BS - len(value) % BS) * chr(BS - len(value) % BS))
 
 
def padding_zero(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)
 
def aes_ecb_encrypt(key, value):
    # AES/ECB/PKCS5padding
    # key is sha1prng encrypted before
    cryptor = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    padding_value = padding_pkcs5(value)    # padding content with pkcs5
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
 
 
 
hexstr_content = '405EE11002F3'    #content
key = '12532802'  #keypassword
expect_result = 'c1ee1f3f2d74e02706be9af78aa79ba4'.upper()
aes128string = aes_ecb_encrypt(get_sha1png_key(key), hexstr_content)
print(aes128string)
