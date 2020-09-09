import os
import nltk

path = '/home/cecile/Bureau/nlpproject/processed_with_script/'
name = 'processedbysentences_'

if __name__ == "__main__":
    for filename in os.listdir(path):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        file = open('/home/cecile/Bureau/nlpproject/processed_with_script/' + filename)
        data = file.read()
        output_file = open('/home/cecile/Bureau/scriptNLP/texts/' + name + filename, 'w')
        output_file.write('\n\n'.join(tokenizer.tokenize(data)))
        f = open('/home/cecile/Bureau/nlpproject/texts_by_sentences/'+name+filename, 'w')
        with open('/home/cecile/Bureau/scriptNLP/texts/' + name + filename, 'r') as fi:
            line = ''
            tab = []
            for lines in fi:
                if lines != '\n':
                    line += lines[:-1] + ' '
                else:
                    a = line[:-1] + '\n\n'
                    f.write(a)
                    line = ''

