# LineageOS OTA website

This is the download page for our unofficial LineageOS builds. It is based on [Universal-DB](https://github.com/Universal-Team/db)'s website files.

### Building the site locally

1. Install [Ruby 3.x](https://www.ruby-lang.org/) for your machine
1. Run `bundle config set --local path vendor/bundle` to ensure that dependency versions do not clash with other ruby projects
1. Run `bundle install` to install dependencies
1. Run `bundle exec jekyll serve`
    - This will build the site to `_site`, and host a simple web server at `127.0.0.1:4000`

### License

- The site theme (`_includes`, `_layouts`, `_sass`, `assets/css`, `assets/js`) is licensed under the following:
    - `SPDX-License-IdentifierL: GPL-3.0-only`
    - You may read more in `LICENSE-code.txt`.
- The site text is licensed under the following:
    - `SPDX-License-Identifier: CC-BY-NC-SA-4.0`
    - You may read more in `LICENSE-docs.txt`.
