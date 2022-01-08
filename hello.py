msg = "Hello wrld 3423"
msg1=msg.split()
msg2=msg.strip(msg)

def prt_info(msg_str,msg_print):
    print(msg_str,"=",msg_print)
    print(msg_str," len=",msg_print.__len__())

# Clear terminal screen
print(chr(27) + "[2J")

prt_info("msg", msg)
prt_info("msg1[0]", msg1[0])
prt_info("msg1[1]", msg1[1])
prt_info("msg1[1]", msg1[1])

print("msg2=",msg2)