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
        print(f"Execution failed for {file_path}")
    else:
        return cmd.stdout.decode()
    return ""

def generate_motd():
    output = ""
    for file in os.listdir(config.GENMOTD_SCRIPTS):
        output += run_part(os.path.join(config.GENMOTD_SCRIPTS, file))

    try:
        motd_file = open(config.GENMOTD_MOTD, "w")
    except Exception:
        print(f"Failed to open {config.GENMOTD_MOTD}")

    try:
        motd_file.write(output)
    except Exception:
        print(f"Failed to write to {config.GENMOTD_MOTD}")

    motd_file.close()
    print(f"Generated {config.GENMOTD_MOTD}")

