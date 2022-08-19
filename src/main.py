'''
 _______       _ _   _              _______      _______    _     _      
|__   __|     (_) | | |            |__   __|    |__   __|  | |   | |     
   | |_      ___| |_| |_ ___ _ __     | | ___      | | __ _| |__ | | ___ 
   | \ \ /\ / / | __| __/ _ \ '__|    | |/ _ \     | |/ _` | '_ \| |/ _ \
   | |\ V  V /| | |_| ||  __/ |       | | (_) |    | | (_| | |_) | |  __/
   |_| \_/\_/ |_|\__|\__\___|_|       |_|\___/     |_|\__,_|_.__/|_|\___|
   
   Author:Felipe Oliveira
   Federal university of Rio de Janeiro
'''
########################################################################
# Requiremnts
import time

from ETL import Twitter
from ETL import DataEnginering 
from ETL import DataModel

########################################################################
# Iterate through a list of keywords
flag=1
word_counter=1

words_bag=["bolsonaro","voto"]
start_while = time.time()

print("searching for data on twitter...\n")

while flag <2:

    for query in words_bag :
        start_int = time.time()

        print("-------------------------------------------------------------------")
        print(f"turn:{flag}|word:{query}|counter:{word_counter}/{len(words_bag)}")
        
        try:
            tweets_content=Twitter().tweets(query=query)
            tweets_dataframe=DataEnginering().dataframe(tweets_content,query)
            DataModel().create(tweets_dataframe)

            end_int=time.time()
            print(f"interation elapsed time: {end_int-start_int}s")
        
        except:
            print(">error: maximum number of queries exceeded - wait 10m and try again")
            time.sleep(60*10)
            pass

        word_counter+=1
    flag+=1

end_while=time.time()
print(f"\ntotal elapsed time: {end_while-start_while}s")