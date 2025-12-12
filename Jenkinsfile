pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                sudo apt update
                sudo apt install -y rpm dpkg-dev
                '''
            }
        }

        stage('Install DEB package') {
            steps {
                sh '''
                sudo dpkg -i countfiles.deb || true
                '''
            }
        }

        stage('Run script') {
            steps {
                sh '''
                /usr/local/bin/count_files.sh
                '''
            }
        }
    }
}
