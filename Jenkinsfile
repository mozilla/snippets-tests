@Library('fxtest@1.1') _

pipeline {
  agent any
  options {
    ansiColor()
    timestamps()
    timeout(time: 5, unit: 'MINUTES')
  }
  environment {
    PYTEST_ADDOPTS = "-n=10 --color=yes"
  }
  stages {
    stage('Lint') {
      steps {
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      steps {
        sh "tox -e tests"
      }
      post {
        always {
          junit 'results/*.xml'
          archiveArtifacts 'results/*'
        }
      }
    }
  }
  post {
    failure {
      mail(
        body: "${BUILD_URL}",
        from: "firefox-test-engineering@mozilla.com",
        replyTo: "firefox-test-engineering@mozilla.com",
        subject: "Build failed in Jenkins: ${JOB_NAME} #${BUILD_NUMBER}",
        to: "fte-ci@mozilla.com")
    }
    changed {
      ircNotification('#snippets')
      ircNotification('#fx-test-alerts')
    }
  }
}
