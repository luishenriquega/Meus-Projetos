from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Luiz', 10)
restaurante_praca.receber_avaliacao('Ste', 8)
restaurante_praca.receber_avaliacao('LS', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()