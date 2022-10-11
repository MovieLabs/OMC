# Versions
### 

This section is under development.

## Version

In general, a version is a particular form of something. It can be used in the same circumstances as the thing of which it is a version - its differences are not enough to fundamentally change what it is. Some systems call these "revisions" or "iterations."

For example, a changed drawing is a version of the original drawing, and a CG model of a spaceship with a different engine exhaust is a new version of the original spaceship.


## Variant

A variant is a distinct new thing that is still innately related to the thing from which it is derived. A model of a car with dents is a variant of the model of the car without dents.

## Representation

A representation is another, equivalent form of something. For example, a low-res proxy of a video is a representation of a high-res original.

In OMC JSON, representations of Assets can exist as separate objects connected by a relationships, or as a single object with two different sets of structural characteristics. (See Assets of an example of the latter.)

*Move all below here into 'stuff to use later'*

*from asset doc*

- *A variant is new entity, it gets it's own identifier*
- *Representations share an asset identifier, each instance of any essence has a unique id, representation is a property of the structural characteristics*
- *A new version maintains the same main identifier across versions, each essence had a unique id. Version is property of the structural characteristics, as the other aspects of the asset do not change (i.e. it's functional characteristics).

*from original v/v/r doc*

## Variant / Version / Representation


Is Proxy a variant or a representation - you decide (we think it variant, make it it's own thing)

- This can be a question as to how you want to relate something, I am probably happy to relate the proxy directly to the slate, but a thumbnail is probably easier to contain that relationship at the upper level. Also separate from a security standpoint (access control - appropriate granularity).


> An asset where the essence has different representations
```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
	representation: fullSize
functionalCharacteristics
	functionalType: artwork.concept

identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue:E2
	representation: thumbnail
functionalCharacteristics
	functionalType: artwork.concept


Resolver
id: E1
recordType: item
mediaType: image/jpg

id: E2
recordType: item
mediaType: image/jpg
```
*Note: This uses the same main id, but a different identifier for each essence, the question is whether this could/should be done with two referent types and the same id*



> An asset where two versions a represented
```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	version: 1.0
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: artwork.storyboard.frame


identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	version: 2.0
	identifier
		identifierValue: E2
functionalCharacteristics
	functionalType: artwork.storyboard.frame


Resolver
id: E1
recordType: item
mediaType: image/json

id: E2
recordType: item
mediaType: image/jpg
```
*Notes:
A version has a new essence identifier. If version is a property of the main entity then it will also need a new main identifier, and versions will need to grouped (asset group). If version is a property of the structural characteristics then the main id can persist across version (I think I prefer this as the functional characteristics and relationships persist across versions)*

Other Use Cases
- Multiple instances of the same thing
	- Multiple physical props
	- Multiple digital instances
- Any issues with versions or variants when it comes to asset groups?


*General Notes:*
- *Functional and structural characteristics are not themselves entities, they do not have their own identifiers*
- *An asset entity only has one functional and structural characteristic, this is no longer an array*
- *A useful side effect of having separate identifiers for the 'whole' asset and the essence is that this more clearly delineates information and item, meaning security authorization can be more easily separated, some applications may only need access to metadata*

*[from assets doc]*

## Variant / Version / Representation

What they mean and when to use them.
Is Proxy a variant or a representation - you decide (we think it variant, make it it's own thing)

- This can be a question as to how you want to relate something, I am probably happy to relate the proxy directly to the slate, but a thumbnail is probably easier to contain that relationship at the upper level. Also separate from a security standpoint (access control - appropriate granularity).


> An asset where the essence has different representations

```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
	representation: fullSize
functionalCharacteristics
	functionalType: artwork.concept

identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue:E2
	representation: thumbnail
functionalCharacteristics
	functionalType: artwork.concept


Resolver
id: E1
recordType: item
mediaType: image/jpg

id: E2
recordType: item
mediaType: image/jpg
```

*Note: This uses the same main id, but a different identifier for each essence, the question is whether this could/should be done with two referent types and the same id*



> An asset where two versions a represented

```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	version: 1.0
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: artwork.storyboard.frame


identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	version: 2.0
	identifier
		identifierValue: E2
functionalCharacteristics
	functionalType: artwork.storyboard.frame


Resolver
id: E1
recordType: item
mediaType: image/json

id: E2
recordType: item
mediaType: image/jpg
```

*Notes:
A version has a new essence identifier. If version is a property of the main entity then it will also need a new main identifier, and versions will need to grouped (asset group). If version is a property of the structural characteristics then the main id can persist across version (I think I prefer this as the functional characteristics and relationships persist across versions)*

