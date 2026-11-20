const itensDisponiveis = new Map();
const itensEscolhidos = new Map();

async function exibirCardapio() {
    const listaCardapio = document.getElementById('listaCardapio');
    itensEscolhidos.clear();
    try {
        let itens = await consultaCardapio();
        exibirItens(itens, listaCardapio);
    } catch(erro) {
        listaCardapio.innerHTML = `<li>${erro.message}</li>`
    }
}

async function consultaCardapio() {

    const cardapio = await fetch('/api/cardapio');
        
    if(!cardapio.ok) throw Error('Cardápio não encontrado');

    let dados = await cardapio.json();

    return dados.listaItens;
}

function exibirItens(itens, listaCardapio) {
    itensDisponiveis.clear()
    let html = '';
    for(item of itens) {
        if (!item.disponibilidade) continue;

        itensDisponiveis.set(String(item.id), item);

        let vegano = ''
        if(item.vegano)
            vegano = ' Vegano';

        html += `<li>
                    <input type="checkbox" value="${item.id}"> 
                    <b>${item.nome}</b><span>${vegano}</span>
                </li>`;
    }

    listaCardapio.innerHTML = html;
}

document.getElementById('listaCardapio').addEventListener('click', (event) => {
    const li = event.target.closest('input[type=checkbox]');
    if (!li) return;

    const id = li.value;

    if(li.checked) {
        itensEscolhidos.set(id, itensDisponiveis.get(id));
    }
    else {
        itensEscolhidos.delete(id);
    }
});

async function fazerPedido() {
    if(itensEscolhidos.size == 0) {
        alert('Selecione ao menos um item.');
        return;
    }

    let listaItens = {
        pedidoItens: Array.from(itensEscolhidos.keys()).map((id) => ({
            idItemCardapio: Number(id),
            porcoes: 1
        }))
    };

    try {
        const cardapio = await fetch('/api/pedido', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(listaItens)
        });

        const dados = await cardapio.json();

        if(!cardapio.ok) throw Error('Erro');

        alert('Pedido realizado.');
    }
    catch(erro) {
        alert(erro.message);
    }
}

document.getElementById('pedidoButton').addEventListener('click', fazerPedido)

exibirCardapio();