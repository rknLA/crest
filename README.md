crest
======
### A hypermedia-influenced curl CLI ###

Doing for REST APIs what curl did for URLs.

So far, just the spec is written, but I'm eager to have this tool,
therefore I'm eager to get it all done and built.


Description
-----------

`crest` is a CLI tool designed for hand-testing RESTful/Hypermedia APIs.  
Its main benefit over tools like [curl](http://curl.haxx.se/) and
[HTTPie](https://github.com/jkbr/httpie) is that `crest` is designed with
more than one request in mind.


Installation
------------
Git clone, gem install, or copypasta or whatever.

Put `crest` somewhere in your path.

Make sure `which crest` gives you something sane.

There it is.  You're done.


Usage
-----

`crest [options] base_url`

### Overview ###
Call it with a base url:
```bash
crest api.github.com
```

This starts a crest shell, from which you can execute a series of curl commands
with ease:

```bash
GET /      # this outputs the same thing as `curl -v -X GET http://api.github.com/`
GET / -s   # `curl -v -X GET https://api.github.com/`
set -s     # use https
set -H 'Accept: application/json'
GET /users/octocat/orgs  # `curl -v -X GET https://api.github.com/users/octocat/orgs -H 'Accept: application/json'`
unset -s   # stop using https
GET /users/octocat/orgs  # `curl -v -X GET http://api.github.com/users/octocat/orgs -H 'Accept: application/json'`
```

### Options ###

Options can be set at invocation, or using the `set` and `unset` directives
on the CLI.

Once options are set, they will be included in all subsequent requests until
they are unset, or until the shell is terminated.

**Valid options are:**
```
-a/--accept <mime>         # set an HTTP Accept header for <mime>
-s/--secure                # use https
-t/--content-type <type>   # specifies the Content-Type of the request body by setting the HTTP Content-Type header
-H <header>                 # use this HTTP header for all subsequent requests.  Same as curl -H
-d <data>                   # send request with <data>.  Same as curl -d
-v                          # verbose. Same as curl -v.  Defaults to being set.
-i                          # include header data.  Same as curl -i.  Defaults to being unset.
```

One day soon, Oauth and Oauth2 may also be supported using `--ouath` and/or
`--oauth2`.

### Basic Commands ###
crest is sort of like a curl shell, and as such, it has a set of options
you can use once you've initialized the shell with a root url.

`set` is used to set an option from the options list above, as in `set -s` or
`set -a application/json`

`unset` is used to unset an option from the option list.  Note that if you have
multiple headers set, `unset -H` will unset all of them.

Use `unset -H Header-Name` to unset only a specific header.

Use HTTP verbs to issue curl requests:

`GET /users` 

`POST /comment -d 'What a silly username!'`

Remember, crest is a thin layer over curl, so if the verb is supported by
the -X option in curl, it's probably supported in crest.


### History ###

`history` will display a list of the endpoints you've recently curled.

Each HTTP request is numbered sequentially, and the output is cached until the
shell is terminated. Use the number directly to see the previous output.  i.e.
`1` will output the results of your first request in this session.  Note that
this will NOT resend the request.

The `!` operator allows you to resend requests you've already sent, and is used
with the request numbers. i.e. `!1` will resend the first request of your
session.  The resent request will be appended to the history list.

### Retention ###

crest doesn't have any inherent retention, but it does have an output mechanism.

Use `dump <filename>` from the shell to write a log of your session to that file.
If you don't want to dump the whole session, `dump` supports an option `-r` to
specify a single request to output to a file, as in `dump -r 3 ~/output.json`

History is not retained between sessions.


Testing
-------

The script at `./test` will run all of the files in the `./tests` directory that
have a filename of `*_test.py`.


