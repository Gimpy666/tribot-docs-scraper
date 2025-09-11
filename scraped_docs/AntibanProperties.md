# AntibanProperties (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/antiban/AntibanProperties.html

**Package:** Packageorg.tribot.script.sdk.antiban

---

* java.lang.Object
* + org.tribot.script.sdk.antiban.AntibanProperties

* ---

```
public class AntibanProperties
extends java.lang.Object
```

Generates and stores values based on the currently logged in Runescape account, which are used in the API as modifiers
to ensure every account has slightly different behavior

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[AntibanProperties.Props](AntibanProperties.Props.html "class in org.tribot.script.sdk.antiban")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[AntibanProperties](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [AntibanProperties.Props](AntibanProperties.Props.html "class in org.tribot.script.sdk.antiban")` | `[getPropsForCurrentChar](#getPropsForCurrentChar())()` | Gets the antiban properties for the current account. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### AntibanProperties

```
public AntibanProperties()
```

+ ### Method Detail

- #### getPropsForCurrentChar

```
public static [AntibanProperties.Props](AntibanProperties.Props.html "class in org.tribot.script.sdk.antiban") getPropsForCurrentChar()
```

Gets the antiban properties for the current account. If logged out and no previous props generated, returns props
for "unknown".

This method will automatically detect account changes (logging into another account) and regenerate props if
necessary, so there is no need to cache the return of this.