pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/belailab/calculator-ci-cd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo Installing dependencies...
                pip3 install --user -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo Running tests...
                python3 -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo Building Docker Image...
                docker build -t calculator-api .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo Deploying to Kubernetes...
                kubectl apply -f k8s/
                '''
            }
        }

    }
}
