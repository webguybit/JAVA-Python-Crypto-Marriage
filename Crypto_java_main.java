KeyGenerator kgen = KeyGenerator.getInstance("AES");
SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
secureRandom.setSeed(keyWord.getBytes());
kgen.init(128, secureRandom);
SecretKey secretKey = kgen.generateKey();
