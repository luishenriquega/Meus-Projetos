// script.js

let equipamentos = [];
let usuario = "UNIP";
let senha = "PIMV";
let isLoggedIn = false;

// login
function login() {
    const usuarioInput = document.getElementById("username").value;
    const senhaInput = document.getElementById("password").value;
    
    if (usuarioInput === usuario && senhaInput === senha) {
        isLoggedIn = true;
        document.getElementById("login").style.display = "none";
        document.getElementById("menu").style.display = "block";
        document.getElementById("loginError").textContent = "";
    } else {
        document.getElementById("loginError").textContent = "Usuário ou senha incorretos.";
    }
}

// Função de logout
function logout() {
    isLoggedIn = false;
    document.getElementById("menu").style.display = "none";
    document.getElementById("login").style.display = "block";
}

// Exibir formulário de reserva
function showCadastro() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("cadastro").style.display = "block";
}

// Cancelar reserva
function cancelarCadastro() {
    document.getElementById("cadastro").style.display = "none";
    document.getElementById("menu").style.display = "block";
}

// reservar equipamento
function cadastrarEquipamento() {
    const nomeEquipamento = document.getElementById("nomeEquipamento").value;
    const tipo = document.getElementById("tipo").value;
    const quantidade = parseInt(document.getElementById("quantidade").value);
    const local = document.getElementById("local").value;
	const date = parseInt(document.getElementById("date").value);
    
    if (!nomeEquipamento || !tipo || !quantidade || !local) {
        document.getElementById("cadastroError").textContent = "Todos os campos devem ser preenchidos.";
        return;
    }
    
    const equipamento = {
        id: equipamentos.length + 1,
        nomeEquipamento,
        tipo,
        quantidade,
        local,
        status: "Disponível"
    };

    equipamentos.push(equipamento);
    document.getElementById("cadastroError").textContent = "";
    cancelarCadastro();
}

// Exibir formulário de consulta
function showConsulta() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("consulta").style.display = "block";
}

// Cancelar consulta
function cancelarConsulta() {
    document.getElementById("consulta").style.display = "none";
    document.getElementById("menu").style.display = "block";
}

// Consultar equipamento
function consultarEquipamento() {
    const id = parseInt(document.getElementById("idConsulta").value);
    const equipamento = equipamentos.find(eq => eq.id === id);

    if (!equipamento) {
        document.getElementById("consultaError").textContent = "Equipamento não encontrado.";
        return;
    }

    document.getElementById("equipamentoDetalhes").innerHTML = `
        <p><strong>Nome:</strong> ${equipamento.nomeEquipamento}</p>
        <p><strong>Tipo:</strong> ${equipamento.tipo}</p>
        <p><strong>Quantidade Disponível:</strong> ${equipamento.quantidade}</p>
        <p><strong>Local:</strong> ${equipamento.local}</p>
        <p><strong>Reservado</strong></p>
    `;
    document.getElementById("consultaError").textContent = "";
}

// Exibir formulário de gerenciamento
function showGerenciamento() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("gerenciamento").style.display = "block";
}

// Cancelar gerenciamento
function cancelarGerenciamento() {
    document.getElementById("gerenciamento").style.display = "none";
    document.getElementById("menu").style.display = "block";
}

// Gerenciar equipamento
function gerenciarEquipamento() {
    const id = parseInt(document.getElementById("idGerenciamento").value);
    const equipamento = equipamentos.find(eq => eq.id === id);

    if (!equipamento) {
        document.getElementById("gerenciamentoError").textContent = "Equipamento não encontrado.";
        return;
    }

    document.getElementById("gerenciamentoDetalhes").innerHTML = `
        <p><strong>Nome:</strong> ${equipamento.nomeEquipamento}</p>
        <p><strong>Tipo:</strong> ${equipamento.tipo}</p>
        <p><strong>Quantidade Disponível:</strong> ${equipamento.quantidade}</p>
        <p><strong>Local:</strong> ${equipamento.local}</p>
        <p><strong>Status:</strong> ${equipamento.status}</p>
        <label>Status:</label>
        <select id="novoStatus">
            <option value="Disponível">Reservado</option>
            <option value="Reservado">Cancelar Reserva</option>
        </select>
        <button onclick="atualizarStatus(${id})">Atualizar Status</button>
        
    `;
    document.getElementById("gerenciamentoError").textContent = "";
}
// Função para realizar a reserva de um equipamento
function reservarEquipamento(id) {
    const equipamento = equipamentos.find(eq => eq.id === id);

    if (!equipamento) {
        document.getElementById("gerenciamentoError").textContent = "Equipamento não encontrado.";
        return;
    }

    if (equipamento.status === "Reservado") {
        document.getElementById("gerenciamentoError").textContent = "Este equipamento já está reservado.";
        return;
    }

    // Verificar quantas unidades estão reservadas do mesmo tipo de equipamento
    const reservasPorTipo = equipamentos.filter(eq => eq.tipo === equipamento.tipo && eq.status === "Reservado").length;

    // Limitar a 2 reservas por tipo de equipamento
    if (reservasPorTipo >= 2) {
        document.getElementById("gerenciamentoError").textContent = `Já existem 2 reservas para o tipo "${equipamento.tipo}". Não é possível reservar mais unidades deste tipo.`;
        return;
    }

    if (equipamento.quantidade > 0) {
        equipamento.status = "Reservado";
        equipamento.quantidade -= 1; // Decrementa a quantidade disponível
        alert(`Equipamento "${equipamento.nomeEquipamento}" reservado com sucesso!`);
    } else {
        document.getElementById("gerenciamentoError").textContent = "Não há unidades disponíveis para reserva.";
    }

    cancelarGerenciamento();
}


// Atualizar status do equipamento
function atualizarStatus(id) {
    const novoStatus = document.getElementById("novoStatus").value;
    const equipamento = equipamentos.find(eq => eq.id === id);
    equipamento.status = novoStatus;
    cancelarGerenciamento();
}
