import pandas as pd 
import pandas_read_xml as pdx
import requests
import re
from tika import parser


class All_Laws:
    def __init__(self, kind="all", number="all", year="all"):
        self.kind=kind
        self.number=number
        self.year=year

    def get_data(self):
        df=pd.read_pickle('congress/data/all_laws.pkl')
        if (self.kind=='all') & (self.number=='all') & (self.year=='all'):
            return df
        elif (self.kind=='all') & (self.number=='all'):
            df=df[df['ano']==self.year]
            return df
        elif (self.kind=='all') & (self.year=='all'):
            df=df[df['numero']==self.number]
            return df
        elif (self.year=='all') & (self.number=='all'):
            df=df[df['tipo']==self.kind]
            return df
        elif (self.kind=='all'):
            df=df[(df['ano']==self.year) & df['numero']==self.number]
            return df
        elif (self.number=='all'):
            df=df[(df['ano']==self.year) & df['kind']==self.kind]
            return df
        elif (self.year=='all'):
            df=df[(df['tipo']==self.kind) & df['numero']==self.number]
            return df
        

class Cham_Votes:
    def __init__(self, kind, number, year):
        self.kind=kind
        self.number=number
        self.year=year
        response=requests.get(self.url)
        if response.status_code!=200:
            raise ValueError("A problem occurs when trying to download data. Status error code: {:d}. Make sure this law exists.".format(response.status_code))
        else:
            pass

    @property
    def url(self):
        """
        instance url
        """
        url='https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo={}&numero={}&ano={}'.format(self.kind, self.number, self.year)
        return url
    
    @property
    def raw(self):
        """
        Raw data from XML file
        """
        raw=pdx.read_xml(self.url,['proposicao', 'Votacoes', 'Votacao'])
        return raw

    @property
    def title(self):
        return "{} {}/{}".format(self.kind, self.number, self.year)

    def obj_votacao(self, only_keys=True):
        """
        Each votation is divided into a main text vote and amendment vote. This method returns the list of voting objects.
        """
        obj=[re.sub(r'\s+', ' ',k.title().strip()) for k in self.raw['@ObjVotacao'].to_list()]
        dict_obj={k:v for v,k in enumerate(obj)}
        if only_keys:
            return list(dict_obj.keys())
        else:
            return dict_obj

    def orientacao(self, obj):
        """
        Returns dictionary with voting guidance to parties and groups
        """
        index=self.obj_votacao(only_keys=False)[obj]
        global orientacao
        orientacao=pd.DataFrame(self.raw.orientacaoBancada[index]['bancada'])
        orientacao.columns=['partido','orientacao_bancada']
        for col in orientacao.columns:
            try:
                orientacao[col]=orientacao[col].str.strip()
            except:
                pass
        group_parties=[k for k in orientacao.partido.to_list() if bool(re.search(r'[A-Z][a-z]+[A-Z]',k))]
        single_parties=[k for k in orientacao.partido.to_list() if not bool(re.search(r'[A-Z][a-z]+[A-Z]',k))]
        parties_dict={k:k for k in single_parties}
        parties_dict.update({parties: re.findall(r'[A-Z][a-z]+', parties) for parties in group_parties})
        orientacao.partido=orientacao.partido.map(parties_dict)
        orientacao=orientacao.explode('partido')
        orientacao.partido=orientacao.partido.str.upper()
        orientacao_dict=orientacao.set_index("partido").to_dict()['orientacao_bancada']
        return orientacao_dict

    def get_data(self, obj):
        """
        This method returns votation data, after the user have selected the object of votation.
        """
        index=self.obj_votacao(only_keys=False)[obj]
        cham_votes=pd.DataFrame(self.raw.votos[index]['Deputado'])
        cham_votes.columns=['nome','id','partido','uf','voto']
        for col in cham_votes.columns:
            try:
                cham_votes[col]=cham_votes[col].str.strip()
            except:
                pass
            
        for data in [cham_votes,orientacao]:
            data['partido']=data['partido'].apply(lambda x: x.strip())

        cham_votes['orientacao_bancada']=cham_votes['partido'].map(self.orientacao(obj))

        for col in ['@Resumo','@Data','@Hora','@ObjVotacao','@codSessao']:
            cham_votes[col.lower().replace('@','')]=self.raw.loc[index,col]

        cham_votes=cham_votes.reindex(['id','nome', 'partido', 'uf', 'voto', 'orientacao_bancada', 'resumo',
         'data', 'hora', 'objvotacao', 'codsessao'], axis=1)
        return cham_votes

    def get_text(self):
        url='https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=501938&filename={}+{}/{}'.format(self.kind, self.number, self.year)
        response=requests.get(url)
        r = requests.get(url, stream=True)
        print(parser.from_buffer(r.content)['content'])

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title

