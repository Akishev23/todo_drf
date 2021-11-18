import os
import sys
import argparse
import random
import string
from users.models import Users


def pass_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', dest='username', type=str)
    parser.add_argument('--email', dest='email', type=str)
    parser.add_argument('--first_name', dest='first_name', type=str)
    parser.add_argument('--last_name', dest='last_name', type=str)
    parser.add_argument('--password', dest='password', type=str, required=False)
    parser.add_argument('--superuser', dest='superuser', action='store_true', required=False)

    args = parser.parse_args()

    username = args.username
    email = args.email
    password = pass_generator(10) if args.password is None else args.password
    superuser = args.superuser

    try:
        user_obj = Users.objects.get(username=args.username)
        user_obj.set_password(password)
        user_obj.save()
    except Users.DoesNotExist:
        if superuser:
            Users.objects.create_superuser(username, email, password)
        else:
            Users.objects.create_user(username, email, password)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
