from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner_text = r"""
███╗   ██╗ ██████╗ ██╗  ██╗███╗   ██╗███████╗████████╗
████╗  ██║██╔═══██╗╚██╗██╔╝████╗  ██║██╔════╝╚══██╔══╝
██╔██╗ ██║██║   ██║ ╚███╔╝ ██╔██╗ ██║█████╗     ██║
██║╚██╗██║██║   ██║ ██╔██╗ ██║╚██╗██║██╔══╝     ██║
██║ ╚████║╚██████╔╝██╔╝ ██╗██║ ╚████║███████╗   ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝
                    NOXNET
        Network Tools in the Shadows
"""
    text = Text(banner_text, style="bold purple on black")
    console.print(Panel(text))
