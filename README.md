# Hello_World_py 
Simple python CI/CD pipeline

---

# 🚀 Python CI/CD Pipeline using Jenkins, Docker & AWS EC2

This project demonstrates a **complete end-to-end CI/CD pipeline** starting from a local Windows machine (without Docker), moving through Jenkins, Docker, and finally deploying a Python application on **AWS EC2** that is accessible via a browser.

---

## 📌 Project Overview

**Flow:**

```

Developer → GitHub → Jenkins → Docker → AWS EC2 → Browser

```

- Code pushed to GitHub
- Jenkins pulls code using GitHub PAT
- Jenkins builds Docker image
- Old container is stopped
- New container is deployed
- Application is exposed to the internet

---

## 🧱 Architecture Diagram

```

┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  GitHub  │ ──▶ │ Jenkins  │ ──▶ │  Docker  │ ──▶ │   EC2    │
└──────────┘     └──────────┘     └──────────┘     └────┬─────┘
│
http://EC2_IP:5000
│
┌───▼───┐
│Browser│
└───────┘

````

---

## 🧰 Tech Stack

- **Language:** Python (Flask)
- **CI/CD:** Jenkins (Pipeline)
- **Containerization:** Docker
- **Cloud:** AWS EC2 (Ubuntu)
- **Source Control:** GitHub

---

## 🛠️ Prerequisites

Before starting this project, ensure you have the following tools and accounts ready.

### 💻 Local Machine

- **Windows 10 / 11**
- **WSL2 (Ubuntu)** – recommended for Linux compatibility
- **Git**
- **Python 3.8+**
- **Docker Desktop** (for local testing, optional)

### ☁️ Cloud & Accounts

- **GitHub Account**
- **GitHub Personal Access Token (PAT)**
- **AWS Account** (or Pluralsight AWS Sandbox)

### 🖥️ AWS EC2 Environment

- Ubuntu 22.04 EC2 instance
- Open ports in Security Group:
  - `22` – SSH
  - `8080` – Jenkins
  - `5000` – Application access

### ⚙️ Software Installed on EC2

Installed during setup:

- **OpenJDK 17** (Jenkins requirement)
- **Jenkins**
- **Docker**
- **Git**

---
## 🖥️ Local Development (Windows – No Docker)

```bash
git clone https://github.com/<your-username>/Hello_World_py.git
cd Hello_World_py
python app.py
````

Access locally:

```
http://localhost:5000
```

---

## ☁️ AWS EC2 Setup

### 1️⃣ Launch EC2

* AMI: Ubuntu 22.04
* Instance type: t2.micro (sandbox)
* Security Group:

  * TCP 22 → My IP
  * TCP 8080 → Anywhere
  * TCP 5000 → Anywhere

---

### 2️⃣ Connect to EC2

#### Linux / WSL

```bash
chmod 400 jenkins-key.pem   # Optional (see below)
ssh -i jenkins-key.pem ubuntu@<EC2_PUBLIC_IP>
```

#### Windows (PowerShell / Git Bash)

```powershell
ssh -i jenkins-key.pem ubuntu@<EC2_PUBLIC_IP>
```

> ℹ️ `chmod 400` is **optional on Windows**
> Use it only if SSH complains about permissions

---

## ⚙️ Install Jenkins & Docker on EC2

```bash
sudo apt update -y
sudo apt install -y openjdk-17-jdk docker.io git
```

### Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
/usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
```

### Permissions

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

## 🌐 Access Jenkins

```
http://<EC2_PUBLIC_IP>:8080
```

Get initial password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## 🔐 GitHub Credentials (PAT)

1. GitHub → Settings → Developer Settings → Tokens
2. Create **Personal Access Token**
3. Jenkins:

   ```
   Manage Jenkins → Credentials → Global → Add Credentials
   ```

* Kind: Username with password
* Username: GitHub username
* Password: GitHub PAT
* ID: `github-pat`

---

## 🧪 Jenkins Pipeline Creation

1. **New Item**
2. Name: `Python-cicd-static-web`
3. Type: **Pipeline**
4. Pipeline Definition: **Pipeline script from SCM**
5. SCM: Git
6. Repo URL:

   ```
   https://github.com/<your-username>/Hello_World_py.git
   ```
7. Credentials: `github-pat`
8. Branch:

   ```
   */main
   ```

---

## 📄 Jenkinsfile

```groovy
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t hello-world-py:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop hello_world_app || true
                docker rm hello_world_app || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 \
                --name hello_world_app hello-world-py:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps | grep hello_world_app'
            }
        }
    }
}
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 🌍 Application Access

After successful Jenkins build:

```
http://<EC2_PUBLIC_IP>:5000
```

✔️ App is live
✔️ Docker container running
✔️ Jenkins managing deployments

---

## 🧠 Key Learnings

* Windows → WSL → Linux differences
* GitHub PAT required (passwords deprecated)
* Jenkins service conflicts on Windows vs WSL
* Docker port binding issues (`port already allocated`)
* EC2 Security Groups control public access
* AWS Sandbox EC2 is **temporary**

---

## 🚀 Future Improvements

* Docker Compose
* Nginx reverse proxy
* GitHub Webhooks
* HTTPS (ALB + ACM)
* Push images to DockerHub / ECR

---

## 👤 Author

**Khalilur Rahman Saeed**
Learning DevOps step-by-step through real projects 🚀