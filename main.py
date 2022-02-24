from itertools import itertool
# all'interno della classe vi sono alcune variabili ad esempio "n" doppie poichè n è presente sia come variabile di istanza e viene usata in alcuni metodi,
# mentre in altre funzioni viene data in input come ad esempio nella funzione che restituisce il coefficiente binomiale
def anagrammi(self): 
        import itertools
        '''
        word -> deve contenere la stringa da analizzare
        carattere -> è il dictionary all'interno del quale salvare le informazioni 
        count -> contiene il numero totale di ripetizioni
        nCaratteri -> contiene il numero di caratteri che si ripetono
        '''
        listapermutazioni = list(itertools.permutations(self.__stringa))
        temp = ''
        anagrammi = []
        for i in listapermutazioni:
            for carattere in i:
                
                temp += carattere 

            anagrammi.append(temp)
            
            temp = ''
        return anagrammi 
class calcComb():
    '''
    lingua = input() #questa potrebbe anche essere inizializzata come attributo di classe, indeciso se di classe o di instanaza 
    '''
    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(self.__stringa)    
        self.__presenza = None #questa potrebbe anche essere inizializzata come attributo di classe, indeciso se di classe o di instanaza 
    '''
    def selezione_lingua(self):
        lingua = {"Italiano":"word.italian.txt"}
        lingua["Italiano"]  #in questo punto potrebbe essere integrato un'input per chiedere all'utente la lingua del gioco
        return lingua #da discutere come usare questa funzione, fino a quel punto la escludo dalle variabili prese dal confutil
    '''
    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def charRipetuti(self):

        word = self.liststringa  

        carattere = {}

        nCaratteri = 0

        count = 0

        for i in word:

            if (i in carattere):  
                carattere[str(i)] += 1
            else:
                carattere[str(i)] = 1 

        for i in carattere:
            if carattere[i]>1: 
                count+=1 
                nCaratteri += carattere[i] 
  
        Variabili_anagrammi = [count,nCaratteri,carattere]
        
        return Variabili_anagrammi

    '''def confUtil(self,lingua):
        
        f = open(lingua, 'r')
        
        riga = f.readline()
        Presenza == False
        for riga in f:
            if self.__stringa == riga[:-1]:
                Presenza == True

        return Presenza
    '''
    
    def confUtilD(self,word):  #verifica se la parola presa in input come attributo di istanza è presente nel dizionario
            
        f = open('r')   #f = open(lingua, 'r')
        
        riga = f.readline()
        self.__presenza == False
        for riga in f:
            if word == riga[:-1]:
                self.__presenza == True

        return self.__presenza
    
    def fattoriale(n):
        n=int(n)
        f = 0 
        if n < 0: 
            print("Non è possibile calcolare il fattoriale di un numero negativo")
        elif n == 0: 
            f= 1
        else: 
            f = 1
            
            while(n > 1): 
                f *= n 
                n -= 1
            
        return f
    
    def coeffBinom(n, k):
        if k == n:
            cb = 1
        
        elif k == 1:         
            cb = n
        
        elif k > n:          
            cb = 0
        
        else:
            cb = calcComb.fattoriale(n) // (calcComb.fattoriale(n) * calcComb.fattoriale(n-k))
    
        return cb
    
    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        NPSR = calcComb.fattoriale(self.__N)
        return NPSR
     

    def nPermutConRip(self):
        NPCR = calcComb.fattoriale(self.__N)/calcComb.charRipetuti(self.__count)
        return NPCR

    def PermutSenzaRip(self):
        import itertools
        listapermutazioni = list(itertools.permutations(self.__stringa))
        temp = ''
        anagrammi = []
        for i in listapermutazioni:
            for carattere in i:
                
                temp += carattere 

            anagrammi.append(temp)
            
            temp = ''
        return anagrammi 

    def permutConRip(self):
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self,k):
        if self.__N >= k:
               NDSSR = calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N-k)
        else:
           print("Si tratta di disposizini semplici!!! n>k")
        return NDSSR
      
            
        

    def nDispSemplConRip(self,k):
        NDSCR = self.__N**k
        return NDSCR

    def dispSemplConRip(self):
        import itertools
        
        listapermutazioni = list(itertools.permutations(self.__stringa))
        temp = ''
        disp = []
        for i in listapermutazioni:
            for carattere in i:
                
                temp += carattere 

            disp.append(temp)
            
            temp = ''
        return disp 

    # COMBINAZIONI

    def nCombSemplSenzaRip(self,k):
        NCSSR = calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

        return NCSSR

    def nCombSemplConRip(self,k):
        NCSCR = calcComb.fattoriale(self.__N+k-1) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-1))
        return 


    def combSenzaRip(self,k):
        import itertools
        listacombinazioni = list(itertools.combinations(self.__stringa, k))
        temp = ''
        comb = []
        for i in listacombinazioni:
            for carattere in i:
                temp += carattere 
            comb.append(temp)
            temp = ''
        return comb


    def combConRip(self,k):
        import itertools
        listacombinazioni = list(itertools.combinations_with_replacement(self.__stringa, k))
        temp = ''
        comb = []
        for i in listacombinazioni:
            for carattere in i:
                temp += carattere 
            comb.append(temp)
            temp = ''
        return comb
    # PROBABILITA'

    def probConfUtil(self):
        # qui basta tirarsi fuori il numero di casi favorevoli usando il metodo confutil per sapere quanti degli anagrammi esistono
        # e dividerlo per il numero totale di anagrammi che si ottiene facendo il len della tupla degli anagrammi
        #wip
        casifav = 0
        for i in self.__anagrammi: 
            Vtemp = calcComb.confUtil(i)
            if Vtemp == False:
                None
            elif Vtemp == True:
                casifav += 1
        
        Prob = casifav/(len(self.__anagrammi))
        return Prob

    
