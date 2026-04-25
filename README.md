# 🍔 Sistema de Lanchonete em Python

Um programa simples desenvolvido em **Python** que simula o funcionamento de uma lanchonete, permitindo ao usuário escolher produtos, definir quantidades e calcular o valor total do pedido com opções de **desconto** ou **entrega**.

---

## 📌 Funcionalidades

✔ Exibição de um menu com produtos
✔ Seleção de itens pelo usuário
✔ Definição de quantidade
✔ Cálculo automático de subtotal e total
✔ Resumo do pedido
✔ Opção de:

* 🚚 Entrega (com taxa)
* 💸 Retirada (com desconto)

---

## 🧾 Menu de Produtos

| ID | Produto      | Preço    |
| -- | ------------ | -------- |
| 1  | Hambúrguer   | R$ 18.00 |
| 2  | Batata Frita | R$ 12.00 |
| 3  | Refrigerante | R$ 5.00  |
| 4  | Milkshake    | R$ 16.00 |

---

## ⚙️ Regras de Negócio

* 📉 **Desconto:** 20% (para retirada no local)
* 🚚 **Taxa de entrega:** R$ 15.00
* ❌ Não permite quantidade menor ou igual a zero
* ❌ Valida opções inválidas no menu

---

## 🧠 Estrutura do Código

O programa foi organizado de forma modular, utilizando funções:

* `menu()` → Exibe os produtos
* `escolher_produto()` → Lê a opção do usuário
* `escolher_quantidade()` → Define quantidade
* `buscar_produto(id)` → Localiza o produto pelo ID
* `mostrar_resumo(pedido, total)` → Exibe o resumo
* `finalizar(total)` → Aplica desconto ou entrega
* `programa()` → Controla o fluxo principal

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python instalado**
2. Salve o código em um arquivo, por exemplo:

```
lanchonete.py
```

3. Execute no terminal:

```
python lanchonete.py
```

---

## 💡 Exemplo de Uso

```
------ MENU ------
1 - Hambúrguer | R$ 18.00
2 - Batata Frita | R$ 12.00
3 - Refrigerante | R$ 5.00
4 - Milkshake | R$ 16.00
0 - Finalizar
------------------

Selecione um produto: 1
Informe a quantidade de Hambúrguers: 2
Produto adicionado com sucesso!
```

---

## 🚀 Possíveis Melhorias

* Adicionar interface gráfica (GUI)
* Salvar pedidos em arquivo
* Implementar sistema de login
* Adicionar mais produtos dinamicamente
* Melhorar tratamento de erros (try/except)

