# Depictions&Portrayals

# Depictions & Portrayals

Depictions are the mechanism used to relate narrative concepts to their production counterparts. The narrative elements that are identified during script breakdown later become production Assets. We need a way to maintain the connections of these Assets back to their Narrative counterparts and the script. 

A Portrayal is a special type of depiction used for Characters.

To represent a Depiction, we use a technique called reification. This technique allows us to bundle up a set of relationships into its own entity and use it as its own thing. The following example illustrates how complex relationships between the narrative elements and their production assets can be created.

It is typical that a Character in a work is depicted (more precisely, portrayed) by an actor. In the ontology, this is done by a Participant that represents the Person in that Role.

![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696282552313_Depiction-1.svg)


However, it is often the case that Characters are depicted by more than one actor; maybe there is a stunt double, or voiceover artist, or a CG model created for special effects. Below we show multiple Depictions of the same character .

![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696362195346_Depiction-2.svg)


Each Depiction will relate to other parts of the production in different ways: the stunt double depiction will only be required in some production scenes, the actor and stunt double will have different wardrobe items, a CG model will be related to CG versions of the props, while the actors will use physical props. To allow for this level of complexity Depictions, like other entities also often need Context.

The diagram below shows how a Depictions and Contexts can be used to describe complex scenarios.

- A Narrative Object(prop) and Narrative Wardrobe are Depicted by physical Assets and a Character is Portrayed by a Participant.
- The prop and wardrobe are related to the Depiction of the Character (through a Context)
- The Character Depiction is also related to the prop and wardrobe through its own Context, which also relates it to a Production Scene. This illustrates how we can combine and use Contexts to create specific or shared relationships to other entities such as scene 10.
- Additionally, each of the assets can carry their own being relation to scene 10.
![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696009803399_Depiction-3.svg)




![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696019344785_Depiction-4.svg)


If this Depiction was also used in another scene, but with a different costume we could create a different Context to represent that.

The next two diagrams show the same Character with a different scenario. The Character is used in two different ProductionScenes, but with a different prop in each scene. The first diagram shows the relationships stemming from the Narrative components and linking them to the ProductionScenes, the second diagram shows the opposite direction, how the ProductionScenes relate to the Narrative components.


- The Character has two Contexts, each with the ProductionScene and Prop usedIn that scene.
![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696029282258_Depiction-5.svg)

- Each ProductionScene has a Context that relates it to the prop specific to the scene, and the shared Character.
![](https://paper-attachments.dropboxusercontent.com/s_80F16C5C3731528E8E363193930AF18C01B8D82F3B6FB51670247F41859EB9EF_1696029303234_Depiction-6.svg)


