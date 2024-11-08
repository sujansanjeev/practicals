// pipeline {
//     agent any
//     environment {
//         DOCKER_IMAGE = "flask_sql_app"
//         DOCKERHUB_CREDENTIALS = credentials('docker')
//     }
//     stages {
//         stage('Clone repository') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/sujansanjeev/practicals.git'
//             }
//         }
//         stage('Docker Login') {
//             steps {
//                 script {
//                     sh '''
//                         echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
//                     '''
//                 }
//             }
//         }
//         stage('Build Docker Images') {
//             steps {
//                 script {
//                     sh '''
//                         docker-compose pull
//                         docker-compose build --no-cache
//                     '''
//                 }
//             }
//         }
//         stage('Deploy Containers') {
//             steps {
//                 script {
//                     sh 'docker-compose up -d'
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             script {
//                 sh 'docker-compose down'
//                 sh 'docker logout'
//             }
//         }
//     }
// }


pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "flask_sql_app"
        DOCKERHUB_CREDENTIALS = credentials('docker')
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
                        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    '''
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    sh '''
                        pwd
                        ls -la
                        docker-compose pull
                        docker-compose build --no-cache
                    '''
                }
            }
        }
        stage('Deploy Containers') {
            steps {
                script {
                    sh '''
                        docker-compose up -d
                        docker ps
                        docker images
                    '''
                }
            }
        }
    }
    // Only run docker-compose down if the build fails
    post {
        failure {
            script {
                sh 'docker-compose down'
                sh 'docker logout'
            }
        }
    }
}
