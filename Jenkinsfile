pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "flask_sql_app"
        DOCKER_CRED = credentials('docker-hub-credentials')
    }
    
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Docker Login') {
            steps {
                // Wrap Docker login in a node block
                node {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'Anuradha4$', usernameVariable: 'sujansanjeev')]) {
                        sh '''
                            echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
                        '''
                    }
                }
            }
        }
        
        stage('Build Docker Images') {
            steps {
                // Ensure we're in a node block
                node {
                    sh 'docker-compose build'
                }
            }
        }
        
        stage('Deploy Containers') {
            steps {
                node {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
    
    post {
        always {
            node {
                sh '''
                    docker-compose down || true
                    docker logout || true
                '''
            }
        }
    }
}
