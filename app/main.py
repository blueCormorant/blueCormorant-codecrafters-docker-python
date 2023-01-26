import subprocess
import sys
import tempfile
import os

def main():

    command = sys.argv[3]
    args = sys.argv[4:]
    
    with tempfile.TemporaryDirectory() as tmp_path:
        os.system(f'mkdir -p {tmp_path}{command}')
        os.system(f'cp {command} {tmp_path}{command}')
        os.chroot(tmp_path)

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
