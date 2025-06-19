import flet as ft


def main(page: ft.Page):
    page.title = "Perfil do Usuário"
    page.bgcolor = "#F8F9FA"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    # MENU LATERAL
    menu_lateral = ft.Column(
        controls=[
            ft.Container(
                bgcolor="#00AFC6",
                width=60,
                height=800,
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.PERSON, color="white"),
                        ft.Icon(ft.Icons.DASHBOARD, color="white"),
                        ft.Icon(ft.Icons.LIST, color="white"),
                        ft.Icon(ft.Icons.SETTINGS, color="white"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                ),
                padding=10,
            )
        ]
    )

    # CABEÇALHO COM TÍTULO + LOGO NO CANTO DIREITO
    cabecalho = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Perfil de Priscila Aranha", size=22, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Image(
                    src="assets/images/logo_rota_reduzida.png",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                ),
                padding=ft.padding.only(right=10, top=10),
                alignment=ft.alignment.top_right,
            ),
        ],
    )

    # BLOCO: EDITAR PERFIL
    bloco_editar_perfil = ft.Container(
        alignment=ft.alignment.center,
        height=400,
        bgcolor="white",
        border=ft.border.all(1, "#D9D9D9"),
        border_radius=10,
        padding=20,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Editar Perfil", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "Mantenha os dados atualizados para uma melhor experiência com uma comunicação eficiente.",
                            size=12,
                        ),
                    ],
                ),
                ft.Divider(),
                ft.TextField(label="Nome Completo", border_radius=10),
                ft.Row(
                    [
                        ft.TextField(
                            label="Celular",
                            expand=True,
                            border_radius=10,
                        ),
                        ft.TextField(
                            label="Função no Sistema",
                            expand=True,
                            # border=ft.InputBorder.OUTLINE,  # OUTLINE ou UNDERLINE
                            border_radius=10,
                        ),
                    ]
                ),
                ft.TextField(label="E-mail", border_radius=10),
                ft.Container(
                    alignment=ft.alignment.center_right,
                    content=ft.ElevatedButton(
                        "Salvar", bgcolor="#00AFC6", color="white"
                    ),
                ),
            ],
            spacing=10,
        ),
    )

    # BLOCO: SEGURANÇA
    bloco_seguranca = ft.Container(
        alignment=ft.alignment.center,
        height=400,
        bgcolor="white",
        border=ft.border.all(1, "#D9D9D9"),
        border_radius=10,
        padding=20,
        width=350,
        content=ft.Column(
            [
                ft.Text("Segurança", size=18, weight=ft.FontWeight.BOLD),
                # ft.Text("Revise suas senhas, acessos e autorizações.", size=12),
                ft.Divider(),
                ft.Text("Senha de Acesso", size=14, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Sua senha é única e criptografada. Para alterá-la, clique no botão abaixo e siga as instruções enviadas para o seu e-mail cadastrado.",
                    size=12,
                ),
                ft.Container(
                    alignment=ft.alignment.center_right,
                    border_radius=10,
                    content=ft.ElevatedButton(
                        "Alterar Senha",
                        bgcolor="#00AFC6",
                        color="white",
                    ),
                ),
                ft.Divider(),
                ft.Text("Duração de Sessão", size=14, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Defina as durações de tempo limite para sua sessão na plataforma para melhorar a segurança e a confiabilidade.",
                    size=12,
                ),
                ft.Container(
                    alignment=ft.alignment.center_right,
                    content=ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Sempre"),
                            ft.dropdown.Option("Diário"),
                            ft.dropdown.Option("Semanal"),
                            ft.dropdown.Option("Mensal"),
                            ft.dropdown.Option("Nunca"),
                        ],
                        width=200,
                        value="Sempre",
                        border_radius=10,
                    ),
                ),
            ],
            spacing=10,
        ),
    )

    # CONTEÚDO PRINCIPAL
    conteudo_principal = ft.Column(
        [
            cabecalho,
            ft.ResponsiveRow(
                columns=12,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Container(
                        content=bloco_editar_perfil,
                        col={"sm": 12, "md": 8, "xl": 8},
                    ),
                    ft.Container(
                        content=bloco_seguranca,
                        col={"sm": 12, "md": 4, "xl": 4},
                    ),
                ],
                spacing=10,
            ),
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )

    # ESTRUTURA FINAL
    page.add(
        ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[menu_lateral, conteudo_principal],
        )
    )


ft.app(target=main)
