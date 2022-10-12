# Assets
Tracking and categorizing the assets that make up a production is probably one of the most complex parts of production management and complex systems have been developed to do this over the years. The role of OMC-JSON is not to replace this but to provide a common mechanism for communicating the assets needed for a given workflow and provide a means for the applications and services to find and access the files and other assets they need. This information includes how an asset relates to other parts of the production; some of those other parts are themselves assets (e.g., a proxy that is derived from the OCF), and some aren't (e.g., the scene in which the asset is used.)

The 2030 vision establishes some core ideas behind the handling of assets:
- Separation of its [structural and functional characteristics](./Functional&Structural.md)
- The specific location of an asset can be abstracted and resolved when needed. This involves the use of a resolution service that returns a specific location on request. [Read our blog post on resolving assets](https://movielabs.com/through-the-looking-glass/)

In practical terms the general expected pattern for using the OMC-JSON is that the payload describes a set of entities and each entity contains one or more identifiers. This tech note focuses on Assets.

If there is only an identifier in the Asset, it can be passed to a resolution service which will return a URL for the required resource. Applications do not have to resolve identifiers if the JSON contains enough information or if the identifier itself is a resolved location (such as a URL.) See  the [Identifiers section in Schema Structure](../Overview/Schema%20Structure.md#Identifiers%20and%20References) for more information.

Often the process of deciding exactly which set of assets a person or service needs for a particular task is complicated. Assets advance through multiple versions and there might be different variants or representations of the same asset. *Note*: An extension to OMC for managing versions is underway; one if its most important features is that a version is itself just another Asset that can be used independently.

## Conventions
### Identifiers
Identifiers are used to identify what we refer to as the 'whole' asset, this includes both the essence of an object and metadata about that object. A separate identifier is used to identify the essence itself (the essence is the collection of bits or the specific file). These are separate because it is possible for there to be more than one essence for asset, also sometimes you only want the metadata not the essence itself.

For a more information see here: [Identifiers and References](../Overview/Schema-Structure.md#Identifiers%20and%20References)

How to construct an asset and use the different identifiers:
- The identifier for the entity uniquely identifies the 'whole' asset - the combination of its structural and functional characteristics.
- The identifier in the structural characteristics identifies the essence of the asset. In many cases the essence (e.g., a file or a URL-accessible resource) can be located or resolved with this identifier.

*Note: A useful side effect of having separate identifiers for the 'whole' asset and the essence is that this more clearly delineates metadata and object, allowing security authorization to be more easily separated. This allows applications and participants to view metadata about assets without being granted access to the asset itself. For example a system admin can provision, move or migrate files without being allowed direct access to the sensitive content itself*

### Structural and Functional Characteristics
In simplified terms the functional attributes of an Asset describe to how it is used, and the structural properties describe what it is.

For a more detailed explanation with examples, see here: [Structural and functional types](./Functional&Structural.md)

**Structural and functional properties**
Along with a functional and structural type, an Asset may also carry additional properties that further describe the structural and functional characteristics.

Structural properties describe details of the asset that are independent of its use, for example the size or color depth of an image, or the GPS coordinates of where it was captured.

Given the large array of structural types and the number of potential properties involved it should be remembered the intent of the OMC-JSON is not to replicate existing metadata schemes. The structural properties provide an opportunity to communicate some key properties that may be useful in finding, identifying, or disambiguating assets in a workflow without the need to explicitly access or parse the underlying formats.

This can be especially useful where these properties are embedded as part of the essence file, as this can avoid having to read and load the file. Where metadata is not embedded with the essence this should generally be considered an asset in its own right, given it's own identifier and made available accordingly.

For file based systems, the structural properties can encode a file path and name for the essence.

*Note: Should we also say, these could be used to encode what a file should be named along with a file path, for use when hydrating a system that uses a resolver. Typically when you retrieve a file from a bucket the URL will describe a path and name used for the cloud system, this may not be how you want to setup files in an application

** RGD: I think this is a separate note on 'using cloud storage with a resolver', **
** DML: Where is that going? **

Similarly, functional properties can be included. They can include, for example, the ordering for a set of assets in some sort of sequence or timing information, and information related to a particular functional use.

## Examples
The following examples use a pseudo representation of the JSON and a similar pseudo example of how parameters in the current resolver spec can be represented.

As part of the 2030 vision we advocate for the use of a resolution system, where identifiers are used to resolve a location of a resource, we include examples of how the JSON can map to resolver entries, for more details on how resolvers work and implementation see here: [Through the Looking Glass](https://movielabs.com/through-the-looking-glass/). If you are not using a resolver, this can be ignored. The resolver examples do not cover all possible ways of using the resolver with Assets.

---
### Single Digital Asset
This shows the simplest case of single digital asset (A1) and single essence (E1).

A1 can be resolved asking for metadata, E1 can be resolved for the URL of the essence.

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

id: E1
recordType: item
mediaType: image/jpg
==> returns URL for the essence, using the essence identifier
```

---

### Digital Asset, two functional uses

This shows two Assets which use the same essence; one uses the image as reference art and the other uses it as a texture.

As with the example above, each Asset can resolve to its metadata or to its essence.

It is possible to have a metadata request on the essence identifier return URLs for the asset or the structural metadata but that is dependent on the functionality and flexibility of the resolution mechanism, and so is not included here.

There does not have to be any formal relationship between A1 and A2, though of course one can be added.

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
identifierValue: A1
recordType: metadata
mediaType: application/json
==> returns URL for metadata for A1

identifierValue: E1
recordType: item
mediaType: image/jpeg
==> returns URL for E1 essence

identifierValue: A2
recordType: metadata
mediaType: application/json
==> returns URL for metadata for A2

identifierVale: E1
recordType: item
mediaType: image/jpg
==> returns URL for E1 essence
```

---

### Single Asset with two different sets of structural characteristics

This shows a single Asset that exists in two different forms, one digital and one physical. The physical copy has a barcode and a database entry that returns information about its physical location. The Asset identifier is the same for both copies, with two different essence IDs.

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
mediaType: image/png
==> returns URL for the barcode (barcodes are images)

id: E1
recordType: location
mediaType: application/json
==> returns information about the location

id: E2
recordType: item
mediaType: image/jpg
==> returns URL for the digital copy of the Asset
```
*Note: The asset identifier is the same for both. The application has to determine which structural form is preferred, the physical or digital copy. If asset information is stored in a MAM or other database it is up to that system to decide how to respond to requests for the asset*

---

## Asset Groups
Asset groups provide for logical groupings of Assets into a single entity. Asset groups are Assets themselves. They can refer to other Assets, Asset groups, or to the essence of an asset as described above. This allows for a hierarchical structure of Assets.

Asset groups are deliberately simple. The intent is to communicate sets of assets needed in a workflow or application. How that group is used in an application can be complex and application-dependent. Other mechanisms like USD, EDL's or AAF's carry complex information about how multiple assets interrelate within specific applications, the OMC-JSON acts more as a manifest, the expectation is that the files describing how an application deploys these files is included as part of this manifest.

Asset groups can be useful as a simple organizing construct; group the concept art for a particular character together, or a series of storyboard frames into an ordered group. They can also be used for things like a 3D Model that is composed of a set of meshes, textures, and rigging.

Using groups can simplify managing the relationships that exist between assets and other pieces of context. If multiple images of concept art in a group together, the character only has to relate to the group, not each individual image. A set of 3D assets may be reused in multiple scenes, each group can be related independently to a scene, or a group representing 3D model can itself be in multiple groups

---
An Asset that is structurally an AssetGroup, with three other Assets as elements of that group.
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



