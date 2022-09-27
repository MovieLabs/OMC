# Functional & Structural
The ontology uses a similar paradigm in several of the entity types that separates what we call its functional and structural characteristics. The structural characteristics describe what it's underlying nature, what it is, whereas the functional characteristics describe what or how it is used.

It is useful to separate and think of these separately because sometimes the same thing can be used for more than one purpose, or something with the same use can have more than one form.

In the ontology Assets, Participants and Tasks can have structural and functional characteristics. It is worth noting that it is not always necessary that an entity have both characteristics, sometimes it may just have one. There is also no requirement, or necessity for it to have specific properties, sometimes just declaring its type is enough.

**Structural & Functional Types**
The ontology does not formally declare or impose a set of enumerated values for the naming the types. We are developing a set of preferred or suggested terms, but it is likely that there is such a large and varied set of types for both that it is impractical to cover them all.

Our naming convention adopts dot notation and camel case for terms, allowing for a hierarchical naming structure, for example:

**Structural Types**
```
	digital.image
	analog.image
	digital.movingImage
	digital.structuredDocument
```

**Functional Types**
```
	artwork.storyboard
	artwork.storyboard.frame
	cgi.render
```

There is of course the inevitable discussion as to whether something is a digital image, or an image that is digital, but there is no right answer to this. Establishing an agreed order can certainly help, sometimes it is useful to be able to search on 'digital.image' as a term, so having agreement across systems allows this. However, we also anticipate that these designations can be split in seperate terms (an array) and searched for different combinations.

#### Assets
- A storyboard often starts life as a hand drawn sketch, structurally this is a physical object. However, if you were to digitize it then it becomes a digital object, but it is still functionally the same thing, a storyboard. The structural properties will be different, the physical drawing will have physical location, an address of where it is stored in a particular flat file, whereas the digital object maybe the URL of cloud storage bucket. They both have dimensions, but one maybe in inches the other in pixels.

- Objects like a digital images will share many of the same structural properties, their size, color depth, encoding, etc. However, their functional uses can vary dramatically and are independent of all these attributes, they may textures for a 3D model, concept artwork, technical reference material, continuity photos, etc. They may be more than one of those things, a technical reference photo may become a texture at some point.

#### Participants
- A Participant that is structurally a person might serve several different functional jobs in a production. The Director that also acts, produces or writes for example.

#### Tasks


