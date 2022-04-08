# Schema Versioning

In this section we address only the issues related to the versioning of the schema, and the versioning of an instance of an entity based on the schema. The versioning of actual assets used in the production will be addressed separately as this will be specific to productions and different types of assets.



## JSON Schema Version

The version of schema specification that this schema is using. This will be a version of JSON Schema, currently we 
are using draft 7, specified here:

```angular2html
"$schema": "http://json-schema.org/draft-07/schema#",
```


## MovieLabs Schema Version

This schema uses the semver conventions for versioning

Major

A major version update indicates that funcionality has been added or removed that creates a breaking change with the 
prior versions.
Examples: Adding additional required fields, changing the naming of attributes or properties

Minor
A minor update indicates that functionalty has been changed, but forward and backward compatability has been 
maintained with the major version number.

Example: A property can be deprecated, but not removed. Properties that are not required can be added.


Patch

A patch has been issued that corrects aspects of the schema that do not directly affect implementation and cause no 
breaking changes

Example: Changes to description or title text, the addition of enumerated values.





Given that the schema for each entity can advance independently does this mean we need have a schema version for 
each of them. This potentially creates a lot of additional payload and complexity in parsing the object as schema 
versions must be checked all the through the object.

- Have a system that locks blocks a changes together and advances versions of all entities in the schema
- Have a system that by definition would inherit a version from the parent, unless overridden, since many changes 
  would be non-breaking this could be done at version level possibly
- The spec allows entities to serialize related entities, so there may well be different versions in related 
  entities, so there must be some way of overriding a parent version.



https://snowplowanalytics.com/blog/2014/05/13/introducing-schemaver-for-semantic-versioning-of-schemas/



## Instance version

Each instance of any entity itself can be versioned, a version will be increased whenever the values of any 
properties are updated, added or deleted.

*Note: This only applies to the values in an instance of this schema, it does not necessarily refer to changes 
in an object the instance might be referencing. For example an Asset describes and image, it functional and 
structural characteristics. The image itself may undergo a revision without its underlying characteristics changing. 
This may result in a version change to the Asset, that is tracked seperately.* 



