import flet as ft
import quiz
import random
import asyncio
import json
import os



c1 = '#060726'
c2='#00011d'
c3 = '#02054e'

arquivo_json = "dados.json"

# Se o arquivo não existir ou estiver vazio, cria um com um valor inicial
if not os.path.exists(arquivo_json) or os.stat(arquivo_json).st_size == 0:
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump({"pj": 0, "ra": 0, "re": 0, "max": 0}, arquivo, indent=4)

# Agora abre e lê o arquivo normalmente
with open(arquivo_json, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Verifica se "pj" existe no dicionário, se não existir, inicializa com 0
if "pj" not in dados:
    dados["pj"] = 0
if "ra" not in dados:
    dados["ra"] = 0
if "re" not in dados:
    dados["re"] = 0
if "max" not in dados:
    dados["max"] = 0

def salvar_dados():
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)



# Salva a alteração no arquivo JSON


class QuizApp:
    def __init__(self):
        self.a = 1
        self.acerto = 0
        self.erro =0
        self.index = 0
        

    def main(self, page: ft.Page):
        page.bgcolor = 'black'
        page.window.width = 450
        page.window.height = 850
        page.vertical_alignment = ft.VerticalAlignment.CENTER
        page.scroll = "auto"
        

        asyncio.run(self.update_quiz(page))

    async def update_quiz(self, page):
        
        if self.a >= len(quiz.matriz_quiz):
            self.a = 0
        
        quiz_per = quiz.matriz_quiz[self.a][0]
        Resp = [quiz.matriz_quiz[self.a][2], quiz.matriz_quiz[self.a][3], quiz.matriz_quiz[self.a][4], quiz.matriz_quiz[self.a][5]]
        random.shuffle(Resp)

        
            
        async def res(e):

            click.play()
            res_cer = quiz.matriz_quiz[self.a][2]
            certo.play() if e.control.content.value == res_cer else erro.play()

            
            if e.control.content.value == res_cer:
                e.control.content = ft.Text(value="Resposta Certa", color='white', size=15,)
                e.control.bgcolor = 'green'
                self.acerto += 1
                dados["ra"] += 1
                salvar_dados()
                if self.acerto > dados["max"]:
                    dados["max"] = self.acerto
                    salvar_dados() 
            else:
                e.control.content = ft.Text(value="Resposta Errada", color='white', size=15,)
                e.control.bgcolor = 'red'
                self.index = 0
                self.a = 0
                self.acerto = 0
                self.erro =0
                dados["re"] += 1
                salvar_dados()
                random.shuffle(quiz.matriz_quiz)

            page.update()  # Atualiza a página imediatamente para mostrar a resposta

            await asyncio.sleep(2)  # Aguarda 2 segundos antes de passar para a próxima pergunta
            self.a += 1
            await self.update_quiz(page)  # Atualiza o questionário para a próxima pergunta

        body = ft.Container(
            width=420,
            height=700,
            bgcolor=c1,
            alignment=ft.alignment.center,
            padding=20,
            border_radius= 20,
            content=ft.Column(
                [
                    ft.Container(
                        width = 400,
                        height = 250,
                        content=ft.Container(
                                    width=400,
                                    height=50,
                                    bgcolor=ft.Colors.BLACK12,
                                    border_radius=30,
                                    content= ft.Column(
                                        [
                                            
                                            ft.Container(
                                                width= 500,
                                                height= 50,
                                                padding= 10,
                                                alignment= ft.alignment.top_center,
                                                
                                                content= ft.Row(
                                                    [
                                                        ft.VerticalDivider(
                                                            width= 60,
                                                            color= 'transparent'),
                                                                ft.Text( value= "Pergunta:  ", size= 20, color= 'blue', weight= 'bold' ),
                                                                ft.Text( value= self.a, size= 20, color= 'blue', weight= 'bold' ),
                                                    ]

                                                )
                                                ),
                                            
                                            ft.Text(value=quiz_per, color='white', size=20),
                                            ]),
                                    padding=20,
                        ),
                    ),
                    ft.Container(
                        ft.Column([
                            ft.Container(
                                width=400,
                                height=50,
                                bgcolor='white12',
                                border_radius=10,
                                content=ft.Text(value=Resp[1], color='white', size=15, text_align= 'center'),
                                on_click=res,
                            ),
                            ft.Divider(height= 30),
                            ft.Container(
                                width=400,
                                height=50,
                                bgcolor='white12',
                                border_radius=10,
                                content=ft.Text(value=Resp[2], color='white', size=15,text_align= 'center'),
                                on_click=res,
                            ),
                            ft.Divider(height= 30),
                            ft.Container(
                                width=400,
                                height=50,
                                bgcolor='white12',
                                border_radius=10,
                                content=ft.Text(value=Resp[3], color='white', size=15,text_align= 'center'),
                                on_click=res,
                            ),
                            ft.Divider(height= 30),
                            ft.Container(
                                width=400,
                                height=50,
                                bgcolor='white12',
                                border_radius=10,
                                content=ft.Text(value=Resp[0], color='white', size=15,text_align= 'center'),
                                on_click=res,
                            )
                        ])
                            
                    )

                ]
            )
        )
        
        def change_scene(e):
            click.play()
            if self.index == 0:
                self.index = 1
            else:
                self.index = 0

            page.clean()  # Limpa a página antes de adicionar o novo conteúdo

            if self.index == 1:
                page.add(cont_inicio, body,creditos,click,erro,certo)
                dados["pj"] += 1
                salvar_dados()
            else:
                page.add(body1,click) 

            page.update()
        
        click = ft.Audio(src= "../assets/mouse_click.mp3", autoplay= False)
        certo = ft.Audio(src= "../assets/correct.wav", autoplay= False)
        erro = ft.Audio(src= "../assets/incorrect.wav", autoplay= False)
        
        cont_inicio= ft.Container(
            width= 500,
            height= 50,
            bgcolor= c1,
            border_radius= 20,
            padding= 5,
            content= ft.Row(
                [
                    ft.ElevatedButton(text= 'Voltar', icon= ft.Icons.HOME, scale= .8, on_click= change_scene),
                    ft.Text(value= " Tema: ", color= 'white', size= 10, weight= 'bold', text_align= 'center'),
                    ft.Text(value= quiz.matriz_quiz[self.a][1] , color= 'blue', size= 10, weight= 'bold',text_align= 'center'),
                    ft.VerticalDivider(
                        width= 5,
                        color= 'transparent'),
                    ft.Text(value= " Maximo acertos: ", color= 'white', size= 10, weight= 'bold', text_align= 'center'),
                    ft.Text(value= dados["max"] if self.acerto<= dados["max"] else self.acerto, color= 'blue', size= 10, weight= 'bold',text_align= 'center'),

                ]
            ),
            
        )
        
        
        creditos =ft.Row(
                [
                ft.Container(
                    width= 20,
                    height= 20,
                    content= ft.Image( src= "../assets/ico.webp", fit= 'cover' )
                ),
                ft.Text(value= " @ed7_game_dev"),
                ft.Container(
                    width= 20,
                    height= 20,
                    bgcolor= 'white',
                    content= ft.Image( src= "../assets/ico2.webp", fit= 'cover' )
                ),
                ft.Text(value= " ed7_gamedev",)
                ]
        )
        
        
        
        
        
        home = ft.Column(
            [
                ft.Container(
                        width= page.window.width * 0.9,
                        height= page.window.height * .40,
                        bgcolor= c3,
                        alignment= ft.alignment.center,
                        border_radius= 20,
                        
                        content= ft.Column(
                            [
                                ft.Container(
                                    width= (page.window.width * 0.9)/2,
                                    height= (page.window.height * .40)/2,
                                    alignment= ft.alignment.center_right,
                                    content= ft.Image(
                                            src="../assets/santola_quiz512x512.ico",
                                            offset=(.3,0),
                                            fit= 'cover',
                                        ),
                                    ),
                                ft.Text(value= " Bem Vindo a Santola Quiz, este quiz contém centenas de perguntas sobre o país de São Tomé E Príncipe, de varios temas aleatórios, jogue e tente sempre bater o seu record ",
                                        
                                        color= 'white', weight= ft.FontWeight.BOLD)
                            ],alignment= ft.alignment.bottom_center
                        )
                        
                    ),
                ft.Container(
                        width= page.window.width * .9,
                        height= 350,
                        bgcolor= c3,
                        padding= 20,
                        alignment= ft.alignment.center,
                        border_radius= 10,
                        content=ft.Column(
                                    [
                                    
                                    ft.ElevatedButton(icon= ft.Icons.PLAY_ARROW,text= "Começar", width= 200, height= 70, offset=(.40,.5) ,bgcolor= c2, color= 'white', on_click= change_scene),
                                            
                                    ft.Container(
                                        padding=10,
                                        
                                        content=ft.Row(
                                                
                                                controls=[
                                                    ft.Container(
                                                        width= 100,
                                                        height= 100,
                                                        bgcolor= 'white12',
                                                        offset=(0,1),
                                                        padding= 15,
                                                        border_radius= 10,
                                                        content= ft.Column(
                                                            [
                                                                ft.Text(value= "Partidas Jogadas:", size= 12 , weight='bold'),
                                                                
                                                                ft.Text(value= dados["pj"], color= c2, size= 20, weight= 'bold')
                                                            ],spacing= 10
                                                            
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width= 100,
                                                        height= 100,
                                                        bgcolor= 'white12',
                                                        offset=(0,1),
                                                        border_radius= 10,
                                                        padding= 15,
                                                        content= ft.Column(
                                                            [
                                                                ft.Text(value= "Respostas Corretas:", size= 12 , weight='bold'),
                                                                ft.Text(value= dados["ra"], color= c2, size= 20, weight= 'bold')
                                                            
                                                            ],spacing= 10
                                                            
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width= 100,
                                                        height= 100,
                                                        bgcolor= 'white12',
                                                        offset=(0,1),
                                                        border_radius= 10,
                                                        padding= 15,
                                                        content= ft.Column(
                                                            [
                                                                ft.Text(value= "Respostas Erradas:", size= 12, weight='bold'),
                                                                ft.Text(value= dados["re"], color= c2, size= 20, weight= 'bold')
                                                            ],spacing= 10
                                                            
                                                        )
                                                    )
                                                ], spacing= 30,
                                            )
                                        
                                        
                                        
                                        
                                        
                                        
                                        ),

                                    ]
                )
                        
                ),
                creditos

            ], spacing= 20
        )
        
        body1= ft.Container(
            width=420,
            height=830,
            bgcolor=c1,
            alignment=ft.alignment.center,
            padding=10,
            border_radius= 20,
            content=ft.Column(
                [
                    home
                ]
            )
        )

        page.clean()  # Limpa a página antes de adicionar o novo conteúdo
        page.add(cont_inicio,body,creditos,certo,erro,click
        )if self.index == 1 else  page.add(
            body1,
            click
        )
        page.update()
        
    
    
    
    
        
    

app = QuizApp()
ft.app(target=app.main)