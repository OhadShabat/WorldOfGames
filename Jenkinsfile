pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                bat "git clone https://github.com/OhadShabat/WorldOfGames"
            }
        }
        stage('Build') {
            steps {
	        bat "docker-compose -f WorldOfGames"
            }  
        }
        stage('Run') {
            steps {
                bat """cd WorldOfGames
		       docker-compose up -d"""
            }
        }
        stage('Test') {
            steps {
	        bat """cd WorldOfGames
                       python -c "import e2e; e2e.main_function()"""
            }
        }
    }   
}

