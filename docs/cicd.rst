CI/CD Pipeline
==============
Description
-----------
This project is pre-parametred to launch Continuous Integration and Continuous Deployement. 

Tools used for CI/CD :
    - CircleCi https://app.circleci.com : 
        CI/CD orchestrator based on Docker containers
    - Docker https://www.docker.com :
        Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.
    - DockerHub https://hub.docker.com :
        Docker Hub is the world's largest library and community for container images.
    - Heroku https://www.heroku.com :
        Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Steps are as follow :
    - git push to Github
    - CircleCi, linked to your github depositry, launch pipeline workflow
    - Build : Python app gets installed and environment variables passed in it
    - Test and Lint : pytest and flake8 are run. No futher steps will occur if any of them fail.
    - After this point, the initial git push had to occur on main branch in order to launch next steps
    - Build docker : Running web app gets build in a docker image. This image gets pushed to docker Hub
    - Deploy : Docker image gets pushed to Heroku repositry and Heroku web app gets released

Setup
-----
Prerequisites :
    - GitHub account with project linked to your local git deposit 
    - CircleCi account linked with your GitHub account
    - DockerHub account with public repository named ``youraccount/oc-lettings``
    - Heroku account with a web app created

