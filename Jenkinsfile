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
                pip3 install --user -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m pytest
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube-server') {
                    sh '''
                    /opt/sonar-scanner/bin/sonar-scanner
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t calculator-api .
                '''
            }
        }

    }
}
