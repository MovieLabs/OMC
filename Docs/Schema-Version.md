# Schema Versioning

## JSON Schema versioning
The version of schema specification that this schema is using. This will be a version of JSON Schema, currently we 
are using draft 7, specified here:
```angular2html
"$schema": "http://json-schema.org/draft-07/schema#",
```
As part of the specification this included in each schema definition using the $schema keyword


## MovieLabs schema version
Each individual schema may evolve


With the exception of required fields the inclusion or exclusion of any given field in an instance is optional.

- The addition or removal of non-required fields is not considered a breaking change
- The renaming of field is considered a mid-level change
- A change in terminology 
