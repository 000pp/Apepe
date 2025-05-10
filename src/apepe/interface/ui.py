from rich.console import Console
console = Console()

def get_banner() -> str:
    '''
    This function will return the main banner from the application
    '''

    console.print(f"\n[bright_white]Apepe - Android App Analyzer v1.5[/]\n", highlight=False)