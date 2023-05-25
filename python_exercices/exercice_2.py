message = input("Enter your message here: ")

print("First character: " , message[0])
print("Last character" , message[-1])
print("Middle character", message[int(len(message) / 2)])
print("Even index characters" , message[0::2])
print("Odd index characters", message[0::1])
print("Reversing characters", message[::-1])
