import os
import time
def main():
    content='北京欢迎你，我爱北理工'
    while True:
        # print(content)
        os.system('cls')
        time.sleep(0.2)
        content=content[1:]+content[0]


main()