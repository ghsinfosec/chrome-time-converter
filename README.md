# About

Google Chrome's timestamp is the number of microseconds since January 1, 1601. A user's browser history will store the time in this format, and it needs to be converted if you want to read it. Might be useful for some dirt digging when combined with sqlitebrowser...

[Here's a Stackoverflow article](https://stackoverflow.com/questions/20458406/what-is-the-format-of-chromes-timestamps) that describes it a little more.

# Usage

You can pass in a single timestamp or a file with a list of timestamps on each line:

## Single timestamp

Pass in a single timestamp with `-t`:

```bash
python3 convert-time.py -t 13327424658066391
2023-05-01 10:24:18
```

## List of timestamps

Got a list from sqlitebrowser? Pass it in:

Timestamp list looks like:

```bash
head -n 8 timestamp-list.txt
13327424658066391
13325110864681963
13326901838088400
13326901934796783
13327616445445551
13327616445445551
13321139379881978
13324143539380318
```

Run the command with `-f` to pass it in:

```bash
python3 convert-time.py -f timestamp-list.txt
2023-05-01 10:24:18
2023-04-04 15:41:04
2023-04-25 09:10:38
2023-04-25 09:12:14
2023-05-03 15:40:45
2023-05-03 15:40:45
2023-02-17 15:29:39
2023-03-24 10:58:59
```
