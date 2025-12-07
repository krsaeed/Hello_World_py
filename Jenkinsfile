pipeline {
    agent any
    stages{

        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/krsaeed/Hello_World_py.git',
                        credentialsId: 'cred_id_git1'
                    ]]
                ])
            }
        }
        stage ("Install Dependencies"){
            steps {
                withPythonEnv('Python3') {
                    bat '%PYTHON% -m pip install --upgrade pip'
                    bat '"%PYTHON%" -m pip install -r requirements.txt'
                }

            }
        }
        stage('Run Test') {
            steps {
                withPythonEnv('Python3') {
                    bat '"%PYTHON%" -m pytest || true'
                    }
            }
        }
        stage('Deploy') {
            steps{
                withPythonEnv('Python3') {
                    echo 'Starting Flask application..'
                    bat 'start /B "%PYTHON%" app.py'}
            }
        }
    }
}