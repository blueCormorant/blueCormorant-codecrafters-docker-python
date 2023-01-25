import subprocess
import sys

def main():

    command = sys.argv[3]
    args = sys.argv[4:]
    if args[0] == "echo":
        cmd = "echo"
        output_stream = sys.stdout
    elif args[0] == "echo_stderr":
        mcd = "echo"
        output_stream = sys.stderr
    else:
        raise Exception("Command not recognized")    

    completed_process = subprocess.run([command, *args], capture_output=True)
    print(completed_process.stdout.decode("utf-8").strip(), file=output_stream)

if __name__ == "__main__":
    main()
