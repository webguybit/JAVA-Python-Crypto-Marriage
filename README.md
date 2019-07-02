# JAVA-Python-Crypto-Marriage
(This is a translated vesion of an awesome post https://blog.csdn.net/max229max/article/details/87639613 by Max.Bai)


Recently, I encountered the AES encryption algorithm in conjunction with the java project. The java code has SecureRandom.getInstance("SHA1PRNG"); Python can't find the corresponding method. This repo tries to solve the issue

C#, php, js code is found in various ways, everyone has encountered and solved Not much, C# directly use java to calculate the key, and then use C# to calculate AES ( https://blog.csdn.net/yunhua_lee/article/details/17226089 ), which takes about 2 days, and finally finds the method in the PHP code. ( https://github.com/myGGT/crypt_aes/blob/master/crypt_aes.php ), the relevant JavaScript code ( https://github.com/bombworm/SHA1PRNG/blob/master/index.js ), recorded for Everyone uses it.


# 0x01 Java implementation
Java encryption parameter description (using the library)

AES encryption mode : ECB /CBC/CTR/OFB/CFB 
padding : pkcs5padding /pkcs7padding/zeropadding/iso10126/ansix923 
data block : 128 bits / 192 bits / 256 bits

Let's take the java default AES encryption method as an example. Other encryption simulations are basically the same for key processing. The Java default AES encryption mode is "AES/ECB/PKCS5Padding".

Java code:
# AESEncode.java

Those lines are to encrypt the password. The pit is here, stackoverflow is recommended to modify the java code, 1. indicate the encryption method and padding 2. Do not use SecureRandom, this is Oracle implementation, may produce different values ​​in different versions, especially Android ( https://blog .csdn.net/banking17173/article/details/8236028 ). Stackoverflow( https://stackoverflow.com/questions/24124091/better-way-to-create-aes-keys-than-seeding-securerandom ).


# 0x02 Python3 implementation
Install AES related libraries

pip install pycryptodome

Full code file:
# Crypto_py.py

Realize the conversion of the key and realize the content of the key code in java. The hex string is returned here, you can modify the code to return the desired format.

The key code is implemented, and the encryption methods of other CBCs are the same.

# 0x03 summary
AES mainly pays attention to two:

1. Encryption methods ECB, CBC, etc.

2. Handling of keys, such as java's sha1prng, or base64.

3. Fill, key and original text are all possible to fill, NoPadding, no padding, 0 padding, and pkcs5padding, no padding is not filled with content, directly encrypted, the above code implements \0 padding and pkcs5padding.

In general, the encrypted content is not the same as the key processing or the padding is not correct.

# 0x04 complete code Crypto_py.py

The complete code contains a bit of decryption code, but the decryption code is not filled. If there is padding, the content needs to be removed after decrypting the content.



