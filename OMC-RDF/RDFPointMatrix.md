## Points and Matrices in RDF

RDF does not have any built-in way to describe points and matrices. There are several ways of implementing them and OMC uses these mechanisms. They are not ideal, but are sufficient for data interchange of points and matrices. Applications that use this data to 'do math' shoudl convert them to an appropriate internal form

### Point

`omc:Point` is a generic point class. it has properties `omc:hasXCoord` and `omc:hasYCoord`

`omc:Point2` and `omc:Point3` are subclasses of `omc:Point`

`omc:Point3` has the additional property `omc:hasZCoord`

### Matrix

`omc:TwoDimMatrix` is the superclass for `omc:Matrix33` and `omc:Matrix44`. It has the property `omc:hasTwoDimMatrixElement` the range of which is `omc:TwoDimMatrixElement`

`omc:TwoDimMatrixElement` has three properties

- `omc:hasRow` (an integer)
- `omc:hasColumn` (an integer)
- `omc:hasMatrixElementValue` (integer or decmal)

So given an instance M of omc:Matrix33 where the matrix has values

1,2,3

2,4,8

3,6,11

the pseudocode for describing the value in the third column of the second row is

`M a omc:Matrix33`

`M omc:hasTwoDimMatrixElement E23`

`E23 a omc:TwoDimMatrixElement`

`E23 omc:hasRowIndex 2`

`E23 omc:hasColumnIndex 3`

`E23 omc:hasMatrixElementValue 6`

There is currently no way for the schema to enforce the arrnagement and number of elements of a omc:Matrix33 or a omc:Matrix44; applications that import matrices in RDF can do any additional checking they need. 