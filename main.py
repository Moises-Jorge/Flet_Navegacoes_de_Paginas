import flet as ft


def main(page: ft.Page) -> None:
    # Configuracoes da pagina
    page.bgcolor = '#8ab9eb'
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'Navegacoes'
    page.window.width = 380
    page.window.height = 700
    page.window.maximizable = False
    
    
    # Criacao do botao central
    page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor='blue')
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    
    # Criacao da barra de navegacao inferior
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#f6f6f6ff',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE, icon_size=26),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLUE, icon_size=26),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLUE, icon_size=26),
                ft.IconButton(icon=ft.Icons.SHARE, icon_color=ft.Colors.BLUE, icon_size=26)
            ]
        )
    )
    
    
    # Criacao da Stack Principal
    
    
    # Criacao das funcoes
    
    
    # Criacao dos widgets
    
    
    # Adicao dos widgets na pagina
    page.add()


ft.app(target=main)