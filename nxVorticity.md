# NeXus 涡量修改器使用说明

这份文档只说明涡量修改器（nxVorticity）。重点说明它怎样在局部范围内给粒子增加旋转趋势，以及半径、强度和力限制分别控制什么。

## 涡量修改器（nxVorticity）

涡量修改器（nxVorticity）用于给粒子施加涡度约束力，让局部粒子运动更容易形成旋转、卷曲和回旋感。它适合做烟雾卷动、碎片旋拧、水流回转，或者给已经在运动的粒子补一层更明显的旋涡趋势。

涡量修改器（nxVorticity）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建涡量修改器（nxVorticity）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认涡量修改器（nxVorticity）已包含在该列表里。

涡量修改器（nxVorticity）可以简单理解成：

- 半径（Radius）：多大范围内的粒子会互相形成旋转趋势。
- 强度（Strength）：旋转趋势有多强。
- 力限制（Force Limit）：给这股旋转力设置上限，避免力过猛。

### 启用（Enabled）

启用（Enabled）控制整个涡量修改器（nxVorticity）是否参与粒子流程。

关闭后，涡量修改器（nxVorticity）不会再给粒子增加旋转和卷曲趋势。调试时可以先关闭它，对比粒子是否明显少了回旋感。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制涡量修改器（nxVorticity）的编辑器辅助显示是否可见。

涡量修改器（nxVorticity）当前没有专门的视口绘制图形；这个开关主要属于通用修改器显示控制，不改变实际涡量计算结果。

### 半径（Radius）

半径（Radius）控制涡量效果影响周围粒子的范围。

数值越高，参与形成旋转趋势的邻域越大，旋转结构更宽、更大块；数值越低，影响范围更局部，更容易形成细碎的小旋流。

实用理解：

- 想要更细密的局部卷曲，降低半径（Radius）。
- 想让更大范围的粒子一起形成回转，增大半径（Radius）。

### 强度（Strength）

强度（Strength）控制涡量效果的力度。

数值越高，粒子越容易出现明显的回旋、扭动和卷曲；数值越低，旋转趋势越轻，只是稍微打破直线运动。

如果粒子已经有速度，但运动看起来太直、太“平”，通常先提高强度（Strength）。如果轨迹开始乱成一团，再把它降下来。

### 力限制（Force Limit）

力限制（Force Limit）控制涡量效果最多可以施加多大的力。

它相当于给旋转推力设一个上限。这样即使强度（Strength）较高，单次施加的力也不会无限增大，更容易避免粒子突然爆开、抖动过猛或出现不稳定的甩动。

实用理解：

- 想保留明显旋转感，但避免局部发疯，降低力限制（Force Limit）。
- 想让强度（Strength）真正完全发挥出来，提高力限制（Force Limit）。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是涡量修改器（nxVorticity）的主设置页。这里主要编辑半径（Radius）、强度（Strength）和力限制（Force Limit）。

如果你要调整旋涡范围和旋转力度，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）分别用于限制作用对象、用粒子数据驱动参数、按空间范围控制影响。

### 设置页（Section）

设置页（Section）是涡量修改器（nxVorticity）面板顶部的页签切换。它只切换当前正在编辑的设置页。

涡量修改器（nxVorticity）当前常见页签包括：

- 物体属性（Object Properties）：涡量本体参数。
- 组（Groups Affected）：限制这个涡量只影响指定 nx 组（nxGroup）里的粒子。
- 映射（Mapping）：用粒子数据去驱动涡量参数。
- 衰减（Falloff）：用 nx 衰减（nxFalloff）控制涡量的空间影响范围。

### 组（Groups Affected）

组（Groups Affected）用于限制涡量修改器（nxVorticity）影响哪些粒子组。

如果这里不添加任何组，涡量通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，涡量会根据组列表来限制影响对象。

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

映射（Mapping）用于让粒子数据动态驱动涡量参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用速度（Speed）驱动强度（Strength），让高速粒子卷得更明显。
- 用生命（Life）驱动半径（Radius），让粒子在后期形成更大范围旋转。
- 用年龄（Age）或文档时间（Document Time）逐渐提高力限制（Force Limit）。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个涡量参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制涡量修改器（nxVorticity）的哪个参数。

对于涡量修改器（nxVorticity），常见目标通常围绕半径（Radius）、强度（Strength）和力限制（Force Limit）这类参数。可选项由当前插件运行时提供，每个界面参数不一定都能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）和文档时间（Document Time）。用什么输入，取决于你想让涡量随什么数据变化。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

涡量修改器（nxVorticity）本身不是分层修改器，所以这个参数通常没有实际意义。

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

衰减（Falloff）用于按空间范围控制涡量修改器（nxVorticity）的影响强弱。

你可以把一个或多个 nx 衰减（nxFalloff）对象加入列表，让涡量只在指定区域里明显生效，或者让边界逐渐变弱。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

每一项都引用一个 nx 衰减（nxFalloff）对象，用来调制涡量修改器（nxVorticity）的最终结果。

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

衰减混合（Falloff Blend）决定当前衰减对象怎样混入涡量修改器（nxVorticity）的最终结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

数值越高，这个衰减对象对涡量结果的调制越明显。
