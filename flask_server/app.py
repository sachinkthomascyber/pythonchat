from flask import Flask, request

app = Flask(__name__)
app.config.update(
    TESTING=True
)


# Storage for public keys
key_bank_3 = dict()


def counterpart(name):
    """
    Assumes there are only two users
    Returns the other user's public key as soon as it's available
    """

    cp = 'a' if name == 'b' else 'b'

    while cp not in key_bank_3:
        # Waiting indefinitely
        continue

    return key_bank_3[cp]


@app.route("/", methods=['POST'])
def receive():
    """
    Accepts public key of user
    Returns public key of the other user
    """
    if request.method == 'POST':
        public_key = request.form['publicKey']
        name = request.form['name']

        if name not in key_bank_3:
            key_bank_3[name] = public_key
        
        return counterpart(name)


if __name__ == "__main__":
    app.run(debug=True)