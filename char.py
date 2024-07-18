import flet as ft


def main(pagina):
    titulo = ft.Text("Chat ao vivo")

    titulo_janela = ft.Text("Bem vindo ao chat")
    campo_nome_usuraio = ft.TextField(label="Escreve seu nome")
    botao_entrar = ft.ElevatedButton("Entar no chat")

    janela = ft.AlertDialog(
        tittle=titulo_janela,
        content=campo_nome_usuraio,
        actions=[botao_entrar]

    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main, view=ft.WEB_BROWSER)
