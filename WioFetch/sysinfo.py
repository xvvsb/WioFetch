import platform
import psutil
import socket
import os
import time
import ctypes
from colorama import Fore, Style, init

# Inicializa o Colorama para suporte a cores no Windows
init(autoreset=True)

# Define o título da janela do terminal
ctypes.windll.kernel32.SetConsoleTitleW("sys_infoByXVVSB")

# Função para calcular o tempo de uptime
def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time
    uptime_days = int(uptime_seconds // (24 * 3600))
    uptime_hours = int((uptime_seconds % (24 * 3600)) // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    return f"{uptime_days}d {uptime_hours}h {uptime_minutes}m"

# Funções para coletar as informações do sistema
def get_os_info():
    return platform.system(), platform.release()

def get_kernel():
    return platform.version()

def get_host():
    return socket.gethostname()

def get_process_count():
    return len(psutil.pids())

def get_shell():
    return os.getenv('SHELL', os.getenv('COMSPEC', 'cmd'))

def get_resolution():
    try:
        from screeninfo import get_monitors
        monitor = get_monitors()[0]
        return f"{monitor.width}x{monitor.height}"
    except ImportError:
        return "Desconhecido"

def get_de():
    return "Explorer.exe"

def get_wm():
    return "DWM"

def get_theme():
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return "Dark Mode" if value == 0 else "Light Mode"
    except:
        return "Unknown"

def get_icons():
    return "Windows Default"

def get_terminal():
    term = os.getenv('TERM_PROGRAM', '')
    if 'pwsh' in term or 'powershell' in term:
        return 'PowerShell'
    elif 'cmd' in term:
        return 'CMD'
    else:
        return 'Windows Terminal'

def get_cpu_info():
    return platform.processor()

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].name
        else:
            return "Integrated GPU (No dedicated GPU found)"
    except ImportError:
        return "Desconhecido (GPUtil não instalado)"

def get_memory_info():
    mem = psutil.virtual_memory()
    return mem.total, mem.available

# Função para criar o banner com personalização de cores
def print_banner(banner_text, colors):
    # Divide o banner em linhas
    banner_lines = banner_text.splitlines()

    # Verifica se o número de cores é suficiente
    if len(colors) < len(banner_lines):
        # Se houver menos cores que linhas, repetir as cores até igualar
        repeat_factor = (len(banner_lines) // len(colors)) + 1
        colors = (colors * repeat_factor)[:len(banner_lines)]

    # Imprime o banner linha por linha com a cor correspondente
    for i, line in enumerate(banner_lines):
        print(colors[i % len(colors)] + line)

# Função para exibir as informações do sistema no lado direito
def print_system_info(text_color):
    os_name, os_version = get_os_info()
    kernel_version = get_kernel()
    uptime = get_uptime()
    processes = get_process_count()
    shell = get_shell()
    resolution = get_resolution()
    de = get_de()
    wm = get_wm()
    theme = get_theme()
    icons = get_icons()
    terminal = get_terminal()
    cpu = get_cpu_info()
    gpu = get_gpu_info()
    total_mem, available_mem = get_memory_info()

    # Organiza as informações no lado direito
    sys_info = [
        f"{text_color}OS:{Style.RESET_ALL} {os_name} {os_version}",
        f"{text_color}Host:{Style.RESET_ALL} {get_host()}",
        f"{text_color}Kernel:{Style.RESET_ALL} {kernel_version}",
        f"{text_color}Uptime:{Style.RESET_ALL} {uptime}",
        f"{text_color}Processes:{Style.RESET_ALL} {processes}",
        f"{text_color}Shell:{Style.RESET_ALL} {shell}",
        f"{text_color}Resolution:{Style.RESET_ALL} {resolution}",
        f"{text_color}DE:{Style.RESET_ALL} {de}",
        f"{text_color}WM:{Style.RESET_ALL} {wm}",
        f"{text_color}Theme:{Style.RESET_ALL} {theme}",
        f"{text_color}Icons:{Style.RESET_ALL} {icons}",
        f"{text_color}Terminal:{Style.RESET_ALL} {terminal}",
        f"{text_color}CPU:{Style.RESET_ALL} {cpu}",
        f"{text_color}GPU:{Style.RESET_ALL} {gpu}",
        f"{text_color}Memory:{Style.RESET_ALL} {convert_bytes(available_mem)}/{convert_bytes(total_mem)}"
    ]

    # Ajusta para que a exibição seja alinhada à direita
    max_len = max(len(line) for line in sys_info)
    for line in sys_info:
        print(f"{line.rjust(max_len + 30)}")

# Função para exibir a paleta de cores no rodapé
def print_palette(colors):
    palette = ''.join([color + '█' * 8 for color in colors])
    print("\n" + palette)

# Função para converter bytes em unidades legíveis
def convert_bytes(size):
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {x}"
        size /= 1024.0

# Função principal
def main():
    # Personalização do banner e das cores
    banner_text = """
██╗  ██╗██╗   ██╗██╗   ██╗███████╗██████╗ 
╚██╗██╔╝██║   ██║██║   ██║██╔════╝██╔══██╗
 ╚███╔╝ ██║   ██║██║   ██║███████╗██████╔╝
 ██╔██╗ ╚██╗ ██╔╝╚██╗ ██╔╝╚════██║██╔══██╗
██╔╝ ██╗ ╚████╔╝  ╚████╔╝ ███████║██████╔╝
╚═╝  ╚═╝  ╚═══╝    ╚═══╝  ╚══════╝╚═════╝ 
"""
    # Gradiente de rosa para azul claro
    banner_colors = [Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.CYAN, Fore.LIGHTCYAN_EX]

    # Cor do texto das informações
    text_color = Fore.CYAN

    # Imprimir o banner
    print_banner(banner_text, banner_colors)
    
    # Imprimir as informações do sistema
    print_system_info(text_color)
    
    # Imprimir a paleta de cores no rodapé
    print_palette(banner_colors)

if __name__ == "__main__":
    main()
    input("\nPressione Enter para sair...")

 

