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
                            // Use --password-stdin to avoid insecure password passing
                            sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'

                            // Push the Docker image to DockerHub
                            sh 'docker push gplchs/Angular10'
                        }
                    }
                }
            }
        }
    }
}
