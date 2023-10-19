# Introduction

The [Ontology for Media Creation](https://mc.movielabs.com/docs/omc) (OMC) provides formal definitions for a set of classes and the relationships that bind them together. OMC is designed to simplify communication between different components in media creation workflows by using common terminology and data model created in RDF (OMC-RDF).

This project implements the classes and relationships from OMC-RDF in JSON (OMC-JSON) and provides a [JSON Schema](https://json-schema.org/) for validating compliance.

It is worth reiterating that the primary goal of OMC is to establish a common expression for exchanging data among applications and services, reducing the effort and work required to integrate applications and components into production workflows. Applications and services can integrate using OMC once, rather than having multiple pairwise integrations with other components.

Key Points:

- OMC and OMC-JSON are not designed as a replacement for an application's internal data models. For any given area it will likely only cover a subset of the information that an application needs internally. Rather, it looks to focus on the information that needs to be shared more broadly across an entire production workflow, allowing workflow components to share a common set of references and context.
- Many existing media formats, such as EDL, EXIF, and USD, encode metadata about an asset, OMC is not intended to replace these open or proprietary standards. Rather, it provides two kinds of additional information: 
    - A way of getting important parts of this information without having to open the associated file
    - Contextual information about how production elements fit in with the rest of the workflow
    Taken together, these allow the construction of software defined workflows from task-specific components.  For example, an editorial sequence is fully described by an EDL, but knowing what assets have to be provided requires opening the EDL. In OMC, the editorial sequence is represented by a set of references to its component shots and a reference to the EDL, allowing a software defined workflow to provision the appropriate shots before starting a task such as edit or review. The editorial sequence also has contextual relationships, such as to the larger scene of which it is a part, and each component shot includes its slate, shoot day, etc. 
- OMC-JSON is intended to be consumed and produced via APIs (e.g., REST or GraphQL) and as a payload in data communication systems (message-based or with text files).
- OMC and OMC-JSON rely heavily on the use of identifiers to uniquely identify instances of individual entities and the assets those entities describe. OMC-JSON allows entities to be expressed ~~stated~~ either as a reference (using an identifier) or as fully realized entities. In the first case the receiving application can dereference the identifiers if it needs the additional information.
- OMC treats relationships as first class citizens. In production, everything is connected to something, and most things are connected to many other things; this results in a graph, not always a tree. Therefore, OMC-JSON is designed so that it can represent graphs and recursion, even though the JSON itself is hierarchical in nature.

## Status

OMC-JSON v2.0 is considered a beta release, the intent is that this is considered stable for development, future updates will follow the [versioning guidelines](./SchemaVersioning.md).

Work in progress:
- Add more formal definitions of more structural and functional characteristics. Audio, CG and On-Set Assets all have active working groups, if you have interest in joining these, please contact us.
- Add structural and functional properties, particularly for commonly used properties and reusable components.
- Implement the Concept and Technical Reference Reifications in OMC-JSON

## Useful Tools

We found some of the following tools useful during development:
- JavaScript: [AJV JSON Schema validator](https://ajv.js.org/), [HyperJump](https://github.com/hyperjump-io/json-schema-validator)
- Python: [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
- Web: [HyperJump - JSON Schema Validator](https://json-schema.hyperjump.io/)


## Contact and feedback

Please provide feedback and send any suggestions and questions to ontology@movielabs.com

<!--
Copyright 2021-2023 Motion Picture Laboratories, Inc.
SPDX-License-Identifier: APACHE-2.0
-->
