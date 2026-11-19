async function exibirCardapio() {
    const listaCardapio = document.getElementById('listaCardapio');

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
    let html = '';
    for(item of itens) {
        if (!item.disponibilidade) continue;

        let vegano = ''
        if(item.vegano)
            vegano = ' Vegano';

        html += `<li><b>${item.nome}</b><span>${vegano}</span></li>`;
    }

    listaCardapio.innerHTML = html;
}

exibirCardapio();