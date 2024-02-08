# PROJETO GERADOR CÓDIGO DE BARRAS EM PYTHON COM FLASK 

## Projeto desenvolvido durante o evento nlw expert ofertado pela rocktseat.com.br


### O intuíto desse projeto foi criar um gerador de código de barras através de uma requisição web
### utilizando o postman para enviar a solicitação.

### Para iniciar primeiro deve clonar este repositório utilizando git clone
### Deve gerar um ambiente virtual em python, utilizando o comando py -m venv .venv (windows)
### Deve gerar um ambiente virtual em python, utilizando o comando python -m venv .venv (linux)

### Execute pip install -r requirements.txt para instalar todas as dependências do projeto

### Após, iniciar o arquivo que se encontra em .venv/Scripts/activate.bat (windows)
### Após, iniciar o arquivo que se encontra em .venv/bin/activate (linux)
### Com o auxilio da ferramenta postman, envie uma requisição POST para http://localhost:3000/create_tag,  do tipo raw com o seguinte objeto json: 
### { "product_code": "conteúdo do código (string ou int)" }