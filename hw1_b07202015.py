import re
  

def hw1(task,s,n=1):
    assert task in range(1,5)
    if task==4:
        sp = re.split('!|\?|\.',s)
        return max(sp, key=len)

    sp = s.split()
    if task==1:
        return max(set(sp), key = sp.count)

    s_out = [[]]*len(sp)
    for i,word in enumerate(sp):
        word_ascii=[ord(e) for e in word]
        if task==2:
            word_ascii=[(e-65+n)%26+65 if e in range(65,91) else e for e in word_ascii]
            word_ascii=[(e-97+n)%26+97 if e in range(97,123) else e for e in word_ascii]
            temp=[chr(e) for e in word_ascii]
            s_out[i]=''.join(temp)
        if task==3:
            word_alpha=[e for e in word if e.isalpha()]
            word_notalpha=[e if not e.isalpha() else 'NaN' for e in word]
            word_alpha.sort(key=lambda x: x.lower())
            # word=[e if e!='NaN' else word_notalpha[i] for i,e in enumerate(word_alpha)]
            temp=[]
            count=0
            for e in word_notalpha:
                if e=='NaN':
                    temp.append(word_alpha[count])
                    count+=1
                else:
                    temp.append(e)
            s_out[i]=''.join(temp)
    return ' '.join(s_out)

if __name__=='__main__':
    s="Python was conceived in the late 1980s by Guido van Rossum at Centrum"\
    "Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC"\
    "programming language, which was inspired by SETL, capable of"\
    "exception handling and interfacing with the Amoeba operating system. Its"\
    "implementation began in December 1989. Van Rossum shouldered sole"\
    "responsibility for the project, as the lead developer, until 12 July 2018,"\
    "when he announced his \"permanent vacation\" from his responsibilities as"\
    "Python's Benevolent Dictator For Life, a title the Python community"\
    "bestowed upon him to reflect his long-term commitment as the project's"\
    "chief decision-maker. In January 2019, active Python core developers"\
    "elected a five-member \"Steering Council\" to lead the project."

    # Things are implemented here
    # task==1 : Find the most frequently used words.
    # task==2 : Shift every alphabets with given integer n.
    # task ==3 : Sort every words in alphebet order.
    # task ==4 : Find the longest sentence

    task = 4
    n=-1 #for task==2
    output=hw1(task,s,n)
    print(output)
