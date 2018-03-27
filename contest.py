from SynThai import SynThai


synthai = SynThai('SynThai/0063-0.0412.hdf5', 60)

def QuesTokenize(doc):
    doc = doc.split('::')
    tokens = synthai.tokenize(doc[1])
    return tokens

# def TokenQuestion(file):
#     document = open(file,'r')
#     for line in document:
#         # doc_question = document.readline()
#         line = line.split('::')
#         token_question = synthai.tokenize(line[1])
#         # print(token_question)
#     return token_question

def getQuestion():
    ques = open('Examples/question_list.txt','r')
    for line in ques:
        token_ques = QuesTokenize(line)
        cut_ques = cutword(token_ques)
        getType(cut_ques)
        keyword = findKeyword(token_ques)
        # findDoc(keyword)
        Doc = SelectDoc(keyword)
        print(Doc)
        
        print("----------------------------")
        
def findWord():
    document = open('Examples/TokenSources/1.txt','r')
    for doc in document:
        if(doc == "/NN"):
            print(doc)

def SelectDoc(keyword):
    document = open('Examples/source_list.txt','r')
    text = []
    for key in keyword:
        print(key)
        print("-------------")
        for doc in document:
            docs = open('Examples/TokenSources/'+doc.rstrip(),'r')
            for line in docs:
                words = cutword(line)
                for word in words:
                    if(key == word):
                        doc.rstrip() in text
                        if((doc.rstrip() in text) == False):
                            text.append(doc.rstrip())    
    return text


def findKeyword(token):
    keyword = []
    words = token.split("|")
    for word in words:
        key = word.split('/')
        if(len(key) == 2):
            if(key[1] == "NN"):
                keyword.append(key[0])
    return keyword

def cutword(token):
    keyword = []
    words = token.split("|")
    for word in words:
        key = word.split('/')
        if(len(key) == 2):
            keyword.append(key[0])
    return keyword

def getType(token):
    for word in token:
        if(isHuman(word) == True):
            return "Human"
        if(isLocation(word) == True):
            return "Location"
        if(Howmuch(word) == True):
            return "Numeric"
        else: "Name"

def WriteDocTokenize(file):
    source_doc = open(file,'r')
    for source in source_doc:
        sources = open('Examples/Sources/'+source.rstrip(),'r')
        token_source = open('Examples/TokenSources/'+source.rstrip(),'w+')
        for line in sources:
            token_doc = synthai.tokenize(line)
            token_source.write(token_doc)
            print(token_doc)

def Howmuch(token):
    if(token == "กี่"):
        return True
    if(token == "ไหร่"):
        return True
    else: return False

def isHuman(token):
    if(token == "ชื่อ"):
        return True
    if(token == "ใคร"):
        return True
    else: return False

def isLocation(token):
    if(token == "ไหน"):
        return True
    if(token == "ใด"):
        return True
    else: return False

# def FindInDoc(keyword):
#     # source_document = open('Examples/source_list.txt','r')
#     keywords = []
#     typeword = []
#     words = keyword.split("|")
#     for word in words:
#         key = word.split("/")
#         if(len(key) == 2):
#             if(key[1] == "NN"):
#                 # print(key[0])
#                 keywords.append(key[0])
#                 typeword.append(key[1])
#             else: continue
#         else: continue
        # for line in source_document:
        #     doc = open('Examples/Sources/'+line.rstrip(),'r')
        #     token_doc = tokenize(doc)
        #     docs = token_doc.split("|")
        #     docword = doc.split("/")
        #     if(len(docword) == 2):
        #         list_doc.append(docword[0])
        #         print(list_doc)
    



def main():
    # print(WriteDocTokenize('Examples/source_list.txt'))
    # print(TokenQuestion('Examples/question_list.txt'))
    # print(getQuestion())
    findWord()

if __name__ == '__main__':
    main()