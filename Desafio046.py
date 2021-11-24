#contagem regressiva para fogos de artifício
from time import sleep
import emoji
print('-' * 30)
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print(emoji.emojize('\033[1;33m:fireworks:\033[m' * 20, use_aliases=True))
sleep(1)
print(emoji.emojize('\033[1;33m:fireworks:\033[m' * 20, use_aliases=True))
sleep(1)