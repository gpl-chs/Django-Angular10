pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        VERSION_FILE = 'version.txt'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout your source code
                    checkout scm

                    // Increment version
                    def currentVersion = readFile(VERSION_FILE).trim()
                    def newVersion = currentVersion.toInteger() + 1
                    writeFile file: VERSION_FILE, text: newVersion.toString()

                    // Build the Docker image
                    dir('Angular10') {
                        sh "docker build -t angular10:v${newVersion} ."
                        sh "docker tag angular10:v${newVersion} gplchsdoc/angular10-app:v${newVersion}"
                        sh 'docker images'
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
                            sh "docker push gplchsdoc/angular10-app:v${newVersion}"
                        }
                    }
                }
            }
        }
    }
}
