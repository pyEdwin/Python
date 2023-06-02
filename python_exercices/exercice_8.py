def encrypted_message(message , shift):
    answer = ""
    for i in range(len(message)):
        ch = message[i]

        if ch == "":
            answer+=""

        elif (ch.upper()):
            answer+= chr((ord(ch)+ shift -65) % 26 + 65)
        
        else:
              answer+= chr((ord(ch)+ shift -97) % 26 + 97)