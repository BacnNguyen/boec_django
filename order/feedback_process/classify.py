def intersection(lst1, lst2):
    for w in lst2:
        if w in lst1:
            return True
    return False
def check(sentense):
    #load positive word
    f=open('G:\\Ky2_Nam4\\PhatTrienHeThongThuongMaiDT\\testBoEC\\BoEC-main\\order\\feedback_process\\pos_words.txt','r')
    pos_words = []
    while True:
        line = f.readline()
        if not line:
            break
        pos_words.append(line.split('\n')[0])

    f.close()
    #load negative word
    f1 = open('G:\\Ky2_Nam4\\PhatTrienHeThongThuongMaiDT\\testBoEC\\BoEC-main\\order\\feedback_process\\neg_words.txt','r')
    neg_words = []
    while True:
        line = f1.readline()
        if not line:
            break
        neg_words.append(line.split('\n')[0])

    f1.close()
    ##############################
    words = sentense.split(' ')
    
    if intersection(words,pos_words):
        # print("Positive")
        return "Positive"
    elif intersection(words,neg_words):
        # print("Negative")
        return "Negative"
    else:
        # print("Neutral") 
        return "Neutral"

if __name__=='__main__':
    sentense = "Sản phẩm đẹp quá"
    print('Result:',check(sentense))