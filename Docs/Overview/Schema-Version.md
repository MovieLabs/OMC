# Schema Versioning

In this section we address only the issues related to the versioning of the schema and the versioning of an instance of an entity built with the schema. The versioning of actual assets used in the production will be addressed separately as that is specific to individual production workflows,  different types of assets, and so on.



## JSON Schema Version

The version of schema specification that this schema is using. This will be a version of JSON Schema, currently we 
are using draft 7, specified here:

```angular2html
"$schema": "http://json-schema.org/draft-07/schema#",
```


## MovieLabs Schema Version

This schema uses the semver conventions for versioning

**Major**

A major version update indicates that functionality has been added or removed that creates a breaking change with prior versions.
Examples: Adding additional required fields, or changing the naming of attributes or properties

**Minor**
A minor update indicates that functionality has been changed, but forward and backward compatibility has been maintained with the major version number.

Example: A property can be deprecated, but not removed. Properties that are not required can be added.

**Patch**

A patch has been issued that corrects aspects of the schema that do not directly affect implementation and cause no breaking changes

Example: Changes to description or title text, or the addition of enumerated values.

***[this next section is something to discuss with the implementers'' group]***

Given that the schema for each entity can advance independently does this mean we need have a schema version for each of them. This potentially creates a lot of additional payload and complexity in parsing the object as schema versions must be checked all through the object.

- Have a system that groups changes together and advances versions of all entities in the group.
- Have a system that by inherits a version from the parent, unless overridden. Since many changes 
  would be non-breaking this could be done at ***(minor?)*** version level possibly.
- The spec allows entities to serialize related entities, so there may well be different versions in related 
  entities, so there must be some way of overriding a parent version.



https://snowplowanalytics.com/blog/2014/05/13/introducing-schemaver-for-semantic-versioning-of-schemas/



## Instance version

We foresee that it would be convenient for clients of OMC-JSON data to have the ability to easily find the entities that have changed from document to document, or to encode changes only in a message body. This is an area for future work.

*Note: This only applies to the values in an instance. It does not refer to changes in an object the instance might be referencing. For example an Asset describes an image and its functional and 
structural characteristics. The image itself may undergo a revision without its underlying characteristics changing. 
This may result in a version change to the Asset, that is tracked separately.* 

***[needs a better, simpler example, perhaps just changing or adding a description]***

