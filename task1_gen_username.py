import math

def pseudo_encrypt(value):
    l1, l2, r1, r2 = 0, 0, 0, 0
    T = 65535
    l1 = (value >> 16) & 0xffff
    r1 = value & 0xffff
    for i in range(3):
        l2 = r1
        r = round(((1366 * r1 + 150889) % 714025) / 714025 * 32767)
        r2 = l1 ^ int(r)
        l1 = l2
        r1 = r2
    
    return (r1 << 16) + l1

if __name__ == "__main__":
    for i in range(1024):
        username = 'u' + str(pseudo_encrypt(i))
        print(f'username = {username}')

