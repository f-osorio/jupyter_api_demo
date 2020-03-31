# TODO:
## Set up a docker container with the following:
* based on some Jupyter image - data science, maybe need to include some additional libraries
* has jupyter kernel gateway
* contains MySQL databse
    * The databse loads data related to Journal metrics
    * pull data for database from a Git repo?
* there is a python notebook that serves as an API
    * API should be able to take in an ISSN (EconBiz)
    * Return some graphs? What would be useful?
    * Create a swagger doc for the API
