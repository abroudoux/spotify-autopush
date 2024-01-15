import typer
from rich import print

app = typer.Typer(rich_help_panel="rich")

@app.command(rich_help_panel="Utils & Configs")
def get():
