# NeXus 群聚修改器使用说明

这份文档只说明群聚修改器（nxFlock）。它用于让粒子按群体行为运动，例如内聚、分离、对齐、混沌、蜂拥，以及对目标或几何体作出反应。

## 群聚修改器（nxFlock）

群聚修改器（nxFlock）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建群聚修改器（nxFlock）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认群聚修改器（nxFlock）已包含在该列表里。

创建群聚修改器（nxFlock）时，插件会自动添加默认行为：内聚（Cohesion）、分离（Separation）、对齐（Alignment）和混沌（Chaos）。

### 启用（Enabled）

启用（Enabled）控制整个群聚修改器（nxFlock）是否参与粒子流程。

关闭后，群聚行为、反应器和几何避让都不会继续影响粒子。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制群聚修改器（nxFlock）的编辑器辅助显示是否可见。

反应（Reactions）可以在视口里显示十字、球体或盒子辅助图形。这个开关只影响编辑器显示，不直接改变群聚计算结果。

### 群聚权重（Flock Weight）

群聚权重（Flock Weight）控制整个群聚修改器（nxFlock）的总体影响强度。

数值越高，群聚行为、反应和避让对粒子运动的整体影响越明显；数值越低，群聚修改器越弱。

### 最小速度（Min Speed）

最小速度（Min Speed）限制群聚运动后的粒子最低速度。

当群聚行为让粒子趋于停下时，最小速度可以避免粒子速度过低。

### 最大速度（Max Speed）

最大速度（Max Speed）限制群聚运动后的粒子最高速度。

当多个行为或反应叠加后速度过高时，最大速度可以限制粒子不要飞得过快。

### 启用自然限制（Enable Natural Limits）

启用自然限制（Enable Natural Limits）用于限制粒子每一步转向的最大角度。

开启后，最大角度（Maximum Angle）和混合百分比（Blend Percentage）才可编辑。关闭后，这两个限制参数在界面中不可编辑。

### 最大角度（Maximum Angle）

最大角度（Maximum Angle）控制启用自然限制（Enable Natural Limits）后，粒子每一步允许转向的最大角度。

较小的角度会让群聚转向更平滑；较大的角度允许粒子更快改变方向。

### 混合百分比（Blend Percentage）

混合百分比（Blend Percentage）控制转向超过最大角度（Maximum Angle）时，限制结果与原始结果之间的混合程度。

较高数值会更明显地应用自然转向限制。

### 群聚分区（Flock Section）

群聚分区（Flock Section）是群聚修改器（nxFlock）内部的页签切换。

可用页签包括：

- 行为（Behaviors）：编辑内聚、分离、对齐、混沌和蜂拥速度调节。
- 反应（Reactions）：添加追逐、逃离、到达和环绕反应器。
- 避让（Avoidance）：设置几何体避让。

### 行为（Behaviors）

行为（Behaviors）是群聚行为列表。列表中的每一项代表一种群体运动规则。

默认行为通常已经足够形成基础群聚效果。你可以继续添加、移除、启用、禁用或调整每个行为的参数。

### 活动行为索引（Active Behavior Index）

活动行为索引（Active Behavior Index）记录当前正在编辑行为（Behaviors）列表中的哪一项。

普通用户通常不需要直接修改它。

### 行为名称（Behavior Name）

行为名称（Behavior Name）是行为列表项在界面中显示的名称。

它只帮助识别列表项，不直接改变行为类型。

### 行为启用（Behavior Enabled）

行为启用（Behavior Enabled）控制当前行为列表项是否参与群聚计算。

关闭后，这一条行为会保留在列表里，但不会继续影响粒子。

### 行为类型（Behavior Type）

行为类型（Behavior Type）决定当前行为列表项使用哪一种群聚规则。

可用类型包括：

- 内聚（Cohesion）：让粒子向附近群体中心靠拢。
- 分离（Separation）：让粒子避让过近的邻居，减少拥挤。
- 对齐（Alignment）：让粒子速度方向与附近群体趋于一致。
- 混沌（Chaos）：加入随机扰动运动。
- 蜂拥（Swarming）：按“快乐/不快乐”逻辑调节速度。

### 半径（Radius）

半径（Radius）控制行为查找附近群体成员的范围。

半径越大，行为会参考更远的粒子；半径越小，行为只影响近距离邻居。

### 行为强度（Behavior Strength）

行为强度（Behavior Strength）控制当前行为对粒子运动的影响强度。

对于内聚、分离、对齐和混沌等行为，它决定该行为在最终群聚结果中的权重。

### 使用外围（Use Periphery）

使用外围（Use Periphery）控制当前行为是否限制到一个视角范围内。

开启后，视场（View Angle）才会影响该行为。它适合模拟只响应前方或一定视野范围内邻居的群体运动。

### 视场（View Angle）

视场（View Angle）控制使用外围（Use Periphery）时，当前行为能看到的角度范围。

角度越大，粒子可响应的邻居范围越宽。

### 内聚类型（Cohesion Type）

内聚类型（Cohesion Type）决定内聚（Cohesion）行为怎样计算群体中心。

位置（Position）使用几何位置中心；质量（Mass）使用质量加权中心。

### 混沌缩放（Chaos Scale）

混沌缩放（Chaos Scale）控制混沌（Chaos）噪波图案的空间尺度。

数值变化会改变随机扰动的分布尺度。

### 混沌频率（Chaos Frequency）

混沌频率（Chaos Frequency）控制混沌（Chaos）噪波图案的频率。

数值越高，随机扰动变化越密集。

### 其他粒子让我快乐（Others Make Me Happy）

其他粒子让我快乐（Others Make Me Happy）用于切换蜂拥（Swarming）行为的快乐计算方式。

开启后，拥挤会被视为更快乐；关闭时，快乐计算按默认逻辑工作。

### 快乐率（Happiness Ratio）

快乐率（Happiness Ratio）控制蜂拥（Swarming）判断快乐状态的阈值比例。

它会影响粒子使用快乐速度或不快乐速度的倾向。

### 满意时速度（Speed When Happy）

满意时速度（Speed When Happy）控制蜂拥（Swarming）中粒子处于快乐状态时的速度倍率。

### 不满意时速度（Speed When Unhappy）

不满意时速度（Speed When Unhappy）控制蜂拥（Swarming）中粒子处于不快乐状态时的速度倍率。

### 蜂拥类型（Swarming Type）

蜂拥类型（Swarming Type）决定蜂拥（Swarming）怎样判断成员关系。

可用方式包括发射器（Emitter）、组（Group）和物体（Object）。具体效果取决于当前粒子来源和分组设置。

### 避让（Avoidance）

避让（Avoidance）是群聚分区（Flock Section）中的几何避让页。

这里设置避让权重（Avoidance Weight）、避让距离（Avoidance Distance）、避让模式（Avoidance Mode）和避让几何（Avoidance Geometry）列表。

### 反应（Reactions）

反应（Reactions）是群聚反应器列表。每个反应项会创建或引用一个反应器对象，用于让粒子追逐、逃离、到达或环绕目标。

反应器对象会作为群聚修改器（nxFlock）的子对象存在，并可在视口中显示辅助图形。

### 活动反应索引（Active Reaction Index）

活动反应索引（Active Reaction Index）记录当前正在编辑反应（Reactions）列表中的哪一项。

普通用户通常不需要直接修改它。

### 反应名称（Reaction Name）

反应名称（Reaction Name）是反应列表项在界面中显示的名称。

### 反应启用（Reaction Enabled）

反应启用（Reaction Enabled）控制当前反应是否参与群聚计算。

关闭后，这一条反应器保留在列表里，但不会继续影响粒子。

### 反应类型（Reaction Type）

反应类型（Reaction Type）决定当前反应器的运动规则。

可用类型包括：

- 追逐（Pursuit）：追逐目标。
- 逃离（Flee）：远离目标。
- 到达（Arrive）：靠近目标并在到达时减速。
- 环绕（Orbit）：围绕目标运动。

### 反应器对象（Reactor Object）

反应器对象（Reactor Object）是当前反应项对应的 Empty 对象。

它代表反应器在场景中的位置，并用于视口辅助显示。

### 反应器显示（Reactor Display）

反应器显示（Reactor Display）控制反应器在视口中的辅助图形。

可用显示方式包括交叉（Cross）、球体（Sphere）、盒体（Box）和无（None）。

### 反应设置（Reactor Settings）

反应设置（Reactor Settings）控制反应器类型专用设置区是否展开。

展开后会显示追逐、逃离、到达或环绕自己的参数。

### 反应权重（Reaction Weight）

反应权重（Reaction Weight）控制当前反应器对群聚结果的影响强度。

数值越高，反应器越明显地影响粒子运动。

### 激活范围（Activation Range）

激活范围（Activation Range）决定反应器按什么范围条件生效。

无限（Infinite）表示不按距离限制；距离（Distance）表示按激活距离（Activation Distance）限制。

### 激活距离（Activation Distance）

激活距离（Activation Distance）只在激活范围（Activation Range）为距离（Distance）时可编辑。

它也会影响反应器视口辅助图形的大小。

### 反应时机（Reaction Timing）

反应时机（Reaction Timing）决定当前反应器在时间上何时生效。

可用方式包括总是（Always）、之前（Before）、之后（After）、开启（On）、脉冲（Pulse）和之间（Between）。

### 起始帧（Frame 1）

起始帧（Frame 1）是反应时机（Reaction Timing）使用的第一个帧值。

它在之前、之后、在某帧、脉冲和之间等模式下可编辑。

### 结束帧（Frame 2）

结束帧（Frame 2）是反应时机（Reaction Timing）为之间（Between）模式使用的第二个帧值。

### 追逐目标类型（Pursuit Target Type）

追逐目标类型（Pursuit Target Type）决定追逐（Pursuit）反应怎样确定目标位置。

可用方式包括静态位置（Static Position）、中心位置（Center Position）、质心（Center of Mass）和最近（Nearest）。

### 追逐模式（Pursuit Mode）

追逐模式（Pursuit Mode）决定追逐（Pursuit）目标来自发射器（Emitter）还是组（Group）。

当追逐目标类型（Pursuit Target Type）为静态位置（Static Position）时，这个参数不可编辑。

### 追逐目标（Pursuit Target）

追逐目标（Pursuit Target）是追逐（Pursuit）反应使用的目标对象。

当追逐目标类型（Pursuit Target Type）为静态位置（Static Position）时，这个参数不可编辑。

### 追逐偏移（Pursuit Offset）

追逐偏移（Pursuit Offset）是追逐目标位置的偏移量。

当前界面中这个参数以不可编辑状态显示。

### 停止距离（Stop Distance）

停止距离（Stop Distance）只在追逐目标类型（Pursuit Target Type）为最近（Nearest）时可编辑。

它控制追逐到多近时停止继续靠近。

### 逃离目标类型（Flee Target Type）

逃离目标类型（Flee Target Type）决定逃离（Flee）反应怎样确定要远离的位置。

可用方式包括静态位置（Static Position）、中心位置（Center Position）、质心（Center of Mass）和最近（Nearest）。

### 逃离模式（Flee Mode）

逃离模式（Flee Mode）决定逃离（Flee）目标来自发射器（Emitter）还是组（Group）。

当逃离目标类型（Flee Target Type）为静态位置（Static Position）时，这个参数不可编辑。

### 逃离目标（Flee Target）

逃离目标（Flee Target）是逃离（Flee）反应使用的目标对象。

当逃离目标类型（Flee Target Type）为静态位置（Static Position）时，这个参数不可编辑。

### 逃离偏移（Flee Offset）

逃离偏移（Flee Offset）是逃离目标位置的偏移量。

当前界面中这个参数以不可编辑状态显示。

### 安全距离（Safe Distance）

安全距离（Safe Distance）只在逃离目标类型（Flee Target Type）为最近（Nearest）时可编辑。

它控制逃离到多远时停止继续远离。

### 到达目标（Arrive Target）

到达目标（Arrive Target）是到达（Arrive）反应使用的目标对象。

### 到达速度（Arrival Speed）

到达速度（Arrival Speed）控制到达（Arrive）反应接近目标时使用的速度。

### 环绕目标（Orbit Target）

环绕目标（Orbit Target）是环绕（Orbit）反应围绕运动的目标对象。

### 环绕强度（Orbit Strength）

环绕强度（Orbit Strength）控制环绕（Orbit）反应的环绕运动强度。

### 避让权重（Avoidance Weight）

避让权重（Avoidance Weight）控制几何避让对群聚结果的影响强度。

### 避让距离（Avoidance Distance）

避让距离（Avoidance Distance）控制粒子开始避让几何体的距离。

### 避让模式（Avoidance Mode）

避让模式（Avoidance Mode）决定几何避让的方式。

柔和（Soft）会逐渐偏转；强硬（Hard）会更直接地改变方向。

### 避让几何（Avoidance Geometry）

避让几何（Avoidance Geometry）是用于几何避让的网格对象列表。

列表只接受网格（Mesh）对象。

### 活动避让索引（Active Avoidance Index）

活动避让索引（Active Avoidance Index）记录避让几何（Avoidance Geometry）列表中当前选中的项目。

### 添加避让几何（Add Avoidance Geometry）

添加避让几何（Add Avoidance Geometry）用于把网格对象加入避让几何（Avoidance Geometry）列表。

### 避让对象（Avoidance Object）

避让对象（Avoidance Object）是避让几何（Avoidance Geometry）列表项引用的网格对象。

### 避让对象启用（Avoidance Object Enabled）

避让对象启用（Avoidance Object Enabled）控制这一条避让几何对象是否参与几何避让。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是群聚修改器（nxFlock）的主设置页。这里编辑整体权重、速度限制、自然限制，以及行为、反应和避让分区。

### 设置页（Section）

设置页（Section）是普通 NeXus 修改器的页签切换。

群聚修改器（nxFlock）还在物体属性（Object Properties）里提供自己的群聚分区（Flock Section）。

### 组（Groups Affected）

组（Groups Affected）用于限制群聚修改器（nxFlock）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动群聚参数。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制这一条映射层是否参与计算。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制群聚修改器（nxFlock）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定映射层读取哪一种粒子数据作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定映射作用到哪一个层或目标槽位。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围后如何处理。

### 衰减（Falloff）

衰减（Falloff）用于用空间衰减对象控制群聚修改器（nxFlock）的影响范围。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

---

## 列表操作按钮

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）会开关当前列表项是否参与当前列表的作用。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表，把当前项目向更深一层移动。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表，把当前项目向外提升一层。
