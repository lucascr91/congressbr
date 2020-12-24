import pandas as pd 
import pandas_read_xml as pdx
import requests
import re

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
        raw data from XML file
        """
        raw=pdx.read_xml(self.url,['proposicao', 'Votacoes', 'Votacao'])
        return raw


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
    def get_data(self, obj):
        """
        This method returns votation data, after the user have selected the object of votation.
        """
        index=self.obj_votacao(only_keys=False)[obj]
        orientacao=pd.DataFrame(self.raw.orientacaoBancada[index]['bancada'])
        orientacao.columns=['partido','orientacao_bancada']
        cham_votes=pd.DataFrame(self.raw.votos[index]['Deputado'])
        cham_votes.columns=['nome','id','partido','uf','voto']
        for col in cham_votes.columns:
            try:
                cham_votes[col]=cham_votes[col].str.strip()
            except:
                pass

        for col in orientacao.columns:
            try:
                orientacao[col]=orientacao[col].str.strip()
            except:
                pass
            
        for data in [cham_votes,orientacao]:
            data['partido']=data['partido'].apply(lambda x: x.strip())

        group_parties=[k for k in orientacao.partido.to_list() if bool(re.search(r'[A-Z][a-z]+[A-Z]',k))]
        single_parties=[k for k in orientacao.partido.to_list() if not bool(re.search(r'[A-Z][a-z]+[A-Z]',k))]
        parties_dict={k:k for k in single_parties}
        parties_dict.update({parties: re.findall(r'[A-Z][a-z]+', parties) for parties in group_parties})
        orientacao.partido=orientacao.partido.map(parties_dict)
        orientacao=orientacao.explode('partido')
        orientacao.partido=orientacao.partido.str.upper()
        orientacao_dict=orientacao.set_index("partido").to_dict()['orientacao_bancada']
        cham_votes['orientacao_bancada']=cham_votes['partido'].map(orientacao_dict)

        for col in ['@Resumo','@Data','@Hora','@ObjVotacao','@codSessao']:
            cham_votes[col.lower().replace('@','')]=self.raw.loc[index,col]

        cham_votes=cham_votes.reindex(['id','nome', 'partido', 'uf', 'voto', 'orientacao_bancada', 'resumo',
         'data', 'hora', 'objvotacao', 'codsessao'], axis=1)
        return cham_votes