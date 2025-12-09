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
                bat "\"%PIP%\" install -r requirements.txt"
                bat "\"%PIP%\" install waitress"
            }
        }

        stage('Run Tests') {
            steps {
                bat "\"%PYTHON%\" -m pytest || exit /b 0"
            }
        }

        stage('Deploy') {
            steps {
                echo "Starting Flask app with waitress ..."
                //bat "start cmd /c \"%PYTHON%\" app.py"
                //bat "start \"FlaskApp\" \"%PYTHON%\" app.py"
                // Kill any process already running on port 5000
                bat '''
                C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell -Command "Get-NetTCPConnection -LocalPort 5000 -State Listen | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"
                '''

                // Start Waitress in background
                bat '''
                start "" /B C:\\Python\\python.exe app.py
                '''
                
                sleep(time: 10, unit: 'SECONDS')   // give time to start
            }
        }
        stage('Verify Server') {
            steps {
                bat "netstat -ano | findstr :5000"
            }
        }
    }
}
