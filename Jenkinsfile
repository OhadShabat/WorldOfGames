pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh "git clone https://github.com/OhadShabat/WorldOfGames"
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t worldofgames:latest"
            }  
        }
        stage('Run') {
            steps {
                sh "cd WorldOfGames"
                sh "docker run -it worldofgames:latest"
            }
        }
        stage('Test') {
            steps {
                sh "cd WorldOfGames"
                sh "python3 e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                sh "docker stop worldofgames:latest"
            }
        }
    }   
}
