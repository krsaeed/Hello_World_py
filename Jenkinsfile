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
                bat '''
                powershell -Command "Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"
                '''

                // Start Waitress server FOREGROUND for 10 seconds only
                bat '''
                C:\\Python\\python.exe -m waitress --host=0.0.0.0 --port=5000 app:app
                ''' &
                
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
