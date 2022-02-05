#!/usr/bin/env python3
import secrets;
import string;
import pyperclip;
from rich.console import Console;
from rich.panel import Panel;

console = Console();
srandom = secrets.SystemRandom;
alphabet = string.ascii_letters + string.digits + string.punctuation;

console.print(Panel("🔒  [bold green] spg: secure password generator [/] 🔒 ", expand=False, border_style="red"));
lengthnum = console.input("[yellow] password length: ");
length = int(lengthnum);
if length < 0:
    console.print("❌ [red]The password can not be less than zero");
else:
    password = ''.join(secrets.choice(alphabet) for i in range(length));
    console.print("[bold blue]pass: ", password);
    pyperclip.copy(password);
    console.print("[bold green]password coppied to the clipboard! 📋");
