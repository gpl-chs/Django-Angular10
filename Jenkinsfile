pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout your source codE
                    checkout scm

                    // Build the Docker image
                    dir('Django/DjangoAPI') {
                        sh 'docker build -t django .'
                        sh 'docker tag django gplchsdoc/django-app:latest'
                    }                    
                    dir('Angular10') {
                        sh 'docker build -t angular10 .'
                        sh 'docker tag angular10 gplchsdoc/angular10-app:latest'
                    }
               
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Log in to DockerHub using credentials
                    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD']]) {
                        dir('Django/DjangoAPI') {                            
                            // Use --password-stdin to avoid insecure password passing
                            sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'
                            // Push the Docker image to DockerHub
                            sh 'docker push gplchsdoc/django-app:latest'
                        }                        
                        dir('Angular10') { 
                             // Use --password-stdin to avoid insecure password passing
                            sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'
                            // Push the Docker image to DockerHub
                            sh 'docker push gplchsdoc/angular10-app:latest'
                        }                        
                    }
                }
            }
        }
    }
}
