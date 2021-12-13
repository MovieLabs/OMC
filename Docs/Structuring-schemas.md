# Structuring schemas

The ontology provides an overriding data model, with a set of entities and the relationships that bind them together. However for practical purposes this model needs to be serialized, generally as either JSON or XML. The following document describes a set of best practices and guidelines when designing application or class specific schemas.



An object within a JSON document is composed of keys, each with a corresponding value ``<key>: <value>``

```
{
	"Slate": {
		"SlateUID":  "1234",
		"shootDay": 4
	}
}
```

The keys are always strings, the values can be a objects, arrays, or primitives such as strings, numbers or Booleans.

The following schema provides a set of conventions and definitions for building data representations using JSON. Schemas can be constructed from a set of components that can assembled together in a variety of ways to suit particular needs.



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

