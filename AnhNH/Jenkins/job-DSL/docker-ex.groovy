job('Docker-dsl-example'){
    scm {
        git('git://github.com/wardviaene/docker-demo.git') {
            node ->
            node / gitConfigName('AnhNH198')
            node / gitConfigEmail('AnhNH198@bizfly.academy')
        }
    }
    triggers {
        scm('H/8 * * * *')
    }
    wrappers {
        nodejs('nodejs-7.10')
    }
    steps {
        dockerBuildAndPublish {
            repositoryName('boploi/job-dsl-docker-jenkins')
            tag('${GIT_REVISION,length=9}')
            registryCredentials('dockerhub')
            forcePull(false)
            forceTag(false)
            createFingerprints(false)
            skipDecorate()
        }
    }
}