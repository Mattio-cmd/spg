#!/usr/bin/env python3
# Imports
import random
import pyperclip
from rich.console import Console
from rich.panel import Panel

# rich variables
console = Console()

# possible characters variables x2
lower = "qwertyuiopasdfghjklzxcvbnñm"
uper = "QWERTYUIOPASDFGHJKLZXCVBNÑM"
symb = "!@#$%^&*()_+~`,<>./|][{}':;*-=+"
nums = "1234567890"
lower2 = "qwertyuiopasdfghjklzxcvbnñm"
uper2 = "QWERTYUIOPASDFGHJKLZXCVBNÑM"
symb2 = "!@#$%^&*()_+~`,<>./|][{}':;*-=+"
nums2 = "1234567890"

all  = lower + uper + symb + nums + lower2 + uper2 + symb2 + nums2
console.print(Panel("🔒  [bold green] spg: secure password generator [/] 🔒 ", expand=False, border_style="red"))
lenghtnum = console.input("[yellow] password lenght (190 max): ")
length = int(lenghtnum)
if length > 190:
    console.print("❌ [red]The password can not be more than 190 characters")
else:
    password = "".join(random.sample(all,length))
    console.print("[bold blue]pass: [/]", password)
    pyperclip.copy(password)
    console.print("[bold green]password coppied to the clipboard! 📋")
