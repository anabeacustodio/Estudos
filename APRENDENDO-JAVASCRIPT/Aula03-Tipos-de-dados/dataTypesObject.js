// {} = objeto vazio, itens dentro do objeto são chamados de propriedades; e o que está fora é a variável, ex.: const fichaDaBia
// toda propriedade precisa ser chamada, seguida por dois pontos e depois o valor, não esquecer de separar por virgula

const fichaDaBia = { 
  nome: "Beatriz", 
  idade: 24, 
  profissao: "programadora", 
  temFilhos: false,
};

fichaDaBia.carro = "Yaris";
delete fichaDaBia.carro;

console.log('Ficha da Bia', fichaDaBia);

// const nome = "Bia";
// const idade = 24;
// const profissao = 'programadora';
// const temFilhos = false;

// const fichaDaBia = {
//   nome,
//   idade,
//   profissao,
//   temFilhos,
// };

// console.log('Ficha da Bia', fichaDaBia);