# NameableContainer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/NameableContainer.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[FriendContainer](FriendContainer.html "interface in net.runelite.api")`, `[FriendsChatManager](FriendsChatManager.html "interface in net.runelite.api")`

---

```
public interface NameableContainer<T extends [Nameable](Nameable.html "interface in net.runelite.api")>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[T](NameableContainer.html "type parameter in NameableContainer")` | `[findByName](#findByName(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Find a nameable by name |
| `int` | `[getCount](#getCount())()` | Get the number of members in this container |
| `[T](NameableContainer.html "type parameter in NameableContainer")[]` | `[getMembers](#getMembers())()` | Get the members in this container |
| `int` | `[getSize](#getSize())()` | Get the maximum size of the container. |

* + ### Method Detail

- #### getCount

```
int getCount()
```

Get the number of members in this container

Returns:
- #### getSize

```
int getSize()
```

Get the maximum size of the container.

Returns:
- #### getMembers

```
[T](NameableContainer.html "type parameter in NameableContainer")[] getMembers()
```

Get the members in this container

Returns:
- #### findByName

```
[T](NameableContainer.html "type parameter in NameableContainer") findByName​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Find a nameable by name

Parameters:
`name` - the name
Returns: