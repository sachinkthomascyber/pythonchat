from user_factory.contact_server import handshake
from user_factory.encrypt_current_message import sender
from user_factory.decrypt_current_message import decrypt
from user_factory.verify_using_email import verify_user_email


def start():
    if not verify_user_email():
        return

    pwd = handshake('b')
    pwd = str(pwd)
    # pwd = "147917681690311406089865219328524729289197771215116378066859364856770798189796985142559286368771813177043342398134144966766447138140849325513800568991013722848038005912833445802510304053991213527757309458785959735714230583275246930108731612534942004637712216673444588401627145764815862025678924522331559755225860254510773277058059280521535562258038706896401296570416772729380013877353172026455740369949705576696714811168984606062810110906752961099231211148988221136116596809230"

    print("Enter action:")
    print("Press 1 for sending a message")
    print("Press 2 for receiving a message")

    action = input("> ")

    if action == "1":
        message = input("Enter message: ").encode()
        sender(message, 'b')

    elif action == "2":
        decrypt(pwd)

    else:
        print("Bad choice enetered")


if __name__ == "__main__":
    start()