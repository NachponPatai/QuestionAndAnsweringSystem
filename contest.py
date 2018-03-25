from SynThai import SynThai


synthai = SynThai('SynThai/0063-0.0412.hdf5', 60)

def tokenize(doc):
    token_string = []
    tokens = synthai.tokenize(doc)
    return tokens

def main():
    document = open('Examples/question_list.txt','r')
    for line in document:
        # doc_question = document.readline()
        line = line.split('::')
        token_question = tokenize(line[1])
        print(token_question)

if __name__ == '__main__':
    main()