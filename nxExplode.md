# NeXus 爆炸修改器使用说明

这份文档只说明爆炸修改器（nxExplode）。它的重点是说明爆炸效果何时触发、粒子从哪里向外爆开、爆炸速度怎样设置，以及显示里的视口辅助图标怎样控制。

## 爆炸修改器（nxExplode）

爆炸修改器（nxExplode）用于把已有粒子从指定中心向外推开，形成爆开、喷散或瞬间外扩的运动效果。

爆炸修改器（nxExplode）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建爆炸修改器（nxExplode）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认爆炸修改器（nxExplode）已包含在该列表里。

爆炸修改器（nxExplode）的核心设置分成三类：

- 触发时机：决定爆炸是一直生效，还是在场景时间或粒子年龄到达指定条件后触发。
- 爆炸方向来源：决定粒子是从粒子群自身的质量中心向外爆开，还是从爆炸修改器对象的位置向外爆开。
- 速度设置：决定爆炸向外推开的速度、速度随机变化和随机种子。

### 启用（Enabled）

启用（Enabled）控制整个爆炸修改器（nxExplode）是否参与粒子流程。

关闭后，爆炸修改器（nxExplode）不会继续把粒子向外推开。调试时可以临时关闭它，确认当前外扩运动是否来自爆炸修改器（nxExplode）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制爆炸修改器（nxExplode）的视口辅助图形是否显示。

爆炸修改器（nxExplode）会在视口中绘制一个圆形和向外箭头，用来提示爆炸中心与向外方向。这个开关只影响编辑器显示，不直接改变粒子运动结果。

### 时序（Timing）

时序（Timing）决定爆炸效果何时触发。

可用模式包括：

- 始终开启（Always On）：爆炸效果一直处于活动状态。
- 在场景时间触发（Trigger at Scene Time）：按场景时间与时间（Time）的比较结果触发。
- 在粒子年龄触发（Trigger at Particle Age）：按粒子自身年龄与时间（Time）的比较结果触发。

当时序（Timing）为始终开启（Always On）时，时序模式（Timing Mode）和时间（Time）在界面中会变为不可编辑，因为此时不需要额外的时间条件。

### 时序模式（Timing Mode）

时序模式（Timing Mode）决定时序（Timing）使用场景时间或粒子年龄时，怎样和时间（Time）做比较。

可用模式包括：

- 等于（Equals）：时间正好等于指定值时触发。
- 大于或等于（Equals or Greater Than）：时间达到或超过指定值后触发。
- 小于或等于（Equals or Less Than）：时间小于或等于指定值时触发。

这个参数只在时序（Timing）不是始终开启（Always On）时可编辑。

### 时间（Time）

时间（Time）是爆炸触发条件使用的时间值。

当时序（Timing）为在场景时间触发（Trigger at Scene Time）时，它表示场景时间条件。当时序（Timing）为在粒子年龄触发（Trigger at Particle Age）时，它表示粒子年龄条件。

这个参数只在时序（Timing）不是始终开启（Always On）时可编辑。

### 背向爆炸（Explode Away From）

背向爆炸（Explode Away From）决定粒子从哪个中心向外爆开。

可用模式包括：

- 粒子质量中心（Particle Mass Center）：粒子从当前粒子群的质量中心向外爆开。
- 此修改器（This Modifier）：粒子从爆炸修改器（nxExplode）对象的位置向外爆开。

如果需要把粒子从一个明确的空间位置向外推开，通常选择此修改器（This Modifier），并移动爆炸修改器对象的位置。

### 速度（Speed）

速度（Speed）控制爆炸向外推开粒子的基础速度。

数值越高，粒子被推出得越快。速度变化（Variation）不能高于速度（Speed）；当速度（Speed）降低到小于当前速度变化（Variation）时，插件会把速度变化限制到不超过速度本身。

### 变化（Variation）

速度变化（Variation）给爆炸速度加入随机差异。

数值越高，不同粒子的爆炸速度差异越明显。它适合用来避免所有粒子以完全相同速度向外飞出。

### 种子（Seed）

随机种子（Seed）控制速度变化（Variation）产生随机结果的种子。

在速度变化（Variation）大于 0 时，修改随机种子（Seed）可以改变粒子之间的随机速度分布，同时保持整体设置不变。

### 必要时取消粘滞（Unstick if Necessary）

必要时取消粘滞（Unstick if Necessary）控制爆炸时是否解除已经粘附在表面的粒子。

开启后，爆炸效果可以把需要参与爆炸的粘附粒子从表面状态中释放出来。关闭后，已经处于粘附状态的粒子可能继续受粘附状态限制。

### 仅在开始时设置速度（Set Speed at Start Only）

仅在开始时设置速度（Set Speed at Start Only）控制爆炸速度是否只在效果开始时写入一次。

开启后，爆炸修改器（nxExplode）会在爆炸开始时设置速度，后续不会持续重设同一爆炸速度。关闭后，爆炸修改器（nxExplode）可以在效果活动期间继续按当前设置影响速度。

---

## 显示

### 显示（Display）

显示（Display）是爆炸修改器（nxExplode）的额外页签，用于控制视口辅助图形。

这里主要控制视口可见（Visible in Editor）和图标大小（Icon Size）。显示不会改变爆炸物理结果，只影响编辑器里的辅助显示。

### 视口显示（Viewport Display）

视口显示（Viewport Display）控制显示中的视口辅助设置是否展开。

展开后可以看到图标大小（Icon Size）等显示参数。

### 图标大小（Icon Size）

图标大小（Icon Size）控制爆炸修改器（nxExplode）在视口中绘制的圆形和向外箭头大小。

数值越大，辅助图形越大。它只影响编辑器显示，不改变爆炸范围、速度或触发条件。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是爆炸修改器（nxExplode）的主设置页。这里编辑触发时机、爆炸远离点、爆炸速度、速度变化、随机种子和爆炸行为选项。

如果你要控制粒子什么时候爆开、从哪里爆开、以多快速度爆开，通常先回到物体属性（Object Properties）页。

### 设置页（Section）

设置页（Section）是爆炸修改器（nxExplode）面板顶部的页签切换。它只切换当前正在编辑的设置页。

爆炸修改器（nxExplode）常见页签包括物体属性（Object Properties）、显示（Display）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制爆炸修改器（nxExplode）影响哪些粒子组。

如果这里不添加任何组，爆炸通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，爆炸效果会根据组列表来限制影响对象。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要直接修改它。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

关闭后，这一条组引用会暂时失效，但不会从列表中删除。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动爆炸参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用年龄（Age）驱动速度（Speed）或速度变化（Variation），让不同生命阶段的粒子爆开强度不同。
- 用 ID（ID）或随机相关数据驱动速度变化，让爆炸分布更不规则。
- 用组（Group）或其他粒子数据控制是否更强地爆开某类粒子。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个爆炸参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制这一条映射层是否参与计算。

关闭后，这一条映射规则会保留在列表里，但不会继续驱动目标参数。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制爆炸修改器（nxExplode）的哪个参数。

对于爆炸修改器（nxExplode），常见目标包括时间（Time）、速度（Speed）、速度变化（Variation）、随机种子（Seed）或其他由插件运行时提供的可映射参数。可选项以实际界面为准。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定映射层读取哪一种粒子数据作为输入。

常见输入包括粒子年龄、速度、ID、距离、组或其他粒子属性。具体可用项由当前插件运行时提供。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定映射作用到哪一个层或目标槽位。

爆炸修改器（nxExplode）没有像方向修改器那样的爆炸层列表；这里通常保持默认，除非当前界面提供了明确可选的目标层。

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

衰减（Falloff）用于用空间衰减对象控制爆炸修改器（nxExplode）的影响范围。

如果你想控制“哪里发生爆炸”，用衰减（Falloff）；如果想控制“哪些组受爆炸影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前爆炸修改器（nxExplode）。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。

关闭后，这一条衰减引用会暂时失效，但仍保留在衰减对象（Falloff Objects）列表中。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象对爆炸影响范围的作用越明显；值越低，它的影响越弱。

---

## 和其他修改器的联动

爆炸修改器（nxExplode）需要作用到已有粒子才会生效。最常见的粒子来源是发射器（nxEmitter）。

如果看不到爆炸效果，按这个顺序检查：

- 发射器（nxEmitter）是否正在产生粒子。
- 当前粒子流程是否包含爆炸修改器（nxExplode）；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，需要确认列表里包含它。
- 爆炸修改器（nxExplode）的启用（Enabled）是否开启。
- 时序（Timing）是否等待场景时间或粒子年龄达到条件。
- 速度（Speed）是否为 0，或速度变化（Variation）是否太低。
- 组（Groups Affected）或衰减（Falloff）是否限制了作用对象或范围。

如果场景里同时有重力修改器（nxGravity）、阻力修改器（nxDrag）、湍流修改器（nxTurbulence）或其他力类修改器，它们会和爆炸一起影响粒子运动。判断爆炸是否有效时，可以临时关闭其他力类修改器，只保留爆炸修改器（nxExplode）做对比。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与爆炸计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象、类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。它通常只移除列表引用，不等于删除场景里的对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）会开关当前列表项是否参与当前列表的作用。它只影响这一项，不等于关闭整个修改器。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表，把当前项目向更深一层移动。普通平铺列表不会使用这个按钮。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表，把当前项目向外提升一层。
