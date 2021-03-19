'''
Escreva uma classe Aluno com os atributos relacionados às principais características de um aluno
- nome
- matrícula
- curso
- média desse aluno.
Desenvolva os seguintes métodos:
- verificar se o aluno está aprovado (média maior ou igual a 7).
'''


class cls_Aluno:
    def __init__(self, nome, matricula, curso, media):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.media = media

    def mtd_check_is_approved(self):
        if self.media >= 7:
            self.status = 'aprovado'
        else:
            self.status = 'reprovado'
        print(f'Aluno foi {self.status} na matéria')
