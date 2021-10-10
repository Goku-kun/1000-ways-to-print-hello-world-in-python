from json import loads

json = '{"message": "Hello, World!"}'

if __name__ == '__main__':
    print(loads(json)['message'])
