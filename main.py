import tkinter as tk

janela=tk.Tk()
janela.title('Cotação Moeda')

janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1],weight=1)

mensagem=tk.Label(text='Sistema de Busca de Cotação de Moedas',fg='white',bg='black',width=35,height=5)
mensagem.grid(row=0,column=0,columnspan=2,sticky='NSEW')

mensagem2=tk.Label(text='Selecione moeda desejada')
mensagem2.grid(row=1,column=0)

moeda=tk.Entry(bg='white')
moeda.grid(row=1,column=1)

dicionario_cotacoes={
    'Dolar':5.47,
    'Euro':6.68,
    'Bitcoin':20.000,
}


def buscar_cotaçao():
    moeda_preenchida=moeda.get()
    cotacao_moeda=dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=3,column=0)
    if cotacao_moeda:
       mensagem_cotacao['text']= f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'


botão=tk.Button(text='Buscar Cotação',command=buscar_cotaçao)
botão.grid(row=2,column=1)


janela.mainloop()