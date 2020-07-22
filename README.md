# Private Rewrite

Private Rewrite is a Python script that transforms URLs from YouTube and Twitter into their more privacy-friendly equivalents Invidio.us and Nitter.net.
This is somewhat similar to what [Invidition](https://addons.mozilla.org/en-US/firefox/addon/invidition/) does in Firefox.

## Requirements

* Python

## Installation

[Get the latest release](https://github.com/VeryBadFrags/pvtrwt/releases)

```shell
python setup.py install
```

## Documentation

```shell
pvtrwt -h
```

```
optional arguments:
  -h, --help         show this help message and exit
  -c, --clean        Clean the input URL
  -u URL, --url URL  Specify the URL to handle (can be replaced by STDIN)
  -V, --verbose      Verbose outputs
  -v, --version      Print the version and exit
```

## Samples

```shell
$ pvtrwt -u https://twitter.com/Twitter
https://nitter.net/Twitter
```

```shell
$ echo "youtu.be/dQw4w9WgXcQ" | pvtrwt -c
https://invidio.us/watch?v=YbJOTdZBX1g
```

## Source Code

<https://github.com/VeryBadFrags/pvtrwt>
