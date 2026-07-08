pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pipeline Started...'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Verify Git') {
            steps {
                sh 'git --version'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Verify kubectl') {
            steps {
                sh 'kubectl version --client'
            }
        }

        stage('Verify Helm') {
            steps {
                sh 'helm version'
            }
        }

    }

    post {

        always {
            echo 'Pipeline Finished'
        }

        success {
            echo 'Everything is working!'
        }

        failure {
            echo 'Something failed.'
        }

    }
}
