# Overview

The [Ontology for Media Creation](https://mc.movielabs.com/docs/omc) (OMC) was created in RDF, and provides formal definitions and a data model for a set classes and relationships that bind them together. The purpose of OMC is to facilitate communication between different software components in a media creation workflow using common data models and terminology. In today's software environment JSON is a more common interchange format than RDF and this project implements the classes and relationships from OMC as a JSON schema.

It is important to restate that primary goal of OMC and this schema is to establish standards for exchanging data among applications or microservices, reducing the effort required to integrate new applications and components into a production workflow. In the data plane, applications and services can integrate with OMC once, rather than having multiple pairwise integrations with other components. 

- It is NOT designed as a replacement for internal data models. It is likely that for any given area this schema will cover a subset of information that an application will need internally. The goal is cover the types of information shared more broadly across the entire production, and make available a canonical set of references and context needed across multiple areas.
- Given the scope of this entire domain we will never be able to define everything. To this end there are  mechanisms for embedding or referencing additional application specific data.
- The model is written in JSON, which in todays environment, has wide support across multiple languages and protocols. It is intended for use via APIs (e.g. REST and GraphQL) and as a payload in data communication systems (whether message-based or with text files.) 

