# Assets
Tracking and categorizing the assets that make up a production is probably one of the most complex parts of production management and complex systems have been developed to do this over the years. The role of OMC-JSON is not to replace this but to provide a common mechanism for communicating the assets needed for a given workflow and provide a means for the applications and services to find and access the files and other assets they need. This information includes how an asset relates to other parts of the production; some of those other parts are themselves assets (e.g., a proxy that is derived from the OCF), and some aren't (e.g., the scene in which the asset is used.) 

The 2030 vision establishes some core ideas behind the handling of assets:
- Separation of its [structural and functional characteristics](Functional&Structural.md)
- The specific location of an asset can be abstracted and resolved when needed. This involves the use of a resolution service that returns a specific location on request. [Read our blog post on resolving assets]([Through the Looking Glass - MovieLabs](https://movielabs.com/through-the-looking-glass/))

In practical terms the general expected pattern for using the OMC-JSON is that the payload describes a set of entities and each entity contains one or more identifiers. This tech note focuses on Assets. 

If there is only an identifier in the Assets, it can be passed to a resolution service which will return a URL for the required resource. Applications do not have to resolve identifiers if the JSON contains enough information or if the identifier itself is a resolved location (such as a URL.) See <<<Identifiers and References in Schema-Structure>>> for more on identifiers vs fully formed entities.

Often the process of deciding exactly which set of assets a person or service needs for a particular task is complicated. Assets advance through multiple versions and there might be different variants or representations of the same asset. *Note*: An extension to OMC for managing versions is underway; one if its most important features is that a version is itself just another Asset that can be used independently.



<<< i don;t think we need the next sentence. it;s been said before, and over-emphasizes resolution>>>

The intent in the OMC-JSON is that a set of assets needed for a task can be communicated and unambiguously resolved.

### Conventions
#### Identifiers
How to construct an asset and use the different identifiers:

- The asset identifier for the entity uniquely identifies the 'whole' asset - the combination of its structural and functional characteristics. [LINK: See Functional& Structural for an explanation of this concept]

- The structural identifier in the structural characteristics is for the essence of the asset. In many cases the essence (e.g., a file or a URL-accessible resource) can be located or resolved with this identifier.

  


#### Structural and Functional
[*Structural and functional types*](./Functional&Structural.md)

Roughly speaking, the functional attributes of an Asset relate to how it is used, and the structural properties relate to what it is.

**Structural and functional properties**
Along with a functional and structural type, specific properties related to its structural and functional type may also be included.

Structural properties describe details of the asset that are independent of its use, for example the size or color depth of an image, or the gps coordinates of where it was captured. 

Given the large array of structural types and the number of potential properties involved it should be remembered the intent of the OMC-JSON is not to replicate existing metadata schemes. The structural properties provide an opportunity to communicate some key properties that may be useful in finding, identifying or disambiguating assets in a workflow without the need to explicitly parse the underlying formats.

This can be especially useful where these properties are embedded as part of a file. Where metadata is not embedded it would generally  *RGD: is htis really 'generally'?* be considered an asset in its own right, identified and made available accordingly.

For systems that are file based, the structural properties can encode a file path and name for the essence.

*Note: Should we also say, these could be used to encode what a file should be named along with a file path, for use when hydrating a system that uses a resolver. Typically when you retrieve a file from a bucket the URL will describe a path and name used for the cloud system, this may not be how you want to setup files in an application*

Similarly functional properties can be included. These may also be subsets of existing metadata, for example the ordering for a set of assets in some sort of sequence or timing information, and informaiton related to a particular functional use.

### Examples
The following examples use a pseudo representation of the JSON and a similar pseudo example of how parameters in the current resolver spec can be represented.

*[Need to point this to the resolver spec/code and blog]*

*[move resolver-specific stuff to another document?]*

#### Single Digital Asset

A single digital asset, identifier A1; essence identifier E1. A1 can be resolved asking for metadata or for essence, and E1 can be resolved to the essence.  

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
id: A1
recordType: metadata
mediaType: application/json
==> returns URL for the Asset metadata

id: A1
recordType: item
mediaType: image/jpg
==> returns URL for the essence itself,  using the Asset identfier.

id: E1
recordType: item
mediaType: image/jpg
==> returns URL for the essence, using the essence identifier
```

---

 A single digital asset where metadata about the asset is encoded and can be resolved separately.

*[ do we need this? if so, is it really a separate example?']*

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
#### 



---

#### Digital Asset, multiple uses

This shows two Assets which use the same essence. 

asset where the essence serves 2 functional uses, in this case the resolver would be return the same result (as it is the same file), an application would determine how to present and use the asset.

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
*Note: This uses a unique asset identifier for each functional type (it is the same essence so this identifier is the same). There is no need for a formal relationship to exist between the two entities, this is for the production to decide if it is useful

---

 An asset where the essence has different structural characteristics:
  - A physical copy that has a barcode and database entry that returns location information
  - A digital copy
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
recordType: location
mediaType: application/json

id: E2
recordType: item
mediaType: image/jpg
```
*Note: The asset identifier is the same for both, here the application would decide which structural form is preferred, the physical or digital copy*

When a production requires multiple copies of the same thing how does this manifest.
- For physical props, each instance would need a unique essence id, because each can be physically in separate places. Do they have a unique asset id?
- For digital versions we can leave that up to the production.


---
-- Separate Doc?


## Asset Groups
Asset groups provide for logical groupings of Assets into a single entity. Asset groups are Assets themselves. They can refer to other Asset groups or to the essence of an asset as described above, this allows for a hierarchical structure of Assets to be constructed.

Asset groups are deliberately simple. The intent is to communicate sets of assets needed in a workflow or application. How that group is used in an application can be complex and application-dependent. Other mechanisms like USD, EDL's or AAF's carry complex information about how multiple assets interrelate within specific applications, the OMC-JSON acts more as a manifest, the expectation is that the files describing how an application deploys these files is included as part of this manifest.

Asset groups can be useful as a simple organizing construct; group the concept art for a particular character together, or a series of storyboard frames into an ordered group. They can also be used for things like a 3D Model that is composed of a set of meshes, textures, and rigging.

Using groups can simplify managing the relationships that exist between assets and other pieces of context. If multiple images of concept art in a group together, the character only has to relate to the group, not each individual image. A set of 3D assets may be reused in multiple scenes, each group can be related independently to a scene, or a group representing 3D model can itself be in multiple groups

---
An Asset that is structurally an AssetGroup, with three other Assets as elements. 
```
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: AssetGroup
functionalCharacteristics
	functionalType: artwork.storyboard
Asset: [
	identifier
		identifierValue: A2
	identifier
		identifierValue: A3
	identifier
		identifierValue: A4
]
```





---
-- Separate Doc?

## Analogue & Digital
Data has to be stored somewhere. In the ontology, analog data is bound to the media on which it has been recorded. Something shot on film is essentially bound and carried on the physical film it recorded on.

Digital data is a little different, in that it is often moved or copied to different devices. Something recorded on the camera Mag may be moved onto some sort of hard drive, then later onto long term tape. Digital data has the distinct advantage that it does not degrade in quality when it transferred across storage devices. 

For this reason, the ontology allows for digital data to optionally to specify a 'carrier', which is the piece of Infrastructure being used to hold the data. This might be something like a thumb-drive, DVD, LTO tape, etc. This separate piece of infrastructure has its own identifier and specifics  like its physical location, or who has custody of it, are part of its structural properties. For data stored natively in a cloud environment location is tracked through a URL; in many cases you don't really know (or care) exactly what the carrier itself is or the exact physical location.

### Carrier
The documentation says the carrier is an Asset and not Infrastructure, isn't the data the Asset not what it is stored on. Data always has a carrier, it's just not always worth explicitly naming it, data in the cloud is still on a hard drive.

A asset that is structurally digital with a carrier
```
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
	carrier: Infrastructure
				identifier
					identifierValue: I1
functionalCharacteristics
	functionalType: referenceMaterial


Resolver
id: E1
recordType: digital.image
mediaType: image/jpg

```

- What does E1 resolve to, the URI on the file system of the carrier or whatever mechanism is used to retrieve the essence from the carrier?
- Presumably any structural properties that describe a file location would be doing that in relation to the carrier. If an asset is in two or more locations, a carrier and the cloud, how do we differentiate. Is it not the resolver that should tell us where the file is, i.e. that it is on a carrier (not the OMC-JSON)?
- I would think the Infrastructure should carry things like its physical location as one its properties. To me this feels you should resolve the asset and the resolver should return 'the carrier'?


A piece of digital media with a carrier
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


---
-- Separate Doc?

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

Other Use Cases
- Multiple instances of the same thing
	- Multiple physical props
	- Multiple digital instances
- Any issues with versions or variants when it comes to asset groups?


*General Notes:*
- *Functional and structural characteristics are not themselves entities, they do not have their own identifiers*
- *An asset entity only has one functional and structural characteristic, this is no longer an array*
- *A useful side effect of having separate identifiers for the 'whole' asset and the essence is that this more clearly delineates information and item, meaning security authorization can be more easily separated, some applications may only need access to metadata*



