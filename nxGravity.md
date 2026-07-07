# NeXus 重力修改器使用说明

这份文档只说明重力修改器（nxGravity）。它的重点是说明重力强度、随机变化和作用方向怎么理解，以及什么时候需要用目标对象来控制方向。

## 重力修改器（nxGravity）

重力修改器（nxGravity）用于给粒子施加一个持续的加速度效果。它适合模拟下落、上浮、斜向牵引、局部方向力等效果。

重力修改器（nxGravity）不产生粒子；它影响当前 NeXus 粒子流程里的已有粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建重力修改器（nxGravity）。只要当前粒子流程会执行这个重力修改器，它就会按自身朝向施加加速度；如果场景使用发射器的修改器（Modifiers）列表组织后续修改器，需要确认重力修改器（nxGravity）已包含在该列表里。

重力修改器（nxGravity）的方向由重力对象本身的朝向决定，不需要填写单独的方向数值。当前视口图标里的红色箭头指示重力方向，它沿着重力对象的负 Z 轴方向作用。你可以旋转重力对象来改变方向，也可以用效果朝向（Effect Towards）指定目标对象，让重力对象自动朝向目标。

### 启用（Enabled）

启用（Enabled）控制当前项目是否参与模拟。它在不同位置代表不同层级：

- 在重力修改器（nxGravity）本体上，启用（Enabled）控制整个重力修改器是否对粒子生效。
- 在组（Groups Affected）列表里，启用（Enabled）控制当前这个组限制是否生效。
- 在映射（Mapping）列表里，启用（Enabled）控制当前这一条映射层是否生效。
- 在衰减（Falloff）列表里，启用（Enabled）控制当前这个衰减对象是否参与影响范围计算。

如果关闭的是重力修改器（nxGravity）本体，这个重力修改器不会继续对粒子施加重力效果。它适合用来临时对比：关闭后观察粒子是否还会向同一方向加速，就能判断当前运动是不是由这个重力修改器造成的。

常见用法：

- 调试多个力修改器时，逐个关闭启用（Enabled）来确认是哪一个在起主要作用。
- 做版本对比时，保留参数但暂时不让重力生效。
- 如果粒子突然被拉走，先关闭重力修改器（nxGravity）本体的启用（Enabled），确认问题是否来自这个修改器。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制重力修改器（nxGravity）的视口辅助图标是否显示。

它只影响编辑器里的可视化，不直接改变重力计算结果。重力修改器（nxGravity）的红色箭头能帮助你判断当前重力方向；如果这个显示被关闭，你仍然可以通过旋转对象或设置效果朝向（Effect Towards）改变方向，只是视口里不再直观看到辅助图标。

常见用法：

- 调方向时建议开启视口可见（Visible in Editor），方便看红色箭头。
- 场景里修改器很多、视口很乱时，可以关闭它来减少干扰。

### 强度（Strength）

强度（Strength）控制重力加速度的大小。

值越高，粒子沿重力方向加速越快；值越低，重力影响越弱。默认值是 9.81，直观上可以理解为接近常见重力加速度的基准值。

常见用法：

- 粒子下落太慢，提高强度（Strength）。
- 粒子被拉得太猛，降低强度（Strength）。
- 想做反重力或斜向风格的运动，优先旋转重力对象或设置效果朝向（Effect Towards）；强度正负不适合作为方向控制手段。

需要注意：强度（Strength）只决定“拉得多强”，不决定“朝哪里拉”。方向由重力对象朝向决定。

### 变化（Variation）

变化（Variation）控制重力强度的随机差异。

值为 0 时，所有受影响粒子使用相同的重力强度。值越高，不同粒子或不同帧之间的重力强度差异越明显，运动会更不整齐。

常见用法：

- 想让粒子下落不完全一致，可以增加变化（Variation）。
- 想要整齐、稳定、像真实统一重力一样的效果，把变化（Variation）保持为 0 或较低。
- 如果粒子运动忽快忽慢，检查变化（Variation）是否过高，以及变化量模式（Variation Mode）当前是哪一种。

### 变化量模式（Variation Mode）

变化量模式（Variation Mode）决定变化（Variation）如何应用。

插件提供两种模式：

- 每帧（Per Frame）：随机变化会随帧变化，重力强度可能每帧改变。
- 每粒子（Per Particle）：每个粒子获得自己的变化值，并且这个变化更偏向保持在该粒子身上。

实用理解：

- 每帧（Per Frame）更容易产生时间上的抖动或飘忽感，适合需要不稳定力场的效果。
- 每粒子（Per Particle）更适合让粒子之间有差异，但每个粒子的运动更连续。

如果你想让一批粒子有轻微不同的下落速度，但不希望每帧乱跳，优先使用每粒子（Per Particle）。如果你想做不稳定力场，再考虑每帧（Per Frame）。

变化量模式（Variation Mode）只有在变化（Variation）大于 0 时才有明显意义。变化（Variation）为 0 时，模式怎么选都不会产生可见随机差异。

### 种子（Seed）

种子（Seed）控制随机变化的随机序列。

它不会直接改变重力强度本身，而是改变由变化（Variation）产生的随机分布。简单理解：同样的变化（Variation）和变化量模式（Variation Mode），换一个种子（Seed），随机结果会换一套。

常见用法：

- 当前随机运动方向或节奏不好看，换一个种子（Seed）。
- 想保持效果可重复，不要随意改种子（Seed）。
- 如果变化（Variation）为 0，种子（Seed）通常不会产生可见影响。

### 效果朝向（Effect Towards）

效果朝向（Effect Towards）用于指定一个目标对象，让重力修改器（nxGravity）朝向它。

选择目标对象后，插件会给重力对象添加或更新一个跟踪约束，让重力对象的负 Z 轴朝向目标。这样重力方向会跟随目标对象变化。清空效果朝向（Effect Towards）后，这个自动跟踪关系会被移除，方向回到由重力对象自身旋转决定。

常见用法：

- 想让粒子被拉向某个移动目标，可以设置效果朝向（Effect Towards）。
- 想做斜向重力或固定方向重力，可以不设置目标，直接旋转重力对象。
- 如果重力方向不对，先看视口里的红色箭头，再检查效果朝向（Effect Towards）是否还绑定着某个目标对象。

它和强度（Strength）的关系是：

- 效果朝向（Effect Towards）决定重力朝哪里作用。
- 强度（Strength）决定重力有多强。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是重力修改器（nxGravity）的主设置页。这里主要编辑重力本体参数，包括强度（Strength）、变化（Variation）、变化量模式（Variation Mode）、种子（Seed）和效果朝向（Effect Towards）。

如果你要调整重力有多强、是否有随机差异、或者朝哪个方向作用，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）分别用于限制作用对象、用粒子数据驱动参数、按空间范围控制影响。

### 设置页（Section）

设置页（Section）是重力修改器（nxGravity）面板顶部的页签切换。它不直接改变重力强度，而是切换你正在编辑哪一类设置。

重力修改器（nxGravity）当前常见页签包括：

- 物体属性（Object Properties）：重力本体参数，例如强度（Strength）、变化（Variation）、变化量模式（Variation Mode）、种子（Seed）、效果朝向（Effect Towards）。
- 组（Groups Affected）：限制这个重力只影响指定 nx 组（nxGroup）里的粒子。
- 映射（Mapping）：用粒子数据去驱动重力参数，例如按年龄、速度、质量、颜色等数据改变强度。
- 衰减（Falloff）：用nx 衰减（nxFalloff）控制重力的空间影响范围。

如果你右键点的是这些页签本身，帮助文档会显示这个总说明。页签里的具体参数有各自的小节说明。

### 组（Groups Affected）

组（Groups Affected）用于限制重力修改器（nxGravity）影响哪些粒子组。

如果这里不添加任何组，重力通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，重力会根据组列表来限制影响对象。

实用理解：

- 想让所有粒子都受重力影响，可以不使用组（Groups Affected）。
- 想让只有某一类粒子受重力影响，先用发射器（nxEmitter）或其他流程把粒子分到 nx 组（nxGroup），再把该组加入组（Groups Affected）。
- 如果重力只对部分粒子生效，检查这里是否添加了组过滤。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要手动调它。它主要用于界面选择：你在列表中选中哪一个组，活动组索引（Active Group Index）就指向哪一个。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器、碰撞体或其他修改器对象不会作为有效组过滤使用。

如果你想让重力只影响某个组，必须先确保场景里真的有对应的 nx 组（nxGroup），并且粒子已经被分配到这个组。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里真的存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动重力参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

映射的基本逻辑是：

- 选择粒子数据（Particle Data）作为输入，例如年龄（Age）、速度（Speed）、质量（Mass）、半径（Radius）、颜色（Color）等。
- 选择要被控制的参数（Parameter），例如重力强度（Strength）或变化（Variation）。
- 设置输入范围（Range Min / Range Max）、映射权重（Mapping Weight）、钳制（Clamp）和曲线，让输入数据转换成目标参数的变化。

常见用法：

- 让年轻粒子受重力弱，老粒子受重力强。
- 让速度快的粒子受到不同重力强度。
- 让不同组、不同半径或不同质量的粒子产生不同下落效果。

如果映射（Mapping）里没有任何层，重力参数就按物体属性（Object Properties）里的固定值工作。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个重力参数”的规则。

列表里每一项通常会显示类似“粒子数据 → 目标参数 · 权重 · 范围”的信息。你可以添加多层映射，让不同粒子数据共同影响重力。

如果某一层没有选择目标参数（Parameter），这层不会真正参与映射。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制重力修改器（nxGravity）的哪个参数。

对于重力修改器（nxGravity），常见目标通常会围绕强度（Strength）、变化（Variation）这类可被数据驱动的参数。可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

如果目标参数没有选择，映射层不会产生实际效果。

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

选择不同粒子数据（Particle Data）后，范围（Range Min / Range Max）的含义也会跟着变化。例如年龄（Age）和文档时间（Document Time）会更偏向时间范围，速度（Speed）则是速度数值范围。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

重力修改器（nxGravity）本身不是分层修改器，所以这个参数通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

在重力修改器（nxGravity）里看到它时，可以理解为通用映射系统保留的字段。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

如果粒子数据低于这个值，会按钳制（Clamp）设置处理。它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

常见理解：

- 选择年龄（Age）时，范围最小值（Range Min）可以表示从多早开始让映射生效。
- 选择速度（Speed）时，它表示低速边界。
- 选择质量（Mass）或半径（Radius）时，它表示对应属性的下限。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

它和范围最小值（Range Min）一起形成映射区间。范围太窄时，变化可能过于突然；范围太宽时，变化可能不明显。

如果映射效果看起来完全没有变化，先检查粒子数据实际值是否落在范围最小值（Range Min）和范围最大值（Range Max）之间。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。它不会改变粒子数据本身，只改变这条映射结果混入目标参数的比例。

如果映射方向正确但影响太强或太弱，优先调映射权重（Mapping Weight）。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供三种模式：

- 钳制（Clamp）：超出范围后停在边界值，不继续外推。
- 循环（Cycle）：超出范围后按区间循环，适合重复变化。
- 继续（Continue）：超出范围后继续按趋势外推。

常见用法：

- 想要稳定可控的映射，优先使用钳制（Clamp）。
- 想要按时间或数值重复变化，可以使用循环（Cycle）。
- 想要范围外继续增强或减弱，可以使用继续（Continue），但更容易得到过强结果。

### 衰减（Falloff）

衰减（Falloff）用于用空间衰减对象控制重力修改器（nxGravity）的影响范围。

简单理解：没有衰减对象时，重力按正常方式影响粒子；加入nx 衰减（nxFalloff）后，粒子在衰减范围内外会得到不同强度的重力影响。

常见用法：

- 让某个区域内重力更强或更弱。
- 做局部引力场，例如只在一个盒体、球体或线性范围附近影响粒子。
- 用多个衰减对象叠加出复杂影响范围。

如果你想控制“哪里受重力影响”，用衰减（Falloff）；如果想控制“哪些组受重力影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

每个衰减对象都有自己的形状、范围和曲线。重力修改器（nxGravity）会读取这些衰减对象，用它们控制重力影响的空间范围。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

普通用户通常不需要手动调它。你在列表中选中哪个衰减对象，下面显示的混合和衰减对象参数就对应哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。如果场景里没有合适的衰减对象，可以用衰减页右侧的创建按钮新建一个，再加入列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前重力修改器（nxGravity）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

插件提供这些模式：

- 法线方向（Normal）：按普通方式使用当前衰减。
- 添加（Add）：把当前衰减叠加到已有结果上。
- 减去（Subtract）：从已有结果里减去当前衰减。
- 相乘（Multiply）：用当前衰减乘上已有结果，常用于收窄影响。
- 差值（Difference）：使用差异结果。
- 屏幕（Screen）：更偏向增强亮区/高值区域。
- 叠加（Overlay）：按叠加方式混合。
- 最小（Min）：取较小影响值。
- 最大（Max）：取较大影响值。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。多个衰减对象叠加时，再根据需要选择相加、相乘、最小值或最大值。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象对重力范围的影响越明显；值越低，它的影响越弱。

如果衰减对象位置和形状正确，但对重力影响太强或太弱，优先调衰减混合强度（Falloff Blend Strength）。

---

## 和其他修改器的联动

重力修改器（nxGravity）需要作用到已有粒子才会生效。最常见的粒子来源是发射器（nxEmitter）。

如果看不到重力效果，按这个顺序检查：

- 发射器（nxEmitter）是否正在产生粒子。
- 当前粒子流程是否包含重力修改器（nxGravity）；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，需要确认列表里包含它。
- 重力修改器（nxGravity）的启用（Enabled）是否开启。
- 强度（Strength）是否太低。
- 重力对象的朝向是否正确，视口红色箭头是否指向预期方向。
- 效果朝向（Effect Towards）是否绑定了目标对象，导致方向被自动跟踪覆盖。

如果场景里同时有碰撞体修改器（nxCollider）、约束修改器（nxConstraints）或其他力修改器，它们会一起影响粒子运动。此时判断重力是否有效，最直接的方法是临时关闭其他修改器，只保留重力修改器（nxGravity）做对比。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、修改器列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象、类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。它通常出现在有多种项目类型的列表里。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

如果列表只接受特定类型，例如 nx 组（nxGroup）、nx 衰减（nxFalloff）或网格（Mesh）物体，不符合类型的对象不会被加入。

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
