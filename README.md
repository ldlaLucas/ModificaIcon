# 🗂️ Script para Alterar Ícones de Pastas com Python

Um script em Python para personalizar ícones de pastas de forma simples e rápida.

## 🚀 Como Usar

1. Clone o repositório:
   ```sh
   git clone https://github.com/ldlaLucas/ModificaIcon.git
   ```

2. Navegue até o diretório do projeto:
   ```sh
   cd ModificaIcon
   ```

3. Instale as dependências:
   ```sh
   pip install tk pyinstaller
   ```

4. Crie o executável:
   ```sh
   pyinstaller --onefile --windowed mudar_icone.py
   ```

5. Execute o script:
   - Navegue até a pasta `dist`:
     ```sh
     cd dist
     ```
   - Execute o `mudar_icone.exe`.

## 🛠️ Funcionalidades

- **Seleção de Pasta**: Escolha a pasta que deseja personalizar.
- **Seleção de Ícone**: Escolha um ícone personalizado no formato `.ico`.
- **Aplicação Automática**: O script aplica o novo ícone à pasta selecionada.
- **Criação Automática de Pasta de Ícones**: Cria a pasta `icons`, caso ela não exista.
- **Interface Gráfica**: Interface gráfica amigável com mensagens de sucesso e erro.

## 📁 Estrutura do Projeto

```
ModificaIcon/
├── mudar_icone.py
├── README.md
├── .gitignore
└── icons/
```

## 📜 Requisitos

- **Python 3.x**
- **tkinter**
- **pyinstaller**

## 👥 Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua modificação:
   ```sh
   git checkout -b minha-modificacao
   ```
3. Faça o commit:
   ```sh
   git commit -m "Descrição da modificação"
   ```
4. Envie para o seu repositório remoto:
   ```sh
   git push origin minha-modificacao
   ```
5. Abra um Pull Request.

## 👤 Autor

- **Lucas** - [Seu Perfil no GitHub](https://github.com/ldlaLucas)
