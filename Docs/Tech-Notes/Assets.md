# Assets
Tracking and categorizing the assets that make up a production is probably one of the most complex parts of production management and complex systems have been developed to do this over the years. The role of the OMC-JSON is not to replace this but to provide a common mechanism for communicating what assets are needed for a given workflow and provide a means for the applications and services to find and access the files they need. This information includes how an asset relates to other parts of the production; some of those other parts are themselves assets (e.g., the OCF form which a proxy is derived), and some aren't (e.g., the scene in which the asset is used.) 

The 2030 vision establishes some core ideas behind the handling of assets:
- Separating of its [structural and functional characteristics](Functional&Structural.md)
- That the specific location of an asset can be abstracted and resolved when it is needed. This involves the use of a resolution service that returns a specific location on request. (point to resolver explanation)

In practical terms the general expected pattern for using the OMC-JSON is that the payload describes a set of assets, each asset contains one or more identifiers. The identifiers are then passed to a resolution service which will return back the URL of the required resource.

Often the process of deciding exactly which set of assets a person or service needs for a particular task is a complex one. Assets typically advance through multiple versions, there might be different variants or representations of the same asset, etc.

The intent in the OMC-JSON is that a set of assets needed for a task can be communicated and unambiguously resolved.

- The main identifier identifies the 'whole' asset, including its structural and functional properties.
- The identifier within an asset's structural characteristics identifies the essence

> The OMC-JSON is often just an array of objects. Therefore there is not a uniqueness constraint on identifiers within the array. Unlike a database where there is often a uniqueness constraint an identifier.


### Variant / Version / Representation
What they mean and when to use them.
Is Proxy a variant or a representation - you decide (we think it variant, make it it's own thing)
- This can be a question as to how you want to relate something, I am probably happy to relate the proxy directly to the slate, but a thumbnail is probably easier to contain that relationship at the upper level. Also separate from a security standpoint (access control - appropriate granularity).


### Conventions

**Structural and functional types**
The specification only requires these be strings and as such they are not controlled. However, MovieLabs is developing guidelines for them and a set of recommended terms that if used would help in cross platform interchange.

-- old

Individual terms should be written in camel case, separated using dot notation
digital.image

The ordering is somewhat arbitrary, it is helpful to have an ordained order, but is it a digital image or an image that is digital? What is important is that key terms should be separate, this allows for easy searching and categorization by either using terms singularly or in combination.

artwork.storyboard
artwork.storyboard.frame

-- new

Individual terms should be written in camel case, separated using dot notation, going from more general to more specific, e.g. for structural classes:
digital.image

And for functional classes:

artwork.storyboard
artwork.storyboard.frame



**Identifiers**
How to construct an asset and use the different identifiers.
- The identifier for the entity uniquely identifies the 'whole' asset - the combination of its structural and functional characteristics.
- The identifier in the structural characteristics references the essence of the asset. In many cases the asset can be resolved with this identifier.

- *A variant is new entity, it gets it's own identifier*
- *Representations share an asset identifier, each instance of any essence has a unique id, representation is a property of the structural characteristics*
- *A new version maintains the same main identifier across versions, each essence had a unique id. Version is property of the structural characteristics, as the other aspects of the asset do not change (i.e. it's functional characteristics).



#### Examples

> A single digital asset where metadata about the asset can also be resolved
```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: artwork.concept

Resolver
id: E1
recordType: item
mediaType: image/jpg

id: E1
recordType: item
mediaType: application/json
```
*Note: This uses the same main id, but a different identifier for each essence, the question is whether this could/should be done with two referent types and the same id*




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


> An asset where the essence serves 2 functional uses, in this case the resolver will be returning the same result
```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: reference


identifier
	identifierValue: A2
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: texture


Resolver
identifierVale: E1
recordType: item
mediaType: image/jpg

```
*Note: This requires 2 separate main identifiers, so there is no formal relationship between them, if a relationship were needed this would have to added, or both put in group (but with these being functionally different that may not be important) *


> An asset where the essence has different structural characteristics:
>  - A physical copy that has a barcode and database entry that returns location information
>  - A digital copy
```
OMC
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: physical.paper
	identifier
		identifierValue: E1
functionalCharacteristics
	functionalType: artwork.storyboard.frame


identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E2
functionalCharacteristics
	functionalType: artwork.storyboard.frame


Resolver
id: E1
recordType: item
mediaType: image/json

id: E1
recordType: data?
mediaType: application/json

id: E2
recordType: item
mediaType: image/jpg
```


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






## Asset Groups
Asset groups provide for grouping of other Assets into a single entity. Asset groups are Assets themselves, so they can contain other Asset groups, allowing for a structure of Assets that are made up of other assets.

Asset groups are deliberately simple. The intent is to communicate sets of assets needed in a workflow or application. How that group is used in an application can be complex and application-dependent. Other mechanisms like USD, EDL's or AAF's carry complex information about how multiple assets interrelate within specific applications,; these files are Assets themselves and can be sent to a relevant workflow.

Asset groups can be useful as a simple organizing construct: put all the concept art for a particular character together or put a series of storyboard frames into an ordered group. They can also be used for things like a 3D Model that is composed of meshes, textures, and rigging.

Using groups can simplify managing the relationships that exist between the assets and other pieces of context. If multiple images of concept art in a group together, the character only has to relate to the group, not each individual image.

> This storyboard is represented as an Asset Group with three elements. The scene it represents only has to have a single relationship to the group. However, each frame is still itself an Asset, so each frame can still use the standard mechanisms for supporting, e.g., physical and diital representaitons.
```
identifier
	identifierValue: AG1
structuralCharacteristics
	structuralType: AssetGroup
functionalCharacteristics
	functionalType: artwork.storyboard
Asset: [
	identifier: A1,
	identifier: A2,
	identifier: A3,
]
```










### Analogue & Digital
Data has to be stored somewhere. IN the ontology, analog data is bound to the media on which it has been recorded. Something shot on film is essentially bound and carried on the physical film it recorded on.

Digital data is a little different, in that it is often moved or copied to different devices. Something recorded on the camera Mag may be moved onto some sort of hard drive, then later onto long term tape. Digital data has the distinct advantage that it does not degrade in quality when it transferred across storage devices. 

For this reason, the ontology allows for digital data to optionally to specify a 'carrier', which is the piece of Infrastructure being used to hold the data. This might be something like a thumb-drive, DVD, LTO tape, etc. This separate piece of infrastructure it has its own identifier and things like location can be tracked. For data stored natively in a cloud type environment this is not really required, since its location is tracked through a URL; in many cases you don't even really know exactly what the carrier itself is, or where it is physically located.

### Carrier
The documentation says the carrier is an Asset and not Infrastructure, isn't the data the Asset not what it is stored on. Data always has a carrier, it's just not always worth explicitly naming it, data in the cloud is still on a hard drive.

From a schema perspective Infrastructure would be better, I already have an Asset property inside an Asset, using this effectively makes it an AssetGroup.

> A piece of digital media with a carrier
```
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier: E1
functionalCharacteristics
	functionalType: referenceMaterial
carrier: Asset/Infrastructure

Resolver
id: E1
recordType: digital.image
mediaType: image/jpg

```

There is the question as to whether the carrier is a property of an asset or whether this is something you use the resolver for? If I query the resolver for something stored on a carrier, does it return a reference to piece of Infrastructure that carries the data, if not then what?

> A piece of digital media with a carrier
```
ASSET
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier: E1
functionalCharacteristics
	functionalType: referenceMaterial
carrier: Asset/Infrastructure

Resolver
id: E1
recordType: thumbdrive
mediaType: image/jpg


INFRASTRUCTURE
identifier
	identifierValue: I1
structuralCharacteristics
	structuralType: thumbdrive
	identifier: E1
Location: Location

# If you resolve this you need to infer from the referent format that you are likely going to get metadata back, but is this metadata about the image (as in prior examples) or about the carrier. Or does the app have to figure this out, and if you want/need both how do you disambiguate

```

** There is no mention of carrier in the RDF



## Prop
> An asset with a functional type of Prop and physical and digital versions
```
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: physical
	identifier: P1
	Location: L1 // A physical location somewhere (or is this what you resolve)
functionalCharacteristics
	functionalType: prop

Resolver
id: P1
recordType: physical
mediaType: application/json // Resolves to physical location


identifier
	identifierValue: A2
structuralCharacteristics
	structuralType: digital.3dModel
	identifier: P1
functionalCharacteristics
	functionalType: prop


Resolver
id: P1
recordType: digital.3dModel
mediaType: application/3ds
```

When a production requires multiple copies of the same thing how does this manifest.
- For physical props, each instance would need an essence id, because each can be physically in seperate places.
- For digital versions we can leave that up to the production.

