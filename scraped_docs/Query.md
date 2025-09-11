# Query (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/Query.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` - the entity type to query
`QueryType` - the query type

All Known Subinterfaces:
`[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")`, `[GraphicObjectQuery](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")`, `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface Query<EntityType,​QueryType extends Query<EntityType,​QueryType>>
```

An interface for querying entities.

Each [`Query`](Query.html "interface in org.tribot.script.sdk.query") instance should only be executed once.

Queries are modified in-place when calling methods such as [`filter(Predicate)`](#filter(java.util.function.Predicate)).
Therefore the expression `query.filter(x -> true) == query` will always be true.

No methods will return `null` unless otherwise indicated within that method's documentation.

Queries are lazily evaluated.

* + ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `static [BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")` | `[bank](#bank())()` | Creates a new [`BankQuery`](BankQuery.html "class in org.tribot.script.sdk.query") |
| `default int` | `[count](#count())()` | Executes this query and gets the number of results |
| `static [EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")` | `[equipment](#equipment())()` | Creates a new [`EquipmentQuery`](EquipmentQuery.html "class in org.tribot.script.sdk.query") |
| `[QueryType](Query.html "type parameter in Query")` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<[EntityType](Query.html "type parameter in Query")> filter)` | Applies the specified filter to this query. |
| `default java.util.Optional<[EntityType](Query.html "type parameter in Query")>` | `[findFirst](#findFirst())()` | Executes this query, and gets the first result if it exists |
| `default java.util.Optional<[EntityType](Query.html "type parameter in Query")>` | `[findRandom](#findRandom())()` | Executes this query, and selects a random result based on a uniform distribution |
| `default void` | `[forEach](#forEach(java.util.function.Consumer))​(java.util.function.Consumer<[EntityType](Query.html "type parameter in Query")> consumer)` | Executes this query and passes each result to the specified consumer |
| `static [GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")` | `[gameObjects](#gameObjects())()` | Creates a new [`GameObjectQuery`](GameObjectQuery.html "class in org.tribot.script.sdk.query") |
| `static [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[grandExchangeOffers](#grandExchangeOffers())()` | Creates a new [`GrandExchangeOfferQuery`](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") |
| `static [GraphicObjectQuery](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")` | `[graphicObjects](#graphicObjects())()` | Creates a new [`GraphicObjectQuery`](GraphicObjectQuery.html "class in org.tribot.script.sdk.query") |
| `static [GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")` | `[groundItems](#groundItems())()` | Creates a new [`GroundItemQuery`](GroundItemQuery.html "class in org.tribot.script.sdk.query") |
| `static [InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")` | `[inventory](#inventory())()` | Creates a new [`InventoryQuery`](InventoryQuery.html "class in org.tribot.script.sdk.query") |
| `default boolean` | `[isAny](#isAny())()` | Executes this query and checks if any result exists |
| `static [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[itemDefinitions](#itemDefinitions())()` | Creates a new [`ItemDefinitionQuery`](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") |
| `static [NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")` | `[npcs](#npcs())()` | Creates a new [`NpcQuery`](NpcQuery.html "class in org.tribot.script.sdk.query") |
| `static [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[players](#players())()` | Creates a new [`PlayerQuery`](PlayerQuery.html "class in org.tribot.script.sdk.query") |
| `static [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[projectiles](#projectiles())()` | Creates a new [`ProjectileQuery`](ProjectileQuery.html "class in org.tribot.script.sdk.query") |
| `static [ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")` | `[shop](#shop())()` | Creates a new [`ShopItemQuery`](ShopItemQuery.html "class in org.tribot.script.sdk.query") |
| `[QueryType](Query.html "type parameter in Query")` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<[EntityType](Query.html "type parameter in Query")> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<[EntityType](Query.html "type parameter in Query")>` | `[stream](#stream())()` | Returns this query as a stream. |
| `static [TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")` | `[tiles](#tiles())()` | Creates a new [`TileQuery`](TileQuery.html "class in org.tribot.script.sdk.query") |
| `default java.util.List<[EntityType](Query.html "type parameter in Query")>` | `[toList](#toList())()` | Executes this query, and gets the results |
| `static [TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")` | `[trade](#trade())()` | Creates a new [`TradeQuery`](TradeQuery.html "class in org.tribot.script.sdk.query") |
| `static [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[widgets](#widgets())()` | Creates a new [`WidgetQuery`](WidgetQuery.html "class in org.tribot.script.sdk.query") |
| `static [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[worlds](#worlds())()` | Creates a new [`WorldQuery`](WorldQuery.html "class in org.tribot.script.sdk.query") |

* + ### Method Detail

- #### filter

```
[QueryType](Query.html "type parameter in Query") filter​(java.util.function.Predicate<[EntityType](Query.html "type parameter in Query")> filter)
```

Applies the specified filter to this query.
This query is **not** executed at this point.

Parameters:
`filter` - the filter to apply to this query
Returns:
this query
- #### sorted

```
[QueryType](Query.html "type parameter in Query") sorted​(java.util.Comparator<[EntityType](Query.html "type parameter in Query")> comparator)
```

Orders the query by the specified comparator.
This query is **not** executed at this point.

Parameters:
`comparator` - the comparator to order the query by
Returns:
this query
- #### stream

```
java.util.stream.Stream<[EntityType](Query.html "type parameter in Query")> stream()
```

Returns this query as a stream.
This query is **not** executed at this point **but** it will be executed whenever the stream executes a terminal operation.

Returns:
this query as a stream
- #### toList

```
default java.util.List<[EntityType](Query.html "type parameter in Query")> toList()
```

Executes this query, and gets the results

Returns:
the results of this query
- #### findFirst

```
default java.util.Optional<[EntityType](Query.html "type parameter in Query")> findFirst()
```

Executes this query, and gets the first result if it exists

Returns:
the first result of this query, or an empty optional if no entity found
- #### findRandom

```
default java.util.Optional<[EntityType](Query.html "type parameter in Query")> findRandom()
```

Executes this query, and selects a random result based on a uniform distribution

Returns:
a random result of this query, or an empty optional if no entities found
- #### isAny

```
default boolean isAny()
```

Executes this query and checks if any result exists

Returns:
true if any result exists, false otherwise
- #### count

```
default int count()
```

Executes this query and gets the number of results

Returns:
the number of results
- #### forEach

```
default void forEach​(java.util.function.Consumer<[EntityType](Query.html "type parameter in Query")> consumer)
```

Executes this query and passes each result to the specified consumer

Parameters:
`consumer` - the consumer to accept each result
- #### widgets

```
static [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") widgets()
```

Creates a new [`WidgetQuery`](WidgetQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`WidgetQuery`](WidgetQuery.html "class in org.tribot.script.sdk.query")
- #### shop

```
static [ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query") shop()
```

Creates a new [`ShopItemQuery`](ShopItemQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`ShopItemQuery`](ShopItemQuery.html "class in org.tribot.script.sdk.query")
- #### players

```
static [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") players()
```

Creates a new [`PlayerQuery`](PlayerQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`PlayerQuery`](PlayerQuery.html "class in org.tribot.script.sdk.query")
- #### gameObjects

```
static [GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query") gameObjects()
```

Creates a new [`GameObjectQuery`](GameObjectQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`GameObjectQuery`](GameObjectQuery.html "class in org.tribot.script.sdk.query")
- #### groundItems

```
static [GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query") groundItems()
```

Creates a new [`GroundItemQuery`](GroundItemQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`GroundItemQuery`](GroundItemQuery.html "class in org.tribot.script.sdk.query")
- #### npcs

```
static [NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query") npcs()
```

Creates a new [`NpcQuery`](NpcQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`NpcQuery`](NpcQuery.html "class in org.tribot.script.sdk.query")
- #### projectiles

```
static [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") projectiles()
```

Creates a new [`ProjectileQuery`](ProjectileQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`ProjectileQuery`](ProjectileQuery.html "class in org.tribot.script.sdk.query")
- #### equipment

```
static [EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query") equipment()
```

Creates a new [`EquipmentQuery`](EquipmentQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`EquipmentQuery`](EquipmentQuery.html "class in org.tribot.script.sdk.query")
- #### inventory

```
static [InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query") inventory()
```

Creates a new [`InventoryQuery`](InventoryQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`InventoryQuery`](InventoryQuery.html "class in org.tribot.script.sdk.query")
- #### bank

```
static [BankQuery](BankQuery.html "class in org.tribot.script.sdk.query") bank()
```

Creates a new [`BankQuery`](BankQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`BankQuery`](BankQuery.html "class in org.tribot.script.sdk.query")
- #### graphicObjects

```
static [GraphicObjectQuery](GraphicObjectQuery.html "class in org.tribot.script.sdk.query") graphicObjects()
```

Creates a new [`GraphicObjectQuery`](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`GraphicObjectQuery`](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")
- #### worlds

```
static [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") worlds()
```

Creates a new [`WorldQuery`](WorldQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`WorldQuery`](WorldQuery.html "class in org.tribot.script.sdk.query")
- #### grandExchangeOffers

```
static [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") grandExchangeOffers()
```

Creates a new [`GrandExchangeOfferQuery`](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`GrandExchangeOfferQuery`](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")
- #### trade

```
static [TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query") trade()
```

Creates a new [`TradeQuery`](TradeQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`TradeQuery`](TradeQuery.html "class in org.tribot.script.sdk.query")
- #### tiles

```
static [TileQuery](TileQuery.html "class in org.tribot.script.sdk.query") tiles()
```

Creates a new [`TileQuery`](TileQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`TileQuery`](TileQuery.html "class in org.tribot.script.sdk.query")
- #### itemDefinitions

```
static [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") itemDefinitions()
```

Creates a new [`ItemDefinitionQuery`](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")

Returns:
a new [`ItemDefinitionQuery`](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")