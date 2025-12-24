pipeline {
    agent any

    environment {
        IMAGE = "hello-world-py"
        CONTAINER = "hello_world_app"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER || true
                docker rm $CONTAINER || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name $CONTAINER $IMAGE:latest'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps | grep $CONTAINER'
            }
        }
    }
}
