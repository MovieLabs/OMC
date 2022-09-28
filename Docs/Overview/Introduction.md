# Introduction

The [Ontology for Media Creation](https://mc.movielabs.com/docs/omc) (OMC) was originally created in RDF and provides formal definitions and a data model for a set of classes and the relationships that bind them together. OMC is designed to simplify communication between different components in a media creation workflow by a using common data exchange model and terminology.  This project implements the classes and relationships from  RDF OMC as a JSON schema.

It is worth reiterating that a primary goal of OMC is to establish a common mechanism for exchanging data among applications or microservices, reducing the effort and work required to integrate new applications and components into production workflows. In the data plane, applications and services can integrate using OMC once, rather than having multiple pairwise integrations with other components.

Key Points:
- It is not designed as a replacement for an application's internal data models. It is likely that for any given area this schema will cover only a subset of the information that an application needs internally. Rather, it covers the types of information that need to be shared more broadly across the entire production workflow, allowing a workflow components to share a common set of references and context.
- It is not designed as a replacement for existing open or proprietary formats for encoding metadata such as USD, EXIF, EDL, etc. OMC instead addresses the common problem of exchanging files and data that use these and other formats by providing additional contextual information for setup and execution of more automated workflows.
- JSON that uses OMC is intended to be consumed and produced via APIs (e.g. REST and GraphQL) and as a payload in data communication systems (message-based or with text files.)
- The model and schema rely heavily on the use of identifiers to uniquely identify instances of individual entities and the assets those entities describe. The schema allows entities to be passed either as a reference  or as fully realized entities. In the first case the receiving application can dereference the identifiers if it needs more information.
- The model treats relationships as first class citizens . In production, everything is connected to something, and most things are connected to many other things; this results in a graph, not a tree. Therefore, we built the schema so it can represent graphs and recursion, even though JSON itself is strictly hierarchical.

