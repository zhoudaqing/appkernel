import uuid
from datetime import datetime
from passlib.hash import pbkdf2_sha256


def create_uuid_generator(prefix=None):
    def generate_id():
        return '{}{}'.format(prefix, str(uuid.uuid4()))

    return generate_id


def date_now_generator():
    return datetime.now()


def current_user_generator():
    # todo: finalise this
    return ''


def password_hasher(rounds=20000, salt_size=16):
    def to_value_converter(password):
        # type: (str) -> str
        if password.startswith('$pbkdf2-sha256'):
            return password
        else:
            return pbkdf2_sha256.encrypt(password, rounds=rounds, salt_size=salt_size)

    return to_value_converter, None


def unix_time_converter():
    # todo: implement this
    def to_unix_time(property_value):
        print(property_value)
        pass

    def from_unix_time(property_value):
        print(property_value)
        pass

    return to_unix_time, from_unix_time


def enigma_converter():
    # todo: implement this
    def to_encrypt(property_value):
        print(property_value)
        pass

    def to_decrypt(property_value):
        print(property_value)
        pass

    return to_encrypt, to_decrypt
