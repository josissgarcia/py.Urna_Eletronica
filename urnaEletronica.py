
class Urna_Eletronica:
    def __init__(self):
        self.candidatos = [
            {"Nome_Candidato": "Maria","Partido": "ABC"},
            {"Nome_Candidato": "João", "Partido": "TES"},
            {"Nome_Candidato": "Rafael", "Partido": "PRS"}
            ]
   
    
    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print (f'Nome do candidato: {candidato["Nome_Candidato"]}, Partido: {candidato.get("Partido")}') # 2 formas de pegar
            
    def adicionar_candidato(self,Nome_Candidato, Partido):
        self.candidatos.append({"Nome_Candidato": Nome_Candidato,"Partido":  Partido})
    
   
    def remover_candidato(self,nome_candidato):
        check=False
        for candidato in self.candidatos:
            if candidato["Nome_Candidato"] == nome_candidato:
                self.candidatos.remove(candidato)
                return "Candidato removido com sucesso!"
                check = True
                
        if check == False:
          return "Candidato não encontrado!" 
                
          
    def remover_Ultimo_Candidato(self):
      self.candidatos.pop()
      
    
    def atualizar_candidato(self,indice,nome=None, partido=None):
        if nome != None:
            self.candidatos[indice]["Nome_Candidato"] = nome
        if partido != None:
            self.candidatos[indice]["Partido"] = partido
        
         

              
urna = Urna_Eletronica()
urna.exibe_candidatos()
print('-------------------------------------')

urna.adicionar_candidato( "JOSI",  "CTR")
urna.exibe_candidatos()
print('-------------------------------------')

print(urna.remover_candidato("Maria"))
urna.exibe_candidatos()
print('-------------------------------------')

urna.remover_Ultimo_Candidato()
urna.exibe_candidatos()
print('-------------------------------------')

urna.atualizar_candidato(0,"Francisco Gomes" ,"TAD")
urna.exibe_candidatos()