# Overview

The Media Creation Ontology was created in RDF, and provides an overriding data model, with a set of classes and relationships that bind them together. The purpose of the Media Creation Ontology is to facilitate communication between different software components in a media creation workflow. In todays software environment it is more common that  JSON be used when sending data between applications, the following document lays out a JSON based schema that standardizes a means for communication information about a given production like the assets, participants and tasks as well as the relationships that bind them together.

It is important to restate that primary goal of this schema is to establish standards for exchanging data among applications or microservices and reduce the effort involved in having to write custom interpretation layers between the different parts of the workflow and the different API standards employed between different developers.

- It is NOT designed as a replacement for internal data models. It is likely that for any given area this schema will cover a subset of information that an application will need internally. The goal is cover the types of information that are shared more broadly across the entire production, and make available a canonical set of references and context needed across multiple areas.
- Given the scope of this entire domain we will never be able to define everything. To this end there are  mechanisms for embedding or referencing additional application specific data.
- The model is written in JSON, which in todays environment, has wide support across multiple languages and protocols. It is intended to useable via REST API's, GraphQL, as well as a payload in things like messaging systems, or even sent as text files via email, ftp or any other protocol.

