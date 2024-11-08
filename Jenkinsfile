pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask_sql_app"
        DOCKER_CREDENTIALS_ID = 'docker'  // Replace with the credentials ID you created
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sujansanjeev/practicals.git'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use Docker Hub credentials to log in
                    docker.withRegistry('', DOCKER_CREDENTIALS_ID) {
                        echo 'Logged into Docker Hub to prevent rate limit issues'
                    }
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
            }
        }
    }
}
