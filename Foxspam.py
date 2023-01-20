import boto3
import time
import os

n = '\033[m' #normal
r = '\033[1;31m' #vermelho
rf = '\033[31m' #vermelho fraco
g = '\033[1;32m' #verde
y = '\033[33m' #amarelo
b = '\033[34m' #azul
p = '\033[35m' #roxo

class foxyspam(object):
    def __init__(self):
        try:

            self.banner()
            self.tabela()
            self.num = int(input(f'{r}[{y}-{r}]{g} Escolha uma opção:{n}'))
            self.escolha_main(self.num)
        except Exception as erro:
            print(erro)
            print(f'{r}DIGITE APENAS NUMEROS!!!')
            time.sleep(2)
            self.__init__()
    def banner(self):
        os.system('cls')
        print(f""" {g}
FFFFFFFFF   OOOOO     XXX   XXX         SSSSSSSSSS  PPPPPPPPPP      AAAAA      MMMM    MMMM
FF        OO     OO    XXX XXX          SS          PP      PP     AA   AA     MM MM  MM MM
FFFFFF    OO     OO      XXX    ------  SSSSSSSSSS  PPPPPPPPPP    AA AAA AA    MM  MMMM  MM
FF        OO     OO    XXX XXX                  SS  PP           AA       AA   MM        MM
FF          OOOOO     XXX   XXX         SSSSSSSSSS  PP          AA         AA  MM        MM
        {n}           
{g} CRIADOR:{y} LYNCH      {g} APOIO:{y} HIRO KAMI                         {r}versão 1.0{n}

{g} NÃO NOS RESPONSABILIZAMOS PELO USO INDEVIDO, SE VOCE SE FUDER ENTÃO SE FODA SOZINHO!!!{n}
        """)
    def tabela(self):
        print(f""" 
{r}[{y}1{r}]{g} SPAM-SMS
{r}[{y}2{r}]{g} SPAM-GMAIL
        """)
    def escolha_main(self, esc):
            if esc == 1: 
                self.main1()
            elif esc == 2:
                self.main2()
    def main1(self):
        os.system('cls') 
        print(f""" {g}
ll      YY    YY   NNNNN     NN   CCCCCCCCC   HH     HH
ll       YY   YY   NN  NN    NN   CC          HH     HH
ll         YYYYY   NN   NN   NN   CC          HHHHHHHHH
ll            YY   NN    NN  NN   CC          HH     HH
lllllllll     YY   NN     NNNNN   CCCCCCCCC   HH     HH
        {n}
{y} SPAM DE SMS (MENSAGENS) {n}
        """)
        print(f"""Digite /exit para voltar ao menu principal

{y}(EXEMPLO DE COMO DEVE COLOCAR O NUMERO: +5518997961878){n}
        """)
        numero= (input(f'{g}Numero que recebera o spam:{n}'))
        if numero == '/exit':
            self.__init__()
        quantidade_sms = input(f'{g}Quantidade de spam:{n}')

    def main2(self):
        os.system('cls')
        print(f""" {g}
ll      YY    YY   NNNNN     NN   CCCCCCCCC   HH     HH
ll       YY   YY   NN  NN    NN   CC          HH     HH
ll         YYYYY   NN   NN   NN   CC          HHHHHHHHH
ll            YY   NN    NN  NN   CC          HH     HH
lllllllll     YY   NN     NNNNN   CCCCCCCCC   HH     HH
        {n}
{y} SPAM DE EMAIL (GMAIL){n}

{r}[{y}1{r}]{g} PADRÃO
{r}[{y}2{r}]{g} CUSTOMIZADO
{r}[{y}3{r}]{g} EXIT
(obs: Se não souber usar a ferramenta então use a opção padrão)
______________________________________________________________________
        """)
        self.opção = int(input(f'{r}[{y}-{r}]{g} Digite a opção desejada:{n}'))
        self.escolha_opção(self.opção)

    def escolha_opção(self, esc):
        if esc == 1:
            self.padrão()
        elif esc == 2:
            self.customizado()
        elif esc == 3:
            self.__init__()
        else:
            print(f'{r}DIGITE APENAS NUMEROS QUE ESTEJAM NAS OPÇÕES ACIMA!!!')
            time.sleep(2)
            self.main2()
        
    def padrão(self):
        os.system('cls')
        email_rec = input(f'{g}Qual email rebera o Spam:{n}')
        quantidade_email = input(f'{g}Quantidade de spam:{n}')
    def customizado(self):
        os.system('cls')
        email_rec = input(f'{g}Qual email recebera o spam:{n}')
        email_env = input(f'{g}Qual email enviara o spam:{n}')
        senha_email = input(f'{g}Qual a senha do email que enviara o spam:{n}')
        quantidade_email = input(f'{g}Quantidade de spam:{n}')
    
foxyspam()