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