import json
import pandas as pd

def main():

    #Pull data and parse through JSON
    devset = parseSet("/Users/rollerc/AFRL/2018/Development/iqa/SQUAD/dev-v1.1.json", train=False)
    print("Devset Size =%s " % devset.size)
    trainset = parseSet("/Users/rollerc/AFRL/2018/Development/iqa/SQUAD/train-v1.1.json", train=True)
    print("Trainset Size =%s " % trainset.size)

def parseSet(path, train=True):

    good_columns = [
        "id",
        "qid",
        "topic",
        "context",
        "question",
        "answer"]

    dataset = []
    #questions = []
    #answers = []

    count = 1
    with open(path, 'r') as f:
        jsonFile = json.load(f)
        version = jsonFile['version']
        print("Dataset Version = %s" % version)
        for part in jsonFile['data']:
            title = part['title']
            #print("Train=%s, Title=%s, Paragraphs= %s" % (train, title, len(part['title'])))
            #Context And Question / Answers
            for paragraph in part['paragraphs']:
                context = paragraph['context']
                for qas in paragraph['qas']:
                    question = qas['question']
                    #questions.append(question)
                    id = qas['id']
                    for answer in qas['answers']:
                        #answers.append(answer['text'])
                        dataset.append([count, id, title, context, question, answer['text']])
                        count += 1

    return pd.DataFrame(dataset, columns=good_columns)

if __name__ == "__main__":
    main()