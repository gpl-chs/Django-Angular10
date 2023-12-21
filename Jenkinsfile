pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout your source code
                    checkout scm

                    // Build the Docker image
                    dir('Angular10') {
                        sh 'docker build -t angular10-app .'
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Log in to DockerHub using credentials
                    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD']]) {
                        dir('Angular10') {
                            sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"

                            // Push the Docker image to DockerHub
                            sh 'docker push gplcs/Angular10'
                        }
                    }
                }
            }
        }
    }
}
