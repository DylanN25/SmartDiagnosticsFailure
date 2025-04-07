import subprocess

def start_flask():
    print("Starting Flask backend...")
    subprocess.Popen(["python", "app.py"], cwd="./my-project-backend")

def start_react():
    print("Starting React frontend...")
    subprocess.Popen(["npm", "start"], cwd="./my-project-reactapp", shell=True)

if __name__ == "__main__":
    start_flask()
    start_react()
    print("Both Flask and React are starting! Check their respective terminals.")

