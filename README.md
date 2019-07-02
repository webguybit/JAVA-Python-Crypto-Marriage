# JAVA-Python-Crypto-Marriage
Recently, I encountered the AES encryption algorithm in conjunction with the java project. The java code has SecureRandom.getInstance("SHA1PRNG"); Python can't find the corresponding method. This repo tries to solve the issue

C#, php, js code is found in various ways, everyone has encountered and solved Not much, C# directly use java to calculate the key, and then use C# to calculate AES ( https://blog.csdn.net/yunhua_lee/article/details/17226089 ), which takes about 2 days, and finally finds the method in the PHP code. ( https://github.com/myGGT/crypt_aes/blob/master/crypt_aes.php ), the relevant JavaScript code ( https://github.com/bombworm/SHA1PRNG/blob/master/index.js ), recorded for Everyone uses it.


# 0x01 Java implementation
Java encryption parameter description (using the library)

AES encryption mode : ECB /CBC/CTR/OFB/CFB 
padding : pkcs5padding /pkcs7padding/zeropadding/iso10126/ansix923 
data block : 128 bits / 192 bits / 256 bits

Let's take the java default AES encryption method as an example. Other encryption simulations are basically the same for key processing. The Java default AES encryption mode is "AES/ECB/PKCS5Padding".

Java code:
# Crypto_java.java
Run from main:
# Crypto_java_main.java

Those lines are to encrypt the password. The pit is here, stackoverflow is recommended to modify the java code, 1. indicate the encryption method and padding 2. Do not use SecureRandom, this is Oracle implementation, may produce different values ​​in different versions, especially Android ( https://blog .csdn.net/banking17173/article/details/8236028 ). Stackoverflow( https://stackoverflow.com/questions/24124091/better-way-to-create-aes-keys-than-seeding-securerandom ).


# 0x02 Python3 implementation
Install AES related libraries

pip install pycryptodome

