# The Brazilian's: Cultura Brasileira

**The Brazilian's** é um site dedicado à cultura brasileira, explorando suas diversas vertentes: **Literatura**, **Gastronomia**, **Música**, **Arquitetura** e **Cinema**. O objetivo do projeto é fornecer um espaço centralizado onde usuários possam aprender mais sobre essas áreas, através de textos, imagens e curiosidades.

O site possui uma estrutura simples, com uma interface amigável e um design que reflete as cores vibrantes da cultura brasileira. Todo o conteúdo é publicado e gerenciado pelos administradores, sem a opção de comentários pelos usuários.

## Funcionalidades

- **Literatura**: Explore a rica produção literária brasileira, com artigos sobre autores, obras e movimentos literários.
- **Gastronomia**: Descubra receitas tradicionais, ingredientes e a história da culinária brasileira.
- **Música**: Conheça os gêneros musicais, artistas e a evolução da música no Brasil.
- **Arquitetura**: Destaque para as principais obras arquitetônicas e estilos que moldaram o Brasil.
- **Cinema**: Informações sobre filmes, cineastas e a evolução do cinema brasileiro.

### Funcionalidades Adicionais

- **CRUD de Culturas**: Gerencie diferentes culturas.
- **CRUD de Posts**: Adicione e gerencie postagens.
- **CRUD de Responsáveis**: Gerencie responsáveis pelo conteúdo.
- **CRUD de Subcategorias**: Adicione e gerencie subcategorias.
- **CRUD de Tipo de Responsável**: Defina e gerencie diferentes tipos de responsáveis.
- **CRUD de Usuários**: Adicione e gerencie usuários.
- **CRUD de Usuários e Posts**: Gerencie a relação entre usuários e postagens.
- **Interface Amigável**: Uma interface intuitiva desenvolvida com HTML e CSS, proporcionando uma boa experiência ao usuário.
- **Interatividade**: Uso de JavaScript para manipulação de dados e chamadas assíncronas à API.

## Tecnologias Utilizadas

- **Backend**: Python (FastAPI)
- **Frontend**: 
  - HTML5
  - CSS3
  - JavaScript
- **Banco de Dados**: SQLite / MySQL / PostgreSQL

## Estrutura do Projeto

```plaintext
The-Brazilians/
│
├── backend/               # Código backend (Python)
│   ├── culturas.py        # Gerenciamento de culturas
│   ├── posts.py           # Gerenciamento de posts
│   ├── responsaveis.py    # Gerenciamento de responsáveis
│   ├── subcategorias.py    # Gerenciamento de subcategorias
│   ├── tipo_responsavel.py # Tipos de responsáveis
│   ├── usuarios.py        # Gerenciamento de usuários
│   ├── usuariospost.py    # Relação entre usuários e posts
│   └── viewsResp.py       # Visualizações dos responsáveis
│
├── frontend/              # Arquivos do frontend (HTML, CSS, JS)
│   ├── index.html         # Página principal
│   ├── css/               # Arquivos CSS
│   │   └── styles.css     # Estilos principais
│   └── js/                # Scripts JavaScript
│       └── scripts.js     # Scripts principais
│
├── README.md              # Documentação
└── requirements.txt       # Dependências do projeto

└── requirements.txt       # Dependências do projeto
