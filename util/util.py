from hashlib import sha1


def get_password(password):
    """简单密码加密"""
    return sha1(password.encode()).hexdigest()


if __name__ == '__main__':
    print(get_password('123'))

