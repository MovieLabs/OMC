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

The use of identifiers is a central tenet of all the schemas, any entity should be uniquely identifiable with an Identifier class. Using identifiers allows any other entity to be included by reference as well as by inclusion. 

##### Example 1

This shows a Character with attributes encoded inline, given the attributes should include an Identifier, this could be used to do a secondary lookup, in case data has been updated between the time this encoded and used.

```JSON
"hasCharacter": [
    {
    "Identifier": {
      "identifierValue": "1234",
      "identifierScope": "Movielabs"
    },
    "name": "Daniel",
    "height": "6'3"
	}
 ]
```



###### Example 2

This only includes the references to the Characters by use of their identifiers, to retrieve the relevant information about them, they must be looked up.

```JSON
  "hasCharacter": [
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

