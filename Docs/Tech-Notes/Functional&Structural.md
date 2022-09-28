# Functional & Structural
The ontology uses a common model for several of the entity types that separates what we call its functional and structural characteristics. The structural characteristics describe its underlying nature, what it is, and the functional characteristics describe what or how it is used.

It is useful to treat these as separate because sometimes the same thing can be used for more than one purpose, or something with the same use can have more than one form.

In the ontology Assets, Participants and Tasks can have structural and functional characteristics. It is worth noting that it is not always necessary that an entity have both characteristics; sometimes it may just have one. There is also no requirement, or necessity for it to have specific properties - sometimes just declaring its type is enough.

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

There is of course the inevitable discussion as to whether something is a digital image, or an image that is digital, but there is no right answer to this. Establishing an agreed order can certainly help; it can be useful to be able to search on 'digital.image' as a term, so having agreement across systems allows this. However, we also anticipate that these designations can be split in separate terms (an array) and searched for different combinations.

Our conventions for the types go from more general on the right of the string to more specific towards the left of the string.

#### Assets
- A storyboard often starts life as a hand drawn sketch. Structurally this is a physical object. However, if you were to digitize it then it becomes a digital object, but it is still functionally the same thing: a storyboard. The structural properties will be different, e.g., the physical drawing may have physical location or dimensions in inches, whereas the digital object might contain the URL of cloud storage bucket and measurements in pixels. 

- Objects like a digital images will share many of the same structural properties, such as size, color depth, and encoding. However, their functional uses can vary dramatically and are independent of all these attributes. They may textures for a 3D model, concept artwork, technical reference material, continuity photos, an so on. A single item may be more than one of those things in different parts of the workflow: a technical reference photo may become a texture at some point.

#### Participants
- A Participant that is structurally a person can have several different functional jobs in a production, such as a Director who also acts, produces or writes.

#### Tasks
- Tasks are currently in development.

#### Infrastructure
- Infrastructure is currently in development


