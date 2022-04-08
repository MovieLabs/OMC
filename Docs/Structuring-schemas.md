# JSON Schema Overview

The formal ontology created in RDF provides an overriding data model, with a set of entities and the relationships that bind them together. However,  it is more common that  JSON is used to send and receive data between applications . The following document describes a set of best practices and guidelines when designing application or class specific schemas.

## Composition vs Inheritence

RDF is a class based system, however JSON does not inherently have a class based structure. The goal behind the JSON model is to provide a flexible mechanism to communicate. To achieve this the JSON data model defines a collection of Entities that are in turn composed from a sets of Properties. These Properties are either other Entities or Attributes.

**Entity**: A set of properties that together describe a single concept within the model.

**Property**: May be <key><value> pair describing a single Attribute or an Entity.

**Attribute**: A primitive value (or array of primitive values), i.e. a string, number, Boolean or null.

This allows new Entities to be created by composing a combination of individual Property and to re-use

By convention we capitalize the first letter of any defined Entity. Properties that describe an Attribute are camel cased (first letter is lower case). Entities can therefore be easily identified by their being capitalized, and each Entity will have it's own JSON schema defining it.

##### Examples:

The Entity that represents an identifier is used in many situations and has the form:

```json
    {
        "Identifier": {
          "identifierValue": "1234",
          "identifierScope": "Movielabs"
        }
    }
```

Here identifierValue and identifierScope are primitive values of type string.

The Identifier can then be used to compose other entities:

```JSON
{
    "Character": {
        "Identifier": [{
            "identifierValue": "1234",
            "identifierScope": "Movielabs"
        }],
        characterName: "Sven",
        description: "The protagonist"
    }
}
```

In this example the Character entity has the Identifier Property, which is itself and entity and additional Properties that are unique to itself.





## Identifiers and referencing

The use of identifiers is a central tenet of all the schemas, any entity should be uniquely identifiable with an Identifier. Using identifiers allows any other entity to be included by reference as well as by inclusion, a decision that is left to the application. Where only an identifier is included in a payload the presumption is that this would allow the receiving party to make a secondary lookup to retrieve the full set of attributes.

##### Example 1

This shows a Character with attributes encoded inline, given the attributes should include an Identifier, this could be used to do a secondary lookup, in case data has been updated between the time this encoded and used.

```JSON
"Character": [
    {
    "Identifier": {
      "identifierValue": "1234",
      "identifierScope": "Movielabs"
    },
    "name": "Sven",
    "description": "The protagonist",
    "CompleteName": {
        "scriptName": "SVEN",
        "firstName": "Sven",
    }
    "profile": {
        height: "6ft3in"
	    }
	}
 ]
```



###### Example 2

This only includes the references to the Characters by use of their identifiers. To retrieve the relevant information about them, they must be looked up in separate action.

```JSON
  "Character": [
 	{
    	"Identifier": {
        	"identifierValue": "1234",
        	"identifierScope": "Movielabs"
        }
    },
    {
    	"Identifier": {
    		"identifierValue": "7890",
    		"identifierScope": "Movielabs"
    	}
  	}   
]
```



## Standard Properties

There are some properties that are used fairly consistently throughout each of the entities

##### Schema Version

Blah

##### Instance



##### Entity Type

An optional property that enumerates the type of the entity within the structure of the entity itself. This is an optional field for convenience, it is human readable, it can be useful when programmatically parsing the entity to know what it is and be able to apply the correct function and finally it provides an easy way to setup an index in a database.

##### name

For entities where a name is not an intrinsic part of the entity itself it can be useful to have a human readable name for something. For example a name would be an intrinsic property of a person or character, but something like an asset does not by definition need a name (that is what identifiers are for), however people like names not long strings of random characters.

##### description

A human readable (preferably short) description of the entity

##### unstructuredData

This schema does not attempt to define every attribute that might ever be associated with any given entity, the purpose is to surface enough to allow a production to track and relate enough attributes to find things. An asset such as the camera metadata file, and image or video file may contain dozens or hundreds of specific metadata fields in multiple formats. This data could be embeded in a file format like IMF or JPG, or as a separate Asset file, like a sidecar. However if it is desirable to include additional data in the payload it can be included here. It is presumed that the receiving application will know how to process and interpret this data.

