import random


lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "ASDFGHJKLQWERTYUIOPZXCVBNM"
num = "1234567890"
symbol = "@.[]!"


all = lower+upper+num+symbol
length = 16

password = "".join(random.sample(all,length))
print(password)