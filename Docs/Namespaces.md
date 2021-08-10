# Namespaces

Namespaces are used to create logical and manageable collections of related entities and properties.

A namespace is unique unto itself, meaning any definitions and structural characteristics only apply within that namespace. However, things from other namespaces can be incorporated and included by reference, thereby extending the original. We typically refer to this a Connected Ontology.

The individual components inside a namespace are typically referred to by their qualified name, e.g., ``mmc:Slate``. The use of the prefix helps to identify and distinguish names of properties, especially as sometimes the same name is used in different namespaces, sometimes with different meaning.

| Prefix | Name                     | URI                        |
| ------ | ------------------------ | -------------------------- |
| mmc    | MovieLabs Media Creation | https://mmc.movielabs.com/ |
| mcw    | MovieLabs Creative Works | https://mcw.movielabs.com/ |



```json
{
    "mmc": "https://mmc.movielabs.com#",
    "mcw": "https://mcw.movielabs.com#"
}
```



mmc.movielabs.com/vocabulary/

[^]: *This includes all vocab terms, ontology and non, as well as other ontology terms, i.e. creative works*

mmc.movielabs.com/ontology/

mmc.movielabs.com/schema/







