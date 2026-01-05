# GrandExchangeOfferChanged (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/GrandExchangeOfferChanged.html

**Package:** Packagenet.runelite.api.events

**Description:** When the client initially logs in, this event is called for all grand
 exchange slots with theGrandExchangeOfferState.EMPTYstate,
 regardless of whether any slots have offers. Once the exchange is
 in...

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.GrandExchangeOfferChanged

* ---

```
public class GrandExchangeOfferChanged
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event where a [`GrandExchangeOffer`](../GrandExchangeOffer.html "interface in net.runelite.api") has been updated with
new information.

When the client initially logs in, this event is called for all grand
exchange slots with the [`GrandExchangeOfferState.EMPTY`](../GrandExchangeOfferState.html#EMPTY) state,
regardless of whether any slots have offers. Once the exchange is
initialized, the client then updates any offers with items as it
receives information from the server.

See [`GrandExchangeOfferState`](../GrandExchangeOfferState.html "enum in net.runelite.api") for potential states an offer
can change into.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[GrandExchangeOfferChanged](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `[GrandExchangeOffer](../GrandExchangeOffer.html "interface in net.runelite.api")` | `[getOffer](#getOffer())()` | The offer that has been modified. |
| `int` | `[getSlot](#getSlot())()` | The index value of the slot. |
| `int` | `[hashCode](#hashCode())()` | |
| `void` | `[setOffer](#setOffer(net.runelite.api.GrandExchangeOffer))​([GrandExchangeOffer](../GrandExchangeOffer.html "interface in net.runelite.api") offer)` | The offer that has been modified. |
| `void` | `[setSlot](#setSlot(int))​(int slot)` | The index value of the slot. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### GrandExchangeOfferChanged

```
public GrandExchangeOfferChanged()
```

+ ### Method Detail

- #### getOffer

```
public [GrandExchangeOffer](../GrandExchangeOffer.html "interface in net.runelite.api") getOffer()
```

The offer that has been modified.
- #### getSlot

```
public int getSlot()
```

The index value of the slot.
- #### setOffer

```
public void setOffer​([GrandExchangeOffer](../GrandExchangeOffer.html "interface in net.runelite.api") offer)
```

The offer that has been modified.
- #### setSlot

```
public void setSlot​(int slot)
```

The index value of the slot.
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### canEqual

```
protected boolean canEqual​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)
```
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`