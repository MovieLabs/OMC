## Utility Types





### Frames per Second



### Timecode

Normative reference SMPTE xxxxxx



### Monetary Value

Monetary amounts are represented as a value and the currency of that value. The currency use the ISO 4217 specification.



| Attribute     | Type   | Description                                       |
| ------------- | ------ | ------------------------------------------------- |
| monetaryValue | number | The value                                         |
| currency      | string | An ISO 4217 3 letter code indicating the currency |

*This allows for fractional amounts, do we need a provision for using commas in the value field as separators as this is sometimes used in place of decimal point*



### Linear Distance ( imperial / metric )

- D indicates a measurement of linear distance

**Metric**

- km indicates the number of kilometers
- m indicates the number of meters
- cm indicates the number of centimeters
- mm indicates the number of millimeters

**Imperial**

- mi indicates the number of miles
- ft indicates the number of feet 
- in indicates the number of inches (how to do fractions)



**

``` 
[
	{"height": "D4km05m03cm12mm"}, // 4 kilimeters, 5 meters, 3 centimeters and 12 milimeters
	{"length": "D12ft"} // 12 feet (12')
	{"width": "D6in"} // 6 inches (6")
	{"distance": "D4mi"} // 4 miles
]
```

Consider:

- DM - indicates a distance in metric units
- DI - indicates a distance in imperial units

This helps simplify validation a little and ensuring different systems aren't intermingled



** Should we capitalize these (would be in line with ISO time then, but less like normal use)

Imperial and Metric systems of measurements must not be combined


http://xml.coverpages.org/OlkenMeasurementUnitsSyntax.html#baseunits

https://www.w3schools.com/cssref/css_units.asp





### Weight ( imperial / Metric )

- W indicates this is measurement of weight

**Metric**

- kg indicates wight in kilograms
- g indicates weight in grams 

**Imperial**

- lb indicates weight in pounds
- oz indicates weight in ounces



**Example**

``` 
[
	{"weight": "W9kg04g"}, // 9 kilos, 4 grams
	{"weight": "W2lb04oz"} // 2 pounds 4 ounces
]
```

Consider:

- WM indicates a metric measurement of weight
- WI indicates an imperial measurement of weight





#### Pixels
Aspect ratio
Color depth



### Color Space


#### Encoding

Audio/Video/3D




### Structural characteristics


Encoding ( images / moving images )







