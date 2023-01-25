import subprocess
import sys

def main():

    command = sys.argv[3]
    args = sys.argv[4:]
    
    completed_process = subprocess.run([command, *args], capture_output=True)

    if completed_process.returncode == 0:
        if args[0] == "echo":
            print(completed_process.stdout.decode("utf-8").strip(), file=sys.stdout)
        elif args[0] == "echo_stderr":
            print(completed_process.stderr.decode("utf-8").strip(), file=sys.stderr)
        elif args[0] == "exit":
            sys.exit(0)
        else:
            raise Exception("Command not recognized")    
    else:
        sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
