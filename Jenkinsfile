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
	        sh "docker-compose -f WorldOfGames"
            }  
        }
        stage('Run') {
            steps {
                sh """cd WorldOfGames
		       docker-compose up -d"""
            }
        }
        stage('Test') {
            steps {
	        sh """cd WorldOfGames
                       python -c "import e2e; e2e.main_function()"""
            }
        }
    }   
}

