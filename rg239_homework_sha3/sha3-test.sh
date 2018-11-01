#!/bin/bash

OUTPUT_CERT="test-report.txt"
rm -f $OUTPUT_CERT

SELF=$(readlink -f $0)

if [ "$#" -lt 1 ]; then
    echo "Auto-grader for Duke University ECE590 (Computer and Information Security) HW3 SHA3 programming assignment"
    echo "Version 1.1 by Dr. Tyler Bletsch (Tyler.Bletsch@duke.edu)"
    echo ""
	echo "Syntax: $0 <your_program>"
    echo ""
    echo "Saves the signed results to $OUTPUT_CERT."
    exit 1
fi

function do_test() {
    local IN_FILE=$1
    local EXP_OUTPUT=$2
    local ACT_OUTPUT=$($TARGET $IN_FILE | tr -d '[[:space:]]')
    if [ "$EXP_OUTPUT" == "$ACT_OUTPUT" ] ; then
        printf "%-10s: %-4s %s\n" "$IN_FILE" "ok" "($ACT_OUTPUT)" | tee -a $OUTPUT_CERT
        ((NUM_CORRECT++))
        return 0
    else
        printf "%-10s: %-4s %s\n" "$IN_FILE" "FAIL" "(Expected '$EXP_OUTPUT', got '$ACT_OUTPUT')" | tee -a $OUTPUT_CERT
        return 1
    fi
    NUM
}

TARGET=$(readlink -f $1)

NUM_CORRECT=0

cat <<EOL | tee -a $OUTPUT_CERT
sha3-test v1.1 by Dr. Tyler Bletsch (Tyler.Bletsch@duke.edu)
= Certified results report =

Binary under test: $TARGET
Current username: $(whoami)
Current hostname: $(hostname)
Timestamp: $(date)

EOL

echo -n "" > in_empty
do_test  in_empty     'a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26'

echo -n "abc" > in_abc
do_test  in_abc       'b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0'

seq 1 100000 > in_nums
do_test  in_nums      'fc2c7d064771a4a3ba90a2e0c11fa8f7f6f3220b00fac456da680dcfb506914026848a8a0b1ae5eaa3251faffdbaaf5a4e6b6c22e6274d23fcf56ac2ba1abca6'

case "$NUM_CORRECT" in
    0) SCORE=0    ;;
    1) SCORE=3    ;;
    2) SCORE=6    ;;
    3) SCORE=15   ;;
    *) SCORE=-999 ;;
esac

echo "Score: $SCORE" | tee -a $OUTPUT_CERT

echo "Signing..."
echo -e "\nSignatures:" >> $OUTPUT_CERT
./hw3sign < $TARGET >> $OUTPUT_CERT
./hw3sign < $OUTPUT_CERT >> $OUTPUT_CERT
RETVAL=$?
if [ "$RETVAL" -ne 0 ] ; then
    echo -e "\n\nWARNING: Signature tampering has been detected!"
fi
