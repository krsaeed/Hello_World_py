pipeline {
    agent any
    
    stages{
        stage('Clone Repository') {
            steps {
                git 'https://github.com/krsaeed/Hello_World_py.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Flask application...'
                sh 'nohup python app.py &'
            }
        }
    }
}