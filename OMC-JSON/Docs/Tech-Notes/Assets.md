# Assets
Tracking and categorizing the assets that make up a production is probably one of the most complex parts of production management and complex systems have been developed to do this over the years. The role of OMC-JSON is not to replace this but to provide a common mechanism for communicating between applications and workflows certain information about these assets. This might include information about assets relate to other parts of the production; such as an asset being for a particular scene or character. Or how they might relate to other assets (e.g., a proxy that is derived from the OCF).

The 2030 vision establishes some core ideas behind the handling of assets:
- The separation of an assets metadata (information about the asset) and the essence of the asset (the actual thing, often a digital file like an image). This allows information about the asset to made available without actually needing access to the essence, this improves security and can save resources when an asset does not need to be retrieved and interrogated for embeded data.
- Separation of an assets [structural and functional characteristics](Functional&Structural.md), this is what an asset is (structural) from what it is used for (functional).
- All assets are uniquely identified, this allows the specific location of an asset to be abstracted and resolved when needed. This typically involves the use of a resolution service that returns a specific location on request. [Read our blog post on resolving assets](https://movielabs.com/through-the-looking-glass/)

An Asset is generally comprised of the following main parts:
- An identifier that is unique to the particular object. This identifier can remain static even if the underlying essence undergoes updates as iterates through versions.
- Structural Characteristics (AssetSC), that is itself uniquely identified, and describes the essence currently associated with the Asset, the AssetSC can change over time, for example if a new version of something is created.
- Functional Characteristics (FC) that describe what the Asset is used for in the production. In RDF this is a seperate object, but to simplify the JSON, this is held as a property of the Asset. Essence that has more than one functional use can be either be held as part of a new Asset or two instances of the same Asset with different functional characteristics.

Click the link for a more detailed explanation of [structural and functional types](Functional&Structural.md).

Often the process of deciding exactly which set of assets a person or service needs for a particular task is complicated. To help with this Assets can be related to other parts of the production, generally through a related Context. Assets also often advance through multiple versions, with different variants or representations of the same asset. Click here to learn more about [[Versions]].


## Conventions
### Identifiers
Identifiers are used to identify what is referred to as the Asset. An instance of an Asset includes properties that describe it, including it's structural and functional characteristics and prior versions. The essence is represented by an Asset Structural Characteristic (AssetSC), it is also uniquely identified. These are identified separately because it is possible the essence may change over time.

For a more information see here: [Identifiers and References](../Overview/Schema-Structure.md#Identifiers%20and%20References)

How to construct an asset and use the different identifiers:
- The identifier for the entity uniquely identifies the 'whole' asset - the combination of its structural and functional characteristics.
- The identifier in the structural characteristics identifies the essence of the asset. In many cases the essence (e.g., a file or a URL-accessible resource) can be located or resolved using the AssetSC identifier.

*Note: A useful side effect of having separate identifiers for the 'whole' asset and the essence is that this more clearly delineates metadata and object, allowing security authorization to be more easily separated. This allows applications and participants to view metadata about assets without being granted access to the asset itself. For example a system admin can provision, move or migrate files without being allowed direct access to the sensitive content itself*

### Structural and functional properties
Along with a functional and structural type, an Asset may also carry additional properties that further describe the structural and functional characteristics.

Structural properties describe details of the asset that are independent of its use, for example the size or color depth of an image, or the GPS coordinates of where it was captured.

Given the large array of structural types and the number of potential properties involved it should be remembered the intent of the OMC-JSON is not to replicate existing metadata schemes. The structural properties provide an opportunity to communicate some key properties that may be useful in finding, identifying, or disambiguating assets in a workflow without the need to explicitly access or parse the underlying formats.

This can be especially useful where these properties are embedded as part of the essence file, as this can avoid having to read and load the file to read and interrogate it.

Metadata itself can be essence, e.g. metadata in sidecar. In using a resolvable identifier this may retrieve the data either from a file or a URL that queries something like a REST endpoint.

For file based systems, the structural properties can encode a file path and name for the essence.

*Note: These can be used to encode what a file should be named along with a file path, for use when hydrating a system that uses a resolver. Typically when you retrieve a file from a bucket the URL will describe a path and name used for the cloud system, this may not be how you want to setup files in an application, (we will add additional notes on using file systems in the future).

Similarly properties associated with an assets functional characteristics can be included. These may also be subsets of existing metadata, for example the ordering for a set of assets in some sort of sequence or timing information, and information related to a particular functional use.

## Examples
The following examples use a pseudo representation of the JSON for brevity with only the pertinent attributes include, the structural and functional characteristics can contain specific properties related to each of these elements. For example, an image may have a width and height as part of it's structural characteristics

As part of the 2030 vision we advocate for the use of a resolution system, where identifiers are used to resolve a location of a resource, we include examples of how the JSON can map to resolver entries, for more details on how resolvers work and implementation see here: [Through the Looking Glass](https://movielabs.com/through-the-looking-glass/). If you are not using a resolver, this can be ignored. The resolver examples do not cover all possible ways of using the resolver with Assets.

---
### Single Digital Asset
This shows the simplest case of single digital asset (A1) and single essence (E1).

A1 can be resolved asking for metadata, E1 can be resolved for the URL of the essence.

```
identifier
	identifierValue: A1
AssetSC
	structuralType: digital.image
	identifier
		identifierValue: E1
assetFC
	functionalType: reference
```

![[Asset-1.svg]]

---
### Digital Asset, two functional uses

This shows two Assets which use the same essence; one uses the image as reference art and the other uses it as a texture.

There does not have to be any formal relationship between A1 and A2, though of course one can be added.

```
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
```

![[Asset-2.svg]]

---

### Single Asset with two different sets of structural characteristics

This shows a single Asset that exists in two different forms, one digital and one physical. The physical copy has a barcode and a database entry that returns information about its physical location. The Asset identifier is the same for both copies, with two different essence IDs.

```
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
```

![[Asset-3.svg]]
*Note: The asset identifier is the same for both. The application has to determine which structural form is preferred, the physical or digital copy. If asset information is stored in a MAM or other database it is up to that system to decide how to respond to requests for the asset*

---

## Asset Groups
Asset groups provide for logical groupings of Assets into a single entity. Asset groups are Assets themselves. They can refer to other Assets or Asset groups. This creates a hierarchical structure of Assets.

Asset groups are deliberately simple. The intent is to communicate sets of assets needed in a workflow or application. How that group is used in an application can be complex and application-dependent. Other mechanisms like USD, EDL's or AAF's carry complex information about how multiple assets interrelate within specific applications, the OMC-JSON acts more as a manifest, the expectation is that the files describing how an application deploys these files is included as part of this manifest.

Asset groups can be useful as a simple organizing construct; group the concept art for a particular character together, or a series of storyboard frames into an ordered group. They can also be used for things like a 3D Model that is composed of a set of meshes, textures, and rigging.

Using groups can simplify managing the relationships that exist between assets and other pieces of context. By placing multiple images in a group, a relationship need only be kept to the top level of the group, for example character then only has to relate to a single top level entity for all of it's concept art, not each individual image. A set of 3D assets may be reused in multiple scenes, each group can be related independently to a scene, or a group representing the 3D model can itself be in multiple groups

---
An Asset that is structurally an Asset Group, with three other Assets as elements of that group.
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



