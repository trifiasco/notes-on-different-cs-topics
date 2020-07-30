### React.js

- [Create react app](https://github.com/facebook/create-react-app) is a tool to create a react app.
```
npx create-react-app <app-name>
cd my-app
npm start
```

- If you see already running in port 3000 error - 
```
sudo lsof -i:<PORT_NO>
sudo kill <PID>
sudo killall -9 node // just in case
```