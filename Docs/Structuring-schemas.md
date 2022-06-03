# JSON Schema Overview

OMC is written in RDF, which provides a useful degree of formality, especially for relationships and complex classes. JSON, of course, can also be used for data modelling, but it has different mechanics for classes, properties, and types, and less emphasis on relationships than RDF. The JSON schema retains the vocabulary, concepts, and top-level structures of the RDF, although some changes are necessary to support expressing the details of the concepts in JSON. In particular, the JSON schema provides standard mechanisms for relationships (in the RDF sense) and complex classes.

# Key Concepts

There are three pervasive concepts in the JSON schema:

- Classes
- Identifiers and references
- Relationships

## Classes

RDF is a class based system. JSON does not have a class based structure or the idea of class inheritance. We  use a compositional model, where a set of individual schemas are used to create entities that align with the RDF classes. These schemas can then be composed (via referencing) to create new entities. They can be nested, or included in sets. Each entity includes its entity type, which can then be used to validate or parse the properties in the entity.

The JSON data model defines a set of Entities which are in turn composed from sets of Properties. These Properties are either other Entities or Attributes.

**Entity**: A set of properties that together describe a single concept within the model.

**Property**: A <key> <value> pair where the value can be an entity, complex type (object or array of objects)   or an attribute.

**Attribute**: A primitive value (or array of primitive values), i.e. a string, number, Boolean or null.

The schema follow some general conventions:

- Each entity is defined in its own JSON schema.
- The first letter of any defined entity is capitalized. 
- Properties that describe the attributes of an entity are camel cased (first letter is lower case). 

Here is section of the schema for Narrative Location, which illustrates how the identifier subSchema is included by reference. The Location is itself an entity and therefore capitalized; it includes an identifier for for the Location ***(see Identifiers and references)*** and two attribute, a name and a description.

***Daniel: i added a name in the instance, but i may have gotten the nesting wrong....***

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
    "name": "221B Baker Street - exterior"
    "description": "Sherlock Holmes' residence"
}
```



## Identifiers and References

### Identifiers

The example above used an identifier. In the ontology, an Identifier is "a string of characters that uniquely identifies an object within a particular scope." An identifier is really just a way of referring to something; undifferentiated strings and URIs/IRIs are common forms for an identifier, and there are many more specialized ones as well. For the production system (and any system that consists of multiple cooperating systems) it is essential to know the *scope* of the identifier - the universe within which the identifier is valid and unique. For example, "42" is a perfectly god identifier, but without knowing the scope, there is no way of knowing what it represents. See [OMC Part 9: Utilities](https://mc.movielabs.com/docs/omc/utilities/concepts) for further details, including some meanings of "42".

There is a JSON schema for an identifier/scope pair, as shown here, followed by an example of an instance.

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
          "identifierScope": "MovieLabs"
        }]
    }
```



### References

The use of identifiers is a central component for all Entities; an entity must be uniquely identifiable with an Identifier. Using identifiers allows any entity to be included by reference or by inclusion; this decision is left to the application. Where only an identifier is included in a payload the presumption is the receiving party would make a request to retrieve additional information.

This shows a Narrative Location, where the Location itself is only referenced by its identifier. If a party received this they would need to make a request using the Location's identifier to get the full set of attributes.

```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "identifier": [{
            "identifierValue": "221B",
            "identifierScope": "LocationDB"
        }],
    },
    "description": "Sherlock Holmes' residence"
}
```

##### Example 2:

The model also allows for any entity to be fully resolved and sent as part of the Entity's data.

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
            "identifierValue": "221B",
            "identifierScope": "LocationDB"
        }],
        "name": "Sherlock Holmes' residence",
        "address": {
            "street": "221b Baker St.",
            "region": "London",
            "postalCode": "NW1 6XE"
            "country": "uk"
        }
    },
    "description": "Sherlock Holmes' residence"
}
```



The schemas are structured in such a way that in theory there is things can nest *ad infinitum*, so care should be taken since it is easy to create circular references.

The decision to dereference an entity and include it in a data payload, or to just send the identifier is for the application to make. If a reference is included then it is likely that any party receiving the data may want to make a request for the missing information. This will require that they have a means to do so, including the requisite security credentials and knowledge of where and how to make the request. This may not be so obvious if data is sent as a payload via a messaging system, as the receiving party may not even know who sent the data. 

***Need a comment on resolver/resolution?***

## Relationships

***describe the structure: relationshipName: [ {entities}]***

## Standard Properties

***This section needs work; also, doe sit go here, or under 'classes'?***

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

It is useful to have a human-readable name for entities whose name is not an intrinsic part of the entity itself. For example, a name is an intrinsic property of a person or character, but something like an asset does not necessarily need a name (that is what identifiers are for.) ,However people prefer names to long strings of random characters, and this property is often included for that reason.

##### description

A human readable (preferably short) description of the entity. As with name, this is really meant for human consumption and should not be used for encoding structured information.

##### extension

This schema does not attempt to define every attribute that might ever be associated with any given entity, the goal is to surface enough to allow a production to track and relate enough attributes to find things. An asset such as the camera metadata file, image or video file may contain dozens or hundreds of specific metadata fields in multiple formats.

Generally we recommend that more extensive metadata be held separately, either as its own thing or in a container format like IMF, JPG, etc. This additional data can then be given an identifier have an asset created for and be related to anything pertinent. 

However, if it is desirable to embed data beyond the defined properties the attribute can be used freely. There are no restrictions beyond those imposed by JSON itself, so adding additional JSON, serialize text, base64 encoded objects are all allowed. It is the responsibility of the sending and receiving parties to know what to do with the data.

