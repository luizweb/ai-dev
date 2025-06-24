## GitHub CLI

A ferramenta **GitHub CLI** é uma interface de linha de comando que permite interagir com o GitHub diretamente pelo terminal, facilitando tarefas como criação de *issues*, *pull requests* e gerenciamento de repositórios de forma rápida e automatizada.

🔗 [https://cli.github.com](https://cli.github.com)

---

## Comandos iniciais

```bash
$ gh auth login
```
→ O comando é usado para autenticar sua conta do GitHub por meio de um processo interativo no terminal.

```bash
$ gh auth status
```
→ Exibe o status da autenticação atual, mostrando se você está conectado ao GitHub e com quais permissões.

```bash
$ gh repo list
```
→ Comando para listar seus repositórios.

---

## Criar um novo repositório no GitHub

**Navegue até o diretório do projeto:**

```bash
$ cd /caminho/para/seu/projeto
```

**Criar o repositório:**

```bash
$ gh repo create <nome-do-repo> --private
```
→ Cria um novo repositório no GitHub definindo a visibilidade (`--public` ou `--private`)

---

## Inicializar o repositório local com o Git:

```bash
$ git init
```

```bash
$ git remote add origin git@github.com:usuario/nome-do-repositorio.git
```

---

## Atualizar descrição do repositório:

```bash
$ gh repo edit --description "<descrição do repositório>"
```
→ Atualiza a descrição do repositório
