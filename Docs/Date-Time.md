# Date & Time

## Date & Time

A date with optional time stamp related to an entity. Can be used to denote start times, end times, creation times and a multiplicity of other uses.

Dates and time should conform to the ISO 8601 standard

| **Property** | **Type** | **Definition**                              |
| ------------ | -------- | ------------------------------------------- |
| dateTime     | string   | A date and time (2018-11-13T20:20:39+00:00) |
| date         | string   | A date only (2018-11-13)                    |
| time         | string   | A time only (20:20:39+00:00)                |
| creationDate |          |                                             |
| creationTime |          |                                             |
| modifiedDate |          |                                             |
| modifiedTime |          |                                             |
| startDate    |          |                                             |
| endDate      |          |                                             |

*** Should we have separate named terms for year, date, time and dateTime - added complication but covers widest range of use cases.*
** *Need to provide a more extensive list of examples, use of +- for dates prior to year 0(BC).*
** *Best practices around use of local time or UTC*


    date: yyyy-mm-dd
    year: yyyy
    time: hh:mm:ss
    dateTime: yyyy-mm-dd

**(Missing the 8601 'type' designation (PT, T))

## TimeStamp

Unix timestamp (just a number)



## Period of Time

A measurement of time from a fixed starting point

| **Property**       | **Type** | **Definition**                     |
| ------------------ | -------- | ---------------------------------- |
| startTime/end      | string   | A date and time in ISO 8601 format |
|                    |          |                                    |
| startTime/duration |          |                                    |
| duration/endTime   |          |                                    |
|                    |          |                                    |

** *Make use of ISO 8601 duration naming for the unitOfTime, provide examples (Y, M, W, D, H, etc.)*



## Duration Time

A duration of time, some period of time

Durations of time should conform to the ISO 8601 standard


| **Property** | **Type** | **Definition**                        |
| ------------ | -------- | ------------------------------------- |
| durationTime | string   | A duration of time in ISO 8601 format |

*** Need to provide examples*


## Descriptive Time

There are several ways that time or periods in time can be described outside of the literal contexts above.

Many of these relate to the story and script, which may not allows make reference to specific dates and times

| **Property** | **Type** | **Definition**                                               |
| ------------ | -------- | ------------------------------------------------------------ |
| periodOfDay  | string   | Morning, noon, afternoon night                               |
| relativeTime | string   | Later, continuous, 6 months earlier, a long time ago         |
| periodInTime | string   | Ming dynasty, World War II, Jurassic period                  |
| eventInTime  | string   | Hindenburg disaster, World Trade Center Attack, Queen Elizabeth coronation. |

## Timecodes
    SMPTE
    Frame rate (Not sure if this is strictly time)



