import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    """
    ASPECT      RADIO
    9:16        0.56
    2:3         0.66
    1:1         1.0
    16:9        1.77
    """
    
    grid = ft.GridView(
        controls = [
            ft.Image(src= f'https://picsum.photos/250/300?{num}', fit= 'cover') for num in range( 20 )],
        # runs_count= 2, #define quanto componentes terão por cada linha
        padding= 5,
        spacing= 15,
        run_spacing= 15,
        max_extent= 200, #aplica um tamanho máximo em pixels para cada componente - nesse caso o runs_count pode ser desconsiderado
        expand= True, # ocupa todo o espaço disponível da app - com isso ele habilita o scroll
        # auto_scroll= True,
        child_aspect_ratio= 0.9, #pode-se usar a tabela acima  para usar os valores padrões ou editar da maneira que desejar
        
    )
    page.add(grid)

ft.app(main)