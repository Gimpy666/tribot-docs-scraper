# GrandExchange.CreateOfferConfig (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GrandExchange.CreateOfferConfig.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.GrandExchange.CreateOfferConfig

* Enclosing class:
[GrandExchange](GrandExchange.html "class in org.tribot.script.sdk")

---

```
public static class GrandExchange.CreateOfferConfig
extends java.lang.Object
```

Describes a configuration for a new grand exchange offer.

Each of the following config requirements must be met:

A type must be specified.

A price adjustment or a price must be specified.

A quantity must be specified.

An item name or an item id must be specified.

Custom search text (only used for buying) is completely optional. A sensible default will be used if one is not provided.

A specific slot is completely optional. A sensible default will be used if one is not provided.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[builder](#builder())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### builder

```
public static [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") builder()
```