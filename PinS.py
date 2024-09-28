import random, string, hashlib, base64
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def gen(length, letters=True, numbers=True, symbols=True):
    chars = (string.ascii_letters if letters else "") + (string.digits if numbers else "") + (string.punctuation if symbols else "")
    return ''.join(random.choice(chars) for _ in range(length))

def strength(password):
    s = sum([len(password) >= 8, any(c.isupper() for c in password), any(c.islower() for c in password),
             any(c.isdigit() for c in password), any(c in string.punctuation for c in password)])
    return f"[{'red' if s<3 else 'yellow' if s<4 else 'green'}]{'█'*s}{'░'*(5-s)}[/]"

def encode(password, method):
    return getattr(hashlib, method)(password.encode()).hexdigest() if method != 'base64' else base64.b64encode(password.encode()).decode()

def print_banner():
    console.print(Panel("[bold red]██████╗ ██╗███╗   ██╗███████╗\n██╔══██╗██║████╗  ██║██╔════╝\n██████╔╝██║██╔██╗ ██║███████╗\n██╔═══╝ ██║██║╚██╗██║╚════██║\n██║     ██║██║ ╚████║███████║\n╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝[/bold red]", 
                        title="[bold cyan]Creator: @AFoid_official[/bold cyan]", border_style="red"))

def menu(options):
    table = Table(show_header=False, border_style="red")
    for i, option in enumerate(options, 1):
        table.add_row(f"[{i}] {option}", style=["cyan", "magenta", "green", "yellow", "blue"][i % 5])
    console.print(Panel(table, title="[bold]Меню[/bold]", border_style="red"))
    return console.input("[bold red]Выберите опцию: [/bold red]")

def password_menu():
    length = int(console.input("[bold]Длина пароля: [/bold]"))
    password = gen(length, 
                   console.input("[bold]Буквы? (д/н): [/bold]").lower() == 'д',
                   console.input("[bold]Цифры? (д/н): [/bold]").lower() == 'д',
                   console.input("[bold]Символы? (д/н): [/bold]").lower() == 'д')
    console.print(Panel(f"[bold]Пароль:[/bold] {password}\n[bold]Сила:[/bold] {strength(password)}", 
                        title="[bold]Сгенерированный пароль[/bold]", border_style="cyan"))

def encoding_menu():
    password = console.input("[bold]Введите пароль для кодирования: [/bold]")
    table = Table(title="Результаты кодирования", border_style="magenta")
    table.add_column("Метод", style="cyan", justify="right")
    table.add_column("Результат", style="magenta")
    for method in ['sha256', 'md5', 'sha1', 'base64']:
        table.add_row(method.upper(), encode(password, method))
    console.print(table)

def analyze_password():
    password = console.input("[bold]Введите пароль для анализа: [/bold]")
    s = sum([len(password) >= 12, any(c.isupper() for c in password), any(c.islower() for c in password),
             any(c.isdigit() for c in password), any(c in string.punctuation for c in password)])
    advice = ["Используйте не менее 12 символов", "Добавьте заглавные буквы", "Добавьте строчные буквы",
              "Добавьте цифры", "Добавьте специальные символы"]
    console.print(Panel(f"[bold]Сила:[/bold] {strength(password)}\n[bold]Советы:[/bold]\n" + 
                        "\n".join(f"• {advice[i]}" for i in range(5) if not (s & (1 << i))), 
                        title="[bold]Анализ пароля[/bold]", border_style="yellow"))

def generate_passphrase():
    words = ['sjskks', 'jsjs', 'gajjqkM', 'jskwlqmzmm', 'sjsjskkm', 'qqqpq', 'sjsjjsqq', 'zebr', 'iris', 'sssjsjsdnp', 
             'zzzzzs', 'sjkaax', 'owosoz', 'jdjdjdj', 'oqkdjz', 'sjkaxx', 'jsjs', 'hsjs', 'jsjs', 'Gak']
    passphrase = ' '.join(random.choice(words) for _ in range(4))
    console.print(Panel(f"[bold]Парольная фраза:[/bold] {passphrase}", 
                        title="[bold]Сгенерированная парольная фраза[/bold]", border_style="green"))

def generate_temporary_password():
    length = random.randint(12, 16)
    password = gen(length)
    console.print(Panel(f"[bold]Временный пароль:[/bold] {password}\n[bold]Действителен:[/bold] 24 часа", 
                        title="[bold]Временный пароль[/bold]", border_style="blue"))

def main():
    while True:
        print_banner()
        choice = menu(["Генерация пароля", "Кодирование", "Анализ пароля", "Парольная фраза", 
                       "Временный пароль", "Выход"])
        if choice == '1': password_menu()
        elif choice == '2': encoding_menu()
        elif choice == '3': analyze_password()
        elif choice == '4': generate_passphrase()
        elif choice == '5': generate_temporary_password()
        elif choice == '6': break
        else: console.print("[bold red]Неверный выбор. Попробуйте снова.[/bold red]")

if __name__ == "__main__":
    main()