If you are applying as a Tech Writer at [Datadog](https://www.datadoghq.com/) you are in the right spot.

<img src="https://repository-images.githubusercontent.com/2967233/246a3700-b83c-11e9-9960-8b03925fc6f7" width="500" height="500" alt="Logo">

## Instructions

If you have a question, create an issue in this repository or email us.

To submit your answers:

* Fork this repo.
* Answer the questions in answers.md
* Commit as much code and images as you need to support your answers.
* Submit a pull request.
* Don't forget to include links to your dashboard(s), or, even better, links and screenshots. We recommend that you include your screenshots inline with your answers.

Don’t forget to read the [References](https://github.com/jeremy-lq/hiring-engineers/blob/tech-writer/README.md#references)

## Prerequisites - Setup the environment

You can utilize [any OS/host](https://app.datadoghq.com/account/settings#agent) to complete this exercise. However, we recommend one of the following approaches:

* Spin up a fresh Linux VM via Vagrant or other tools so that you don’t run into any OS or dependency issues. [Here are instructions](https://github.com/jeremy-lq/hiring-engineers/blob/tech-writer/README.md#vagrant) for setting up a Vagrant Ubuntu LTS VM.
* You can utilize a Containerized approach with Docker for Linux and our dockerized Datadog Agent image.

Then, [sign up for Datadog](https://app.datadoghq.com/signup) (use “Datadog Recruiting Candidate” in the “Company” field), and get the Agent reporting metrics from your local machine.

## Collecting Metrics:

* Add tags in the Agent config file and show us a screenshot of your host and its tags on the Host Map page in Datadog.
* Install a database on your machine (MongoDB, MySQL, or PostgreSQL) and then install the respective Datadog integration for that database.
* Create a custom Agent check that submits a metric named my_metric with a random value between 0 and 1000.
* Change your check's collection interval so that it only submits the metric once every 45 seconds.
* **Bonus Question** Can you change the collection interval without modifying the Python check file you created?

## Visualizing Data:

Utilize the Datadog API to create a Timeboard that contains:

* Your custom metric scoped over your host.
* Any metric from the Integration on your Database with the anomaly function applied.

Please be sure, when submitting your hiring challenge, to include the script that you've used to create this Timemboard.

Once this is created, access the Dashboard from your Dashboard List in the UI:

* Set the Timeboard's timeframe to the past 5 minutes
* Take a snapshot of this graph and use the @ notation to send it to yourself.
* **Bonus Question**: What is the Anomaly graph displaying?

## Final Question:

The Datadog community has written a substantial number of high-quality integrations and libraries. Select one from [this page](https://docs.datadoghq.com/developers/libraries/). With this selection in mind, write a blog post that announces your selection and explains the benefits it offers our users/community. The post should cover installation, configuration, usage, and best practices along with code samples where applicable. You should also thank the contributor for their effort.

## References

### How to get started with Datadog
* [Datadog getting started](https://docs.datadoghq.com/getting_started/)
* [Guide to graphing in Datadog](http://docs.datadoghq.com/graphing/)
* [Guide to monitoring in Datadog](https://docs.datadoghq.com/monitors/)

### The Datadog Agent and Metrics

* [Guide to the Agent](http://docs.datadoghq.com/agent/)
* [Datadog Docker-image repo](https://hub.docker.com/r/datadog/docker-dd-agent/)
* [Writing an Agent check](https://docs.datadoghq.com/agent/agent_checks/)
* [Datadog API](https://docs.datadoghq.com/api/)

### APM
* [Datadog Tracing Docs](https://docs.datadoghq.com/tracing)
* [Flask Introduction](http://flask.pocoo.org/docs/0.12/quickstart/)

### Vagrant
 * [Setting Up Vagrant](https://www.vagrantup.com/intro/getting-started/)

### Other questions:

* [Datadog Help Center](https://help.datadoghq.com/hc/en-us)
