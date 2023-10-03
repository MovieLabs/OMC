## Analogue & Digital
Data has to be stored somewhere. In the ontology, analog data is bound to the media on which it has been recorded. Something shot on film is essentially bound and carried on the physical film it recorded on.

Digital data is a little different, in that it is often moved or copied to different devices. Something recorded on the camera Mag may be moved onto some sort of hard drive, then later onto long term tape. Digital data has the distinct advantage that it does not degrade in quality when it transferred across storage devices. 

For this reason, the ontology allows for digital data to optionally to specify a 'carrier', which is the piece of Infrastructure being used to hold the data. This might be something like a thumb-drive, DVD, LTO tape, etc. This separate piece of infrastructure has its own identifier and specifics  like its physical location, or who has custody of it, are part of its structural properties. For data stored natively in a cloud environment location is tracked through a URL; in many cases you don't really know (or care) exactly what the carrier itself is or the exact physical location.

### Carrier
The documentation says the carrier is an Asset and not Infrastructure, isn't the data the Asset not what it is stored on. Data always has a carrier, it's just not always worth explicitly naming it, data in the cloud is still on a hard drive.

An asset that is structurally digital with a carrier
```
identifier
	identifierValue: A1
structuralCharacteristics
	structuralType: digital.image
	identifier
		identifierValue: E1
	carri[Asset](..%2FJSON-Schema%2Fomc%2FAsset)er: Infrastructure
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

