import os

restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa' , 'ativo' : False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana','ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana','ativo': False},]

def exibir_nome_do_programa():
    '''essa função exibe o nome do programa'''
    print("""
    ██████╗░███████╗░█████╗░███████╗██╗████████╗░█████╗░
    ██╔══██╗██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔══██╗
    ██████╔╝█████╗░░██║░░╚═╝█████╗░░██║░░░██║░░░███████║
    ██╔══██╗██╔══╝░░██║░░██╗██╔══╝░░██║░░░██║░░░██╔══██║
    ██║░░██║███████╗╚█████╔╝███████╗██║░░░██║░░░██║░░██║
    ╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝

██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
""")

def exibir_opcoes():
    '''essa função exibe as opções do menu principal'''
    print(' 1. Cadastrar restaurante')
    print(' 2. Listar restaurante')
    print(' 3. Alternar estado do restaurante')
    print(' 4. Sair\n')

def finalizar_app():
    '''essa função finaliza o app'''
    exibir_subtitulo('Finalizar APP.')

def voltar_ao_menu_principal():
    '''essa função exibe uma mensagem de volta ao menu principal
    
    input:
    -  tecla para voltar ao menu principal
    
    
    '''

    input('digite uma tecla para voltar ao menu')
    main()

def opcao_invalida():
    '''essa função exibe uma mensagem de opção inválida'''
    print('opção invalida"\n')
    voltar_ao_menu_principal ()

def exibir_subtitulo(texto):
    '''essa função exibe o subtítulo do programa'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''essa função cadastra um novo restaurante
    
    Input:
    - nome_do_restaurante
    - categoria
    - ativo

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    
    '''
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('DIgite o nome do restaurante que deseja cadastar: ')
    categoria =  input (f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f' O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n ')
    
    voltar_ao_menu_principal ()

def listar_restaurantes():
    '''essa função lista os restaurantes cadastrados
    
    Output:
    - Exibe os restaurantes cadastrados com seus respectivos estados (ativo ou inativo)
       
    '''
    exibir_subtitulo('Listando restaurantes')
    

    print(f'{'Nome do Restaurante'.ljust(22)}  | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante ['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')


    voltar_ao_menu_principal ()

def alternar_estado_de_restaurante():
    '''essa função alterna o estado do restaurante entre ativo e inativo
    
    output:
    - Altera o estado do restaurante selecionado e exibe uma mensagem de sucesso ou erro
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal ()

def escolher_opcao():
    '''essa função escolhe a opção do menu principal
    
    Input:
    - opcao_escolhida: número da opção escolhida pelo usuário
        Output:
            - Chama a função correspondente à opção escolhida ou exibe uma mensagem de opção inválida
            
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:  
            alternar_estado_de_restaurante()
        elif opcao_escolhida == 4:  
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    '''essa função é a função principal do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
