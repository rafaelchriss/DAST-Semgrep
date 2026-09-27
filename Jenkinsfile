pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Semgrep') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install semgrep
                '''
            }
        }

        stage('Semgrep SAST') {
            steps {
                sh '''
                    . .venv/bin/activate
                    semgrep scan --config auto . --error
                '''
            }
        }

        stage('Security Gate Passed') {
            steps {
                echo 'Semgrep aprovado. Pipeline pode continuar.'
            }
        }
    }
}
