pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 compile_app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Insurance Application...'
            }
        }
    }
}
