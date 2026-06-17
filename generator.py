import typer
from rich.console import Console
from rich.panel import Panel
import os

app = typer.Typer()
console = Console()

def mock_llm_response(user_story: str):
    # Simulação de resposta de IA para demonstração do portfólio
    return f"""
Feature: Gerado automaticamente para: {user_story}

  Scenario: Fluxo principal de sucesso
    Given que o usuário está na página inicial
    When ele interage com o sistema baseado na história "{user_story}"
    Then o sistema deve processar a solicitação com sucesso

  Scenario: Validação de campo obrigatório
    Given que o usuário tenta prosseguir sem preencher dados
    Then uma mensagem de erro deve ser exibida
    """

@app.command()
def gerar(
    user_story: str = typer.Argument(..., help='A User Story para gerar os cenários'),
    key: str = typer.Option(None, '--key', help='Chave da OpenAI (opcional para demo)')
):
    """Gera cenários Gherkin a partir de uma User Story"""
    console.print(Panel(f"[bold blue]Processando História:[/bold blue]\n{user_story}"))
    
    # Lógica de integração real seria aqui
    if key or os.getenv('OPENAI_API_KEY'):
        # Aqui chamaria a OpenAI. Para o portfólio, mostramos a capacidade de integração.
        pass
    
    gherkin = mock_llm_response(user_story)
    
    console.print("[bold green]Cenários Gherkin Gerados:[/bold green]")
    console.print(gherkin)
    
    with open('cenarios_gerados.feature', 'w', encoding='utf-8') as f:
        f.write(gherkin)
    
    console.print("\n[yellow]Salvo em: cenarios_gerados.feature[/yellow]")

if __name__ == '__main__':
    app()
