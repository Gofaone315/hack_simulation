import time
import random
import sys
import subprocess

# Simulated file system
fake_file_system = {
    "/": ["home", "var", "etc", "usr", "hack.txt"],
    "/home": ["user1", "user2", "admin"],
    "/home/user1": ["file1.txt", "file2.txt", "notes.txt", "draft.docx"],
    "/home/user2": ["document.docx", "image.png", "report.pdf", "presentation.pptx"],
    "/home/admin": ["secret.txt", "passwords.csv", "backup.zip", "photos"],
    "/var": ["log", "tmp", "cache", "www"],
    "/var/log": ["syslog", "auth.log", "error.log"],
    "/var/tmp": ["temp1.tmp", "temp2.tmp"],
    "/etc": ["passwd", "hosts", "network.conf"],
    "/usr": ["bin", "lib", "local"],
    "/usr/bin": ["bash", "python", "grep", "sed"],
    "/usr/lib": ["libc.so", "libm.so", "libssl.so"],
    "/usr/local": ["bin", "lib", "share"],
    "/usr/local/bin": ["app1", "app2"],
    "/usr/local/lib": ["plugin1.so", "plugin2.so"]
}

stages = ["Scanning ports", "Cracking passwords", "Exploiting vulnerabilities", "Bypassing firewalls", "Extracting data"]

def update_callback(text):
    word = ""
    for letter in text:
        word += letter
        sys.stdout.write("\r" + "\033[92m" + word + "\033[0m")
        time.sleep(0.025)

def update_error(text):
    sys.stdout.write("\r" + "\033[91m" + text + "\033[0m")

def do_hacking(target):
    progress = 0
    time.sleep(1.0)
    command = "clear"
    subprocess.Popen(command, shell=True)
    update_callback(f"Hacking {target} starting...\n")
    # Simulate stages of hacking
    for stage in stages:
        update_callback(f"{stage}...\n")
        for i in range(1, 7):
            time.sleep(random.uniform(0.05, 0.1))
            progress += 3
            update_callback(f"{stage}... {progress}%\n")
            if random.random() < 0.1:  # Introduce a random error with a 10% chance
                    
                update_error("Error encountered! Retrying...\n")
                time.sleep(2)
                update_callback(f"{stage} resumed...\n")

    # Simulate accessing the file system based on user input
    update_callback(f"Hacking {target} complete\n")
    for file in fake_file_system:
        update_callback(f"Accessing {target}://{file}")
    update_callback(f"Done hacking {target} files saved in /victims/{target}")

def type_anim(text):
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

def initialize_hack():
    command = "clear"
    subprocess.Popen(command, shell=True)
    intro = "TOOL BY GOFAONE315...(https://github.com/Gofaone315)"
    text = ""
    for letter in intro:
        text += letter
        type_anim("\033[34m" + text + "\033[0m")
        time.sleep(0.1)
    time.sleep(1.0)
    subprocess.Popen(command, shell=True)
    time.sleep(1.0)
    target = input("\033[35m" + "enter target name: " + "\033[0m")
    if target == "":
        initialize_hack()
    else:
        do_hacking(target)

initialize_hack()
