from ctypes import wstring_at
import redis
import random
gioco = 'ColonnaDeVitaMattielloSigillo' 
account1= None 
account2 = None 
r = redis.StrictRedis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)
r.keys
def aggiorna_database_classifica(gioco,account):
    kdb = bytes(gioco + '_' + account, 'utf-8')
    print(kdb)
    if kdb in r.keys():
        print('Già salvato')
    else:
        r.sadd(kdb,'valore partita')  #il punteggio partita è un valore numerico separato da : che separano i giocatori in ordine di apparizione
r.keys()


it = "words.italian.txt"
f = open(it, 'r')
line = f.readline()

def insCanc():
    
    if(r.scard(it)>0):
        for i in range(r.scard(it)):  
                r.spop(it)
                print(r.scard(it))

    else:
        for line in f:  
            r.sadd(it, line[:-1])
            print(line[:-1])
            print(r.scard(it))

        
def cerca(parola):
    str = (parola)  # parola è la parola insreita dall'utente 
    risultato = r.sismember(it,str)
    print(it)

    if (risultato):
        print("trovato!")
    else: print("non trovato!")

def crea_account():
    nomeutente = str(gioco)+str('aldo')#None #input dell'utente
    password = str('pippo') #None #input dell'utente
    id = generaid
    profiloutentedb = bytes(':'.join([nomeutente,password,id]), 'utf-8')
    r.set(id,profiloutentedb)
 

def generaid():
    idt = 0
    idt += 1
    return idt




