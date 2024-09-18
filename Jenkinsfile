pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout'){
           steps {
                git credentialsId: 'Github_LOGIN', 
                url: 'https://github.com/abhi-shek-2/TextUtils-CI-CD/',
                branch: 'main'
           }
        }

        stage('Build and Push Docker Image') {
            environment {
                DOCKER_IMAGE = "ranaabhi02/TextUtils:${BUILD_NUMBER}"
                REGISTRY_CREDENTIALS = credentials('docker-cred')
            }
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                    def dockerImage = docker.image("${DOCKER_IMAGE}")
                    docker.withRegistry('https://index.docker.io/v1/', "docker-cred") {
                        dockerImage.push()
                    }
                }
            }
        }
        

        stage('Update Deployment File') {
            environment {
                GIT_REPO_NAME = "TextUtils-CI-CD"
                GIT_USER_NAME = "abhi-shek-2"
            }
            steps {
                withCredentials([string(credentialsId: 'github', variable: 'GIT_TOKEN')]) {
                    sh '''
                        git config user.email "abhi.786.35@gmail.com"
                        git config user.name "Abhishek Rana"
                        BUILD_NUMBER=${BUILD_NUMBER}
                        cat deploy/deploy.yaml
                        sed -i "s/TextUtils:v1/TextUtils:${BUILD_NUMBER}/g" deploy/deploy.yaml
                        git add deploy/deploy.yaml
                        git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                        git push https://${GIT_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                    '''
                }
            }
        }

        stage("Update Jenkins file with new Build Number") {
           environment {
                GIT_REPO_NAME = "Django-todo"
                GIT_USER_NAME = "abhi-shek-2"
            }
            steps {  
                withCredentials([string(credentialsId: 'github', variable: 'GIT_TOKEN')]) {
                    sh '''
                        git config user.email "abhi.786.35@gmail.com"
                        git config user.name "Abhishek Rana"
                        BUILD_NUMBER=${BUILD_NUMBER}
                        cat Jenkinsfile
                        sed -i "s/TextUtils:v1/TextUtils:${BUILD_NUMBER}/g" Jenkinsfile
                        git add Jenkinsfile
                        git commit -m "Update Jenkinsfile file  to version ${BUILD_NUMBER}"
                        git push https://${GIT_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                    '''
                }
            }
        }
    }
}
