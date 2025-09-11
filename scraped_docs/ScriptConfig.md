# ScriptConfig (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/script/ScriptConfig.html

**Package:** Packageorg.tribot.script.sdk.script

---

* java.lang.Object
* + org.tribot.script.sdk.script.ScriptConfig

* ---

```
public class ScriptConfig
extends java.lang.Object
```

Defines a set of configuration options for a script. These are "meta" configurations that the Tribot client will use
to determine how to execute the script.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ScriptConfig](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[isBreakHandlerEnabled](#isBreakHandlerEnabled())()` | When this setting is enabled, Tribot will pause the script to logout and break in accordance with the break settings
of the user. |
| `boolean` | `[isRandomsAndLoginHandlerEnabled](#isRandomsAndLoginHandlerEnabled())()` | When this setting is enabled, Tribot will run the Randoms Handler thread, which will pause the script to login,
solve randoms, and enter the bank pin. |
| `void` | `[setBreakHandlerEnabled](#setBreakHandlerEnabled(boolean))​(boolean isBreakHandlerEnabled)` | When this setting is enabled, Tribot will pause the script to logout and break in accordance with the break settings
of the user. |
| `void` | `[setRandomsAndLoginHandlerEnabled](#setRandomsAndLoginHandlerEnabled(boolean))​(boolean isRandomsAndLoginHandlerEnabled)` | When this setting is enabled, Tribot will run the Randoms Handler thread, which will pause the script to login,
solve randoms, and enter the bank pin. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ScriptConfig

```
public ScriptConfig()
```

+ ### Method Detail

- #### isBreakHandlerEnabled

```
public boolean isBreakHandlerEnabled()
```

When this setting is enabled, Tribot will pause the script to logout and break in accordance with the break settings
of the user.
- #### setBreakHandlerEnabled

```
public void setBreakHandlerEnabled​(boolean isBreakHandlerEnabled)
```

When this setting is enabled, Tribot will pause the script to logout and break in accordance with the break settings
of the user.
- #### isRandomsAndLoginHandlerEnabled

```
public boolean isRandomsAndLoginHandlerEnabled()
```

When this setting is enabled, Tribot will run the Randoms Handler thread, which will pause the script to login,
solve randoms, and enter the bank pin.
- #### setRandomsAndLoginHandlerEnabled

```
public void setRandomsAndLoginHandlerEnabled​(boolean isRandomsAndLoginHandlerEnabled)
```

When this setting is enabled, Tribot will run the Randoms Handler thread, which will pause the script to login,
solve randoms, and enter the bank pin.