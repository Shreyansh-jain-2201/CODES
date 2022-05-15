package SimplifiedEcc;

import java.io.UnsupportedEncodingException;
import java.security.*;
import java.util.Enumeration;
import java.util.Scanner;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyAgreement;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.ShortBufferException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import org.bouncycastle.jce.ECNamedCurveTable;
import org.bouncycastle.jce.spec.ECNamedCurveParameterSpec;
import java.security.Security;
import java.util.concurrent.TimeUnit;

public class Understadable_Code {

    public static byte[] iv = new SecureRandom().generateSeed(16); // generateSeed is used to define the
                                                                   // number of random nos needed.

    public static void main(String[] args) throws InterruptedException {
        String cipherText = "";

        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        try {
            SecureRandom rng = SecureRandom.getInstance("SHA1PRNG");
            rng.setSeed(711); // used for reseeding the object rng.
        } catch (NoSuchAlgorithmException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            // exception.
        }
        // Initialize two key pairs
        KeyPair keyPairA = generateECKeys();
        KeyPair keyPairB = generateECKeys();
        // Create two AES secret keys to encrypt/decrypt the message
        SecretKey secretKeyA = generateSharedSecret(keyPairA.getPrivate(), keyPairB.getPublic());
        SecretKey secretKeyB = generateSharedSecret(keyPairB.getPrivate(), keyPairA.getPublic());
        do {

            System.out.println("Hello admin, what do you want Alexa to do?");
            System.out.println("1.Send Data");
            System.out.println("2.Retrieve Data");
            System.out.println("3.Quit");
            Scanner scan = new Scanner(System.in);
            int choice = scan.nextInt();
            scan.nextLine();
            switch (choice) {
                case 1:
                    iv = new SecureRandom().generateSeed(16);
                    System.out.println("Enter the plaintext");
                    String plainText = scan.nextLine();

                    // System.out.println("Username is "+ plainText);
                    // String plainText = "My name is Aryan";
                    System.out.println("Original plaintext message: " + plainText);
                    // Encrypt the message using 'secretKeyA'
                    cipherText = encryptString(secretKeyA, plainText);
                    System.out.println("Encrypted cipher text: " + cipherText);
                    System.out.print("Sending encrypted data to cloud");
                    for (int i = 0; i < 6; i++) {
                        System.out.print(".");
                        TimeUnit.SECONDS.sleep(1);
                    }
                    System.out.println("");
                    System.out.println("");

                    break;
                case 2:
                    if (cipherText == "") {
                        System.out.println("There is no data to retrieve.");
                        break;
                    }
                    // Decrypt the message using 'secretKeyB'
                    String decryptedPlainText = decryptString(secretKeyB, cipherText);
                    System.out.print("Decrypting and Retrieving data from cloud");
                    for (int i = 0; i < 6; i++) {
                        System.out.print(".");
                        TimeUnit.SECONDS.sleep(1);

                    }
                    System.out.println("");
                    System.out.println("Decrypted cipher text: " + decryptedPlainText);
                    System.out.println("");
                    break;
                case 3:
                    System.exit(0);
                    break;

                default:
                    System.out.println("Enter the valid input.");
            }

        } while (true);
    }

    public static KeyPair generateECKeys() {
        try {
            ECNamedCurveParameterSpec parameterSpec = ECNamedCurveTable.getParameterSpec("brainpoolp256r1");
            KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("ECDH", "BC");

            keyPairGenerator.initialize(parameterSpec);
            KeyPair keyPair = keyPairGenerator.generateKeyPair();

            return keyPair;
        } catch (NoSuchAlgorithmException | InvalidAlgorithmParameterException | NoSuchProviderException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static SecretKey generateSharedSecret(PrivateKey privateKey, PublicKey publicKey) {
        try {
            KeyAgreement keyAgreement = KeyAgreement.getInstance("ECDH", "BC");
            keyAgreement.init(privateKey);
            keyAgreement.doPhase(publicKey, true);

            SecretKey key = keyAgreement.generateSecret("AES");
            return key;
        } catch (InvalidKeyException | NoSuchAlgorithmException | NoSuchProviderException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            return null;
        }
    }

    public static String encryptString(SecretKey key, String plainText) {
        try {
            IvParameterSpec ivSpec = new IvParameterSpec(iv);
            Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "BC");
            byte[] plainTextBytes = plainText.getBytes("UTF-8");
            byte[] cipherText;

            cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
            cipherText = new byte[cipher.getOutputSize(plainTextBytes.length)];
            int encryptLength = cipher.update(plainTextBytes, 0, plainTextBytes.length, cipherText, 0);
            encryptLength += cipher.doFinal(cipherText, encryptLength);

            return bytesToHex(cipherText);
        } catch (NoSuchAlgorithmException | NoSuchProviderException | NoSuchPaddingException | InvalidKeyException
                | InvalidAlgorithmParameterException | UnsupportedEncodingException | ShortBufferException
                | IllegalBlockSizeException | BadPaddingException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String decryptString(SecretKey key, String cipherText) {
        try {
            Key decryptionKey = new SecretKeySpec(key.getEncoded(), key.getAlgorithm());
            IvParameterSpec ivSpec = new IvParameterSpec(iv);

            Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "BC");
            byte[] cipherTextBytes = hexToBytes(cipherText);

            byte[] plainText;

            cipher.init(Cipher.DECRYPT_MODE, decryptionKey, ivSpec);

            plainText = new byte[cipher.getOutputSize(cipherTextBytes.length)];
            int decryptLength = cipher.update(cipherTextBytes, 0, cipherTextBytes.length, plainText, 0);
            decryptLength += cipher.doFinal(plainText, decryptLength);

            return new String(plainText, "UTF-8");
        } catch (NoSuchAlgorithmException | NoSuchProviderException | NoSuchPaddingException | InvalidKeyException
                | InvalidAlgorithmParameterException | IllegalBlockSizeException | BadPaddingException
                | ShortBufferException | UnsupportedEncodingException e) {
            e.printStackTrace();

            return null;
        }
    }

    public static String bytesToHex(byte[] data, int length) {
        String digits = "0123456789ABCDEF";
        StringBuffer buffer = new StringBuffer();

        for (int i = 0; i != length; i++) {
            int v = data[i] & 0xff;

            buffer.append(digits.charAt(v >> 4));
            buffer.append(digits.charAt(v & 0xf));
        }

        return buffer.toString();
    }

    public static String bytesToHex(byte[] data) {
        return bytesToHex(data, data.length);
    }

    public static byte[] hexToBytes(String string) {
        int length = string.length();
        byte[] data = new byte[length / 2];
        for (int i = 0; i < length; i += 2) {
            data[i / 2] = (byte) ((Character.digit(string.charAt(i), 16) << 4)
                    + Character.digit(string.charAt(i + 1), 16));
        }
        return data;
    }
}