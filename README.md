# Githubdate

## Use case

You've got dozens of pull-requests on hold. Some of them are ready to be merged.
But as a release manager, you need to warn everyone with "merge" rights **not
to** merge any of these pull-requests. Because you're on a hot lava field, you
have to stabilize things, etc.

Anyway. Just push a "it's not cool to merge this" status. And then, when the
situation is cooler, just send an update with a green light.

## Install

* clone this repository,
* pip install it (preferrably in a virtualenv)

Or

    pip install githubdate


## Configure

Pick the [githubdate.ini.example](githubdate.ini.example) file and save it as
``githubdate.ini``. Edit it to configure the different variables:
``personal_access_token``, ``owner`` (github user account), target
``repository``, ``target_url`` (optional), and the ``description`` (the message
to be sent to the user).

## Run

    githubdate pause  # to pause your PRs
    githubdate unpause  # to free your PRs from this pending status
