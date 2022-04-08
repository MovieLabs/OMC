# Overview

The purpose of the Media Creation Ontology and this JSON implementation of the model is to facilitate communication between different software components of a media pipeline. It's primary goal being to establish standards for exchanging data among applications or microservices and reduce the effort involved in having to write custom interpretation layers between the different parts of the workflow and the different API standards employed between different developers.



- It is not designed as a replacement for internal data models, this is always likely to be a superset of information that an application will need internally, although to the extent it is useful aspects of this model may be adopted.
- Given the scope of this entire domain we will never be able to define everything. To this end there are  mechanisms for embedding or referencing additional application specific data.
- The model is written in JSON, which in todays environment, has wide support across multiple languages and protocols. It is intended to useable via REST API's, GraphQL, as well as a payload in messaging systems, or sent text files via email, ftp or any other protocol.

