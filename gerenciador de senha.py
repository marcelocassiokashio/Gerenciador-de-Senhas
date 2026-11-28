import random 
import string
import customtkinter as ctk
from tkinter import messagebox


def gerar_senha():
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento <= 0:
            raise ValueError("O comprimento deve ser maior que zero")
    except ValueError:
        messagebox.showerror('Erro', 'Digite um numero valido para o comprimento da senha.')
        return

    if not caracteres:
            messagebox.showwarning('Aviso', 'Selecione ao menos um tipo de caracter!!')
            return
    
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        entry_senha.delete(0, ctk.END)
        entry_senha.insert(0, senha)
    
    
    def salvar_senha():
        nome_servico = entry_servico.get()
        senha = entry_senha.get()
    
        if not nome_servico:
            messagebox.showerror('Erro', 'Digite um nome de serviço.')
            return
        
        if not senha:
            messagebox.showerror('Erro', 'Nenhuma senha para ser gerada.')
            return
    
        nome_arquivo = "senhas.txt"
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome_servico}:{senha}\n')
    
            messagebox.showinfo('Sucesso', f'Senha salva para o serviço: {nome_servico}.')
            limpar_campos()
    
    def copiar_senha():
        senha = entry_senha.get()
    
        if senha:
            root.clipboard_clear()
            root.clipboard_append(senha)
            root.update()
            messagebox.showinfo('Sucesso', 'Senha copiada para área de transferencia.')
    
        else:
            messagebox.showwarning('Aviso', 'Nenhuma senha gerada para copiar.')
    
    def limpar_campos():
        entry_comprimento.delete(0, ctk.END)
        entry_servico.delete(0, ctk.END)
        entry_senha.delete(0, ctk.END)
        checkbox_letras.select()
        checkbox_numeros.select()
        checkbox_simbolos.select()

# PALETAS DE CORES

temas = {

    'Cinza': {
        'fundo': '#242424',
        'frame': '#303030',
        'entrada': '#454545',
        'texto': '#FFFFFF',
        'secundario': '#BDBDBD',
        'borda': '#606060',
        'botao': '#666666',
        'hover': '#858585'
    },

    'Verde': {
        'fundo': '#10251B',
        'frame': '#193B2A',
        'entrada': '#254B37',
        'texto': '#FFFFFF',
        'secundario': '#B8DCC5',
        'borda': '#397A53',
        'botao': '#238B50',
        'hover': '#32AA68'
    },

    'Azul': {
        'fundo': '#101D35',
        'frame': '#192D4D',
        'entrada': '#263F63',
        'texto': '#FFFFFF',
        'secundario': '#B8D1F0',
        'borda': '#426A9D',
        'botao': '#276CC2',
        'hover': '#3989E5'
    },

    'Vermelho': {
        'fundo': '#301616',
        'frame': '#492020',
        'entrada': '#633030',
        'texto': '#FFFFFF',
        'secundario': '#F0C1C1',
        'borda': '#914747',
        'botao': '#B83232',
        'hover': '#E04B4B'
    }
}

# APLICAR TEMA

def aplicar_tema(nome_tema):

    cores = temas[nome_tema]

    # Janela e painel
    root.configure(fg_color=cores['fundo'])
    frame.configure(fg_color=cores['frame'])

    # Títulos e textos
    label_titulo.configure(
        text_color=cores['texto']
    )

    label_creditos.configure(
        text_color=cores['secundario']
    )

    label_comprimento.configure(
        text_color=cores['texto']
    )

    label_servico.configure(
        text_color=cores['texto']
    )

    label_senha.configure(
        text_color=cores['texto']
    )

    label_tema.configure(
        text_color=cores['texto']
    )

    # Campos de entrada
    entradas = [
        entry_comprimento,
        entry_servico,
        entry_senha
    ]

    for entrada in entradas:
        entrada.configure(
            fg_color=cores['entrada'],
            text_color=cores['texto'],
            border_color=cores['borda']
        )

    # Caixas de seleção
    checkboxes = [
        checkbox_letras,
        checkbox_numeros,
        checkbox_simbolos
    ]

    for checkbox in checkboxes:
        checkbox.configure(
            text_color=cores['texto'],
            fg_color=cores['botao'],
            hover_color=cores['hover'],
            border_color=cores['borda']
        )

    # Botões
    botoes = [
        button_gerar,
        button_salvar,
        button_copiar,
        button_limpar
    ]

    for botao in botoes:
        botao.configure(
            fg_color=cores['botao'],
            hover_color=cores['hover'],
            text_color=cores['texto']
        )

    # Seletor de tema
    menu_tema.configure(
        fg_color=cores['botao'],
        button_color=cores['botao'],
        button_hover_color=cores['hover'],
        text_color=cores['texto'],
        dropdown_fg_color=cores['frame'],
        dropdown_text_color=cores['texto'],
        dropdown_hover_color=cores['botao']
    )