# Initial set up is done
- To run locally `npm start`
- To deploy `npm run deploy`
- It's in `/my world/github-trifiasco/trifiasco.github.io/trifiasco.github.io.local/with-react/trifiasco-github-io`
- the react version control is - `/my world/github-trifiasco/github-io-react-repo`

# how it's done ->
1. first of all it's a react app - created with `create-react-app`.
2. Set up remote origin url for your `github.io` site.
3. Update package.json with - `homepage`
4. install `gh-pages`.
5. Add pre and deployment script in package.json
6. To deploy in master branch add - 
```
"predeploy": "npm run build",
"deploy": "gh-pages -b master -d build",
```

### Need to do - 
- Finish and add project part.
- Add blog
- Add skype
- Add responsibility in craftsmen experience. [partially done]
- Add site link to relevant other sites.
