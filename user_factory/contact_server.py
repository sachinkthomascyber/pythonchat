from user_factory.pyDHE_local import DHE
import requests

def contact_server_for_public_key_exchange(name, a):
    aPubKey = a.getPublicKey()
    payload = {'publicKey': aPubKey, "name": name}
    r = requests.post("http://localhost:5000/", data=payload)
    return r.text


def handshake(name):
    a = DHE()
    bp = contact_server_for_public_key_exchange(name, a)
    uk = a.update(int(bp))
    return uk