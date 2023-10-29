'''
PROJETO DO INTERDISCIPLINAR DE 2023.2 DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - ADS4NB (2023.2)
UNIVERSIDADE: UNIBRA (CENTRO UNIVERSITÁRIO BRASILEIRO)

DESENVOLVIMENTO FRONT / BACK : Jonathan, Jorge, Victor e Henrique
UX/UI : Azuos, Thiago

>> PARA FUNCIONAMENTO DO CÓDIGO RECOMENDAMOS OS ITENS ABAIXO

1 - Ter o Python da versão 3.10 ou superior: (https://www.python.org/)
2 - Instalar na máquina local, (não rodar no replit ou compilador online)

Recomendações: Recomendamos os compiladores:

* Pycharm (https://www.jetbrains.com/pt-br/pycharm/)
* VsCode (https://code.visualstudio.com/)

------------------------------------------------------------------------------------------------------------

>> RECURSOS PARA O SOFTWARE
>> instalando package
>> Verificação de pacotes e versões: pip freeze


Kivy==2.2.1
kivy-deps.angle==0.3.3
kivy-deps.glew==0.3.1
kivy-deps.gstreamer==0.3.3
kivy-deps.sdl2==0.6.0
Kivy-Garden==0.1.5
kivymd==1.1.1
pandas==2.1.0

------------------------------------------------------------------------------------------------------------

>> RECURSOS PARA BANCO DE DADOS

1 - arquivo .csv

-------------------------------------------------------------------------------------------------------------

INFORMAÇÕES DO DEPLOY .PY PARA APK

Ferramenta: Google Colab
Cython: 0.29.34
Kivy: 2.2.1

-------------------------------------------------------------------------------------------------------------

>> "this life academy" 

'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox


# Criando múltiplas telas para fins de rolagem
# e controle o gerenciador de tela a partir dos arquivos .kv


# PRIMEIRA TELA
Builder.load_string("""
<Interface>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "inicio.png"    
            
        
    
    RelativeLayout:
        Button:
            pos: 1, 1
            size: 1000, 1000
            multiline: False
            text: ""
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'login'
            on_press: app.root.current = 'login'                 
                   

""")

# MENU LOGIN COM CADASTRO
Builder.load_string("""
<LoginWindow>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "tela_login.png"
            
    
    email : email
    pwd : pwd
    
    RelativeLayout:
    
        size: root.width, root.height
        Label:
            text: ""
            color: 0,0,0,1
            size_hint: 0.8, 0.1
            pos_hint : {"x" : 0.1, "top" : 0.9}
            font_size: 25
            
        Label:
            text : "LOGIN "
            size_hint : 0.1, 0.1
            pos_hint : {"x":0.25, "top":0.80}
        TextInput:
            hint_text: 'Informe seu E-mail'
            id : email
            multiline :False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.27, "top" : 0.68}
            
            
        Label:
            text : " " #SENHA
            color: 0,0,0,1
            size_hint : 0.2, 0.1
            pos_hint : {"x" : 0.18, "top" : 0.6}
        TextInput:
            hint_text: 'Digite sua senha'
            id : pwd
            multiline :False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.27, "top" : 0.62}
            password: True
        
        Button:
            # text : "ENTRAR" 
            size_hint : 0.2, 0.15
            pos_hint : {"x" : 0.43, "top" : 0.52}
            background_color: 1, 2, 0, 0
            on_release: 
                # root.validate()
                root.manager.transition.direction = "up"
                app.root.current = 'Page 0'
                    
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnlogin.png"
                        

        Button:
            # text: "Criar Nova Conta"
            pos_hint: {"x" : 0.33, "top" : 0.40}
            size: 1, 1
            size_hint: 0.4, 0.15
            background_color: 1, 1, 12, 0
            on_press: root.manager.current = 'signup'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnnovaconta.png"
                    
        Button:
            # text: "Esqueci a senha"
            pos_hint: {"x" : 0.33, "top" : 0.27}
            size: 1, 1
            size_hint: 0.4, 0.15
            background_color: 10, 0, 0, 0
            on_press: root.manager.current = 'EsqueciSenha'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnesqueciasenha.png"

        
        Button:
            # text: "Nossa História"
            pos_hint: {"x" : 0.43, "top" : 0.16}
            size: 1, 1
            size_hint: 0.2, 0.15
            background_color: 1, 2, 2, 0
            on_press: 
                import webbrowser
                webbrowser.open('https://site-ong-jorge-gabriels-projects.vercel.app/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnsite.png"
            
            
                        
""")

# MENU CRIAÇÃO DE CONTA
Builder.load_string("""
<SignupWindow>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundo1.png"
            
    name2 : name2
    email : email
    pwd : pwd
    
               
    RelativeLayout:
                    
        Label:
            text: "CADASTRO"
            pos_hint : {"x" : 0.03, "top" : 1.45}
            font_size: 25
                    
        Label:
            text : "Nome: "
            size_hint : 0.1, 0.1
            pos_hint : {"x":0.15, "top":0.81}
        TextInput:
            hint_text: 'Informe seu nome'
            id : name2
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.78}
            
            
        Label:
            text : "E-mail: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.71}
        TextInput:
            hint_text : 'Digite seu melhor e-mail'
            haling: 'center'
            id : email
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.68}
            
            
        Label:
            text : "Senha: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.61}
        TextInput:
            hint_text: 'Escolha uma senha forte'
            haling: 'center'
            id : pwd
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.58}
            password: True
            
            
        Button:
            # text : "CRIAR"
            size_hint : 0.2, 0.15
            background_color: 1, 2, 0, 0
            pos_hint : {"x" : 0.43, "top" : 0.42}
            on_press :
                root.manager.current = 'CadastroLogin'  
                root.manager.curreent = 'LogDataWindow' 
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btncriar.png" 
                                        
        Button:
            # text: "LOGIN"
            pos_hint: {"x": 0.43, "top": 0.28}
            size_hint : 0.2, 0.16
            background_color: 1, 1, 12, 0
            on_press: root.manager.current = 'login'  
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnsair.png"  
                    
""")

#ESQUECI A SENHA

Builder.load_string("""
<EsqueciSenha>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundo1.png"
            
               
    RelativeLayout:
                    
        Label:
            text: "REDEFININDO SENHA"
            pos_hint : {"x" : 0.03, "top" : 1.45}
            font_size: 25
                    
        Label:
            text : "E-mail: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.17, "top" : 0.71}
        TextInput:
            hint_text : 'Informe seu e-mail'
            haling: 'center'
            id : email
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.32, "top" : 0.68}
            
            
        Label:
            text : "Senha Nova: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.17, "top" : 0.61}
        TextInput:
            hint_text: 'Escolha uma senha'
            haling: 'center'
            id : pwd
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.32, "top" : 0.58}
            password: True
                    
        Label:
            text : "Confirmar: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.17, "top" : 0.51}
        TextInput:
            hint_text: 'Confirme a senha'
            haling: 'center'
            id : pwd
            multiline : False
            size_hint : 0.5, 0.05
            pos_hint : {"x" : 0.32, "top" : 0.48}
            password: True
            
            
        Button:
            # text : "REDEFINIR"
            size_hint : 0.2, 0.15
            background_color: 1, 2, 0, 0
            pos_hint : {"x" : 0.43, "top" : 0.38}
            on_press :
                root.manager.current = 'RedefinirSenha' 
                    
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnredefinir.png"
               
                                        
        Button:
            # text: "VOLTAR"
            pos_hint: {"x": 0.44, "top": 0.24}
            size_hint : 0.19, 0.14
            background_color: 1,2,0,0
            on_press: root.manager.current = 'login'  
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png"  
                    
""")

Builder.load_string("""
<RedefinirSenha>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "redefinirsenha.png"
            
               
    RelativeLayout:
                                             
        Button:
            # text: "LOGIN"
            pos_hint: {"x": 0.43, "top": 0.32}
            size_hint: 0.2, 0.07
            background_color: 1, 2, 0, 0
            on_press: root.manager.current = 'login'   
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnlogin.png" 
                    
""")


Builder.load_string("""
<CadastroLogin>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "cadastro.png"                    

    RelativeLayout:
                    
        Button:
            # text : "ENTRAR"
            pos_hint : {"x" : 0.43, "top" : 0.30}
            size_hint:0.2, 0.15
            background_color: 0,1,0,0
            on_release: 
                app.root.current = 'login'
                root.manager.transition.direction = "down"
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnlogin.png"
                    

""")

# Validação do cadastro
Builder.load_string("""
<LogDataWindow>:
    info : info
    FloatLayout:
        Label:
            id : info
            size_hint : 0.8, 0.2
            pos_hint : {"x" : 0.15, "top" : 0.8}
            text : "Conta criada com Sucesso !!!"
        Button:
            text : "Entrar"
            size_hint : 0.4, 0.1
            pos_hint : {"x" : 0.33, "top" : 0.55}
            background_color: 1, 2, 0, 0.8
            on_release: 
                app.root.current = 'login'
                root.manager.transition.direction = "down"
        Button:
            text : "Criar nova conta"
            size_hint : 0.4, 0.1
            pos_hint : {"x" : 0.33, "top" : 0.4}
            on_release: 
                app.root.current = 'signup'
                root.manager.transition.direction = "down"
""")

Builder.load_string("""
<P>:
    Label:
        text: "Endereço de E-mail NÃO existe."
        size_hint: 0.2, 0.1 
        pos_hint: {"x": 0.3, "top": 0.8}   
""")

Builder.load_string("""
<Q>:
    Label:
        text: "Usuário Inválido !!!"
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")

Builder.load_string("""
<R>:
    Label:
        text: "Conta criada com sucesso! !"
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")

Builder.load_string("""
<S>:
    Label:
        text: "Seja Bem vindo(a) !!!"
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")

Builder.load_string("""
<SubscriptionPage>:
    
    GridLayout:
        Button:
            text: "Sair do Aplicativo"
            size: 200, 60
            on_press: root.manager.current = 'Pagina Login' 
""")


# PAGINA 0 - Menu Principal
Builder.load_string("""
<Menu>: 
    
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogato.png"
            
    Widget:
        Label:
            markup: True
            text: "[b] [/b]"
            color: 0,0,0,1
            pos: 130, 450
            font_size: 25
            
    RelativeLayout:
    
        Button:
            # text: "ADOTAR"
            pos_hint : {"x" : 0.35, "top" : 0.85}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page TipoAnimal'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnadotar.png"
            
    
        Button:
            # text: "DOAR"
            pos_hint : {"x" : 0.35, "top" : 0.65}
            size_hint:0.3, 0.2
            background_color: 9, 1, 1, 0
            on_press: root.manager.current = 'Page DoarAnimal'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btndoar.png"
            
        Button:
            # text: "CONTRIBUIR"
            pos_hint : {"x" : 0.35, "top" : 0.45}
            size_hint:0.3, 0.2
            background_color: 0,1,0,0
            on_press: root.manager.current = 'Page Contribuir'  
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btncontribuir.png" 
               
            
            
                    
""")

# TIPO DE ANIMAL CACHORRO OU GATO
Builder.load_string("""
<TipoAnimal>:
    
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "tela_login.png" 
            
        # #FAVICONS
        # Rectangle:
        #     pos: 90,280
        #     size: 50, 50
        #     source: "fcat.png"  
            
        # Rectangle:
        #     pos: 90, 380
        #     size: 50, 50
        #     source: "fdog.png"

    RelativeLayout:
        Widget:
            Label:
                # markup: True
                # text: "[b] Selecione o Pet [/b]"
                # color: 0,0,0,1
                # pos: 130, 450
                # font_size: 25
                
        Button:
            # text: "CACHORRO"
            pos_hint : {"x" : 0.35, "top" : 0.80}
            size_hint:0.3, 0.22
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page CachorroPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btncachorro.png"
            
             
    
        Button:
            # text: "GATO"
            pos_hint : {"x" : 0.35, "top" : 0.60}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page GatoPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btngato.png"
            
        
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.41, "top" : 0.30}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 0' 
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                
""")

#---------------------------------------------------------------------------
# PAGINA DE DOAÇÃO ANIMAL
Builder.load_string("""
<DoarAnimal>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogato.png"
         
    RelativeLayout:
        Label:
            text : "Nome: "
            size_hint : 0.1, 0.1
            pos_hint : {"x":0.15, "top":0.95}
        TextInput:
            hint_text: 'Nome do doador'
            id : name2
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.92}
            
            
        Label:
            text : "CPF: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.85}
        TextInput:
            hint_text: 'CPF do doador'
            id : cpf
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.82}
            
            
        Label:
            text : "Animal: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.75}
        TextInput:
            hint_text: 'Gato ou Cachorro'
            id : animal
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.72}
            
        Label:
            text : "Porte: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.65}
        TextInput:
            hint_text: 'Pequeno, Médio ou Grande'
            id : porte
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.62}
            
        Label:
            text : "Obs.: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.55}
        TextInput:
            hint_text: 'Detalhe mais informações'
            id : info
            multiline : True
            size_hint : 0.6, 0.18
            pos_hint : {"x" : 0.28, "top" : 0.52}
            
            
        Button:
            # text : "CONFIRMAR"
            size_hint : 0.2, 0.15
            background_color: 0, 1, 0 , 0
            pos_hint : {"x" : 0.35, "top" : 0.25}
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnconfirmar.png"
            
                   
                                        
        Button:
            # text: "VOLTAR"
            pos_hint: {"x": 0.57, "top": 0.23}
            size_hint: 0.2, 0.13
            background_color: 10, 0, 0, 0
            on_press: root.manager.current = 'Page 0'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png"                   
""")

#---------------------------BOTÃO CONTRIBUIR---------------------------------------
Builder.load_string("""
<Contribuir>:

    canvas.before:
        
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundo1.png"
         
    RelativeLayout:
    
        Label:
            text: "Informações do Doador"
            pos_hint : {"x" : 0.03, "top" : 1.45}
            font_size: 25
         
        Label:
            text : "Nome: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.85}
        TextInput:
            hint_text: 'Informe o nome'
            id : nome
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.82}
            
            
        Label:
            text : "CPF: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.75}
        TextInput:
            hint_text: 'Preencha o CPF'
            id : cpf
            multiline : False
            size_hint : 0.6, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.72}
            
        Label:
            text : "Valor: "
            size_hint : 0.1, 0.1
            pos_hint : {"x" : 0.15, "top" : 0.65}
        TextInput:
            hint_text: 'Informe o valor'
            id : valor
            multiline : False
            size_hint : 0.4, 0.05
            pos_hint : {"x" : 0.28, "top" : 0.62}
            
            
            
        Button:
            # text : "DOAR"
            size_hint : 0.2, 0.15
            background_color: 0, 1, 0 , 0
            pos_hint : {"x" : 0.33, "top" : 0.45}
            on_press: root.manager.current = 'Page QrCode'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btndoara.png"
                   
                                        
        Button:
            # text: "VOLTAR"
            pos_hint: {"x": 0.54, "top": 0.45}
            size_hint : 0.2, 0.15
            background_color: 10, 0, 0, 0
            on_press: root.manager.current = 'Page 0'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<QrCode>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundoqrcode.png"
                    
    # RelativeLayout:
    #     canvas.before:
    #         Rectangle:
    #             pos: 820, 500
    #             size: 300, 300
    #             source: "qrcode.png" 

                                     
    RelativeLayout:
    
        Button:
            text: ""
            pos_hint : {"x" : 0.23, "top" : 0.78}
            size_hint:0.55, 0.40
            background_color: 0,0,0,0
            on_press:
                root.manager.current = 'Pagamento'
               
        # Button:
        #     text : "SITE"
        #     size_hint : 0.3, 0.08
        #     background_color: 0, 1, 0 , 1
        #     pos_hint : {"x" : 0.21, "top" : 0.25}
        #     on_press: 
        #         import webbrowser
        #         webbrowser.open('https://www.google.com.br')
                                            
        Button:
            # text: "VOLTAR"
            pos_hint: {"x": 0.42, "top": 0.25}
            size_hint: 0.2, 0.15
            background_color: 10, 0, 0, 0
            on_press: root.manager.current = 'Page 0'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                    


""")

#PÁGINA FINAL DO PAGAMENTO
Builder.load_string("""
<Pagamento>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "pagamentoconfirmado.png"
            
               
    RelativeLayout:
                                             
        Button:
            # text: "VOLTAR"
            pos_hint: {"x": 0.42, "top": 0.25}
            size_hint: 0.2, 0.15
            background_color: 10, 0, 0, 0
            on_press: root.manager.current = 'Page 0'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png"     
                    
""")

#---------------------------------------------------------------------------
# PAGINA 1 - Tela com os menus e as áreas PaginaUm
#Cachorro Porte
Builder.load_string("""
<CachorroPorte>: 
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundo1.png"
    
            

    RelativeLayout:
                    
        Label:
            text: "Qual porte ?"
            pos_hint : {"x" : 0.00, "top" : 1.45}
            font_size: 25

     
        Button:
            # text: "PEQUENO"
            pos_hint : {"x" : 0.35, "top" : 0.90}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page CachorroPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnpequeno.png"
    
        
        Button:
            # text: "MÉDIO"
            pos_hint : {"x" : 0.35, "top" : 0.73}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page CachorroMedio'   
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnmedio.png" 
        
    
        Button: 
            # text: "GRANDE"
            pos_hint : {"x" : 0.36, "top" : 0.54}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page CachorroGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btngrande.png"
                    

        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page TipoAnimal'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
            
        
            
""")

# CACHORRO PEQUENO PORTE
Builder.load_string("""
<CachorroPequeno>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundocachorropequeno.png"
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "cp1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "cp2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "cp3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "cp4.png"
            
            
    RelativeLayout:
        
        # Label:
        #     text: " Cachorro Pequeno Porte "
        #     pos: 5, 440
        #     font_size: 25

        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPorte'  
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png"           
                
        
        #BOTÃO DE REDIRECIONAMENTO P1 
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.85}
            background_color: 1,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogPUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO P2
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.85}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogPDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO P3
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogPTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO P4
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogPQuatro'           
""")
# CACHORRO MÉDIO PORTE
Builder.load_string("""
<CachorroMedio>:
    canvas.before:
        Color: 
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "fundocachorromedio.png"  
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "cm1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "cm2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "cm3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "cm4.png"
            
    RelativeLayout:
        # Label:
        #     text: "Cachorro Médio Porte"
        #     pos: 5, 440
        #     font_size: 25

                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                
                    
        #BOTÃO DE REDIRECIONAMENTO M1 
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.85}
            background_color: 1,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogMUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO M2
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.85}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogMDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO M3
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogMTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO M4
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogMQuatro'  
                                        
""")
# CACHORRO GRANDE PORTE
Builder.load_string("""
<CachorroGrande>:

    canvas.before:
        Color: 
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "fundocachorrogrande.png"  
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "cg1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "cg2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "cg3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "cg4.png"
            
    RelativeLayout:
        
        # Label:   
        #     text: "Cachorro Grande Porte"
        #     pos: 5, 440
        #     font_size: 25
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                
                
        #BOTÃO DE REDIRECIONAMENTO G1 
        Button:
            text: ""
            pos_hint : {"x" : 0.15, "top" : 0.75}
            background_color: 1,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogGUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO G2
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.80}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogGDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO G3
        Button:
            text: ""
            pos_hint : {"x" : 0.15, "top" : 0.50}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogGTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO G4
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.50}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page DogGQuatro'
""")

#Cachorros de Pequeno Porte
Builder.load_string("""
<DogPUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "bobi.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cp1.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
        
""")
Builder.load_string("""
<DogPDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "billy.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cp3.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogPTres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "ster.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cp2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPequeno'
                    
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogPQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "duda.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cp4.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

# Cachorros de Médio Porte
Builder.load_string("""
<DogMUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "victor.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 180,180
        #     source: "cm1.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint: 0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogMDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jon.png"
            
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogMTres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "henrique.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cm2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogMQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jorge.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cm4.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

#Cachorros de Grande Porte
Builder.load_string("""
<DogGUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jhey.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "dg1.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
            
""")
Builder.load_string("""
<DogGDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "anderson.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cg3.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogGTres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "thiago.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "cg2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<DogGQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "azuos.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "azuos.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page CachorroGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

#---------------------------------------------------------------------------
# PORTE GATOS
Builder.load_string("""
<GatoPorte>:       
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogato.png"
    

    RelativeLayout:
        Label:
            text: "Qual porte ?"
            pos_hint : {"x" : 0.00, "top" : 1.45}
            font_size: 25
                    

        Button:
            # text: "PEQUENO"
            pos_hint : {"x" : 0.35, "top" : 0.90}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page GatoPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnpequeno.png"
        
        Button:
            # text: "MÉDIO"
            pos_hint : {"x" : 0.35, "top" : 0.73}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page GatoMedio' 
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnmedio.png"

        Button: 
            # text: "GRANDE"
            pos_hint : {"x" : 0.36, "top" : 0.54}
            size_hint:0.3, 0.2
            background_color: 0, 0, 51, 0
            on_press: root.manager.current = 'Page GatoGrande'  
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btngrande.png"          
    
            
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page TipoAnimal'    
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png"         
""")

# GATO PEQUENO PORTE
# https://www.patasdacasa.com.br/noticia/raca-de-gato-pequeno-conheca-os-menores-bichanos-do-mundo#:~:text=O%20Singapura%20%C3%A9%20considerado%20a,uma%20manchinha%20preta%20na%20cauda.
Builder.load_string("""
<GatoPequeno>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogatopequeno.png"
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "gp1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "gp2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "gp3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "gp4.png"
            
            
    RelativeLayout:
        # Label:
        #     text: "Gato Pequeno Porte"
        #     pos: 5, 440
        #     font_size: 25
    
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
        
        #BOTÃO DE REDIRECIONAMENTO G1 
        Button:
            text: ""
            pos_hint : {"x" : 0.15, "top" : 0.80}
            background_color: 1,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page CatPUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO G2
        Button:
            text: ""
            pos_hint : {"x" : 0.60, "top" : 0.80}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page CatPDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO G3
        Button:
            text: ""
            pos_hint : {"x" : 0.15, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page CatPTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO G4
        Button:
            text: ""
            pos_hint : {"x" : 0.60, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.20, 0.20
            on_press:
                root.manager.current = 'Page CatPQuatro'
""")
# GATOS MÉDIO PORTE
# https://www.peritoanimal.com.br/racas-de-gatos/tamanho/medio.html
Builder.load_string("""
<GatoMedio>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogatomedio.png"
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "gm1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "gm2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "gm3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "gm4.png"
            
            
    RelativeLayout:
        # Label:
        #     text: "Gato Médio Porte"
        #     pos: 5, 440
        #     font_size: 25
    
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                    
        #BOTÃO DE REDIRECIONAMENTO G1 
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.85}
            background_color: 1,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatMUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO G2
        Button:
            text: ""
            pos_hint : {"x" : 0.55, "top" : 0.85}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatMDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO G3
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatMTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO G4
        Button:
            text: ""
            pos_hint : {"x" : 0.60, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatMQuatro'
                
""")
# GATO GRANDE PORTE
# https://www.peritoanimal.com.br/racas-de-gatos/tamanho/grande.html
Builder.load_string("""
<GatoGrande>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fundogatogrande.png"
            
        # Rectangle:
        #     pos: 500,700
        #     size: 200,200
        #     source: "gg1.png"  
            
        # Rectangle:
        #     pos: 1100, 700
        #     size: 200,200
        #     source: "gg2.png"  
            
        # Rectangle:
        #     pos: 550,400
        #     size: 200,200
        #     source: "gg3.png"  
            
        # Rectangle:
        #     pos: 1100,400
        #     size: 200,200
        #     source: "gg4.png"
            
            
    RelativeLayout:
        # Label:
        #     text: "Gato Grande Porte"
        #     pos: 5, 440
        #     font_size: 25
    
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.40, "top" : 0.25}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPorte'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 

        #BOTÃO DE REDIRECIONAMENTO G1 
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.85}
            background_color: 1,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatGUm'
                
        
        #BOTÃO DE REDIRECIONAMENTO G2
        Button:
            text: ""
            pos_hint : {"x" : 0.67, "top" : 0.85}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatGDois'
                
                
        #BOTÃO DE REDIRECIONAMENTO G3
        Button:
            text: ""
            pos_hint : {"x" : 0.20, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatGTres'
                
        
        #BOTÃO DE REDIRECIONAMENTO G4
        Button:
            text: ""
            pos_hint : {"x" : 0.65, "top" : 0.55}
            background_color: 0,0,0,0
            size_hint:0.15, 0.20
            on_press:
                root.manager.current = 'Page CatGQuatro'
        
""")

# GATOS DE PEQUNO PORTE
Builder.load_string("""
<CatPUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "brenna.png"
            
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
                    
""")

Builder.load_string("""
<CatPDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jardson.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gp3.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatPTres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "belly.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gp2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatPQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "hemy.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gp4.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoPequeno'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

# GATOS DE MÉDIO PORTE
Builder.load_string("""
<CatMUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "blade.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gm1.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatMDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jax.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gm3.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatMTres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "tai.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gm2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint: 0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatMQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "bils.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gm4.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoMedio'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

# GATOS DE GRANDE PORTE
Builder.load_string("""
<CatGUm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "jailsonmendes.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gg1.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint: 0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatGDois>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "bolla.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gg3.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatGtres>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "wagner.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gg2.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint: 0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint: 0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")
Builder.load_string("""
<CatGQuatro>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "diego.png"
            
        # Rectangle:
        #     pos: 50, 310
        #     size: 250,250
        #     source: "gg4.png"
         
    RelativeLayout:        
        Button:
            # text : "WhatsApp"
            pos_hint : {"x" : 0.42, "top" : 0.35}
            size_hint:0.2, 0.15
            background_color: 0, 1, 0 , 0
            on_press: 
                import webbrowser
                webbrowser.open('https://web.whatsapp.com/')
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnwhatsapp.png"
            
                
        Button:
            # text: "Voltar"
            background_color: 10, 0, 0, 0
            pos_hint : {"x" : 0.42, "top" : 0.20}
            size_hint:0.2, 0.15
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page GatoGrande'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size  
                    source: "btnvoltar.png" 
""")

# Interface de criação
class Interface(Screen):
    # Window.size = (350, 580)
    Window.fullscreen = 'auto'
    # Window.fullscreen = True


# Criação das Classes
class SubscriptionPage(Screen):
    pass

class Menu(Screen):
    pass

class TipoAnimal(Screen):
    pass

# Conjunto de Classes de Cachorro Porte
class CachorroPorte(Screen):
    pass
class CachorroPequeno(Screen):
    pass
class CachorroMedio(Screen):
    pass
class CachorroGrande(Screen):
    pass

# Conjunto de Cachorro Pequeno
class DogPUm(Screen):
    pass
class DogPDois(Screen):
    pass
class DogPTres(Screen):
    pass
class DogPQuatro(Screen):
    pass

# Conjunto de Cachorro Médio
class DogMUm(Screen):
    pass
class DogMDois(Screen):
    pass
class DogMTres(Screen):
    pass
class DogMQuatro(Screen):
    pass

# Conjunto de Cachorro Grande
class DogGUm(Screen):
    pass
class DogGDois(Screen):
    pass
class DogGTres(Screen):
    pass
class DogGQuatro(Screen):
    pass


# Conjunto de Classes de Gato Porte
class GatoPorte(Screen):
    pass
class GatoPequeno(Screen):
    pass
class GatoMedio(Screen):
    pass
class GatoGrande(Screen):
    pass

# Conjunto de Gato Pequeno
class CatPUm(Screen):
    pass
class CatPDois(Screen):
    pass
class CatPTres(Screen):
    pass
class CatPQuatro(Screen):
    pass

# Conjunto de Gato Médio
class CatMUm(Screen):
    pass
class CatMDois(Screen):
    pass
class CatMTres(Screen):
    pass
class CatMQuatro(Screen):
    pass

# Conjunto de Gato Grande
class CatGUm(Screen):
    pass
class CatGDois(Screen):
    pass
class CatGTres(Screen):
    pass
class CatGQuatro(Screen):
    pass

# Conjunto de Classes de Menu Contribuição
class Contribuir(Screen):
    pass

class QrCode(Screen):
    pass

class DoarAnimal(Screen):
    pass

# CLASSES AINDA SEM FUNÇÃO
class CadastroLogin(Screen):
    pass

class EsqueciSenha(Screen):
    pass

class RedefinirSenha(Screen):
    pass

class Pagamento(Screen):
    pass

class PaginaDezesete(Screen):
    pass

class PaginaDezoito(Screen):
    pass

class PaginaDezenove(Screen):
    pass

class PaginaVinte(Screen):
    pass

class PaginaVinteUm(Screen):
    pass

class PaginaVinteDois(Screen):
    pass

# Conjunto de Classes do App
class AppRelativeLayout(RelativeLayout):
    pass


class AppScrollView(ScrollView):
    pass


class AppStackLayout(StackLayout):
    pass


class AppFloatLayout(FloatLayout):
    pass


class AppAnchorLayout(AnchorLayout):
    pass


class AppGridLayout(GridLayout):
    pass


class AppBoxLayout(BoxLayout):
    pass


class AppPageLayout(PageLayout):
    pass


# Armazenar os dados do usuário
class PopupWindow(Widget):

    @staticmethod
    def button():
        pop_fun()


class P(RelativeLayout):
    pass


class Q(RelativeLayout):
    pass


class R(RelativeLayout):
    pass


class S(RelativeLayout):
    pass


def pop_fun():
    show = P()
    window = Popup(title='popup', content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


def account_creation():
    show0 = R()
    window0 = Popup(title='popup', content=show0,
                    size_hint=(None, None), size=(300, 300))
    window0.open()


def wrong_email():
    show1 = Q()
    window1 = Popup(title='popup', content=show1,
                    size_hint=(None, None), size=(300, 300))
    window1.open()


def login_successful():
    show2 = S()
    window2 = Popup(title='popup', content=show2,
                    size_hint=(None, None), size=(300, 300))
    window2.open()


class LoginWindow(Screen):
     email = ObjectProperty(None)
     pwd = ObjectProperty(None)

     def validate(self):

         # validando se o e-mail já existe
         if self.email.text not in users['Email'].unique():
             pop_up()
             login_successful()
         else:

             # alternando a tela atual para exibir o resultado da validação
             screen_manager.current = 'logdata'

             # redefinir o widget TextInput
             self.email.text = ""
             self.pwd.text = ""


class SignupWindow(Screen):
     name2 = ObjectProperty(None)
     email = ObjectProperty(None)
     pwd = ObjectProperty(None)

     def sign_up_button(self):
         #criando um DataFrame com as informações
         user = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
                             columns=['Name', 'Email', 'Password'])
         if self.email.text != "":
             if self.email.text not in users['Email'].unique():

                 user.to_csv('db/CadastroLogin.csv', mode='a',
                             header=False, index=False)
                 account_creation()
                 screen_manager.current = 'login'
                 self.name2.text = ""
                 self.email.text = ""
                 self.pwd.text = ""
             else:
                 pop_fun()
         else:
             wrong_email()


class LogDataWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


screen_manager = WindowManager()
screen_manager.add_widget(LoginWindow(name='login'))
screen_manager.add_widget(SignupWindow(name='signup'))
screen_manager.add_widget(LogDataWindow(name='logdata'))
#users = pd.read_csv('db/CadastroLogin.csv')


class AdotaPo(App):

    def build(self):
        screen_manager1 = ScreenManager(transition=SwapTransition())
        screen_manager1.add_widget(Interface(name='Pagina Login'))
        screen_manager1.add_widget(
            (SubscriptionPage(name='Subscription Page')))
        screen_manager1.add_widget(LoginWindow(name='login'))
        screen_manager1.add_widget(SignupWindow(name='signup'))
        screen_manager1.add_widget(LogDataWindow(name='logdata'))
        screen_manager1.add_widget(Menu(name='Page 0'))
        screen_manager1.add_widget(TipoAnimal(name='Page TipoAnimal'))
        #--------------------Doar Animal---------------------------------#
        screen_manager1.add_widget(DoarAnimal(name='Page DoarAnimal'))
        #--------------------CONTRIBUIR----------------------------------#
        screen_manager1.add_widget(Contribuir(name='Page Contribuir'))
        screen_manager1.add_widget(QrCode(name='Page QrCode'))
        #---------------------CACHORROS------------------------------------------#
        screen_manager1.add_widget(CachorroPorte(name='Page CachorroPorte'))
        screen_manager1.add_widget(CachorroPequeno(name='Page CachorroPequeno'))
        screen_manager1.add_widget(CachorroMedio(name='Page CachorroMedio'))
        screen_manager1.add_widget(CachorroGrande(name='Page CachorroGrande'))
        #---------------------CACHORRO PEQUENO-----------------------------------#
        screen_manager1.add_widget(DogPUm(name='Page DogPUm'))
        screen_manager1.add_widget(DogPDois(name='Page DogPDois'))
        screen_manager1.add_widget(DogPTres(name='Page DogPTres'))
        screen_manager1.add_widget(DogPQuatro(name='Page DogPQuatro'))
        #---------------------CACHORRO MÉDIO-------------------------------------#
        screen_manager1.add_widget(DogMUm(name='Page DogMUm'))
        screen_manager1.add_widget(DogMDois(name='Page DogMDois'))
        screen_manager1.add_widget(DogMTres(name='Page DogMTres'))
        screen_manager1.add_widget(DogMQuatro(name='Page DogMQuatro'))
        #---------------------CACHORRO GRANDE------------------------------------#
        screen_manager1.add_widget(DogGUm(name='Page DogGUm'))
        screen_manager1.add_widget(DogGDois(name='Page DogGDois'))
        screen_manager1.add_widget(DogGTres(name='Page DogGTres'))
        screen_manager1.add_widget(DogGQuatro(name='Page DogGQuatro'))
        #-----------------------GATOS----------------------------------------#
        screen_manager1.add_widget(GatoPorte(name='Page GatoPorte'))
        screen_manager1.add_widget(GatoPequeno(name='Page GatoPequeno'))
        screen_manager1.add_widget(GatoMedio(name='Page GatoMedio'))
        screen_manager1.add_widget(GatoGrande(name='Page GatoGrande'))
        #---------------------GATO PEQUENO-----------------------------------#
        screen_manager1.add_widget(CatPUm(name='Page CatPUm'))
        screen_manager1.add_widget(CatPDois(name='Page CatPDois'))
        screen_manager1.add_widget(CatPTres(name='Page CatPTres'))
        screen_manager1.add_widget(CatPQuatro(name='Page CatPQuatro'))
        #---------------------GATO MÉDIO-------------------------------------#
        screen_manager1.add_widget(CatMUm(name='Page CatMUm'))
        screen_manager1.add_widget(CatMDois(name='Page CatMDois'))
        screen_manager1.add_widget(CatMTres(name='Page CatMTres'))
        screen_manager1.add_widget(CatMQuatro(name='Page CatMQuatro'))
        #---------------------GATO GRANDE------------------------------------#
        screen_manager1.add_widget(CatGUm(name='Page CatGUm'))
        screen_manager1.add_widget(CatGDois(name='Page CatGDois'))
        screen_manager1.add_widget(CatGTres(name='Page CatGTres'))
        screen_manager1.add_widget(CatGQuatro(name='Page CatGQuatro'))
        #------------------------CLASSES SEM FUNÇÃO----------------------#
        screen_manager1.add_widget(CadastroLogin(name='CadastroLogin'))
        screen_manager1.add_widget(EsqueciSenha(name='EsqueciSenha'))
        screen_manager1.add_widget(RedefinirSenha(name='RedefinirSenha'))
        screen_manager1.add_widget(Pagamento(name='Pagamento'))
        screen_manager1.add_widget(PaginaDezesete(name='Page 17'))
        screen_manager1.add_widget(PaginaDezoito(name='Page 18'))
        screen_manager1.add_widget(PaginaDezenove(name='Page 19'))
        screen_manager1.add_widget(PaginaVinte(name='Page 20'))
        screen_manager1.add_widget(PaginaVinteUm(name='Page 21'))
        screen_manager1.add_widget(PaginaVinteDois(name='Page 22'))
        
        return screen_manager1


if __name__ == "__main__":
    AdotaPo().run()
