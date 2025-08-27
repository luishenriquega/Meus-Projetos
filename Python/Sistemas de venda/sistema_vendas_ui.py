import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SistemaVendas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas")

        self.criar_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_login(self):
        self.limpar_tela()
        self.root.title("Login")

        lbl_usuario = ttk.Label(self.root, text="Usuário:")
        lbl_usuario.grid(row=0, column=0, padx=10, pady=10)
        self.ent_usuario = ttk.Entry(self.root)
        self.ent_usuario.grid(row=0, column=1, padx=10, pady=10)

        lbl_senha = ttk.Label(self.root, text="Senha:")
        lbl_senha.grid(row=1, column=0, padx=10, pady=10)
        self.ent_senha = ttk.Entry(self.root, show="*")
        self.ent_senha.grid(row=1, column=1, padx=10, pady=10)

        btn_login = ttk.Button(self.root, text="Entrar", command=self.validar_login)
        btn_login.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_login(self):
        usuario = self.ent_usuario.get()
        senha = self.ent_senha.get()

        # Simulação de autenticação (substituir por lógica real)
        if usuario == "supervisor" and senha == "123":
            self.criar_tela_supervisor()
        elif usuario == "estoquista" and senha == "456":
            self.criar_tela_estoquista()
        elif usuario == "vendedor" and senha == "789":
            self.criar_tela_vendedor()
        else:
            messagebox.showerror("Erro", "Login inválido.")
            self.ent_senha.delete(0, tk.END)

    def criar_tela_supervisor(self):
        self.limpar_tela()
        self.root.title("Supervisor")

        lbl_titulo = ttk.Label(self.root, text="SUPERVISOR", font=("Arial", 16))
        lbl_titulo.pack(pady=20)

        btn_historico = ttk.Button(self.root, text="HISTÓRICO DE MOVIMENTAÇÃO")
        btn_historico.pack(pady=10, padx=20, fill="x")

        btn_produtos = ttk.Button(self.root, text="PRODUTOS", command=self.criar_tela_produtos)
        btn_produtos.pack(pady=10, padx=20, fill="x")

        btn_vendas = ttk.Button(self.root, text="VENDA", command=self.criar_tela_vendas)
        btn_vendas.pack(pady=10, padx=20, fill="x")

        btn_clientes = ttk.Button(self.root, text="CLIENTE", command=self.criar_tela_clientes)
        btn_clientes.pack(pady=10, padx=20, fill="x")

        btn_sair = ttk.Button(self.root, text="SAIR", command=self.root.destroy)
        btn_sair.pack(pady=20, padx=20, fill="x")

    def criar_tela_estoquista(self):
        self.limpar_tela()
        self.root.title("Estoquista")

        lbl_titulo = ttk.Label(self.root, text="ESTOQUISTA", font=("Arial", 16))
        lbl_titulo.pack(pady=20)

        btn_vendas = ttk.Button(self.root, text="VENDA", command=self.criar_tela_vendas)
        btn_vendas.pack(pady=10, padx=20, fill="x")

        btn_produtos = ttk.Button(self.root, text="PRODUTOS", command=self.criar_tela_produtos)
        btn_produtos.pack(pady=10, padx=20, fill="x")

        btn_novo_cadastro = ttk.Button(self.root, text="NOVO CADASTRO")
        btn_novo_cadastro.pack(pady=10, padx=20, fill="x")

        btn_clientes = ttk.Button(self.root, text="CLIENTE", command=self.criar_tela_clientes)
        btn_clientes.pack(pady=10, padx=20, fill="x")

        btn_sair = ttk.Button(self.root, text="SAIR", command=self.root.destroy)
        btn_sair.pack(pady=20, padx=20, fill="x")

    def criar_tela_vendedor(self):
        self.limpar_tela()
        self.root.title("Vendedor")

        lbl_titulo = ttk.Label(self.root, text="VENDEDOR", font=("Arial", 16))
        lbl_titulo.pack(pady=20)

        btn_vendas = ttk.Button(self.root, text="VENDA", command=self.criar_tela_vendas)
        btn_vendas.pack(pady=10, padx=20, fill="x")

        btn_produtos = ttk.Button(self.root, text="PRODUTOS", command=self.criar_tela_produtos)
        btn_produtos.pack(pady=10, padx=20, fill="x")

        btn_novo_cadastro = ttk.Button(self.root, text="NOVO CADASTRO")
        btn_novo_cadastro.pack(pady=10, padx=20, fill="x")

        btn_clientes = ttk.Button(self.root, text="CLIENTE", command=self.criar_tela_clientes)
        btn_clientes.pack(pady=10, padx=20, fill="x")

        btn_sair = ttk.Button(self.root, text="SAIR", command=self.root.destroy)
        btn_sair.pack(pady=20, padx=20, fill="x")

    def criar_tela_produtos(self):
        self.limpar_tela()
        self.root.title("Produtos")

        lbl_titulo = ttk.Label(self.root, text="PRODUTOS", font=("Arial", 16))
        lbl_titulo.grid(row=0, column=0, columnspan=3, pady=10)

        lbl_cod_barras = ttk.Label(self.root, text="Cód. de Barras:")
        lbl_cod_barras.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ent_cod_barras = ttk.Entry(self.root)
        ent_cod_barras.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        lbl_nome = ttk.Label(self.root, text="Nome do Produto:")
        lbl_nome.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ent_nome = ttk.Entry(self.root)
        ent_nome.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        lbl_categoria = ttk.Label(self.root, text="Categoria:")
        lbl_categoria.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ent_categoria = ttk.Entry(self.root)
        ent_categoria.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        lbl_fabricante = ttk.Label(self.root, text="Fabricante:")
        lbl_fabricante.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ent_fabricante = ttk.Entry(self.root)
        ent_fabricante.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        lbl_quantidade = ttk.Label(self.root, text="Quantidade Atual:")
        lbl_quantidade.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ent_quantidade = ttk.Entry(self.root)
        ent_quantidade.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        lbl_valor = ttk.Label(self.root, text="Valor do Produto:")
        lbl_valor.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ent_valor = ttk.Entry(self.root)
        ent_valor.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        frame_botoes_direita = ttk.Frame(self.root)
        frame_botoes_direita.grid(row=1, column=2, rowspan=4, padx=10, pady=10, sticky="ns")

        btn_cadastrar = ttk.Button(frame_botoes_direita, text="CADASTRO")
        btn_cadastrar.pack(pady=5, fill="x")

        btn_consultar = ttk.Button(frame_botoes_direita, text="CONSULTA")
        btn_consultar.pack(pady=5, fill="x")

        btn_alterar = ttk.Button(frame_botoes_direita, text="ALTERAR")
        btn_alterar.pack(pady=5, fill="x")

        btn_excluir = ttk.Button(frame_botoes_direita, text="EXCLUIR")
        btn_excluir.pack(pady=5, fill="x")

        frame_botoes_inferior = ttk.Frame(self.root)
        frame_botoes_inferior.grid(row=7, column=0, columnspan=3, pady=10)

        # Botão VOLTAR já está aqui
        btn_voltar = ttk.Button(frame_botoes_inferior, text="VOLTAR", command=self.criar_tela_supervisor)
        btn_voltar.pack(side=tk.LEFT, padx=10)

        btn_sair = ttk.Button(frame_botoes_inferior, text="SAIR", command=self.root.destroy)
        btn_sair.pack(side=tk.RIGHT, padx=10)

    def criar_tela_clientes(self):
        self.limpar_tela()
        self.root.title("Clientes")

        lbl_titulo = ttk.Label(self.root, text="CLIENTE", font=("Arial", 16))
        lbl_titulo.grid(row=0, column=0, columnspan=3, pady=10)

        lbl_cod = ttk.Label(self.root, text="Cód:")
        lbl_cod.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ent_cod = ttk.Entry(self.root)
        ent_cod.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        lbl_rg = ttk.Label(self.root, text="RG:")
        lbl_rg.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ent_rg = ttk.Entry(self.root)
        ent_rg.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        lbl_cpf = ttk.Label(self.root, text="CPF:")
        lbl_cpf.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ent_cpf = ttk.Entry(self.root)
        ent_cpf.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        lbl_nome = ttk.Label(self.root, text="Nome:")
        lbl_nome.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ent_nome = ttk.Entry(self.root)
        ent_nome.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        lbl_data_cadastro = ttk.Label(self.root, text="Data do Cadastro:")
        lbl_data_cadastro.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ent_data_cadastro = ttk.Entry(self.root)
        ent_data_cadastro.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        lbl_endereco = ttk.Label(self.root, text="Endereço:")
        lbl_endereco.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ent_endereco = ttk.Entry(self.root)
        ent_endereco.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        lbl_telefone = ttk.Label(self.root, text="Telefone:")
        lbl_telefone.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        ent_telefone = ttk.Entry(self.root)
        ent_telefone.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

        lbl_email = ttk.Label(self.root, text="E-mail:")
        lbl_email.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        ent_email = ttk.Entry(self.root)
        ent_email.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

        frame_botoes_direita = ttk.Frame(self.root)
        frame_botoes_direita.grid(row=1, column=2, rowspan=4, padx=10, pady=10, sticky="ns")

        btn_cadastrar = ttk.Button(frame_botoes_direita, text="CADASTRO")
        btn_cadastrar.pack(pady=5, fill="x")

        btn_consultar = ttk.Button(frame_botoes_direita, text="CONSULTA")
        btn_consultar.pack(pady=5, fill="x")

        btn_alterar = ttk.Button(frame_botoes_direita, text="ALTERAR")
        btn_alterar.pack(pady=5, fill="x")

        btn_excluir = ttk.Button(frame_botoes_direita, text="EXCLUIR")
        btn_excluir.pack(pady=5, fill="x")

        frame_botoes_inferior = ttk.Frame(self.root)
        frame_botoes_inferior.grid(row=9, column=0, columnspan=3, pady=10)

        # Botão VOLTAR já está aqui
        btn_voltar = ttk.Button(frame_botoes_inferior, text="VOLTAR", command=self.criar_tela_supervisor)
        btn_voltar.pack(side=tk.LEFT, padx=10)

        btn_sair = ttk.Button(frame_botoes_inferior, text="SAIR", command=self.root.destroy)
        btn_sair.pack(side=tk.RIGHT, padx=10)

    def criar_tela_vendas(self):
        self.limpar_tela()
        self.root.title("Vendas")

        lbl_titulo = ttk.Label(self.root, text="VENDA", font=("Arial", 16))
        lbl_titulo.grid(row=0, column=0, columnspan=3, pady=10)

        lbl_dados_cliente = ttk.Label(self.root, text="Dados do Cliente:")
        lbl_dados_cliente.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ent_dados_cliente = ttk.Entry(self.root)
        ent_dados_cliente.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        lbl_produtos_adquiridos = ttk.Label(self.root, text="Produtos Adquiridos:")
        lbl_produtos_adquiridos.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        # Aqui você provavelmente teria uma listbox ou outra forma de selecionar produtos
        ent_produtos_adquiridos = ttk.Entry(self.root)
        ent_produtos_adquiridos.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        lbl_cod_unico = ttk.Label(self.root, text="Cód. Único:")
        lbl_cod_unico.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ent_cod_unico = ttk.Entry(self.root)
        ent_cod_unico.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        lbl_data = ttk.Label(self.root, text="Data:")
        lbl_data.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ent_data = ttk.Entry(self.root)
        ent_data.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        lbl_valor_total = ttk.Label(self.root, text="Valor Total:")
        lbl_valor_total.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ent_valor_total = ttk.Entry(self.root)
        ent_valor_total.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        lbl_metodo_pagamento = ttk.Label(self.root, text="Método de Pagamento:")
        lbl_metodo_pagamento.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ent_metodo_pagamento = ttk.Entry(self.root)
        ent_metodo_pagamento.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        frame_botoes_direita = ttk.Frame(self.root)
        frame_botoes_direita.grid(row=1, column=2, rowspan=4, padx=10, pady=10, sticky="ns")

        btn_cadastrar = ttk.Button(frame_botoes_direita, text="CADASTRO")
        btn_cadastrar.pack(pady=5, fill="x")

        btn_consultar = ttk.Button(frame_botoes_direita, text="CONSULTA")
        btn_consultar.pack(pady=5, fill="x")

        btn_alterar = ttk.Button(frame_botoes_direita, text="ALTERAR")
        btn_alterar.pack(pady=5, fill="x")

        btn_excluir = ttk.Button(frame_botoes_direita, text="EXCLUIR")
        btn_excluir.pack(pady=5, fill="x")

        frame_botoes_inferior = ttk.Frame(self.root)
        frame_botoes_inferior.grid(row=7, column=0, columnspan=3, pady=10)

        # Botão VOLTAR já está aqui
        btn_voltar = ttk.Button(frame_botoes_inferior, text="VOLTAR", command=self.criar_tela_supervisor)
        btn_voltar.pack(side=tk.LEFT, padx=10)

        btn_sair = ttk.Button(frame_botoes_inferior, text="SAIR", command=self.root.destroy)
        btn_sair.pack(side=tk.RIGHT, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaVendas(root)
    root.mainloop()