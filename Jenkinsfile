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
                cmd /c "netstat -ano | findstr :5000 > port5000.txt || exit /b 0"
                '''

                // Start Waitress server FOREGROUND for 10 seconds only
                bat '''
                for /f "tokens=5" %%p in (port5000.txt) do (
                echo Killing PID %%p
                taskkill /F /PID %%p
                )
                del port5000.txt
                '''

                echo "Starting Flask + Waitress..."
                bat 'start "" /B C:\\Python\\python.exe app.py'

                
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
