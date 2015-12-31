from pprint import pprint
import string
import groupy

REPLACEABLE_CHARS = """0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}"""

def get_messages():
    groups = groupy.Group.list()

    for group in groups:
        if group.name == 'PML':
            messages = group.messages()
            iters = int((group.message_count / 100))
            print("Total iters needed: " + str(iters))
            msg = []
            # for message in group.messages():
            i = 1
            with open(group.name, 'w') as f:
                for message in messages:
                    message = message.text
                    if message:
                        message = message.replace('\n', ' ')
                        message = str(message.encode('ascii', errors='ignore'))
                        for letter in REPLACEABLE_CHARS:
                            message = message.replace(letter, ' ')

                        f.write(message)
                while i <= iters:
                    print("Iteration: " + str(i))
                    messages = messages.older()
                    for message in messages:
                        message = message.text
                        if message:
                            message = message.replace('\n', ' ')
                            message = str(message.encode('ascii', errors='ignore'))
                            for letter in REPLACEABLE_CHARS:
                                message = message.replace(letter, ' ')
                            f.write(message)
                    i += 1

if __name__ == '__main__':
    get_messages()