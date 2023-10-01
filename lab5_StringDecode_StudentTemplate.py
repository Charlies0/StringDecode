def main():
    # Change the value of encodedWord to the word you want to decode
    #encodedWord = "WBLARF8TTS" #WATERFALLS
    #encodedWord = "L8KAOUL" #TAKEOUT
    #encodedWord = "E8N8N8" #BANANA
    #encodedWord = "8TRA8DY T8LA" #ALREADY LATE
    #encodedWord = "8TT LHA TILLTA LIMAS" # ALL THE LITTLE TIMES    
    #encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS" #THE GREEN FIELD GLEAMS IN THE WARM SUNBEAMS
    #encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY" #LONG LAB LACKS TASTY TACO TIME AT LEAST LATELY

    encodedWord = "UUHO"        # Used for Bonus
    # encodedWord = "EOUUUUOUU"    # Used for Bonus

    print(DecodeWord(encodedWord))


# Your code goes here.
def DecodeWord(x):
    final = ''
    for letter in x:
        if letter == 'L':
           final += 'T'
        elif letter == 'T':
            final += 'L'
        elif letter == '8':
            final += 'A'
        elif letter == 'B':
            final += 'A'
        elif letter == 'A':
            final += 'E'
        elif letter == 'E':
            final += 'B'
        else:
            final += letter
    return final

# This code triggers the main to run
# We'll talk about this more in chapters 6, 7, & 8.
if __name__ == "__main__":
    main()