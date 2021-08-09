from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

parameters = dh.generate_parameters(generator=2, key_size=2048)
server_private_key = parameters.generate_private_key()
peer_private_key = parameters.generate_private_key()
shared_key = server_private_key.exchange(peer_private_key.public_key())

derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)

# print(server_private_key)
# print(peer_private_key)
# print(shared_key)


parameters2 = dh.generate_parameters(generator=2, key_size=2048)
# server_private_key2 = parameters2.generate_private_key()
peer_private_key2 = parameters2.generate_private_key()
shared_key2 = server_private_key.exchange(peer_private_key2.public_key())

print(shared_key == shared_key2)