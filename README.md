# Relatórios de atividades

Script para extração da tabela de atividades do Relatório de Atividades do SEI e geração de um arquivo xlsx consolidado.

## Pré-requisitos

Crie um ambiente virtual python e instale as dependências com

```
pip install -r requirements.txt
```

## Uso

Salve as tabelas em html (instruções [aqui]()) com nome `YYYY-MM.html` na pasta `data/<servidor>/` e execute o comando

```
python main.py <servidor>
```

Um arquivo `<servidor>.xlsx` vai ser gerado na raiz do projeto.
