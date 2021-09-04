import os
import subprocess

import genmotd.config as config



def insure_directory_structure():
    try:
        os.mkdir(config.GENMOTD_SCRIPTS)
    except FileExistsError:
        print("Configuration directory found")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(e)
    else:
        print("Configuration directory created")

def run_part(file_path):
    try:
        print(f"Executing {file_path}")
        cmd = subprocess.run([file_path], capture_output=True)
    except OSError:
        pass
    else:
        return cmd.stdout.decode()
    return ""

def generate_motd():
    output = ""
    for file in os.listdir(config.GENMOTD_SCRIPTS):
        output += run_part(os.path.join(config.GENMOTD_SCRIPTS, file))

    try:
        motd_file = open(config.GENMOTD_MOTD, "w")
    except:
        pass

    try:
        motd_file.write(output)
    except:
        pass

    motd_file.close()
    print(f"Generated {config.GENMOTD_MOTD}")

