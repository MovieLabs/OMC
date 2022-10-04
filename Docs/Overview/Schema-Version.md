# Schema Versioning

In this section we address only the issues related to the versioning of the schema and the versioning of an instance of an entity built with the schema. The versioning of actual assets used in the production will be addressed separately as that is specific to individual production workflows,  different types of assets, and so on.

## JSON Schema Version
The version of schema specification that this schema is using. This will be a version of JSON Schema. Currently we are using draft 7, specified here:

```
"$schema": "http://json-schema.org/draft-07/schema#",
```

*Note: A topic for consideration by the working group is to migrate to using JSON-Schema 2020-12. There is some additional functionality through extra keywords, and there is more formalized mechanism for bundling schemas (which would be useful). However there does seem to be less support in some of the tooling for 2020-12 over JSON-7*

## OMC Schema Version (Proposal)
We have not adopted a formal versioning mechanism yet; this seemed premature in light of this being a closed release and the rapid rate of change during initial development. The following represents a starting point for discussion with the implementers group

**Major**

A major version update indicates that functionality has been added or removed that creates a breaking change with prior versions.
Examples: Adding additional required fields, or changing the naming of attributes or properties

**Minor**
A minor update indicates that functionality has been changed, but forward and backward compatibility has been maintained with the major version number.

Example: A property can be deprecated, but not removed. Properties that are not required can be added.

**Patch**

A patch has been issued that corrects aspects of the schema that do not directly affect implementation and cause no breaking changes

Example: Changes to description or title text, or the addition of enumerated values.


Given that the schema for each entity can advance independently would this mean we need a schema version for each. This potentially creates a lot of additional payload and complexity in parsing the object as schema versions must be checked for each entity all throughout the payload.

- Have a system that groups changes together and advances versions of all entities in the group.
- Have a system that by inherits a version from the parent, unless overridden. Since many changes would be non-breaking this could be done at the ***(minor?)*** version level possibly.
- The spec allows entities to serialize related entities, there may well be different versions in related entities, so there must be some way of overriding a parent version.

[Introducing SchemaVer for semantic versioning of schemas](https://snowplowanalytics.com/blog/2014/05/13/introducing-schemaver-for-semantic-versioning-of-schemas/)

## Instance version
It may be useful to version the instance of any given entity, i.e. if any of the properties are updated. For example if a characters height or weight properties were updated, you would want to update any systems that are using that data. In the event an application had conflicting records with the same identifier, it would need to disambiguate them and presumably adopt the more recent version.

*Note: This only applies to the properties values of an instance, in the case of an asset there is also the version of the essence itself to consider. This would be considered part of the structural characteristics of an Asset, we will be addressing the versioning of assets in a separate working group.

