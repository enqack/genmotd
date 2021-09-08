import os
import subprocess
import sys

import genmotd.config as config


def insure_directory_structure():
    try:
        os.mkdir(config.SCRIPTS_DIR)
    except FileExistsError:
        raise
    except PermissionError:
        raise

def run_part(file_path, quiet=False):
    try:
        if not quiet:
            print(f"Executing {file_path}")
        cmd = subprocess.run([file_path], capture_output=True)
    except OSError:
        print(f"Execution failed for {file_path}", file=sys.stderr)
    else:
        return cmd.stdout.decode()
    return ""

def generate_motd(quiet=False):
    file_list = os.listdir(config.SCRIPTS_DIR)

    output = ""
    for file in sorted(file_list):
        output += run_part(os.path.join(config.SCRIPTS_DIR, file), quiet)
    if not quiet:
        print(f"Generated {config.MOTD_FILE}")
    return output

def write_motd(output):
    try:
        motd_file = open(config.MOTD_FILE, "w")
    except Exception:
        print(f"Failed to open {config.MOTD_FILE}", file=sys.stderr)

    try:
        motd_file.write(output)
    except Exception:
        print(f"Failed to write to {config.MOTD_FILE}", file=sys.stderr)

    try:
        motd_file.close()
    except Exception:
        raise

