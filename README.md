# FontReducer

reduce font size

## Install

```sh
$ pip install FontReducer
```

## Usage

```sh
$ cat WORDS_TO_REDUCE.txt | fontreducer PATH_TO_FILE PATH_TO_OUTPUT
```

For example, You can use in gulp task.

```coffee
shell   = require 'gulp-shell'

gulp.task 'font:gen_subsets', shell.task [
  'some_nice_grepping_script > words.txt'
  'cat words.txt | fontreducer src/font/some_nice_font.otf dist/some_nice_font.otf'
  'rm words.txt'
]
```

## Inspired

https://github.com/3846masa/japont

japont is Dynamic Subsetting System for Japanese fonts.
Very Easy to try on Heroku.
