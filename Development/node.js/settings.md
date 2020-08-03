- ### [Node.js API Reference](https://nodejs.org/api/)

- ### [Enable ES6 with Node and Express](https://www.freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab/#tl-dr) 
  - [Basic Node + Express](https://www.codementor.io/olawalealadeusi896/building-simple-api-with-es6-krn8xx3k6)
  - [API reference to enable ES6](https://nodejs.org/api/esm.html)

### JS project set up
- `npm install -D @babel/core @babel/cli @babel/preset-env @babel/node`
- create a `.babelrc` file at the root of your project and add this - 
```
{"presets": ["@babel/preset-env"]}
```
- add start script
- add mocha and chai
- add test script


### React + Express + Node - with server side rendering
1. make an express generator app - npx express-generator app-name
2. add git with .gitignore and make a repository.
3. add basic wildcard route.
4. change the port number.
5. npm install
6. test if it works!
7. Add packages with - 
```
npm i --save-dev npm-run-all @babel/cli @babel/core @babel/preset-env @babel/plugin-transform-runtime nodemon rimraf 
```
8. add .babelrc
9. change the start script in package.json from node to babel-node
10. move necessary files to a folder name server  
11. Update scripts.
12. add react project
13. add a proxy in the react project - `"proxy": "http://localhost:8080/"`
14. Test if two different servers works!!
15. Configure a single serving entry point - 
```
app.use(express.static(path.join(__dirname, '../client/build')));
```

```
app.get('*', (req, res) => {
  res.send(express.static(path.join(__dirname, '../client/build/index.html')))
})
```
Make sure your client project is built using npm run build
16. Now to ease client build , add these two command in the main package.json - 
```
    "init": "npm install && cd client && npm install",
    "devstart": "babel-node ./server/bin/www",
    "start": "npm run build && node ./build/bin/www",
    "start:dev": "npm run build:client && npm run build && node ./build/bin/www",
    "build:client": "cd client && npm run build",
    "build": "npm run clean && npm run babel-build",
    "babel-build": "babel -d ./build ./server -s",
    "clean": "rimraf build",
    "heroku-postbuild": "cd client && npm install && npm run build"
```

17. Don't forget to add - 
```
npm install --save-dev @babel/plugin-transform-runtime
```

```
{
  "presets": ["@babel/preset-react", "@babel/preset-env"],
  "plugins": [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-transform-runtime"
  ]
}
```


### NPM package with es6
1. create a directory. do an `npm init`
2. do a `git init`
3. add `readme.md`
4. create a github repository and add remote
5. add a `src` directory and `index.js` in it.
6. now set up es6 compatibility (#1)- 
  a. `npm i --save-dev npm-run-all @babel/cli @babel/core @babel/preset-env @babel/plugin-transform-runtime nodemon`
  b. `npm install --save @babel/runtime`
  c. add a .babelrc and add this - 
    ```
{
  "presets": ["@babel/preset-env"],
  "plugins": [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-transform-runtime"
  ]
}

    ```
  c. update start script as - `nodemon --exec babel-node src/index.js`
  d. if it says - `bable-node: not found` -> then install `@babel/node instead of @babel/cli`

7. setting up es6 compatibility (#2) - (**DON'T MIX THE TWO WAYS**)
   a. use node v>=12.0
   b. add - `"type": "module"` in package.json

8. Now add a prepublish script - `"prepublish": "babel src -d lib"`
9. add an `.npmignore` and include `/src`
10. add `/lib` to `.gitignore`
11. update entry point - `"main" : "lib/index.js"`


### TDD with mocha-chai
1. Add mocha-chai - `npm i mocha chai --save-dev`
2. Add @babel/register - `npm i --save-dev @babel/register`
3. Add test script - `"test": "mocha --require @babel/register --watch --reporter spec tests/ --exec babel-node"`
