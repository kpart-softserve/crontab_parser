#/bin/bash

test_function() {
    if [[ $1 == $2 ]]; then
    echo -e "Pass"
else
    echo -e "Fail - Excepted output: \n${1}\n\nGot:\n${2}"
    exit 1
fi
}

#TEST 1

TEST_OUTPUT="minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find"

OUTPUT=$(python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find")

test_function "$TEST_OUTPUT" "$OUTPUT"

#TEST 2

TEST_OUTPUT="minute 0
hour 0
day of month 1
month 1
day of week 2
command /usr/bin/find"

OUTPUT=$(python cron_parser.py "0 0 1 1 2 /usr/bin/find")

test_function "$TEST_OUTPUT" "$OUTPUT"

#TEST 3

TEST_OUTPUT="Wrong crontab entry"

OUTPUT=$(python cron_parser.py "/15 0 1,15 * 1-5 /usr/bin/find")

test_function "$TEST_OUTPUT" "$OUTPUT"

#TEST 4

TEST_OUTPUT="Wrong crontab entry"

OUTPUT=$(python cron_parser.py "/15 0 1,15 * 1-5")

test_function "$TEST_OUTPUT" "$OUTPUT"

#TEST 5

TEST_OUTPUT="Wrong crontab entry"

OUTPUT=$(python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find /usr/bin/find")

test_function "$TEST_OUTPUT" "$OUTPUT"
