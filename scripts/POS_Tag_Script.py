from nltk import sent_tokenize, word_tokenize, pos_tag
import os
def main():
    
    path = 'C:\\Users\\Utilisateur\\Documents\\NLP\\NLP Project\\ProcessedAuthors'
    name = 'POStagged_'
    for f in os.walk(path):
        if __name__ == "__main__":
            for filename in os.listdir(path):
                with open('C:\\Users\\Utilisateur\\Documents\\NLP\\NLP Project\\ProcessedAuthors\\' + filename , "r", encoding="utf-8") as file:
                    fl = file.readlines()
                    file.close
                    booklist = []
                    for line in fl:
                        booklist.append(line.rstrip())
                    booklist = list(filter(None, booklist))
    
                    fil= open('C:\\Users\\Utilisateur\\Documents\\NLP\\NLP Project\\POStagged\\' + name + filename, "w+", encoding="utf-8")
                    for i in range(0, len(booklist)):
                        text=booklist[i]
                        text=[pos_tag(word_tokenize(sent)) for sent in sent_tokenize(text)]
                        fil.write(str(text))
    
                fil.close
    print("here")
    
main()
