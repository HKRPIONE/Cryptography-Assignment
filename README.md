# Assignment 1: Theory Section

1. **Introduction to Cryptography**
   - Cryptography secures communication by ensuring confidentiality, integrity, and authenticity.
   - Importance:
     - Protects sensitive data.
     - Enables secure communication over untrusted networks.
     - Supports digital authentication and integrity checks.
   - Types of Cryptography:
     - Symmetric Encryption: Single key for encryption and decryption (e.g., AES, DES).
     - Asymmetric Encryption: Public key for encryption, private key for decryption (e.g., RSA, ECC).

2. **Caesar Cipher Overview**
   - Substitution cipher where each letter is shifted by a fixed key value.
   - History: Used by Julius Caesar for military communication.
   - Working:
     - Shift each plaintext letter by the key value.
     - Wrap-around occurs if the shift exceeds the alphabet.

3. **Mathematical Representation**
   - Encryption:
   - Decryption:
     - : Ciphertext letter (numeric)
     - : Plaintext letter (numeric)
     - : Shift key

4. **Limitations of Caesar Cipher**
   - Vulnerable to frequency analysis due to fixed substitutions.
   - Limited security with only 25 possible keys.
   - Inadequate for modern cryptographic needs.

5. **Implementation Logic**
    - Convert plaintext letters to numbers (A=0, B=1, ..., Z=25).
    - Use encryption or decryption formulas.
    - Apply modulus operation to handle wrap-around.
    - Retain non-alphabetic characters unchanged.
    - Convert numbers back to letters for the final result.

6. **Applications of Caesar Cipher**
    - Historical use in securing military communications.
    - Educational tool to teach cryptography basics.

7. **Example**
    - Plaintext: HELLO
    - Key: 3
    - Encryption:
      - Convert letters: H=7, E=4, L=11, O=14
      - Apply formula:
        - H: (7 + 3) mod 26 = 10 (K)
        - E: (4 + 3) mod 26 = 7 (H)
        - L: (11 + 3) mod 26 = 14 (O)
        - O: (14 + 3) mod 26 = 17 (R)
      - Ciphertext: KHOOR
    - Decryption:
      - Convert ciphertext: K=10, H=7, O=14, R=17
      - Apply formula:
        - K: (10 - 3 + 26) mod 26 = 7 (H)
        - H: (7 - 3 + 26) mod 26 = 4 (E)
        - O: (14 - 3 + 26) mod 26 = 11 (L)
        - R: (17 - 3 + 26) mod 26 = 14 (O)
      - Plaintext: HELLO

