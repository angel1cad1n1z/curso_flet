import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    # Lista de hábitos
    habits_list = [
        {"title": "Estudar inglês", "done": False},
        {"title": "Praticar violão", "done": False},
        {"title": "Estudar flet", "done": False},
        {"title": "Correr", "done": False},
        {"title": "Nadar", "done": False},
        {"title": "Lanche com o mozzi", "done": False},
    ]

    def change(e=None):
        if e:
            # para cada elemento da lista habits_list ele vai verificar qual label foi clicada e vai marcar ou desmarcar conforme ação do usuário. Exemplo: cliquei em Estudar inglês, ele verifica se tem uma label com esse nome e altera o done para true ou false dependendo da minha ação
            for hl in habits_list:
                if hl["title"] == e.control.label:
                    hl["done"] = e.control.value

        # soma todos os elementos que estão marcados como concluídos.
        # O filtro vai pegar só o que der verdadeiro, então se o done for false ele não retorna nada.
        # Ele pega cada elemento de habits_list e vai verificar qual o valor da variaável done e cmomo o filtersó retorna o que é verdadeiro ele retorna todos os dones que estão como true e salva numa nova lista já que estamos colocando eles dentro de um list
        done = list(filter(lambda x: x["done"], habits_list))

        # contagem total dos
        # tarefas concluidas dividido pelo total de elementos que tem em habits_list
        total = len(done) / len(habits_list)
        # altera o valor do progress bar e do text e atualiza
        progress_bar.value = total
        progress_text.value = f"{total: .0%}"
        progress_bar.update()
        progress_text.update()

    # Função para adicionar novos hábitos
    def add_habit(e):
        habits_list.append({"title": e.control.value, "done": False})
        habits_column.controls = [
            ft.Checkbox(
                label=hl["title"],
                value=hl["done"],
                on_change=change,
            )
            for hl in habits_list
        ]
        habits_column.update()
        e.control.value = ""
        e.control.update()
        change()

    # Coluna que exibirá os hábitos dinamicamente
    habits_column = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            ft.Checkbox(
                label=hl["title"],
                value=hl["done"],
                on_change=change,
            )
            for hl in habits_list
        ],
    )

    # Container que envolve os hábitos
    habits = ft.Container(
        expand=True,
        padding=ft.padding.all(10),
        bgcolor=ft.Colors.ORANGE_500,
        border_radius=ft.border_radius.all(8),
        margin=ft.margin.symmetric(vertical=10),
        content=habits_column,
    )

    # Layout principal
    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(value="Que bom ter você aqui.", size=30, color=ft.Colors.BLACK),
            ft.Text(
                value="Como estão seus hábitos hoje?", size=20, color=ft.Colors.BLACK
            ),
            ft.Container(
                padding=ft.padding.all(10),
                bgcolor=ft.Colors.BLACK,
                border_radius=ft.border_radius.all(8),
                margin=ft.margin.symmetric(vertical=10, horizontal=10),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="Sua evolução hoje", size=20, color=ft.Colors.ORANGE
                        ),
                        progress_text := ft.Text(
                            value="0%", size=50, color=ft.Colors.BLUE_GREY
                        ),
                        progress_bar := ft.ProgressBar(
                            value=0,
                            color=ft.Colors.ORANGE,
                            bgcolor=ft.Colors.INDIGO_100,
                            height=10,
                            border_radius=ft.border_radius.all(5),
                        ),
                    ],
                ),
            ),
            ft.Text(value="Hábitos de hoje", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(
                value="Marcar suas tarefas como concluídas te motiva a continuar focado.",
                size=20,
            ),
            habits,
            ft.Text(value="Adicionar novo hábito", size=20),
            ft.TextField(
                hint_text="Escreva um hábito...",
                border=ft.InputBorder.UNDERLINE,
                on_submit=add_habit,
            ),
        ],
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
