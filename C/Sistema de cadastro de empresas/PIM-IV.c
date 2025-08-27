#include <stdio.h>
#include <string.h>

#define MAX_CLIENTES 100
#define MAX_NOME 100
#define MAX_ENDERECO 200
#define MAX_EMAIL 100
#define MAX_TELEFONE 20
//armazenamento da empresa
typedef struct {
    char nome_responsavel[MAX_NOME];
    char nome_empresa[MAX_NOME];
    char telefone[MAX_TELEFONE];
    char endereco[MAX_ENDERECO];
    char email[MAX_EMAIL];
} Cliente;
//login
int login() {
    char usuario[50], senha[50];
    const char usuario_correto[] = "UNIP";
    const char senha_correta[] = "PIMIV";

    printf("XXXX Sistema de Cadastro de Empresas XXXX\n");
    while (1) {
        printf("Digite o nome de usuario: ");
        scanf("%s", usuario);
        printf("Digite a senha: ");
        scanf("%s", senha);

        if (strcmp(usuario, usuario_correto) == 0 && strcmp(senha, senha_correta) == 0) {
            printf("Login bem-sucedido!\n");
            return 1;
        } else {
            printf("Usuario ou senha incorretos. Tente novamente.\n");
        }
    }
}
//cadastro empresa/cliente
void cadastrar_cliente(Cliente clientes[], int *contador) {
    if (*contador >= MAX_CLIENTES) {
        printf("Nao e possivel cadastrar mais Empresas.\n");
        return;
    }
    Cliente novo_cliente;

    printf("\nCadastro da Empresa\n");
    printf("Nome do Responsavel: ");
    scanf(" %[^\n]s", novo_cliente.nome_responsavel);
    printf("Nome da Empresa: ");
    scanf(" %[^\n]s", novo_cliente.nome_empresa);
    printf("Telefone: ");
    scanf(" %[^\n]s", novo_cliente.telefone);
    printf("Endereco: ");
    scanf(" %[^\n]s", novo_cliente.endereco);
    printf("Email: ");
    scanf(" %[^\n]s", novo_cliente.email);

    clientes[*contador] = novo_cliente;
    (*contador)++;

    printf("Empresa cadastrada com sucesso!\n");
}
//consulta do cadastro
void consultar_cliente(Cliente clientes[], int contador) {
    int id;

    printf("\nConsulta de Empresa\n");
    printf("Digite o ID da Empresa (1 a %d): ", contador);
    scanf("%d", &id);

    if (id < 1 || id > contador) {
        printf("Empresa nao encontrada.\n");
        return;
    }
    Cliente c = clientes[id - 1];
    printf("\nID: %d\n", id);
    printf("Nome do Responsavel: %s\n", c.nome_responsavel);
    printf("Nome da Empresa: %s\n", c.nome_empresa);
    printf("Telefone: %s\n", c.telefone);
    printf("Endereco: %s\n", c.endereco);
    printf("Email: %s\n", c.email);
}
//alteracao de cadastro
void gerenciar_cliente(Cliente clientes[], int contador) {
    int id, opcao;

    printf("\nGerenciamento de Empresas\n");
    printf("Digite o ID da Empresa (1 a %d) para modificar: ", contador);
    scanf("%d", &id);

    if (id < 1 || id > contador) {
        printf("Empresa nao encontrado.\n");
        return;
    }
    Cliente *c = &clientes[id - 1];

    printf("\nO que deseja modificar?\n");
    printf("1. Nome do Responsavel\n");
    printf("2. Nome da Empresa\n");
    printf("3. Telefone\n");
    printf("4. Endereco\n");
    printf("5. Email\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &opcao);
//opcoes para os botoes
    switch (opcao) {
        case 1:
            printf("Novo Nome do Responsavel: ");
            scanf(" %[^\n]s", c->nome_responsavel);
            break;
        case 2:
            printf("Novo Nome da Empresa: ");
            scanf(" %[^\n]s", c->nome_empresa);
            break;
        case 3:
            printf("Novo Telefone: ");
            scanf(" %[^\n]s", c->telefone);
            break;
        case 4:
            printf("Novo Endereco: ");
            scanf(" %[^\n]s", c->endereco);
            break;
        case 5:
            printf("Novo Email: ");
            scanf(" %[^\n]s", c->email);
            break;
        default:
            printf("Opcao invalida.\n");
            break;
    }
    printf("Informacoes da Empresa atualizadas com sucesso!\n");
}
//tela de menu
int main() {
    Cliente clientes[MAX_CLIENTES];
    int contador = 0;

    if (!login()) {
        return 1;
    }
    int opcao;
    while (1) {
        printf("\nXXXXX MENU XXXXX\n");
        printf("1. Cadastrar Empresa\n");
        printf("2. Consultar Empresa\n");
        printf("3. Gerenciar Cadastro de Empresa\n");
        printf("4. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                cadastrar_cliente(clientes, &contador);
                break;
            case 2:
                consultar_cliente(clientes, contador);
                break;
            case 3:
                gerenciar_cliente(clientes, contador);
                break;
            case 4:
                printf("Saindo do programa...\n");
                return 0;
            default:
                printf("Opcao invalida. Tente novamente.\n");
        }
    }
    return 0;
}
