# Introduction

The [Ontology for Media Creation](https://mc.movielabs.com/docs/omc) (OMC) was originally created in RDF and provides formal definitions and a data model for a set of classes and the relationships that bind them together. OMC is designed to simplify communication between different components in a media creation workflow by using a common data model and terminology.  This project implements the classes and relationships from  RDF OMC as a [JSON Schema](https://json-schema.org/).

It is worth reiterating that a primary goal of OMC is to establish a common mechanism for exchanging data among applications and services, reducing the effort and work required to integrate new applications and components into production workflows. In the data plane, applications and services can integrate using OMC once, rather than having multiple pairwise integrations with other components.

Key Points:
- It is not designed as a replacement for an application's internal data models. For any given area this schema will cover only a subset of the information that an application needs internally. Rather, it covers the information that needs to be shared more broadly across the entire production workflow, allowing workflow components to share a common set of references and context.
- It is not designed as a replacement for existing open or proprietary formats for encoding metadata such as USD, EXIF, EDL, etc. OMC instead addresses the common problem of exchanging files and data that use these and other formats by providing additional contextual information for setup and execution of more automated workflows.
- JSON that uses OMC is intended to be consumed and produced via APIs (e.g. REST and GraphQL) and as a payload in data communication systems (message-based or with text files).
- The model and schema rely heavily on the use of identifiers to uniquely identify instances of individual entities and the assets those entities describe. The schema allows entities to be passed either as a reference or as fully realized entities. In the first case the receiving application can dereference the identifiers if it needs more information.
- The model treats relationships as first class citizens. In production, everything is connected to something, and most things are connected to many other things; this results in a graph, not a tree. Therefore, we built the schema so it can represent graphs and recursion, even though JSON itself is strictly hierarchical.

## Repo Structure

**Docs**
A set of documents describing key constructs of the JSON schema and a set of tech-notes that cover how top concepts are represented in JSON.

**Examples**
A set of example JSON instances from the MovieLabs internal POC that demonstrate the initial set of entities included in the schema.

**JSON-Schema**
The individual JSON schemas for each entity, and a bundled version suitable for use in test code or online validators (see below for more details).

**RDF**
The original RDF based version of the ontology.

## Status
OMC JSON is currently a pre-alpha release. Areas under development are:

- It does not implement all of OMC. We are filling in the missing parts based on application requirements and user feedback.
- The mechanism for versions, variants, and representations is being defined, and will be implemented in JSON when the model is complete.
- The formal definitions of more structural and functional characteristics are underway, a working group for CG assets is being setup.

## How to use
The tooling for [JSON Schema](https://json-schema.org/) can be a little inconsistent in its interpretation and application of the spec. Schema editors often use the $id field to resolve the schema (the spec specifically says there should be no expectation the $id be resolvable). When developing schemas on a local file system, this means file based paths must be used, which are not as desirable for deployment.

The files in this repo therefore leave the $id field empty. The tooling then resolves relative references to other schemas from the current path, which works for development. If you are just browsing the schema we would suggest using the individual files, which is a little easier for finding and viewing specific concepts.

When deploying it makes sense to include the $id field. Included in the the ``/JSON-Schema/omc`` directory is a bundled version of the schema ``omcBundle.json`` If you plan on using the schema programmatically, we suggest importing this file.

We have tested schema validation with the bundled schema in:
* JavaScript: [AJV JSON Schema validator](https://ajv.js.org/), [HyperJump](https://github.com/hyperjump-io/json-schema-validator)
* Python: [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
* Web: [HyperJump - JSON Schema Validator](https://json-schema.hyperjump.io/)

The examples use data from the MovieLabs internal POC project. These are generally arrays of entities. The schema is designed to validate a single instance, so be aware that if using these examples single instances should be used when testing, not an array of multiple instances.

## Contact and feedback
Please provide feedback and send any suggestions and questions to ontology@movielabs.com
