import string

str = string.ascii_lowercase + string.ascii_uppercase +"".join([str(i) for i in range(10)])


def short_url_generate(id):
    short_url = ""

    while id > 0:
        short_url += str[ id % 62]
        id //=62
    return short_url[::-1]

def decode(url):
    id = 0
    for i in url:
        val_i = ord(i)
        if val_i >= ord('a') and val_i <= ord('z'):
            id = id*62+val_i - ord('a')
        elif val_i >= ord('A') and val_i <= ord('Z'):
            id = id*62+val_i - ord('a') + 26
        else:
            id = id * 62 + val_i - ord('9') + 52
    return id

if __name__ == '__main__':
     id = 1234566
     short_url = short_url_generate(id)
     dec = decode(short_url)
     print(short_url)
     print(dec)