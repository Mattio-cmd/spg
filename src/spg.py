#!/usr/bin/env python3
# Imports
import secrets;
import string;
import pyperclip;
from rich.console import Console;
from rich.panel import Panel;

# rich variables
console = Console();

# random variables
srandom = secrets.SystemRandom;

# Possible letters/digits to use
alphabet = string.ascii_letters + string.digits

console.print(Panel("🔒  [bold green] spg: secure password generator [/] 🔒 ", expand=False, border_style="red"));
lenghtnum = console.input("[yellow] password lenght (200 max): ");
length = int(lenghtnum);
if length > 200:
    console.print("❌ [red]The password can not be more than 200 characters");
else:
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    console.print("[bold blue]pass: ", password);
    pyperclip.copy(password);
    console.print("[bold green]password coppied to the clipboard! 📋");