pipeline {
    agent {dockerfile true}
    stages {
        stage('build') {
            steps {
                sh 'python test.py'
            }
        }
    }
}