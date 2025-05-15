import subprocess

def run_command(command, check=True):
    print(f"\n👉 Running: {command}")
    subprocess.run(command, shell=True, check=check)

try:
    # Step 1: Update packages
    run_command("sudo apt update -y")

    # Step 2: Install dependencies
    run_command("sudo apt install unzip curl -y")

    # Step 3: Download AWS CLI v2 installer
    run_command("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")

    # Step 4: Unzip the installer
    run_command("unzip awscliv2.zip")

    # Step 5: Run the installer
    run_command("sudo ./aws/install")

    # Step 6: Verify installation
    run_command("aws --version")

    print("\n✅ AWS CLI v2 installed successfully!")

except subprocess.CalledProcessError as e:
    print(f"\n❌ Error occurred: {e}")
