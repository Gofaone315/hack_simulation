import time
import random

# Simulated file system
fake_file_system = {
    "/": ["home", "var", "etc", "usr", "hack.txt"],
    "/home": ["user1", "user2", "admin"],
    "/home/user1": ["file1.txt", "file2.txt"],
    "/home/user2": ["document.docx", "image.png"],
    "/home/admin": ["secret.txt", "passwords.csv"],
    "/var": ["log", "tmp"],
    "/var/log": ["syslog", "auth.log"],
    "/var/tmp": [],
    "/etc": ["passwd", "hosts"],
    "/usr": ["bin", "lib"],
    "/usr/bin": ["bash", "python"],
    "/usr/lib": ["libc.so", "libm.so"]
}

def fake_hacking_process(name):
    stages = ["Scanning ports", "Cracking passwords", "Exploiting vulnerabilities", "Bypassing firewalls", "Extracting data"]
    progress = 0
    time.sleep(1.0)
    print(f"Hacking {name} starting")

    for stage in stages:
        print(f"{stage}...")
        for i in range(1, 6):
            time.sleep(random.uniform(0.5, 1.5))
            progress += 3
            print(f"{stage}... {progress}%")
            if random.random() < 0.1:  # Introduce a random error with a 10% chance
                print("Error encountered! Retrying...")
                time.sleep(2)
                print(f"{stage} resumed...")
    
    time.sleep(2.0)
    print(f"Hacking {name} complete")
    file = "/sdcard/" + name + "_information.txt"
    with open(file, 'w') as f:
        f.write(f"Information for {name} lies here\n")
        f.write(simulate_file_extraction("/home/admin/secret.txt\n\n\n"))
        f.write("this is just for fun, hacking is illegal and may land you in serious trouble\n")
        f.write("@Gofaone315 © reserved")

    time.sleep(2.0)
    print(f"{name} information saved in {file}")

def simulate_file_extraction(file_path):
    if file_path in fake_file_system:
        return "\n".join(fake_file_system[file_path])
    else:
        parts = file_path.split('/')
        current_dir = "/"
        for part in parts:
            if part and part in fake_file_system.get(current_dir, []):
                current_dir += part + "/"
            else:
                return "File not found in the file system.\n"
        return "Content of " + file_path + "\n" + "\n".join(fake_file_system.get(current_dir, []))

# Example usage:
name = input("Enter the name of the target to hack: ")
fake_hacking_process(name)
time.sleep(2.0)
print("@Gofaone315 © reserved")
