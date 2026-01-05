# Deque (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Deque.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>`

---

```
public interface Deque<T>
extends [Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")<T>
```

A doubly linked list

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[addLast](#addLast(T))​([T](Deque.html "type parameter in Deque") t)` | Add a new element to the end of the deque |
| `void` | `[clear](#clear())()` | clear the deque |

- ### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true "class or interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#forEach(java.util.function.Consumer) "class or interface in java.lang"), [iterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#iterator() "class or interface in java.lang"), [spliterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Iterable.html?is-external=true#spliterator() "class or interface in java.lang")`

* + ### Method Detail

- #### addLast

```
void addLast​([T](Deque.html "type parameter in Deque") t)
```

Add a new element to the end of the deque

Parameters:
`t` - the element
- #### clear

```
void clear()
```

clear the deque