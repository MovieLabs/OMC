# Best Practices



## Naming Conventions

**Ambiguous naming**
Avoid the use of names that can be ambiguous or apply to multiple types, key names like ‘date’ or ‘id’ should encode a specific reference to their type in the name ‘creationDate’, ‘distributionId’, etc.

** Outline the reasoning for this



** Identifiers that are part of an existing class (person) could be called ‘id’ or ‘identifier’?

**Plurals**
We should discuss, but this is my position.
** Avoid the use of plurals, it creates inconsistencies in naming i.e. parties vs dates vs classes.
** In the event a field name that initially only has a single entry is later updated to allow for multiple entries the field name itself should also be modified to reflect this, which potentially introduces a potential breaking change to people parsing the data.

**Capitalization**
Capital letters for classes, lower case for properties.

Standardizing here between lower-cased first letter for JSON and upper-cased first letter for XML would also be acceptable in that it gives an easy conversion between the two if required.

** camel case



**Punctuation**
Punctuation should be avoided in all naming, do not use hyphens, spaces, underscores, etc. Some database systems require these to be escaped and there is variability across systems in how punctuation is treated as well as how it is sometime represent on screen.

Avoid the use of additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However what is convention in one system rarely translates to other forms of serialization or databases.





**Multiple Values**

If a property only has single value it may be represented with a single value or an array. Where multiple values then an array must be used.

 ** Convention is to use arrays where multiple values are likely

```json
"Identifer": {
	"id": "1234"
}
```



```
"Identifier": [
    {
        "id": "1234"
    },
    {"id": "5678"}
]


```





**Key Value Pairs**
Should use typed definition where applicable

// Preferred

    "creationDate": $ref Date

** This makes the use of non-ambiguous naming more important as a best practice



    {
      "participants": [
         {
          "type": "role",
          "value": "Editor
         },
        {
          "type": "organization",
          "value": "Super Duper Effects"
        }
      ]
    }

** This can work better when dealing with an array of things, such as people attached to a particular parts.


// Acceptable

    "creationDate": "string"





## Definitions

Class: 

Entity: An instance of Class

Element: The values in an instance. An Element can be an Entity or a Property

Property: A key value pair with a field name and primative type (String, Number, Integer or Array of primatives).

Field: The key for an Element or Property

Type: A property has an assigned type which defines it's structure and provide clear semantics



** Some examples for the above.









NEIM JSON LD/RDF/XML/Normalized

https://niem.github.io/NIEM-JSON-Spec/v5.0/niem-json-spec.html

https://github.com/NIEM/NIEM-JSON-Spec/wiki/NIEM-JSON-normalization

NEIM JSON Spec

https://github.com/NIEM/NIEM-JSON-Spec



## Versioning

The schema allows for versioning at several levels

JSON Schema: Defines the version number of the JSON schema specification

