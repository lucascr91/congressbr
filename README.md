# congressbr.py
*Esse pacote é uma implementação em python do pacote em R com o mesmo nome*

Atualmente, o **congressbr** tem uma classe, chamada Cham_Votes, que permite fazer o download dos dados de votação na câmara dos deputados a partir de três informações: tipo de legislação, número e ano.

**Como usar o congressbr**


```python
from congressbr import *

law=Cham_Votes(kind='PL', number='1992',year='2007')
```

Para obter os dados da PL é preciso selecionar antes o objeto de votação. Uma lista dos objetos de votação pode ser obtida com o método `obj_votacao`


```python
law.obj_votacao()
out: ['Subemenda Substitutiva Global De Plenário','Dvs - Dem - Emenda 26','Dvs - Psdb - Emenda 43','Dvs - Psdb - Art. 4º Do Projeto Original (E Seus Correspondentes.)...']
```

```python
df=law.get_data('Subemenda Substitutiva Global De Plenário')
df.head()
```
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nome</th>
      <th>partido</th>
      <th>uf</th>
      <th>voto</th>
      <th>orientacao_bancada</th>
      <th>resumo</th>
      <th>data</th>
      <th>hora</th>
      <th>objvotacao</th>
      <th>codsessao</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>160554</td>
      <td>Berinho Bantim</td>
      <td>PSDB</td>
      <td>RR</td>
      <td>Sim</td>
      <td>Sim</td>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
    </tr>
    <tr>
      <th>1</th>
      <td>141417</td>
      <td>Edio Lopes</td>
      <td>PMDB</td>
      <td>RR</td>
      <td>Sim</td>
      <td>Sim</td>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73982</td>
      <td>Luciano Castro</td>
      <td>PR</td>
      <td>RR</td>
      <td>Sim</td>
      <td>Sim</td>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
    </tr>
    <tr>
      <th>3</th>
      <td>160531</td>
      <td>Jhonatan de Jesus</td>
      <td>PRB</td>
      <td>RR</td>
      <td>Sim</td>
      <td>Sim</td>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
    </tr>
    <tr>
      <th>4</th>
      <td>160668</td>
      <td>Paulo Cesar Quartiero</td>
      <td>DEM</td>
      <td>RR</td>
      <td>Sim</td>
      <td>Não</td>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
    </tr>
  </tbody>
</table>
</div>



Metadados estão disponíveis nos atributos da instância


```python
law.url
```
`https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo=PL&numero=1992&ano=2007'`


```python
law.raw
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>@Resumo</th>
      <th>@Data</th>
      <th>@Hora</th>
      <th>@ObjVotacao</th>
      <th>@codSessao</th>
      <th>orientacaoBancada</th>
      <th>votos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aprovada a Subemenda Substitutiva Global ofere...</td>
      <td>28/2/2012</td>
      <td>20:26</td>
      <td>SUBEMENDA SUBSTITUTIVA GLOBAL DE PLENÁRIO</td>
      <td>4531</td>
      <td>{'bancada': [{'@Sigla': 'PT', '@orientacao': '...</td>
      <td>{'Deputado': [{'@Nome': 'Berinho Bantim', '@id...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rejeitada a Emenda nº 26. Sim: 11; não: 275; a...</td>
      <td>29/2/2012</td>
      <td>19:09</td>
      <td>DVS - DEM - EMENDA 26</td>
      <td>4533</td>
      <td>{'bancada': [{'@Sigla': 'PT', '@orientacao': '...</td>
      <td>{'Deputado': [{'@Nome': 'Berinho Bantim', '@id...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rejeitada a Emenda nº 43, objeto do Destaque p...</td>
      <td>29/2/2012</td>
      <td>18:48</td>
      <td>DVS - PSDB - EMENDA 43</td>
      <td>4533</td>
      <td>{'bancada': [{'@Sigla': 'PT', '@orientacao': '...</td>
      <td>{'Deputado': [{'@Nome': 'Berinho Bantim', '@id...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rejeitado o art. 4º do Projeto original e mant...</td>
      <td>29/2/2012</td>
      <td>17:59</td>
      <td>DVS - PSDB - ART. 4º DO PROJETO ORIGINAL (E SE...</td>
      <td>4533</td>
      <td>{'bancada': [{'@Sigla': 'PT', '@orientacao': '...</td>
      <td>{'Deputado': [{'@Nome': 'Berinho Bantim', '@id...</td>
    </tr>
  </tbody>
</table>
</div>


