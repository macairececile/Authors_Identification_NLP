import os


def retrieve_info(l):
    """retrieve header information"""
    if l.startswith("Title:"):
        metadata.write(l)
        return True
    elif l.startswith('Author:') or l.startswith('Language:'):
        metadata.write(l)
        return False
    else:
        return False


path = '/home/cecile/Bureau/nlpproject/authors/'
if __name__ == "__main__":
    for dir in os.listdir(path):
        open('/home/cecile/Bureau/nlpproject/metadata/authors/' + dir+'.txt', 'w')
        for d in os.listdir(path + dir):
            if d == 'unprocessed' or d == 'Unprocessed':
                for filename in os.listdir(path + dir + '/' + d + '/'):
                    with open(path + dir + '/' + d + '/' + filename, 'r') as file:
                        metadata = open('/home/cecile/Bureau/scriptNLP/texts_f/' + 'data_' + filename, 'w')
                        lines = file.readlines()
                        a = False
                        for line in lines:
                            if a and line != '\n':
                                metadata.write(line)
                            else:
                                a = retrieve_info(line)
