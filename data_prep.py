import json
import random
import glob

class Sentiment:
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"

database = []
data = []

path = r'C:\Users\fathu\Documents\Sentiment Analysis Data\data'
files = glob.glob(path + "/*.json")

for file in files:
    with open(file) as f:
        for line in f:
            review = json.loads(line)
            year = int(review['reviewTime'].split(' ')[-1])
            if year == 2014:
                data.append(review)
    
    data_sample = random.sample(data, 5000)
    for i in range(len(data_sample)):
        if data_sample[i]['overall'] <= 2:
            data_sample[i]['sentiment'] = Sentiment.NEGATIVE
        elif data_sample[i]['overall'] == 3:
            data_sample[i]['sentiment'] = Sentiment.NEUTRAL
        else:
            data_sample[i]['sentiment'] = Sentiment.POSITIVE

    filter_positive = list(filter(lambda x: x['sentiment'] == Sentiment.POSITIVE, data_sample))
    filter_negative = list(filter(lambda x: x['sentiment'] == Sentiment.NEGATIVE, data_sample))
    filter_neutral = list(filter(lambda x: x['sentiment'] == Sentiment.NEUTRAL, data_sample))

    count_sentiment = [len(filter_positive), len(filter_negative), len(filter_neutral)]
    
    positive_shrunk = filter_positive[:min(count_sentiment)]
    neutral_shrunk = filter_neutral[:min(count_sentiment)]
    negative_shrunk = filter_negative[:min(count_sentiment)]

    final_data = positive_shrunk + neutral_shrunk + negative_shrunk
    
    database.append(final_data)
    print(f'done {file}')


flat_database = [item for sublist in database for item in sublist]
print(len(flat_database))

print('Selesai')

with open('database.json', 'w') as f:
	for review in flat_database:
		f.write(json.dumps(review)+'\n')
