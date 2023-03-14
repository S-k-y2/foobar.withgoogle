
def solution(x):
    plaintext=""
    for i in range(0,len(x)):
        #for lowercase
        if x[i].islower():
            c = ord(x[i])-ord('a')
            cde= 25-c+ord('a')
            #print(cde)
            p=chr(cde)

        else:
            p=x[i]
        plaintext=plaintext+ p
    print (plaintext)
        
solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")