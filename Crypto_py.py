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
    ''' AES/ECB/NoPadding encrypt '''
    key = bytes.fromhex(key)
    cryptor = AES.new(key, AES.MODE_ECB)
    ciphertext = cryptor.encrypt(bytes.fromhex(value))
    return ''.join(['%02x' % i for i in ciphertext]).upper()
 
def aes_ecb_decrypt(key:str, value:str) -> str:
    ''' AES/ECB/NoPadding decrypt '''
    key = bytes.fromhex(key)
    cryptor = AES.new(key, AES.MODE_ECB)
    ciphertext = cryptor.decrypt(bytes.fromhex(value))
    return ''.join(['%02x' % i for i in ciphertext]).upper()
 
def get_userkey(key, value):
    ''' AES/ECB/PKCS5Padding encrypt '''
    cryptor = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    padding_value = padding_pkcs5(value)
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
 
 
data = '0513011E0005016400000000000000000001000000000000000000000000000000770013011E0005026400000000000000000001000000000000000000000000000000770013011E0005036400000000000000000001000000000000000000000000000000770013011E0005046400000000000000000001000000000000000000000000000000770013011E000505640000000000000000000100000000000000000000000000000077000000000000'
key = '43C8B53E236C4756B8FF24E5AA08A549'
aes_result = 'AB4F4686218A5FF9F07E5248E6B5525D140602A0FAA21176C9A158A010B1A7C0258E80667BF7DD3B6FF57707B373BF75F57AE634D9F1384002AA6B788F4C658DD77572C207AAE3134F91FB690A4F024EF428DE3E1C5F84D0EA9D01B8AB4ED9FE97D7C0D65D447D92F0E306573F30E1360B3DE999E952BAAB9B22E48B8C7B23DC5480027DEE44988F0E86F7A475EEF599C1D7D3331457E582558BC3447E644913ABD63FC221C2E0D49BD712879261FF5F'
aes128string = aes_ecb_encrypt(key, data)
print(aes128string)
 
aes128string = aes_ecb_decrypt(key, aes_result)
print(aes128string)
 
mac = '405EE11002F3'
device_id = '12532802' #'12403492' #'12532802'
user_key = 'c1ee1f3f2d74e02706be9af78aa79ba4'.upper()
aes128string = get_userkey(get_sha1png_key(device_id), mac)
print(aes128string)
 
# 58F7CD929BFAA0915032536FBA8D3281420E93E3
# 58f7cd929bfaa0915032536fba8d3281
# 58F7CD929BFAA0915032536FBA8D3281
print(get_sha1png_key('12532802')) # 58f7cd929bfaa0915032536fba8d3281
