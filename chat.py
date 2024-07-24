import flet as ft


def main(pagina):
    pagina.bgcolor = ft.colors.LIGHT_BLUE_ACCENT_400
    titulo = ft.Text("Chat ao vivo")

    titulo_janela = ft.Text("Bem vindo ao chat")
    campo_nome_usuraio = ft.TextField(label="Escreve seu nome")

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        texto_mensagem = ft.TextField(label="Escreva sua mensagem")
        pagina.add(texto_mensagem)
        botao_enviar = ft.ElevatedButton("Enviar")
        pagina.add(botao_enviar)
        pagina.update

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuraio,
        actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main, view=ft.WEB_BROWSER)
