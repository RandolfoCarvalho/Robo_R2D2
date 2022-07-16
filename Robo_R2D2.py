
class Robo:

    def __init__(self,bateria):

        self.estado = 'Desligado' 
                                 
        self.bateria = bateria 

    def liga_desliga(self):
                           
        if self.bateria == 0:
            print('\nRobo sem bateria, carregue-o\n') 
            self.estado = 'Desligado' #Desliga o robo
        else:
            #Inversão de estado do Robo e aviso
            if self.estado == 'Desligado':
                self.estado = 'Ligado'
                print('\nRobo ligado\n')
            else:
                self.estado = 'Desligado'
                print('\nRobo desligado\n')

    def movimento(self,lado_andar_robo):
        
        if self.bateria == 0:#Método que controla para qual lado ele irá andar
            print('\nBateria zerada, carregue o R2D2\n') #Aviso
        else:
            if self.estado == 'Desligado': #
                                          
                print('\nRobo desligado, ligue-o para movimentar\n')
            else:
                self.lado_andar_robo = lado_andar_robo 
                                                      
                self.bateria = self.bateria - 10
                                                 
                                                 
                if self.bateria == 0: 
                                     
                    self.estado = 'Desligado'

    def controle_energia(self):
        print(self.estado)
        print(self.bateria)

print('-----------------------MENU-----------------------')

try: 
    bateria = -1 
    while bateria > 100 or bateria < 0: 
                                        
        bateria = int(input('Digite a bateria do Robo: ')) 
    R2D2 = Robo(bateria) 

except ValueError: 
    print('Opcao Invalida') 
else:
    finalizar = '' 
    while finalizar != 'sair':
        try: 
            opcao = int(input('Digite o numero respectivo ao comando que deseja:\n'
                              '1 - Liga/desliga o Robo\n'
                              '2 - Movimentar o Robo\n'
                              '3 - Controle de energia do Robo\n'
                              '4 - Finalizar o programa\n'
                              'Escolha: '))
        except ValueError:
            print('\nOpcao Invalida\n') 
            if opcao == 1:
                R2D2.liga_desliga() 
            elif opcao == 2:
                R2D2.movimento(input('\nDigite o lado para o qual o robo ira andar: '))
            elif opcao == 3:
               R2D2.controle_energia()
            elif opcao == 4:
                finalizar = 'sair'
            else:
                print('\nDigite um numero de 1 a 4\n ')

finally:
    print('Programa Finalizado')









