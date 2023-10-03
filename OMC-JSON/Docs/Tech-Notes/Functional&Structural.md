# Functional & Structural
The ontology uses a similar concept for several entity types that separates what we call an entity's functional and structural characteristics. Structural characteristics describe its underlying nature, what it is, and the functional characteristics describe how it is used. It is often useful separate these two concepts because sometimes the same thing can be used for more than one purpose, or something with the same functional use can have more than one form.

In the ontology Assets, Participants, and Tasks each have structural and functional characteristics. It is worth noting that it is not always necessary that an entity have both characteristics; sometimes it may just have one. There is also no requirement or necessity for it to have specific properties - sometimes just declaring its type is enough.

**Structural & Functional Types**
The ontology does not formally declare or impose a set of enumerated values for naming the functional and structural types, there are potentially a lot of these and they will evolve over time or may be specific to a particular production. However, in the interests of standardization we are developing a set of preferred or suggested terms for many types of things that are commonly used.

In the formal ontology, the specific structural or functional entities are classes and sub-classes. In JSON we do not have classes, so express this through a type property of the structural or functional object. The naming convention uses dot notation and camel case for terms, allowing for a hierarchical naming structure.

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

There is of course the inevitable discussion as to whether something is a digital image, or an image that is digital, but there is no right answer to this. Establishing an agreed order can certainly help; it can be useful to be able to search on 'digital.image' as a term, so having agreement across systems allows this. However, we also anticipate that these designations can be split into separate terms (an array) and searched for different combinations.

Our conventions for the types go from more general on the left of the string to more specific towards the right of the string.

## Assets
- A storyboard often starts life as a hand drawn sketch. Structurally this is a physical object. However, if you were to digitize this it becomes a digital object, but it is still functionally the same thing; a storyboard. However, the structural properties will be different, e.g., the physical drawing may have physical location or dimensions in inches, whereas the digital object is more likely held in cloud storage and measurements are in pixels. 

- Objects like a digital images will share many of the same structural properties, such as size, color depth, and encoding. However, their functional uses can vary dramatically and are independent of these attributes. They may textures for a 3D model, concept artwork, technical reference material, continuity photos, etc. A single item may be more than one of those things in different parts of the workflow: a technical reference photo may become a texture at some point.

See [Assets](Assets.md) for amore detailed examples and descriptions

## Participants
- A Participant that is structurally a person can have several different functional jobs in a production, such as a Director who also acts, produces or writes.

## Tasks
- Tasks are currently in development.

## Infrastructure
- Infrastructure is currently in development

