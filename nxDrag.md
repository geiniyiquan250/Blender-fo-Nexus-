# NeXus 阻力修改器使用说明

这份文档只说明阻力修改器（nxDrag）。它的重点是说明介质密度、阻力系数和强度倍增器怎样共同影响粒子速度，以及哪些数值只有在自定义模式下才可编辑。

## 阻力修改器（nxDrag）

阻力修改器（nxDrag）用于给已有粒子施加空气阻力或液体阻力，让粒子运动逐渐被介质拖慢。它适合模拟空气中的飞散碎片、水中的颗粒、浓稠液体里的慢速运动，或者让高速粒子更快失去速度。

阻力修改器（nxDrag）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建阻力修改器（nxDrag）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认阻力修改器（nxDrag）已包含在该列表里。

阻力效果主要由三类参数决定：

- 密度（Density）：粒子穿过的介质有多“重”。空气密度低，水和水银这类液体密度高。
- 阻力系数（Drag Coefficient）：粒子外形有多容易被介质拖慢。流线型物体系数低，方块、碎片、直立人体这类外形系数高。
- 强度倍增器（Strength Multiplier）：整体放大或缩小当前阻力效果。

### 启用（Enabled）

启用（Enabled）控制整个阻力修改器（nxDrag）是否参与粒子流程。

关闭后，阻力修改器（nxDrag）不会继续拖慢粒子。调试时可以临时关闭它，观察粒子是否仍然快速减速；如果关闭后粒子明显飞得更远，说明当前速度衰减主要来自阻力修改器（nxDrag）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制阻力修改器（nxDrag）的编辑器辅助显示是否可见。

阻力修改器（nxDrag）当前没有专门的视口绘制图形；这个开关主要属于通用修改器显示控制，不改变阻力计算结果。

### 密度（Density）

密度（Density）选择粒子穿过的介质类型。

密度越高，阻力越容易变强，粒子越容易被拖慢。真空（Vacuum）对应 0 密度，通常不会产生介质阻力；空气（Air）适合普通飞散效果；水（Water）、海水（Sea Water）、甘油（Glycerine）、汞（Mercury）这类高密度介质会让粒子更快失去速度。

插件提供这些密度预设：

- 真空（Vacuum）：没有介质密度，适合排除阻力影响。
- 空气（Air）：普通空气环境，默认值。
- 二氧化碳（Carbon Dioxide）、氦气（Helium）、氪气（Krypton）、氙（Xenon）：不同气体密度。
- 液化丙烷（Propane Liquified）、石脑油（Naphtha）、汽油（Gasoline / Petrol）、乙醇（Ethanol）：常见液体或燃料类介质。
- 水（Water）、海水（Sea Water）、重水（Heavy Water）：水相关介质。
- 甘油（Glycerine）、糖蜜（Treacle）、溴（Bromine）、汞（Mercury）：更高密度或更强拖慢感的介质。
- 自定义（Custom）：允许手动编辑密度值（Density Value）。

如果只是想让粒子稍微慢下来，通常从空气（Air）开始，再调强度倍增器（Strength Multiplier）。如果要模拟水下或浓稠介质，先选水（Water）或甘油（Glycerine），再降低强度倍增器，避免粒子瞬间停住。

### 密度值（Density Value）

密度值（Density Value）是当前密度（Density）对应的实际数值。

当密度（Density）选择预设时，插件会自动把密度值（Density Value）更新为对应预设数值，界面里这个字段不可手动编辑。当密度（Density）选择自定义（Custom）时，密度值（Density Value）才可编辑。

实用理解：

- 想完全自己控制介质密度，先把密度（Density）改成自定义（Custom）。
- 数值越高，粒子越容易被阻力拖慢。
- 如果粒子几乎不动，先降低密度值（Density Value）或强度倍增器（Strength Multiplier）。

### 阻力系数（Drag Coefficient）

阻力系数（Drag Coefficient）选择粒子的外形阻力预设。

阻力系数越高，表示外形越容易被介质拖住；阻力系数越低，表示外形更流线、更容易穿过介质。这个参数适合用来区分“同样在空气里，为什么碎片、方块、球体、飞行器减速程度不同”。

插件提供这些阻力系数预设：

- 海豚（Dolphin）、导弹（Missile）、战斗机（Fighter Aircraft）：流线型强，阻力系数低。
- 轿车（Saloon Car）、鸟（Bird）、球体（Sphere）：常见中等阻力外形。
- 立方体（Cube）、自行车（Bicycle）、自行车与骑手（Bicycle and Rider）、直立人体（Human Upright）、摩托车与骑手（Motorcycle and Rider）、矩形框（Rectangular Box）：更容易被空气拖慢。
- xpShatter 碎片（xpShatter Fragments）：适合碎片类粒子。
- 自定义（Custom）：允许手动编辑阻力系数值（Drag Coeff. Value）。

如果你用粒子表现碎石、玻璃片、破碎块，通常可以从 xpShatter 碎片（xpShatter Fragments）或立方体（Cube）开始。如果粒子像小球、泡泡或圆形颗粒，可以从球体（Sphere）开始。

### 阻力系数值（Drag Coeff. Value）

阻力系数值（Drag Coeff. Value）是当前阻力系数（Drag Coefficient）对应的实际数值。

当阻力系数（Drag Coefficient）选择预设时，插件会自动把阻力系数值（Drag Coeff. Value）更新为对应预设数值，界面里这个字段不可手动编辑。当阻力系数（Drag Coefficient）选择自定义（Custom）时，阻力系数值（Drag Coeff. Value）才可编辑。

实用理解：

- 数值越低，粒子越容易保持速度。
- 数值越高，粒子越容易被拖慢。
- 如果密度（Density）已经正确，但减速程度仍不符合外形感觉，再调整阻力系数值（Drag Coeff. Value）。

### 强度倍增器（Strength Multiplier）

强度倍增器（Strength Multiplier）控制整个阻力效果的总体强度。

它会在密度（Density）和阻力系数（Drag Coefficient）的基础上做整体缩放。默认值是 100%，表示按当前密度和阻力系数组合正常工作。降低它可以保留当前介质和外形设定，但让阻力更轻；提高它可以让阻力更明显。

常见用法：

- 粒子飞得太远、速度衰减太慢，提高强度倍增器（Strength Multiplier）。
- 粒子刚出生就几乎停住，降低强度倍增器（Strength Multiplier）。
- 想保留“水中”或“碎片”这种语义预设，但效果太强，优先调强度倍增器（Strength Multiplier），不要立刻改密度（Density）或阻力系数（Drag Coefficient）。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是阻力修改器（nxDrag）的主设置页。这里主要编辑密度（Density）、密度值（Density Value）、阻力系数（Drag Coefficient）、阻力系数值（Drag Coeff. Value）和强度倍增器（Strength Multiplier）。

如果你要调整粒子被介质拖慢的程度，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）分别用于限制作用对象、用粒子数据驱动参数、按空间范围控制影响。

### 设置页（Section）

设置页（Section）是阻力修改器（nxDrag）面板顶部的页签切换。它只切换当前正在编辑的设置页。

阻力修改器（nxDrag）当前常见页签包括：

- 物体属性（Object Properties）：阻力本体参数。
- 组（Groups Affected）：限制这个阻力只影响指定 nx 组（nxGroup）里的粒子。
- 映射（Mapping）：用粒子数据去驱动阻力参数。
- 衰减（Falloff）：用nx 衰减（nxFalloff）控制阻力的空间影响范围。

### 组（Groups Affected）

组（Groups Affected）用于限制阻力修改器（nxDrag）影响哪些粒子组。

如果这里不添加任何组，阻力通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，阻力会根据组列表来限制影响对象。

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

映射（Mapping）用于让粒子数据动态驱动阻力参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用速度（Speed）驱动强度倍增器（Strength Multiplier），让高速粒子受到更明显的阻力。
- 用年龄（Age）驱动强度倍增器（Strength Multiplier），让粒子出生后逐渐被拖慢。
- 用质量（Mass）或半径（Radius）驱动阻力，让大小不同的粒子减速程度不同。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个阻力参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制阻力修改器（nxDrag）的哪个参数。

对于阻力修改器（nxDrag），常见目标通常围绕密度值（Density Value）、阻力系数值（Drag Coeff. Value）和强度倍增器（Strength Multiplier）这类可被数据驱动的参数。可选项由当前插件运行时提供，每个界面参数不一定都能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括：

- 年龄（Age）：按粒子出生后的时间变化。
- 生命（Life）：按粒子生命周期比例变化。
- 速度（Speed）：按粒子当前速度变化。
- 半径（Radius）：按粒子大小变化。
- 质量（Mass）：按粒子质量变化。
- 颜色（Color / Color R / Color G / Color B）：按粒子颜色或颜色通道变化。
- 距离（Distance）：按粒子记录的距离数据变化。
- 文档时间（Document Time）：按当前场景时间变化。
- 组（Group）：按粒子所在组变化。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

阻力修改器（nxDrag）本身不是分层修改器，所以这个参数通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

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

衰减（Falloff）用于用空间衰减对象控制阻力修改器（nxDrag）的影响范围。

如果你想控制“哪里有阻力”，用衰减（Falloff）；如果想控制“哪些组受阻力影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前阻力修改器（nxDrag）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象对阻力范围的影响越明显；值越低，它的影响越弱。

---

## 和其他修改器的联动

阻力修改器（nxDrag）需要作用到已有粒子才会生效。最常见的粒子来源是发射器（nxEmitter）。

如果看不到阻力效果，按这个顺序检查：

- 发射器（nxEmitter）是否正在产生粒子。
- 当前粒子流程是否包含阻力修改器（nxDrag）；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，需要确认列表里包含它。
- 阻力修改器（nxDrag）的启用（Enabled）是否开启。
- 密度（Density）是否选择了真空（Vacuum），或密度值（Density Value）是否为 0。
- 强度倍增器（Strength Multiplier）是否太低。
- 组（Groups Affected）或衰减（Falloff）是否限制了作用范围。

如果场景里同时有重力修改器（nxGravity）、湍流修改器（nxTurbulence）、吸引修改器（nxAttract）或其他力类修改器，它们会和阻力一起影响粒子运动。判断阻力是否有效时，可以临时关闭其他力类修改器，只保留阻力修改器（nxDrag）做对比。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

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
