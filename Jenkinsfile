pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/inputextern']], extensions: [], userRemoteConfigs: [[credentialsId: 'MaruthairajN', url: 'https://github.com/MaruthairajN/TestProject.git']]])
            }
        }
        stage('build') {
            steps {
                bat 'python test_report_project.py %Testname% %Filename%'
            }
        }
    }    
    post {
        always {
          emailext attachLog: true, body: '$DEFAULT_CONTENT', subject: '$DEFAULT_SUBJECT', to: 'maruthairaj1597@gmail.com'
        }
   }
}
