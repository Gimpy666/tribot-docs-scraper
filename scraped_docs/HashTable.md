# HashTable (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/HashTable.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>`

---

```
public interface HashTable<T extends [Node](Node.html "interface in net.runelite.api")>
extends [Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>
```

A data structure that uses a hash function to compute an index into an
array of buckets from which node objects can be quickly obtained.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[T](HashTable.html "type parameter in HashTable")` | `[get](#get(long))​(long value)` | Gets a node by its hash value. |

- ### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#forEach(java.util.function.Consumer) "class or interface in java.lang"), [iterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#iterator() "class or interface in java.lang"), [spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#spliterator() "class or interface in java.lang")`

* + ### Method Detail

- #### get

```
[T](HashTable.html "type parameter in HashTable") get​(long value)
```

Gets a node by its hash value.

Parameters:
`value` - the node value
Returns:
the associated node