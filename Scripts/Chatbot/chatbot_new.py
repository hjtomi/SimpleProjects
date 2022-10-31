# doesn't need to be complicated make it so that it can interpret some sentences and words
# make responses

# grrr it's hard I should only do this project later

class User:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.height = None
        self.interest = None


words = {'user': ['I', 'my'],
         'bot': ['you', 'your', 'yours']
         }


def main():
    user = User()
    message = ''
    while message != 'quit':
        message = input()
        if 'name' in message:
            for word in words['user']:
                if word in message:
                    user.name = message.split(' ')[-1]
                    print(user.name)
                    break


if __name__ == '__main__':
    main()

