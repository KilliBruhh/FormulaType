import time

gegevenWoord = "Aap"
start_time = time.time()
inputWoord = input("Typeracer: type het woord "+gegevenWoord+" over \n")

stop_time = time.time()


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def vergelijk(woord1, woord2):

    counter = 1;
    stringLen = len(gegevenWoord)

    for letter1, letter2 in zip(woord1, woord2):
        
        if letter1 == letter2:
            print("Letter OK")
        elif letter1 != letter2:
            print("Letter NOT OK")
        if counter >= stringLen:
            print('End of word')
            
        counter+=1
    
    time_lapsed = stop_time - start_time
    time_convert(time_lapsed)




        

vergelijk(gegevenWoord, inputWoord)


    