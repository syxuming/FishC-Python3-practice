def hwl(word):
    n = len(word)
    m = 0
    while n:
        if word[m] == word[n-1]:
            n -= 1
            m += 1
        else:
            print('不是回文联')
            break
        if n == 0:
            print('是回文联')
word = input('请输入一句话来检测是不是回文联：')
while len(word) <= 1:
    word = input('至少输入两个字符！\n请输入一句话来检测是不是回文联：')
hwl(word)
