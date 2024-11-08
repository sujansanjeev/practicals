pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_IMAGE = "flask_sql_app"
        TAG = 'latest'
        // Using Jenkins credentials
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_USERNAME = "${sujansanjeev}"
        DOCKER_PASSWORD = "${Anuradha4$}"
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sujansanjeev/practicals.git'
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login $DOCKER_REGISTRY -u $DOCKER_USERNAME --password-stdin
                    '''
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }
        stage('Deploy Containers') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker-compose down'
                sh 'docker logout'
            }
        }
    }
}