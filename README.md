# Locust Runner

[![Travis](https://img.shields.io/travis/hanpeter/locust-runner.svg?logo=travis)](https://travis-ci.org/hanpeter/locust-runner)
[![GitHub tag](https://img.shields.io/github/tag/hanpeter/locust-runner.svg?logo=github)](https://github.com/hanpeter/locust-runner/tags)
[![GitHub last commit](https://img.shields.io/github/last-commit/hanpeter/locust-runner.svg?logo=github)](https://github.com/hanpeter/locust-runner/commits)
[![license](https://img.shields.io/github/license/hanpeter/locust-runner.svg)](LICENSE)

`locust-runner` is a helper for [`locust`](https://locust.io/) to allow users to build Locust tests using a YAML file.

## What does it do?
`locust` is a great library to build load testing with plenty of features, but sometimes you just want to run a simple load test without writing a bunch of code. The `locust-runner` allows you to run a simple load test with a YAML file and without any code writing.

## How do I use it?
Check out the code and update the `config.yaml`. There is a sample config file already ready for you. You should be able to update that file to get you going. Once you have modified the `config.yaml` to match your need, run `locust` with `locust_runner/runner.py` as your locust file and with options that you like.

```bash
$ locust -f locust_runner/runner.py --no-web -c 1 -r 1 -t 10s --only-summary
```

## How do I contribute?
We welcome your contribution! Check out [`CONTRIBUTING.md`](.github/CONTRIBUTING.md).
