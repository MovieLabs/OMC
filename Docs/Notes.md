# Notes

### Sequence

For the Celtx data we have some sequences made up of storyboards.

- Is this an Editorial Sequence (editorial often use or start timelines from storyboards)
- What goes into Sequence Chronology Descriptor (without it becoming an EDL).



### Shot

Do we need a narrative shot and production shot?



### Asset groups

Compound Assets



### Asset Structural & Functional Characteristics

Talk about the structuralType & functionalType, we need to decide what our naming structure for this, is it type based or entity based. If entity based we end up needing to define all of these, which seems like a potentially large task.

If we are using just a string type, we may still want to break things up because the structural attributes are very different depending on the asset



Which set of Structural Types do we consider our base set 

What are we going select as a set of attributes for structural characteristics

- Which types (image, moving image)
- Which attributes

What shall we call 'unstructured data'



Start to review the documentation, what do we even want for this?



Are the structural and functional type entities, or just attributes of their entity.

Assets:

- Structural - Many will likely be unique, but 8M OCF's may have the same StructuralCharacteristics, do you want those to be an entity?
- Functional - Probably lots of similarity
  - Is Context part of Functional







### Creative Work

- How do we want to create this: Celtx, by hand
- What does this connect to

### Script

- What is the asset here, a PDF?
- Do we want to do anything with the script, not sure how to point to things in it as the data structure from Celtx is complex.



### Participants

We have no real 'source' for the Participants at the moment, there may be something in Celtx but there are some ways of getting that out of Okta as well.

- We could create participants initially out of Okta, Celtx uses an email as it's unique id, so we could tie this to a createdBy field.



## Tools

Do we need a way to enter data, edit data, enrich existing data?

Do we need a way to view data, beyond a view into a database or graphql front end

