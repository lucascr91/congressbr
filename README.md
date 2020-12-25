# congressbr
*Esse pacote é uma implementação em python do [pacote em R](https://github.com/duarteguilherme/congressbr) de mesmo nome*

<!-- ##### Sumário  
[Instalação](#headers)  
[Informação geral](#headers)  
[Exemplo de uso](#headers)   -->

## Instalação

**congressbr** está disponível no PyPi e, assim, pode ser instalado pelo pip

```bash
pip install congressbr
```

## Informação geral

A unidade básica de organização do pacote são as peças legislativas. Seguindo esse princípio, atualmente, o **congressbr** possui as seguintes classes:

**Laws:** dá acesso ao nome de todas as PLs, PECs, PDCs e PLPs votadas entre 1991 e 2019. <br>
**Law:** Informações de uma peça legislativa específica. A partir dessa classe é possível acessar o texto da lei, os dados de votação de parlamentares individuais, orientações das bancadas, etc.
## Exemplo de uso

### Criando um banco de dados com os nomes de todos Projetos de Lei do período:
```python
from congressbr import *
laws=All_Laws(kind="PL")
laws.get_data()
```
```
     codproposicao tipo numero   ano datavotacao
0            20976   PL   4580  1990  17/12/1991
1           171333   PL     91  1991  18/12/1991
2           180097   PL    638  1991  28/08/1991
3           182971   PL    822  1991  28/11/1991
4           182971   PL    822  1991  03/12/1991
...            ...  ...    ...   ...         ...
2111        140375   PL   2401  2003  21/01/2004
2112        140375   PL   2401  2003  04/02/2004
2113        140375   PL   2401  2003  05/02/2004
2114        144047   PL   2546  2003  21/01/2004
2115        251745   PL   3476  2004  12/05/2004
```
### Selecionando uma PL para ver os dados de votação na Câmara:
```
law=Cham_Votes(kind='PL', number='1992',year='2007')
```
Para obter os dados da PL é preciso selecionar antes o objeto de votação. Uma lista dos objetos de votação pode ser obtida com o método `obj_votacao`:

```python
law.obj_votacao()
```

```
['Subemenda Substitutiva Global De Plenário','Dvs - Dem - Emenda 26','Dvs - Psdb - Emenda 43','Dvs - Psdb - Art. 4º Do Projeto Original (E Seus Correspondentes.)...']
```

### Orientação das bancadas:
```python
law.orientacao('Subemenda Substitutiva Global De Plenário')
```

```
{'PT': 'Sim',
 'PMDB': 'Sim',
 'PSB': 'Liberado',
 'PTB': 'Liberado',
 'PCDOB': 'Liberado',
 'PSDB': 'Sim',
 'PSD': 'Liberado',
 'PR': 'Sim',
 'PTDOB': 'Sim',
 'PRP': 'Sim',
 'PHS': 'Sim',
 'PTC': 'Sim',
 'PSL': 'Sim',
 'PRTB': 'Sim',
 'PP': 'Sim',
 'DEM': 'Não',
 'PDT': 'Não',
 'PV': 'Liberado',
 'PPS': 'Liberado',
 'PSC': 'Sim',
 'PRB': 'Sim',
 'PSOL': 'Não',
 'PMN': 'Não',
 'MINORIA': 'Liberado',
 'GOV.': 'Sim'}
```

### Dados da votação:
```python
df=law.get_data('Subemenda Substitutiva Global De Plenário')
df.head()
```

```
       id                   nome partido  uf  ...       data   hora                                 objvotacao codsessao
0  160554         Berinho Bantim    PSDB  RR  ...  28/2/2012  20:26  SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO      4531
1  141417             Edio Lopes    PMDB  RR  ...  28/2/2012  20:26  SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO      4531
2   73982         Luciano Castro      PR  RR  ...  28/2/2012  20:26  SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO      4531
3  160531      Jhonatan de Jesus     PRB  RR  ...  28/2/2012  20:26  SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO      4531
4  160668  Paulo Cesar Quartiero     DEM  RR  ...  28/2/2012  20:26  SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO      4531
```


Metadados estão disponíveis como atributos da instância


```python
law.url
```
```
'https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo=PL&numero=1992&ano=2007'
```


```python
law.raw
```
```
                                             @Resumo  ...                                              votos
0  Aprovada a Subemenda Substitutiva Global ofere...  ...  {'Deputado': [{'@Nome': 'Berinho Bantim', '@id...
1  Rejeitada a Emenda nº 26. Sim: 11; não: 275; a...  ...  {'Deputado': [{'@Nome': 'Berinho Bantim', '@id...
2  Rejeitada a Emenda nº 43, objeto do Destaque p...  ...  {'Deputado': [{'@Nome': 'Berinho Bantim', '@id...
3  Rejeitado o art. 4º do Projeto original e mant...  ...  {'Deputado': [{'@Nome': 'Berinho Bantim', '@id...
```
Para uma lista completa dos métodos e atributos da classe Cham_Votes, digite:

```
dir(law)
```

## Como contribuir

O objetivo do **congressbr** é facilitar o acesso aos dados disponibilizados pelos APIs do Congresso. No desenho atual do pacote, os serviços de dados serão acessados através de métodos e atributos da classe **Law**. Para os serviços de dados do Senado, acesse: http://legis.senado.gov.br/dadosabertos/docs/ui/index.html#/ . Para a Câmara, acesse: https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx