# Requiremnts
import time

from ETL import DataEnginering, DataModel, Twitter

# Iterate through a list of keywords
flag = 1
word_counter = 1

words_bag = ["bolsonaro", "voto"]
start_while = time.time()

print("searching for data on twitter...\n")

while flag < 2:

    for query in words_bag:
        start_int = time.time()

        print("-------------------------------------------------------------------")
        print(f"turn:{flag}|word:{query}|counter:{word_counter}/{len(words_bag)}")

        try:
            tweets_content = Twitter().tweets(query=query)
            tweets_dataframe = DataEnginering().dataframe(tweets_content, query)
            DataModel().create(tweets_dataframe)

            end_int = time.time()
            print(f"interation elapsed time: {end_int-start_int}s")

        except Exception as error:
            print(error)
            time.sleep(60 * 10)

        word_counter += 1
    flag += 1

end_while = time.time()
print(f"\ntotal elapsed time: {end_while-start_while}s")
