# Setup
## NVM setup
```
https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating
nvm install 18
nvm use 18
```

## npm create 
```
npm create vite@latest my-app -- --template react-ts

cd my-app
npm install
npm run dev
```

# Docker
```
eval $(minikube docker-env) # build into minikube docker daemon
docker build -t my-react-app:1.0.1 .
docker run -p 3000:80 my-react-app
```

# Contrast Design
* [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
