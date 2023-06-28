# start with a linux distribution
# ubuntu is the image name in this case
FROM ubuntu

RUN apt update && apt install [package]  --y

# transfer app code into container image
# . . copies everything in the current directory
COPY . . 

# install dependencies eg npm
RUN npm install

# add cmd that will be executed at runtime when container is created
CMD [ "npm", "run", "dev" ]


# to execute build
# navigate to Dockerfile directory
# docker build .