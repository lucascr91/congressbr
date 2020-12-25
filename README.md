# congressbr
*Esse pacote é uma implementação em python do [pacote em R](https://github.com/duarteguilherme/congressbr) de mesmo nome*

## Instalação

**congressbr** está disponível no PyPi e, assim, pode ser instalado pelo pip

```bash
pip install congressbr
```

## Uso

Atualmente, o **congressbr** possui as seguintes classes:

**Cham_Votes:** permite fazer o download dos dados de votação na câmara dos deputados a partir de três informações: tipo de legislação, número e ano.

### Exemplo:

```python
from congressbr import *

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