import pickle
import base64

x = {
	"nonce": nonce, 
    "ciphertext": ciphertext, 
    "tag": tag
}
pickled_x = pickle.dumps(x)
# pickled_x is a bytes-object that is a hard to read by humans.

b64 = base64.b64encode(pickled_x) 
print(b64)
pickled_x2 = base64.b64decode(b64) 

ans = pickle.loads(pickled_x2)

print(ans)