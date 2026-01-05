# IterableHashTable (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IterableHashTable.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>`

---

```
public interface IterableHashTable<T extends [Node](Node.html "interface in net.runelite.api")>
extends [Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[T](IterableHashTable.html "type parameter in IterableHashTable")` | `[get](#get(long))​(long hash)` | |
| `void` | `[put](#put(T,long))​([T](IterableHashTable.html "type parameter in IterableHashTable") node,
long hash)` | |

- ### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#forEach(java.util.function.Consumer) "class or interface in java.lang"), [iterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#iterator() "class or interface in java.lang"), [spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#spliterator() "class or interface in java.lang")`

* + ### Method Detail

- #### get

```
[T](IterableHashTable.html "type parameter in IterableHashTable") get​(long hash)
```
- #### put

```
void put​([T](IterableHashTable.html "type parameter in IterableHashTable") node,
long hash)
```