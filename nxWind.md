# NeXus 风力修改器使用说明

这份文档只说明风力修改器（nxWind）。重点说明风模拟模式、基础风力和湍流参数分别控制什么，以及哪些参数只在特定模式下生效。

## 风力修改器（nxWind）

风力修改器（nxWind）用于给粒子持续施加一个带方向的风力。它适合做持续吹拂、风道推进、上升气流、横向吹散，或者在规则风力上叠加随机扰动。

风力修改器（nxWind）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建风力修改器（nxWind）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认风力修改器（nxWind）已包含在该列表里。

风力修改器（nxWind）的结果主要由三部分组成：

- 模式（Mode）：决定使用标准（Standard）还是 冯·卡门（Von Kármán）风模型。
- 强度（Strength）和变化（Variation）：控制基础风力大小，以及粒子之间的风力差异。
- 湍流（Turbulence）参数：在主风方向上叠加随机扰动。

### 启用（Enabled）

启用（Enabled）控制整个风力修改器（nxWind）是否参与粒子流程。

关闭后，风力修改器（nxWind）不会继续推动粒子。调试多个力场时，可以先临时关闭它，判断当前粒子偏移是否主要来自风力修改器（nxWind）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制风力修改器（nxWind）的编辑器辅助显示是否可见。

风力修改器（nxWind）会在视口里绘制方向辅助线和旋转标记。关闭这个开关不会影响实际风力计算，只影响编辑时是否显示辅助图形。

### 模式（Mode）

模式（Mode）决定当前风力使用哪种风模拟方式。

插件提供两种模式：

- 标准（Standard）：普通风力模型，适合大多数直接吹拂、推进和扰动场景。
- 冯·卡门（Von Kármán）：使用 冯·卡门（Von Kármán）湍流模型，更强调尺度和摩擦速度的影响。

实用理解：

- 想快速得到稳定、直观的吹风效果，先用标准（Standard）。
- 想让风的扰动更像具有统计结构的大气湍流，再改用 冯·卡门（Von Kármán）。

### 强度（Strength）

强度（Strength）控制主风力的大小。

它决定粒子沿风力修改器（nxWind）方向被推动的基础力度。数值越高，推动越强；如果使用负值，风向会沿相反方向作用。

如果粒子整体移动方向正确但推进不够，先提高强度（Strength）；如果粒子被吹得过快或整体跑偏太远，先降低强度（Strength）。

### 变化（Variation）

变化（Variation）控制不同粒子之间基础风力的随机差异。

数值越高，每个粒子受到的主风强度越不一致；数值越低，整体风力越整齐。它主要用来避免所有粒子像被同一把尺子推着走。

### 湍流（Turbulence）

湍流（Turbulence）是风力修改器（nxWind）的附加参数区，用于给主风叠加随机扰动。

展开后可以调节湍流强度、每轴湍流强度、坐标空间、频率、缩放和摩擦速度。关闭折叠只是不显示这组参数，不会禁用已经设置好的结果。

### 湍流强度（Strength）

湍流强度（Strength）控制叠加在主风上的随机扰动整体有多强。

数值越高，粒子越容易出现抖动、卷动和不规则偏转；数值越低，风看起来越平顺。

### 轴向强度（Axis Strength）

轴向强度（Axis Strength）控制湍流在 X、Y、Z 三个轴向上的强弱分配。

它适合把湍流限制在某些方向上。例如：

- 提高 X、Z，降低 Y：让扰动更多出现在水平面。
- 提高 Y：让风更容易产生上下翻涌。
- 三轴一致：得到更均匀的立体扰动。

### 坐标空间（Coordinate Space）

坐标空间（Coordinate Space）决定湍流计算使用局部（Local）还是世界（World）坐标。

- 局部（Local）：湍流跟随风力修改器对象自身的变换。
- 世界（World）：湍流按世界坐标固定分布，对象移动后会穿过这片湍流。

实用理解：

- 希望风和扰动一起跟着修改器对象移动，用局部（Local）。
- 希望场景里存在一片固定不动的乱流区域，用世界（World）。

### 频率（Frequency）

频率（Frequency）控制湍流变化得有多密、多快。

数值越高，湍流细节越密，粒子路径变化更频繁；数值越低，扰动更缓、更大块。

### 缩放（Scale）

缩放（Scale）控制标准（Standard）模式下湍流图样的尺度。

它只在模式（Mode）为标准（Standard）时显示。数值越大，湍流图样尺度越大；数值越小，扰动图样越细碎。

### 缩放（Scale）

缩放（Scale）控制 冯·卡门（Von Kármán）模式下的湍流长度尺度。

它只在模式（Mode）为 冯·卡门（Von Kármán）时显示。这个值更偏向“涡结构有多大”的含义，而不是普通噪声贴图式的缩放。

### 摩擦速度（Friction Velocity）

摩擦速度（Friction Velocity）控制 冯·卡门（Von Kármán）模式下湍流的摩擦速度。

它只在模式（Mode）为 冯·卡门（Von Kármán）时可编辑。数值越高，通常表示湍流能量更强，风场更活跃。

如果切到标准（Standard）模式，这个参数会变灰，因为标准模式不使用它。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是风力修改器（nxWind）的主设置页。这里主要编辑模式（Mode）、强度（Strength）、变化（Variation）和湍流（Turbulence）参数。

如果你要调整风本身的方向感和扰动感，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）分别用于限制作用对象、用粒子数据驱动参数、按空间范围控制影响。

### 设置页（Section）

设置页（Section）是风力修改器（nxWind）面板顶部的页签切换。它只切换当前正在编辑的设置页。

风力修改器（nxWind）当前常见页签包括：

- 物体属性（Object Properties）：风力本体参数。
- 组（Groups Affected）：限制这个风力只影响指定 nx 组（nxGroup）里的粒子。
- 映射（Mapping）：用粒子数据去驱动风力参数。
- 衰减（Falloff）：用 nx 衰减（nxFalloff）控制风力的空间影响范围。

### 组（Groups Affected）

组（Groups Affected）用于限制风力修改器（nxWind）影响哪些粒子组。

如果这里不添加任何组，风力通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，风力会根据组列表来限制影响对象。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要手动调它。你在列表中选中哪一个组，活动组索引（Active Group Index）就指向哪一个。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器、碰撞体或其他修改器对象不会作为有效组过滤使用。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动风力参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用速度（Speed）驱动强度（Strength），让高速粒子受到更明显的风推动。
- 用生命（Life）驱动湍流强度（Strength），让粒子在生命周期后段更乱。
- 用组（Group）或质量（Mass）区分不同粒子受到的风力强弱。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个风力参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制风力修改器（nxWind）的哪个参数。

对于风力修改器（nxWind），常见目标通常围绕强度（Strength）、变化（Variation）、湍流强度（Strength）、轴向强度（Axis Strength）、频率（Frequency）、缩放（Scale）和摩擦速度（Friction Velocity）这类参数。可选项由当前插件运行时提供，每个界面参数不一定都能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）和文档时间（Document Time）。用什么输入，取决于你想让风力随什么数据变化。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

风力修改器（nxWind）本身不是分层修改器，所以这个参数通常没有实际意义。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

如果映射效果看起来没有变化，先检查粒子数据实际值是否落在范围最小值（Range Min）和范围最大值（Range Max）之间。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供三种模式：

- 钳制（Clamp）：超出范围后停在边界值。
- 循环（Cycle）：超出范围后按区间循环。
- 继续（Continue）：超出范围后继续按趋势外推。

### 衰减（Falloff）

衰减（Falloff）用于按空间范围控制风力修改器（nxWind）的影响强弱。

你可以把一个或多个 nx 衰减（nxFalloff）对象加入列表，让风力只在指定区域里明显生效，或者让边界逐渐变弱。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

每一项都引用一个 nx 衰减（nxFalloff）对象，用来调制风力修改器（nxWind）的最终结果。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前选中的衰减对象。

普通用户通常不需要手动修改它。你在衰减对象（Falloff Objects）列表中选中哪一项，活动衰减索引（Active Falloff Index）就对应哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把 nx 衰减（nxFalloff）对象加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里引用的具体 nx 衰减（nxFalloff）对象。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制当前这一个衰减对象是否参与调制。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定当前衰减对象怎样混入风力修改器（nxWind）的最终结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

数值越高，这个衰减对象对风力结果的调制越明显。
