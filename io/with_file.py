# 请将本地一个文本文件读为一个str并打印出来：

fpath = '/Users/wuzheqing/Documents/work/auto-script/config/production.config.js'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
