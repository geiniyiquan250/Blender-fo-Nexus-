# NeXus 避让修改器使用说明

这份文档只说明避让修改器（nxAvoid）。重点说明避让对象列表怎样定义检测对象，以及粒子靠近对象时可以改变方向、冻结或死亡。

## 避让修改器（nxAvoid）

避让修改器（nxAvoid）用于让已有粒子根据指定对象进行避让。它通过对象（Objects）列表接收网格（Mesh）或曲线（Curve）对象，并为每个对象设置检测距离、随机变化、散射角度、外壳范围和厚度。

避让修改器（nxAvoid）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建避让修改器（nxAvoid）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认避让修改器（nxAvoid）已包含在该列表里。

常见使用流程：

- 创建发射器（nxEmitter），让场景里先有粒子来源。
- 创建避让修改器（nxAvoid）。
- 在对象（Objects）列表里添加一个网格或曲线对象。
- 用在检测到时（On Detection）决定粒子接近对象后的处理方式。
- 调整检测距离（Detection Distance）、变化（Variation）、散射（Scatter）、对象外壳（Object Shell）和厚度（Thickness）。

### 启用（Enabled）

启用（Enabled）控制整个避让修改器（nxAvoid）是否参与粒子流程。

关闭后，避让修改器（nxAvoid）不会继续处理粒子和避让对象之间的检测。调试多个力类或碰撞类效果时，可以临时关闭它，判断当前运动变化是否来自避让修改器（nxAvoid）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制避让修改器（nxAvoid）的编辑器辅助显示是否可见。

避让修改器（nxAvoid）当前没有专门的视口绘制图形；这个开关主要属于通用修改器显示控制，不直接改变避让计算结果。

### 对象（Objects）

对象（Objects）列表用于添加粒子需要避让或检测的对象。

这个列表只接受网格（Mesh）和曲线（Curve）对象。每个列表项都可以单独启用或关闭，并拥有自己的在检测到时（On Detection）、检测距离（Detection Distance）、变化（Variation）、散射（Scatter）、对象外壳（Object Shell）和厚度（Thickness）设置。

如果对象（Objects）列表为空，避让修改器（nxAvoid）没有可用于检测的目标对象。

### 活动索引（Active Index）

活动索引（Active Index）记录当前正在编辑对象（Objects）列表里的哪一项。

普通用户通常不需要直接修改它。你在对象（Objects）列表里选中哪一项，活动索引（Active Index）就对应哪一项。

### 添加对象（Add Object）

添加对象（Add Object）用于把一个场景对象加入对象（Objects）列表。

它只接受网格（Mesh）和曲线（Curve）对象。添加后，需要继续检查该列表项的在检测到时（On Detection）和避让范围参数。

### 添加集合（Add Collection）

添加集合（Add Collection）用于把一个集合里的对象批量加入对象（Objects）列表。

只有集合里的网格（Mesh）和曲线（Curve）对象会作为有效避让对象。这个入口适合一次添加多个障碍物、轨迹曲线或检测目标。

### 避让对象（Avoid Object）

避让对象（Avoid Object）是列表项里真正用于检测的对象。

它可以是网格（Mesh）或曲线（Curve）。避让修改器（nxAvoid）会把对象（Objects）列表同步为检测数据，粒子靠近这些对象时按照当前列表项的参数处理。

### 避让项启用（Avoid Object Enabled）

避让项启用（Avoid Object Enabled）控制当前列表项是否参与避让检测。

关闭某一项后，该对象不会作为避让对象使用。它适合临时比较不同对象对粒子运动或状态变化的影响。

### 在检测到时（On Detection）

在检测到时（On Detection）决定粒子接近当前避让对象后的处理方式。

插件提供三种模式：

- 改变方向（Change Direction）：粒子改变方向来避让对象。
- 冻结（Freeze）：粒子接近对象时冻结。
- 死亡（Die）：粒子接近对象时死亡。

如果你想让粒子绕开障碍物，先使用改变方向（Change Direction）。如果你想把接近对象的粒子停住或清除，再使用冻结（Freeze）或死亡（Die）。

### 检测距离（Detection Distance）

检测距离（Detection Distance）控制粒子距离对象多近时开始触发避让检测。

数值越大，粒子会在离对象更远的位置开始响应；数值越小，粒子会更靠近对象后才响应。这个值使用场景长度单位，并会按插件的单位缩放同步。

如果粒子太早转向、冻结或死亡，降低检测距离（Detection Distance）。如果粒子已经穿过或贴近对象才有反应，提高检测距离（Detection Distance）。

### 变化（Variation）

变化（Variation）给检测距离增加随机变化。

它以百分比形式设置，用于让不同粒子不在完全相同的距离上触发检测。数值越高，触发距离的差异越明显；数值为 0 时，所有粒子按当前检测距离（Detection Distance）使用同一基础范围。

### 散射（Scatter）

散射（Scatter）控制避让时的角度散射。

它使用角度值。数值越高，粒子改变方向时越容易产生更分散的方向变化；数值为 0 时，避让方向更集中。

散射（Scatter）主要适合在检测到时（On Detection）为改变方向（Change Direction）的避让行为。冻结（Freeze）和死亡（Die）更关注触发检测后的状态处理。

### 对象外壳（Object Shell）

对象外壳（Object Shell）控制对象周围避让外壳的倍率。

默认值为 1。提高它会扩大围绕对象的计算外壳，让粒子更早或更宽地感知对象范围。它和检测距离（Detection Distance）、厚度（Thickness）一起决定避让检测区的大小。

### 厚度（Thickness）

厚度（Thickness）控制避让检测区域的厚度。

数值越大，检测区域越厚；数值越小，检测区域越薄。它使用场景长度单位，并会按插件的单位缩放同步。

如果粒子只有在非常贴近对象时才触发，或者曲线对象的检测范围太窄，可以提高厚度（Thickness）。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是避让修改器（nxAvoid）的主设置页。这里主要编辑对象（Objects）列表和每个避让对象的检测参数。

如果你要调整粒子避让哪些对象、靠近对象后发生什么、检测范围有多大，通常先回到物体属性（Object Properties）页。

### 设置页（Section）

设置页（Section）是避让修改器（nxAvoid）面板顶部的页签切换。它只切换当前正在编辑的设置页。

避让修改器（nxAvoid）常见页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制避让修改器（nxAvoid）影响哪些粒子组。

如果这里不添加任何组，避让通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，避让效果会根据组列表来限制影响对象。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要直接修改它。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器或其他修改器对象不会作为有效组过滤使用。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动避让参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用年龄（Age）驱动检测距离（Detection Distance），让粒子出生后逐渐更容易触发避让。
- 用速度（Speed）驱动厚度（Thickness）或检测距离（Detection Distance），让高速粒子更早响应避让对象。
- 用 ID（ID）或组（Group）驱动变化（Variation），制造不同粒子的触发差异。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个避让参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制避让修改器（nxAvoid）的哪个参数。

对于避让修改器（nxAvoid），常见目标通常围绕检测距离（Detection Distance）、变化（Variation）、散射（Scatter）、对象外壳（Object Shell）和厚度（Thickness）。可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）、组（Group）和 ID（ID）。选择粒子数据（Particle Data）后，要配合范围最小值（Range Min）和范围最大值（Range Max）设定输入区间。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

避让修改器（nxAvoid）本身不是内部多层修改器，所以这个字段通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

如果映射没有变化，先检查粒子数据实际值是否落在范围最小值（Range Min）和范围最大值（Range Max）之间。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供钳制（Clamp）、循环（Cycle）和继续（Continue）三种模式。

### 衰减（Falloff）

衰减（Falloff）用于用空间衰减对象控制避让修改器（nxAvoid）的影响范围。

如果你想控制“哪里会触发避让”，用衰减（Falloff）；如果想控制“哪些组受避让影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前避让修改器（nxAvoid）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象或填写该项目自己的参数。

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

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于树状列表里的层级调整。普通对象列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于树状列表里的层级调整。普通对象列表通常不需要使用它。
