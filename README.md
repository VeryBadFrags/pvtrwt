# Private Rewrite

Private Rewrite is a Python script that transforms URLs from YouTube and Twitter into their more privacy-friendly equivalents Invidio.us and Nitter.net.
This is somewhat similar to what [Invidition](https://addons.mozilla.org/en-US/firefox/addon/invidition/) does in Firefox.

You can use `-o` to directly open the URL in your default browser, or you can clean the url output with `-c` and pass it to another program.

## Requirements

* Python

## Installing

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
  -o, --open         Open the url in the default browser
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
$ echo "youtu.be/YbJOTdZBX1g" | pvtrwt -c
https://invidio.us/watch?v=YbJOTdZBX1g
```

```shell
$ pvtrwt -u "youtube.com/watch?v=dQw4w9WgXcQ" -o
```
