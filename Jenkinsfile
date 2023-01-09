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
        stage('description') {
            steps {
                script {
                    currentBuild.displayName = """ \' No : ${env.BUILD_NUMBER} JOB : ${env.JOB_NAME} \' """
                    currentBuild.description = """ <p> <b> \'PROJECT\'</b> : ${env.JOB_NAME}  <b> \'BUILD NO\'</b> : ${env.BUILD_NUMBER}  <b> \'JOB STATUS\'</b> : SUCCESS  <i>Build Log is sent to required mail </i>"""
                }
            }
        }
    }    
    post {
        always {
          emailext attachLog: true, body: '$DEFAULT_CONTENT', subject: '$DEFAULT_SUBJECT', to: 'maruthairaj1597@gmail.com'
        }
   }
}
