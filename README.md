# pvtrwt

Work in progress.
Private Rewrite is a script that transforms URLs from YouTube and Twitter to their more privacy-friendly equivalents Invidio.us and Nitter.net. This is similar to what [Invidition](https://addons.mozilla.org/en-US/firefox/addon/invidition/) does on Firefox. It has an option to open the URL in your default browser.

## Installing

TODO

## Documentation

```shell
pvtrwt -h
```

## Samples

```shell
$ pvtrwt -u https://twitter.com/Twitter
https://nitter.net/twitter
```

```shell
$ echo "youtu.be/YbJOTdZBX1g" | pvtrwt -c
https://invidio.us/YbJOTdZBX1g
```

```shell
$ pvtrwt -u https://www.youtube.com/watch?v=dQw4w9WgXcQ --open
```
