# PlayerPreferences.Generator (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/antiban/PlayerPreferences.Generator.html

**Package:** Packageorg.tribot.script.sdk.antiban

---

* java.lang.Object
* + org.tribot.script.sdk.antiban.PlayerPreferences.Generator

* Enclosing class:
[PlayerPreferences](PlayerPreferences.html "class in org.tribot.script.sdk.antiban")

---

```
public static class PlayerPreferences.Generator
extends java.lang.Object
```

Class to assist with generating unique player-specific preferences

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `java.util.Random` | `[getRandom](#getRandom())()` | Creates a new `Random` seeded with this seed |
| `long` | `[getSeed](#getSeed())()` | |
| `double` | `[normal](#normal(double,double,double,double))​(double min,
double max,
double mean,
double sd)` | Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation |
| `int` | `[normal](#normal(int,int,int,int))​(int min,
int max,
int mean,
int sd)` | Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation |
| `long` | `[normal](#normal(long,long,long,long))​(long min,
long max,
long mean,
long sd)` | Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation |
| `double` | `[uniform](#uniform(double,double))​(double min,
double max)` | Randomly generates a value uniformly distributed in the range of [min, max] |
| `int` | `[uniform](#uniform(int,int))​(int min,
int max)` | Randomly generates a value uniformly distributed in the range of [min, max] |
| `long` | `[uniform](#uniform(long,long))​(long min,
long max)` | Randomly generates a value uniformly distributed in the range of [min, max] |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### getRandom

```
public java.util.Random getRandom()
```

Creates a new `Random` seeded with this seed

Returns:
a new `Random` seeded with this seed
- #### uniform

```
public int uniform​(int min,
int max)
```

Randomly generates a value uniformly distributed in the range of [min, max]

Parameters:
`min` - the min value
`max` - the max value
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### uniform

```
public long uniform​(long min,
long max)
```

Randomly generates a value uniformly distributed in the range of [min, max]

Parameters:
`min` - the min value
`max` - the max value
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### uniform

```
public double uniform​(double min,
double max)
```

Randomly generates a value uniformly distributed in the range of [min, max]

Parameters:
`min` - the min value
`max` - the max value
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### normal

```
public int normal​(int min,
int max,
int mean,
int sd)
```

Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation

Parameters:
`min` - the min value
`max` - the max value
`mean` - the mean
`sd` - the sd
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### normal

```
public long normal​(long min,
long max,
long mean,
long sd)
```

Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation

Parameters:
`min` - the min value
`max` - the max value
`mean` - the mean
`sd` - the sd
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### normal

```
public double normal​(double min,
double max,
double mean,
double sd)
```

Randomly generates a value normally distributed in the range of [min, max] with the specified mean and standard deviation

Parameters:
`min` - the min value
`max` - the max value
`mean` - the mean
`sd` - the sd
Returns:
a random value in the range of min to max, this value will always be the same given the same seed
- #### getSeed

```
public long getSeed()
```