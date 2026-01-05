# FriendContainer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/FriendContainer.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[NameableContainer](NameableContainer.html "interface in net.runelite.api")<[Friend](Friend.html "interface in net.runelite.api")>`

---

```
public interface FriendContainer
extends [NameableContainer](NameableContainer.html "interface in net.runelite.api")<[Friend](Friend.html "interface in net.runelite.api")>
```

A nameable container of friends

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Deque](Deque.html "interface in net.runelite.api")<[PendingLogin](PendingLogin.html "interface in net.runelite.api")>` | `[getPendingLogins](#getPendingLogins())()` | Get the recent logins/logouts of friends from the last few seconds |

- ### Methods inherited from interface net.runelite.api.[NameableContainer](NameableContainer.html "interface in net.runelite.api")

`[findByName](NameableContainer.html#findByName(java.lang.String)), [getCount](NameableContainer.html#getCount()), [getMembers](NameableContainer.html#getMembers()), [getSize](NameableContainer.html#getSize())`

* + ### Method Detail

- #### getPendingLogins

```
[Deque](Deque.html "interface in net.runelite.api")<[PendingLogin](PendingLogin.html "interface in net.runelite.api")> getPendingLogins()
```

Get the recent logins/logouts of friends from the last few seconds

Returns: