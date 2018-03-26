from SynThai import SynThai


synthai = SynThai('SynThai/0063-0.0412.hdf5', 60)

def tokenize(doc):
    token_string = []
    tokens = synthai.tokenize(doc)
    return tokens

def TokenQuestion(file):
    document = open(file,'r')
    for line in document:
        # doc_question = document.readline()
        line = line.split('::')
        token_question = tokenize(line[1])
        FindInDoc(token_question)
        print(token_question)
    return token_question

def FindInDoc(keyword):
    keywords = []
    words = keyword.split("|")
    for word in words:
        key = word.split("/")
        if(len(key) == 2):
            if(key[1] == "NN"):
                print(key[0])
                keywords.append(key[0])
            else: continue
        else: continue
    return keywords



def main():
    TokenQuestion('Examples/question_list.txt')
    
if __name__ == '__main__':
    main()