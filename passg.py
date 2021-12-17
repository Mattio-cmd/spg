import random
from rich.console import Console
from rich.panel import Panel

lower = "qwertyuiopasdfghjklzxcvbnñm"
uper = "QWERTYUIOPASDFGHJKLZXCVBNÑM"
symb = "!@#$%^&*()_+~`,<>./|][{}':;*-=+"
nums = "1234567890"
lower2 = "qwertyuiopasdfghjklzxcvbnñm"
uper2 = "QWERTYUIOPASDFGHJKLZXCVBNÑM"
symb2 = "!@#$%^&*()_+~`,<>./|][{}':;*-=+"
nums2 = "1234567890"
all  = lower + uper + symb + nums + lower2 + uper2 + symb2 + nums2
lenghtnum = input("password lenght (190 max): ")
length = int(lenghtnum)
password = "".join(random.sample(all,length))
print("pass: ", password)
