import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    page.scroll = ft.ScrollMode.AUTO
    with open('./markdown.md') as f:
        markdown = f.read()

    md1 = ft.Markdown(
        value=markdown,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        # Sempre que usar e.data, você deve verificar se não é None antes de usar. Isso evita que sua aplicação quebre.
        on_tap_link=lambda e: page.launch_url(e.data) if e.data else None,
        code_theme=ft.MarkdownCodeTheme.DRAGULA,
            # ATOM_ONE_DARK
            # ATOM_ONE_LIGHT
            # GITHUB
            # MONOKAI
            # OBSIDIAN
            # SOLARIZED_LIGHT
            # TOMORROW_NIGHT
    )
    page.add(md1)
    
if __name__ == "__main__":
    ft.app(target=main)