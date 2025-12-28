import os

while True:
    try:
        cmd = input("pysh> ")
        if cmd == "exit":
            break
        pid = os.fork()
        if pid == 0:
            os.execvp(cmd.split()[0],cmd.split())
        else:
            os.wait()
    
    except KeyboardInterrupt:
        print()
