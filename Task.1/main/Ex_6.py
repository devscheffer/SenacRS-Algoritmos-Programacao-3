"""
Construa um programa em Python que simule a operação de um CD Player tocando um CD.
Para isso, implemente uma classe chamada CD, que conterá três atributos:
- o número de músicas que o CD possui,
- o número da faixa que está tocando no momento (ao iniciar, este valor deve ser colocado em
1, que é o número da primeira música)
- o CD Player está tocando uma música no momento ou se está parado (o aparelho sempre inicia parado)
"""
"""
Além destes atributos, o programa deve possuir os seguintes métodos:
	1. um método que funcione como o botão play, dizendo ao aparelho que deve começar a tocar a faixa atual;
	2. um método que funcione como o botão pause, fazendo o aparelho parar de tocar;
	3. um método que funcione como o botão stop, que faz com que o aparelho pare de tocar e volte para a faixa 1;
	4. um método que permite avançar para a próxima faixa (se o CD já estiver na última faixa, deve ir para a primeira);
	5. um método que permite retroceder para a faixa anterior (se o CD já estiver na primeira faixa, deve ir para a última).

Ao implementar o programa que use a classe CD, permita ao usuário que informe o número de
músicas.
A simulação ocorrerá da seguinte forma: crie um objeto a partir da classe CD que será a
base da simulação. Após entrar com o número de músicas (armazene esse valor no objeto que você
criou), permita ao usuário entrar com comandos para o CD Player. Os comandos serão informados
através de números:
	1. para play
	2. para pause
	3. para stop
	4. para ir para a próxima faixa
	5. para ir para a faixa anterior.
Para cada comando digitado pelo usuário, chame o método apropriado no objeto que você criou.
O programa irá terminar quando o usuário digitar o comando de número 0 (zero).
"""


class cls_CD:
    def __init__(self, qtd_musica):
        self.qtd_musica = qtd_musica
        self.n_musica = 1
        self.status = "parado"

    def mtd_play(self):
        self.status = "tocando"

    def mtd_pause(self):
        self.status = "parado"

    def mtd_stop(self):
        self.mtd_pause()
        self.n_musica = 1

    def mtd_next(self):
        if self.qtd_musica < self.n_musica + 1:
            self.n_musica = 1
        else:
            self.n_musica += 1

    def mtd_previous(self):
        if self.n_musica - 1 < 1:
            self.n_musica = self.qtd_musica
        else:
            self.n_musica -= 1

    def mtd_check_menu(self):
        try:
            vlr_menu = input("Digite um comando da lista:\n")
            vlr_menu = int(vlr_menu)
            if vlr_menu in self.dict_menu.keys() or vlr_menu == 0:
                return vlr_menu
            else:
                print(f"Valor [{vlr_menu}] não configurado para o menu")
                vlr_menu = int(input("Tente novamente\n"))
                return self.mtd_check_menu(vlr_menu)
        except:
            print(f"Valor [{vlr_menu}] não configurado para o menu")
            return self.mtd_check_menu()

    def mtd_menu_front(self):
        print(
            f"""
	Menu CD Player:
	0. Finalizar programa
	1. Play
	2. Pause
	3. Stop
	4. Ir para a próxima faixa
	5. Ir para a faixa anterior
		"""
        )
        self.dict_menu = {
            1: self.mtd_play,
            2: self.mtd_pause,
            3: self.mtd_stop,
            4: self.mtd_next,
            5: self.mtd_previous,
        }
        print(f"Status: {self.status}")
        print(f"Faixa: {self.n_musica}/{self.qtd_musica}")
        cmd = self.mtd_check_menu()
        if cmd == 0:
            return cmd
        else:
            self.dict_menu[cmd]()
            return cmd

    def mtd_start(self):
        cmd = ""
        while cmd != 0:
            cmd = self.mtd_menu_front()
        print(f"Fim do programa")
