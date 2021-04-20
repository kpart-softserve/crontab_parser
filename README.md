# Simple cron parser

## Requirments
* Python 3

All needed packages is provided by pipenv

## How it works

Script take argument from command line (crontab line) and parse it into human readable format

### Example

#### Input
```bash
*/15 0 1,15 * 1-5 /usr/bin/find
```

#### Output
```bash
minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find
```

#### Script call
```bash
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

## Running tests
To run integration tests simply call

```bash
./tests/integration_test.sh
```

Tests returns 0 when all passed, return 1 when one failed - so its ready to integrate with CI/CD system.

## Build whell (pip) package
To build package run:
```bash
python setup.py bdist_wheel
```
Artifact can be found on `dist` directory.

Then install at host by:
```bash
pip install ${artifactName}
```
