from user import user


@user.route('/')
def hello_world():
    return 'hello world!'
