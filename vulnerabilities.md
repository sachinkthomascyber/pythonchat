## Possible risks
- The app uses Vigenere cipher for symmetric encryption which is not safe & easy to crack. Some industry standard algorithms like AES can be used instead.
- The apps uses simple DH algo (diffie hellman algorithm)
- Using DHE (or EDH), the ephemeral, is strongly preferred over simple DH as it provides forward secrecy when used.
- The server stores public keys in dictionary for one time use which is obviously never a good method. But since they are public keys anyways this risk is low.
- The encrypted text is stored in text files & handled manually.
- All other possible risks associated with the algorithm can be assumed as applicable here.
- Lastly the app assumes the user's computer is the safest place in the world.
