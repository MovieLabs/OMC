# JSON Schema Overview

The formal media creation ontology is written in RDF and provides the overriding model, with a set of classes and relationships that bind them together. However, JSON does not have all the same characteristics as RDF, so a modifications are made to allow for this, while keeping the vocabulary and key concepts intact.

## Composition vs Inheritence

RDF is a class based system, however JSON does not inherently have a class based structure or the idea of class inheritance. We therefore choose to use a compositional model, where a set of individual schemas are used to create entities that align with the RDF classes. These schemas can then be composed (via referencing) to create new entities. They can be nested, or included in sets, each entity contains a description of it's entity type which can then be used to validate or parse the set of enclosed properties.

The goal behind the JSON model is to provide a flexible mechanism to communicate. To achieve this the JSON data model defines a collection of Entities that are in turn composed from a sets of Properties. These Properties are either other Entities or Attributes.

**Entity**: A set of properties that together describe a single concept within the model.

**Property**: A <key> <value> pair where the value can be an entity, complex type (object or array of objects)   or an attribute.

**Attribute**: A primitive value (or array of primitive values), i.e. a string, number, Boolean or null.



## Conventions

By convention the first letter of any defined entity is capitalized. Properties that describe that describe the attributes of an entity are camel cased (first letter is lower case). Entities can therefore be easily identified by their being capitalized, and each entity will have it's own JSON schema defining it.

**Example 1:**

This shows an example of an identifier, used extensively in the model. Firstly the schema definition itself, and secondly an example instance.

##### JSON Schema

``` JSON
{
    "identifier": {
        "type": "array",
        "title": "identifier",
        "additionalItems": true,
        "items": {
            "type": "object",
            "required": ["identifierScope", "identifierValue"],
            "properties": {
                "identifierScope": {
                    "type": "string",
                    "title": "Identifier Scope",
                    "description": "The universe within which an identifier is valid and unique."
                },
                "identifierValue": {
                    "type": "string",
                    "title": "Identifier Value",
                    "description": "A string of characters that uniquely identifies an object within a particular scope."
                }
            },
            "additionalProperties": false
        }
    }
}
```

##### JSON Instance

```json
    {
        "identifier": [{
          "identifierValue": "1234",
          "identifierScope": "Movielabs"
        }]
    }
```



##### Example 2:

Below we show small section of the schema for Narrative Location, this illustrates how the identifier subSchema is included by reference. The Location is itself an entity and therefore capitalized and includes the identifier by which it is referenced, lastly is an attribute, the description.

##### JSON Schema

```
{
    "entityType": {
        "type": "string",
        "title": "Entity Type",
        "const": "NarrativeLocation"
    },
    "identifier": {
        "title": "identifier",
        "$ref": "../Utility/identifier.json#/properties/identifier"
    },
    "Location": {
        "$ref": "../Utility/Location.json"
    },
    "name": {
        "type": "string",
        "title": "Name"
    },
    "description": {
        "type": "string",
        "title": "Description"
    }
}
```

##### JSON Instance

```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "identifier": [{
            "identifierValue": "5678",
            "identifierScope": "Movielabs"
        }],
    },
    "description": "Sherlock Holms residence"
}
```



## Identifiers and referencing

The use of identifiers is a central tenet of all entities, any entity must be uniquely identifiable with an Identifier. Using identifiers allows any entity to be included by reference or by inclusion, a decision that is left to the application. Where only an identifier is included in a payload the presumption is the receiving party would make a secondary request to retrieve additional information.

##### Example 1:

This shows a Narrative Location, where the Location itself is only referenced by it's identifier. If a party received this they would need to make a secondary request using the Locations identifier to get the full set of attributes.

```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "identifier": [{
            "identifierValue": "5678",
            "identifierScope": "Movielabs"
        }],
    },
    "description": "Sherlock Holms residence"
}
```

##### Example 2:

The model however allows for any entity to also be fully resolved and sent as part of a payload.

```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "entityType": "Location",
        "identifier": [{
            "identifierValue": "5678",
            "identifierScope": "Movielabs"
        }],
        "name": "Sherlock Holmes residence",
        "address": {
            "street": "221b Baker St.",
            "region": "London",
            "postalCode": "NW1 6XE"
            "country": "uk"
        }
    },
    "description": "Sherlock Holms residence"
}
```



The schemas are structured in such a way that in theory there is no end to the depth to the levels of nesting, so care should be taken as circular references are easy to create.

The decision to dereference an entity and include it in a payload, or to just send the identifier is the applications to make. If a reference is included then it is likely that any party receiving the payload may want to make a secondary request for the missing information. This will require that they have a means to do so, both the requisite security credentials and knowledge of where and how to make the secondary request. This may not be so obvious if data is sent as a payload via a messaging system, as the receiving party may not even know who sent the data. 





## Standard Properties

There are some properties that are used consistently throughout the schema

##### schemaVersion

Each schema has a version

##### instance

This contains detailed information about the instance itself:

**instance.version**

Specifies the version of the instance of this entity *(we may need to do more detail here)*.

**instance.createdBy**

The Participant responsible for instantiating this instance.

**instance.createdOn**

A date/time stamp of creation.

##### entityType

A required property that enumerates the type of the entity within the structure of the entity itself. It is used to identify the expected fields when programmatically parsing the data, or to be able to identify the correct schema to use if validating.

##### name

For entities where it's name is not an intrinsic part of the entity itself it can be useful to have a human readable name for something. For example, a name is an intrinsic property of a person or character, but something like an asset does not by definition need a name (that is what identifiers are for), however people like names not long strings of random characters, and this property is often included to serve that purpose

##### description

A human readable (preferably short) description of the entity, like name this is really meant for human consumption and should not be used for encoding structured information.

##### extension

This schema does not attempt to define every attribute that might ever be associated with any given entity, the goal is to surface enough to allow a production to track and relate enough attributes to find things. An asset such as the camera metadata file, image or video file may contain dozens or hundreds of specific metadata fields in multiple formats.

Generally we recommend that more extensive metadata be held separately, either as it's own thing or in a container format like IMF, JPG, etc. This additional data can then be given an identifier have an asset created for and be related to anything pertinent. 

However, if it is desirable to embed data beyond the defined properties the attribute can be used freely. There are no restrictions beyond those imposed by JSON itself, so adding additional JSON, serialize text, base64 encoded objects are all allowed. It is the responsibility of the sending and receiving parties to know what to do with the data.

