from SynThai import SynThai
import re

synthai = SynThai('SynThai/0063-0.0412.hdf5', 60)

def QuesTokenize(doc):
    doc = doc.split('::')
    tokens = synthai.tokenize(doc[1])
    return tokens

def getQuestion():
    ques = open('Examples/question_list.txt','r')
    for line in ques:
        token_ques = QuesTokenize(line)
        cut_ques,typecut = cutword(token_ques)
        types = getType(cut_ques)
        keyword = findKeyword(token_ques)
        # findDoc(keyword)
        Doc = SelectDoc(keyword)
        print(keyword)
        findAns(keyword,Doc,types)
        print("----------------------------")

def findAns(keyword,doc,typeques):
    ans = []*5
    for docs in doc:
        document = open('Examples/TokenSources/'+docs.rstrip(),'r')
        for word in document:
            words ,typeword = cutword(word)
            for noun in keyword:
                index = 0
                for text in words:
                    if(text == noun):
                        if(typeques == "Numeric"):
                            for typenoun in range(len(typeword)):
                                if(typeword[typenoun] == "CD" and typeword[typenoun+1] == "CL"):
                                    if(len(ans) < 5):
                                        ans.append(words[typenoun]+" "+ words[typenoun+1])
                                    else: 
                                        print(ans)
                                        return ans
                        if(typeques == "Human"):
                            for typehuman in range(len(typeword)):
                                if((typeword[typehuman] == "NR" and typeword[typehuman+1] == "NR")):
                                    if(len(ans) < 5):
                                        if((words[typehuman]+" "+words[typehuman+1] in ans) == False):
                                            ans.append(words[typehuman]+" "+words[typehuman+1])
                                    else: 
                                        print(ans)
                                        return ans
                        if(typeques == "Location"):
                            for typeplace in range(len(typeword)):
                                if(typeword[typeplace] == "NR" and typeword[typeplace+1] == "NN"):
                                    if(len(ans) < 5):
                                        if((words[typeplace] in ans) == False):
                                            ans.append(words[typeplace])
                                    else:
                                        print(ans)
                                        return ans
                    index += 1
    print(ans)


# def splitDoc(source):
#     document = open('Examples/TokenSources/'+source.rstrip(),'r')
#     for word in document:
#         words, typeword = cutword(word)
#     return words, typeword


def SelectDoc(keyword):
    document = open('Examples/source_list.txt','r')
    text = []
    for key in keyword:
        for doc in document:
            docs = open('Examples/TokenSources/'+doc.rstrip(),'r')
            for line in docs:
                words,typeword = cutword(line)
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
    typekey = []
    words = token.split("|")
    for word in words:
        key = word.split('/')
        if(len(key) == 2):
            keyword.append(key[0])
            typekey.append(key[1])
    return keyword , typekey

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

def main():
    # print(WriteDocTokenize('Examples/source_list.txt'))
    # print(TokenQuestion('Examples/question_list.txt'))
    print(getQuestion())

if __name__ == '__main__':
    main()