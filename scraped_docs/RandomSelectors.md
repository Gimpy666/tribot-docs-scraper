# RandomSelectors (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/RandomSelectors.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.RandomSelectors

* ---

```
public class RandomSelectors
extends java.lang.Object
```

Contains [`ResultSelector`](ResultSelector.html "interface in org.tribot.script.sdk.util")'s to be used with a `Stream` as a collection operation.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[RandomSelectors](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T>` | `[scaledSd](#scaledSd(double))​(double sdPercent)` | Creates a result selector that randomly selects an element where the element index is selected with the formula: |
| `static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T>` | `[scaledSd](#scaledSd(double,double))​(double meanPercent,
double sdPercent)` | Creates a result selector that randomly selects an element where the element index is selected with the formula: |
| `static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T>` | `[uniform](#uniform())()` | Creates a result selector that randomly selects an element using a uniform distribution |
| `static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T>` | `[weighted](#weighted(java.util.function.ToDoubleFunction))​(java.util.function.ToDoubleFunction<T> weightExtractor)` | Creates a result selector that randomly selects an element where each element is given a specific weight based on the weight extractor function. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### RandomSelectors

```
public RandomSelectors()
```

+ ### Method Detail

- #### uniform

```
public static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T> uniform()
```

Creates a result selector that randomly selects an element using a uniform distribution

Type Parameters:
`T` - the result type
Returns:
a result selector that randomly selects an element using a uniform distribution
- #### weighted

```
public static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T> weighted​(java.util.function.ToDoubleFunction<T> weightExtractor)
```

Creates a result selector that randomly selects an element where each element is given a specific weight based on the weight extractor function.
The higher a weight, the more likely that element is to be chosen. The weights are all relative to each other. If one element has twice the weight of another, it's twice as likely to be chosen.

Type Parameters:
`T` - the result type
Parameters:
`weightExtractor` - the weight extraction algorithm
Returns:
a result selector that randomly selects an element where each element is given a specific weight based on the weight extractor function
- #### scaledSd

```
public static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T> scaledSd​(double sdPercent)
```

Creates a result selector that randomly selects an element where the element index is selected with the formula:

```

var resultIndex = randomSd(0, list.size() - 1, 0, sdPercent * list.size())

```

where randomSd generates a random number from a normal distribution with the parameters min/max/mean/sd

Type Parameters:
`T` - the result type
Parameters:
`sdPercent` - the scaled sd value to use when selecting an element (will use `list.size() * sdPercent` as the actual sd parameter)
Returns:
a result selector that randomly selects based on a normal distribution
- #### scaledSd

```
public static <T> [ResultSelector](ResultSelector.html "interface in org.tribot.script.sdk.util")<T> scaledSd​(double meanPercent,
double sdPercent)
```

Creates a result selector that randomly selects an element where the element index is selected with the formula:

```

var resultIndex = randomSd(0, list.size() - 1, meanPercent * (list.size() - 1), sdPercent * list.size())

```

where randomSd generates a random number from a normal distribution with the parameters min/max/mean/sd

Type Parameters:
`T` - the result type
Parameters:
`meanPercent` - the scaled sd value to use when selecting an element (will use `(list.size() - 1) * sdPercent` as the actual sd parameter)
`sdPercent` - the scaled sd value to use when selecting an element (will use `list.size() * sdPercent` as the actual sd parameter)
Returns:
a result selector that randomly selects based on a normal distribution