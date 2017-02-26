# jgrep

Searches for, and prints, Java Stack Traces

## Example usage

`./jgrep 'main' samples/threads.log`
`./jgrep -v 'main' samples/threads.log`
`./jgrep -b 'TIMESTAMP' -e 'java.lang.Thread.run' 'thread-3' samples/threads.2.log`
