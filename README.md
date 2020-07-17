# pvtrwt

Work in progress.

Private Rewrite is a Python script that transforms URLs from YouTube and Twitter into their more privacy-friendly equivalents Invidio.us and Nitter.net.
This is somewhat similar to what [Invidition](https://addons.mozilla.org/en-US/firefox/addon/invidition/) does in Firefox.

You can use `-o` to directly open the URL in your default browser, or you can clean the url output with `-c` and pass it to another program.

## Requirements

* Python 3

## Installing

[Get the latest release](https://github.com/VeryBadFrags/pvtrwt/releases).

```shell
python setup.py install
```

## Documentation

```shell
pvtrwt -h
```

## Samples

```shell
$ pvtrwt -u https://twitter.com/Twitter
https://nitter.net/Twitter
```

```shell
$ echo "youtu.be/YbJOTdZBX1g" | pvtrwt -c
https://invidio.us/watch?v=YbJOTdZBX1g
```

```shell
$ pvtrwt -u "youtube.com/watch?v=dQw4w9WgXcQ" -o
```
