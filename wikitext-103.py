#wikitext-103
import csv
import re
pattern=re.compile("^\s=\s[a-zA-Z\s]+=")
outputfile='/home/randy/Downloads/wikitext-103/all_articles.csv'
f_out=open (outputfile, "w")
article_flag=False
txt=""
with open("/home/randy/Downloads/wikitext-103/wiki.train.tokens.doc") as csv_file, f_out:
    csv_reader =csv.reader(csv_file)
    csv_writer=csv.writer(f_out)
    for row in csv_reader:
        for i in row:
            if pattern.match(i):
                if article_flag==True:
                #write out
                    csv_writer.writerow([j,txt])
                    txt=""
                j=i.replace('=','').strip(' ')
                article_flag=True
                
            else:
                txt=txt+i

        
print('alldone')
                
