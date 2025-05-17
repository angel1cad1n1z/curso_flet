import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    page.title = "Rows"
    # o padding only deixa um espaçamento em cima da tela
    page.padding = ft.padding.only(top=50)
    row1 = ft.Row(
        # a linha ocupa o espaço exato dos componentes, se tiver tres componentes na tela ela vai ter o tamnho total desses tres componentes - ela só expande até o final da paǵina ou se tiver o wrap ligado elaincrementa os componentes na linha abaixo  - para ocupar todo o espaço disponível é preciso ativar o expand aí sim ela ocupa todo o espaço que tem disponível na  aplicação
        # row recebe controls que é uma lista com todos os componentes que vão estar dentro dessa linha
        controls=[
            # se esses botões não estivessem eum uma linha eles ficariam um abaixo do outro. Aqui eles estão lado a lado
            ft.ElevatedButton(text="1", bgcolor="red", color="white"),
            ft.ElevatedButton(text="2", bgcolor="red", color="white"),
            ft.ElevatedButton(text="3", bgcolor="red", color="white"),
            
            # ft.ElevatedButton(text="4", bgcolor="green", color="white"),
            # ft.ElevatedButton(text="5", bgcolor="green", color="white"),
            # ft.ElevatedButton(text="6", bgcolor="green", color="white"),
            
            # ft.ElevatedButton(text="4", bgcolor="black", color="white"),
            # ft.ElevatedButton(text="5", bgcolor="black", color="white"),
            # ft.ElevatedButton(text="6", bgcolor="black", color="white"),
        ],
        
        # alignment=ft.MainAxisAlignment.START, # alinha os botões à esquerda da linha
        
        alignment= ft.MainAxisAlignment.CENTER, # alinha os botões no centro da linha - pega todo o espaço disponível, divide por dois e coloca na lateral do primeiro e último botão
        # alignment= ft.MainAxisAlignment.END # alinha os botões no final da linha
        # alignment=ft.MainAxisAlignment.SPACE_AROUND, # adiciona um espaço ao redor de cada componente - ele pega todo o espaço disponível na linha e divide em partes iguais, só que entre os botões é como se ele duplicasse.
        # alignment=ft.MainAxisAlignment.SPACE_EVENLY, # aqui os espaços entre os botões e as bordas da linha são iguais
        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # adiciona todo o espaço disponível apenas entre os componentes ficando o primeiro e o último componente colado na borda da linha
        
        spacing=25, # cria um espaçamento específico entre os componentes da linha e mesmo que aumente ou diminua a tela ele fica com esse espaço definido
        
        # wrap=True, # cria uma nova linha quando o espaçamento não cabe na linha atual - vem como padrão false
        
        run_spacing=25, # cria um espaçamento entre as linhas - por padrão vem como 10
        
        # vertical_alignment=ft.CrossAxisAlignment.CENTER, # alinha os botões verticalmente no centro - não funciona com wrap=True
        # vertical_alignment=ft.CrossAxisAlignment.BASELINE, # alinha os botões verticalmente na base
        # vertical_alignment=ft.CrossAxisAlignment.STRETCH, # estica os botões verticalmente
        # vertical_alignment=ft.CrossAxisAlignment.END, # alinha os botões verticalmente à direita
        
        vertical_alignment=ft.CrossAxisAlignment.START, # alinha os botões verticalmente à esquerda     
        
        # expand=True, # expande os botões para preencher o espaço total disponível da tela 
    )
    
    row2 = ft.Row(
        
        controls=[
            ft.Image(height=200, src="https://letsenhance.io/static/73136da51c245e80edc6ccfe44888a99/1015f/MainBefore.jpg"),
            ft.Image(height=200, src="https://static.vecteezy.com/ti/fotos-gratis/t2/36324708-ai-gerado-cenario-do-uma-tigre-caminhando-dentro-a-floresta-foto.jpg"),
            ft.Image(height=200, src="https://blog.emania.com.br/wp-content/uploads/2016/02/direitos-autorais-e-de-imagem.jpg"),
            ft.Image(height=200, src="https://thumbs.dreamstime.com/b/imagem-de-fundo-bonita-do-c%C3%A9u-da-natureza-64743176.jpg"),
            ft.Image(height=200, src="https://mariananardi.com.br/wp-content/uploads/2018/09/Gato-x-leao.jpg"),
        ],
        scroll=ft.ScrollMode.AUTO, # verifica automaticamente se o componente precisa habilitar o scroll
        # auto_scroll= True, # faz a rolagem automática para o final
    )
    
    """ 
    são baseados em tamanhos em px que a aplicação tem entre menos de 576px até mais de 400px tem um breakpoint especifico que podemos utilizar para definir o tamanho que queremos nosso componente
    Breakpoint      Dimension (px)
        xs            < 576
        sm           >= 576
        md           >= 768
        xl           >= 1200
        xx           >= 1400
    """
    
    row3 = ft.ResponsiveRow(
        # o componente ocupa todo o espaço disponivel da linha - para que esse esppaço possa ser modificado precisamos usar o parâmetro columns abaixo
        columns=12, # quantidade de colunas que o elemento vai ocupar na tela - vem por padrão definido como 12 - é como se tivéssemos 12 espaços - o espaço total da aplicação dividido por 12
        run_spacing= 15,
        spacing= 15,
        expand= True,
        controls=[
            ft.ElevatedButton(
                # quando não tiver o parâmetro col no componente ele vai ocpupar todo o espaço disponível
                # O col pode ter um numero específico ou usar os breakpoints abaixo - se for um numero especifico, por exemplo 4, o componente vai usar 4 das 12 colunas que definimos acima independente do tamanho da tela
                col= {'sm': 4, 'md': 3, 'lg': 2, 'xl': 1}, # sse componente vai ocupar 4,3,2 ou 1  das 12 colunas definidas acima dependendo do tamanho da tela em px
                text='1',
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # ele tabem pode ocupar tamanhos diferentes na aplicação utilizando os breakpoints
                col= {'sm': 4, 'md': 3, 'lg': 2, 'xl': 1}, # esse componente vai ocupar 4,3,2 ou 1  das 12 colunas definidas acima dependendo do tamanho da tela em px
                text="2",
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 3, 'lg': 2, 'xl': 1}, # esse componente vai ocupar 4,3,2 ou 1 das 12 colunas definidas acima dependendo do tamanho da tela
                text="3",
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 3, 'lg': 6}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="4",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 3, 'lg': 6}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="5",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 3, 'lg': 6}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="6",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 7, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="7",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 6, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="8",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="9",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
        ],
        
    )
    
    page.add(row1, row2, row3)

ft.app(main)