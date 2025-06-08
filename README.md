# Meu Projeto Python

Este é um projeto de exemplo para estudos em Python. Aqui você pode organizar seus scripts, aprender a usar o Git e praticar programação.

## Estrutura do Projeto

```
meu_projeto_python/
├── README.md
├── requirements.txt
├── .gitignore
├── Dockerfile
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
└── data/
```

## Como executar

### Executando localmente

1. Clone o repositório:
   ```
   git clone https://github.com/nandobs1980/MBA_Estudo
   ```
2. Acesse a pasta do projeto:
   ```
   cd MBA_Estudo
   ```
3. (Opcional) Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute o script principal:
   ```
   python src/main.py
   ```

### Executando com Docker

1. Construa a imagem Docker:
   ```
   docker build -t mba_estudo .
   ```
2. Execute o container:
   ```
   docker run --rm mba_estudo
   ```

## Sobre

Este projeto é destinado ao aprendizado da linguagem Python e boas práticas de organização de código.

---
Sinta-se à vontade para modificar e experimentar!
