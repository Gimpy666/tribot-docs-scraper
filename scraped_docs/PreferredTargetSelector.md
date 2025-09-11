# PreferredTargetSelector (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/antiban/PreferredTargetSelector.html

**Package:** Packageorg.tribot.script.sdk.antiban

---

* java.lang.Object
* + org.tribot.script.sdk.antiban.PreferredTargetSelector<T>

* All Implemented Interfaces:
`java.util.Comparator<T>`

---

```
public class PreferredTargetSelector<T extends [Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")>
extends java.lang.Object
implements java.util.Comparator<T>
```

Provides a way to sort game entities in order of "preference" when it comes to interacting with them. Takes into
account mouse position, hovering, "true" distance to the entities, etc. The "lower" the value of the entity, the more
preferred it is.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[PreferredTargetSelector](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[compare](#compare(T,T))​([T](PreferredTargetSelector.html "type parameter in PreferredTargetSelector") target1,
[T](PreferredTargetSelector.html "type parameter in PreferredTargetSelector") target2)` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface java.util.Comparator

`equals, reversed, thenComparing, thenComparing, thenComparing, thenComparingDouble, thenComparingInt, thenComparingLong`

* + ### Constructor Detail

- #### PreferredTargetSelector

```
public PreferredTargetSelector()
```

+ ### Method Detail

- #### compare

```
public int compare​([T](PreferredTargetSelector.html "type parameter in PreferredTargetSelector") target1,
[T](PreferredTargetSelector.html "type parameter in PreferredTargetSelector") target2)
```

Specified by:
`compare` in interface `java.util.Comparator<[T](PreferredTargetSelector.html "type parameter in PreferredTargetSelector") extends [Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")>`