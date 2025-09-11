# BugReports (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/BugReports.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.BugReports

* ---

```
public class BugReports
extends java.lang.Object
```

Contains utilities related to generating a bug report in the client

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[BugReports.WebhookConfig](BugReports.WebhookConfig.html "class in org.tribot.script.sdk.util")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[BugReports](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[configureWebhooks](#configureWebhooks(org.tribot.script.sdk.util.BugReports.WebhookConfig))​([BugReports.WebhookConfig](BugReports.WebhookConfig.html "class in org.tribot.script.sdk.util") config)` | Configures bug report webhook settings with the specified config |
| `static void` | `[reportException](#reportException(java.lang.Throwable))​(java.lang.Throwable throwable)` | Reports the exception through a discord webhook. |
| `static void` | `[setExtraScriptData](#setExtraScriptData(java.util.function.Supplier))​(java.util.function.Supplier<java.lang.String> extraScriptData)` | Sets the extra script data to be included in a bug report. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### BugReports

```
public BugReports()
```

+ ### Method Detail

- #### configureWebhooks

```
public static void configureWebhooks​(@Nullable
[BugReports.WebhookConfig](BugReports.WebhookConfig.html "class in org.tribot.script.sdk.util") config)
```

Configures bug report webhook settings with the specified config

Parameters:
`config` - the bug report webhook configuration to apply
- #### setExtraScriptData

```
public static void setExtraScriptData​(java.util.function.Supplier<java.lang.String> extraScriptData)
```

Sets the extra script data to be included in a bug report. This could be things like script settings.
This will be in it's own file named script-data.txt

Parameters:
`extraScriptData` - a supplier which gets the extra script data to include with the bug report
- #### reportException

```
public static void reportException​(java.lang.Throwable throwable)
```

Reports the exception through a discord webhook. Note [`must be enabled`](BugReports.WebhookConfig.html#sendOnException).

Parameters:
`throwable` - the throwable to report