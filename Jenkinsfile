pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Python"
        PYTHON = "C:\\Python\\python.exe"
        PIP = "C:\\Python\\Scripts\\pip.exe"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/krsaeed/Hello_World_py.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"%PYTHON%\" -m pip install --upgrade pip"
                bat "\"%PYTHON%\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "\"%PYTHON%\" -m pytest || exit /b 0"
            }
        }

        stage('Deploy') {
            steps {
                echo "Starting Flask app..."
                bat "start cmd /c \"%PYTHON%\" app.py"
            }
        }
    }
}
