1. Create a repository with the name - `<username>.github.io`.
2. make a git clone to local machine.
3. create an empty branch `gh-pages`.
```
git checkout --orphan gh-pages
```
4. Install ruby, bundler and jekyll
```
sudo apt-get install ruby ruby-dev
```
5. Make a `Gemfile` in the directory. and put this - 
```
source 'https://rubygems.org'
gem 'github-pages'
```
6. Now run:
```
sudo gem install bundler
bundler install
```
**If you get error for nokogiri then follow [this](https://stackoverflow.com/questions/6277456/nokogiri-installation-fails-libxml2-is-missing)**
7. Create your jekyll blog - 
```
bundle exec jekyll new . --force
```
8. Serve it locally - 
```
bundle exec jekyll serve
```
you can see it if you go to `localhost:4000`

****
1. clone `jasper2` - 
```
git clone https://github.com/jekyller/jasper2.git
```
2. go to `jasper2` folder.
```
cd jasper2
git remote remove origin
git remote add origin <ssh-url>
```
3. Change config file where the static files will be generated. this will point to the directory where local guibhub.io repository will be located. Because on github.io only allows the static files.