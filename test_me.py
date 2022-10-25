from my_classes import Mesg



try:
    print (Mesg.get("NoneDefinition", ["aaa", "bbb"]))
except Exception as e:
    print (e)


try:
    Mesg.read_definition("./notfound.json")
except Exception as e:
    print (e)


Mesg.read_definition("./definitions.json")
print (Mesg.get("NotFound", ["aaa", "bbb"]))
print (Mesg.get("MSGISH00001", ["aaa", "bbb"]))
print (Mesg.get("MSGISH00002", ["aaa", "bbb"]))
print (Mesg.get("MSGESH00001", ["aaa", "bbb"]))
