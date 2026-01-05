# IndexedObjectSet (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IndexedObjectSet.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>`

---

```
public interface IndexedObjectSet<T>
extends [Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")` | `[byIndex](#byIndex(int))​(int index)` | |
| `default [Spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Spliterator.html?is-external=true "class or interface in java.util")<[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")>` | `[spliterator](#spliterator())()` | |
| `default [Stream](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/Stream.html?is-external=true "class or interface in java.util.stream")<[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")>` | `[stream](#stream())()` | |

- ### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#forEach(java.util.function.Consumer) "class or interface in java.lang"), [iterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#iterator() "class or interface in java.lang")`

* + ### Method Detail

- #### byIndex

```
[T](IndexedObjectSet.html "type parameter in IndexedObjectSet") byIndex​(int index)
```
- #### stream

```
default [Stream](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/Stream.html?is-external=true "class or interface in java.util.stream")<[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")> stream()
```
- #### spliterator

```
default [Spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Spliterator.html?is-external=true "class or interface in java.util")<[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")> spliterator()
```

Specified by:
`[spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#spliterator() "class or interface in java.lang")` in interface `[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<[T](IndexedObjectSet.html "type parameter in IndexedObjectSet")>`