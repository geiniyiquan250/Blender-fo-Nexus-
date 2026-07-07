# NeXus 碰撞体修改器使用说明

这份文档只说明碰撞体修改器（nxCollider）。它的重点是说明碰撞体对象列表怎样工作、每个参数实际影响什么、哪些参数当前只是显示在界面但不能编辑。

## 碰撞体修改器（nxCollider）

碰撞体修改器（nxCollider）用于让 NeXus 粒子和网格物体发生碰撞。它本身不产生粒子，也不直接改变粒子的发射数量；它的作用是把指定的网格物体作为碰撞表面交给模拟流程。

当前碰撞体修改器（nxCollider）的核心是碰撞体（Colliders）列表。你可以把一个或多个网格物体加入列表，每个列表项都有自己的碰撞参数，例如法线方向（Normals）、弹力（Bounce）、摩擦力（Friction）和散射（Scatter）。

使用时通常按这个顺序理解：

- 先把网格物体加入碰撞体（Colliders）列表。
- 确认这个列表项已启用。
- 设置法线方向（Normals），决定粒子从网格外侧、内侧还是两侧发生碰撞。
- 再设置弹力（Bounce）、摩擦力（Friction）和散射（Scatter），决定碰撞后的运动表现。

碰撞体修改器（nxCollider）只接受网格（Mesh）物体。如果列表项为空，或者放入的物体不是网格（Mesh）物体，它不会作为有效碰撞体参与同步。

### 碰撞体（Colliders）

碰撞体（Colliders）列表是这个修改器的主入口。列表里的每一项代表一个参与碰撞的网格物体。

如果你希望粒子撞到多个物体，就把多个网格物体加入碰撞体（Colliders）列表。每个列表项可以单独设置是否启用、碰撞侧、弹力、摩擦和散射。

实际使用时要注意：

- 碰撞体（Colliders）列表只接受网格（Mesh）物体。
- 关闭某个列表项的启用状态后，这个物体不会参与碰撞。
- 如果网格物体变形或移动，碰撞数据会按当前物体数据和世界变换参与同步。
- 同一个碰撞体修改器（nxCollider）可以管理多个碰撞物体，但复杂网格越多，计算越重。

### 活动索引（Active Index）

活动索引（Active Index）记录当前正在编辑碰撞体（Colliders）列表里的哪一项。

普通用户通常不需要手动调它。它主要用于界面选择：当你在列表中切换不同碰撞体对象时，活动索引（Active Index）会跟着变化，右侧显示的参数也会变成当前选中项的参数。

### 添加对象（Add Object）

添加对象（Add Object）用于快速把一个物体加入碰撞体（Colliders）列表。

当前碰撞体修改器（nxCollider）只接受网格（Mesh）物体。如果拖入或选择的不是网格（Mesh）物体，它不会成为有效碰撞体。

常见用法：

- 把地面网格加入碰撞体（Colliders）列表，让粒子落地后反弹或滑动。
- 把容器内壁加入碰撞体（Colliders）列表，让粒子被限制在容器里。
- 把角色、障碍物或其他模型加入碰撞体（Colliders）列表，让粒子和模型发生碰撞。

### 添加集合（Add Collection）

添加集合（Add Collection）用于把一个集合里的物体批量加入碰撞体（Colliders）列表。

这个入口同样只接受集合中的网格（Mesh）物体。如果集合里混有灯光、相机、曲线或其他类型对象，它们不会作为有效碰撞体使用。

适合场景：

- 场景里有一组障碍物需要一起变成碰撞体。
- 一个容器由多个网格部件组成，需要一次性加入。
- 想把某个集合专门当作碰撞体集合管理。

### 碰撞体对象（Collider Object）

碰撞体对象（Collider Object）是列表项里真正参与碰撞的网格物体。

它必须是网格（Mesh）物体。如果这个槽为空，或者对象类型不是网格（Mesh）物体，这一项不会参与碰撞同步。

实用理解：

- 碰撞体修改器（nxCollider）只是管理入口。
- 碰撞体对象（Collider Object）才是粒子真正会撞到的表面。
- 一个列表项对应一个网格（Mesh）物体，多个列表项可以组成复杂碰撞环境。

如果粒子完全不发生碰撞，先检查碰撞体对象（Collider Object）是否存在、是否为网格（Mesh）物体、列表项是否启用。

### 碰撞体启用（Collider Enabled）

碰撞体启用（Collider Enabled）控制当前这个列表项是否参与碰撞。

关闭后，这个网格物体不会被同步为有效碰撞体。它适合用来临时排查问题：关闭某个碰撞体，观察粒子是否还会受到它影响。

常见用法：

- 临时关闭某个复杂碰撞体，确认性能或穿透问题是不是它造成的。
- 同一组碰撞体里只测试其中一个。
- 保留列表项设置，但暂时不让它参与模拟。

### 设置页（Section）

设置页（Section）用于切换当前碰撞体列表项的参数页签。

插件提供三个页签：

- 常规（General）：当前主要可用的碰撞参数都在这里。
- 动作（Action）：当前界面显示为即将推出。
- 扩展（Extended）：当前界面显示为即将推出。

也就是说，当前实际可调的核心参数主要在常规（General）页。动作（Action）和扩展（Extended）暂时没有可编辑参数。

### 法线方向（Normals）

法线方向（Normals）决定粒子和网格表面的哪一侧发生碰撞。

插件提供三种模式：

- 外部（Outside）：粒子从网格法线外侧接触时发生碰撞。
- 内部（Inside）：粒子从网格内侧接触时发生碰撞。
- 任何（Any）：网格两侧都参与碰撞。

这是碰撞体修改器（nxCollider）里最容易影响“为什么没有碰撞”的参数之一。

常见用法：

- 地面、墙、障碍物这类普通外表面，通常用外部（Outside）。
- 容器内部、封闭空间内壁，可能需要内部（Inside）。
- 如果你不确定网格法线方向是否正确，或者希望两面都能挡住粒子，可以先用任何（Any）排查。

如果粒子从某一侧能碰撞、从另一侧穿过去，优先检查法线方向（Normals）和网格法线是否正确。

### 绘制边界（Draw Bounds）

绘制边界（Draw Bounds）用于显示碰撞边界的视口辅助信息。

当前界面里这个参数显示为禁用状态，普通用户暂时不能直接编辑。它不会改变碰撞本身的弹力、摩擦或散射，只和视口辅助显示有关。

如果你看到它是灰色的，这是当前碰撞体修改器（nxCollider）的界面状态，不是你的场景设置错误。

### 边界颜色一（Bound Color 1）

边界颜色一（Bound Color 1）是绘制边界（Draw Bounds）相关的主颜色。

当前界面里这个参数显示为禁用状态，普通用户暂时不能直接编辑。它只服务于碰撞边界的可视化，不参与碰撞求解。

### 边界颜色二（Bound Color 2）

边界颜色二（Bound Color 2）是绘制边界（Draw Bounds）相关的辅助颜色。

当前界面里这个参数显示为禁用状态，普通用户暂时不能直接编辑。它只影响边界可视化，不影响粒子碰撞结果。

### 弹力（Bounce）

弹力（Bounce）控制粒子碰到碰撞体后保留多少反弹能量。

值越高，粒子撞到表面后越容易弹开；值越低，粒子撞到表面后越不容易反弹，更像被表面吸收掉一部分速度。

常见用法：

- 想让粒子像弹珠、砂砾或硬颗粒一样弹起，提高弹力（Bounce）。
- 想让粒子像湿颗粒、泥浆或重物一样落下后不怎么反弹，降低弹力（Bounce）。
- 如果粒子撞到地面后一直跳，可以降低弹力（Bounce）或提高摩擦力（Friction）。

弹力（Bounce）只决定碰撞后的反弹倾向，不负责让粒子贴住表面。

### 摩擦力（Friction）

摩擦力（Friction）控制粒子碰撞后沿表面滑动时受到的阻力。

值越高，粒子越不容易沿碰撞体表面滑动；值越低，粒子更容易顺着表面滑走。

常见用法：

- 粒子落到斜坡后滑得太快，提高摩擦力（Friction）。
- 想让粒子顺着表面流动或滑落，降低摩擦力（Friction）。
- 地面颗粒堆积不稳时，可以适当提高摩擦力（Friction）。

摩擦力（Friction）通常要和弹力（Bounce）一起调。高弹力配低摩擦会更活跃，高摩擦配低弹力会更稳。

### 散射（Scatter）

散射（Scatter）控制粒子碰撞后方向的随机打散程度。

值越高，粒子碰撞后的反射方向越随机；值越低，粒子更按规则的反弹方向运动。

常见用法：

- 想让粒子撞到粗糙表面后四散飞开，提高散射（Scatter）。
- 想要更干净、更可预测的反弹轨迹，降低散射（Scatter）。
- 如果粒子碰撞后方向太乱，先降低散射（Scatter），再检查弹力（Bounce）。

散射（Scatter）不是碰撞强度，它主要改变碰撞后的方向随机性。

### 扩展（Expand）

扩展（Expand）用于把碰撞表面向外扩展。

当前界面里这个参数显示为禁用状态，普通用户暂时不能直接编辑。底层同步里保留了这个参数，但当前界面没有开放手动调整。

实用理解：

- 如果以后开放，扩展（Expand）通常可用于让碰撞表面比原始网格稍微外扩，减少粒子贴得太近或轻微穿透。
- 当前如果看到扩展（Expand）是灰色的，这是界面限制，不是参数失效报错。

---

## 和其他修改器的联动

碰撞体修改器（nxCollider）需要有粒子参与模拟后才有意义。用户通常先创建能产生粒子的发射器（nxEmitter），再创建碰撞体修改器（nxCollider），并在碰撞体（Colliders）列表里加入网格（Mesh）物体。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认碰撞体修改器（nxCollider）已包含在该列表里。

如果场景里只有碰撞体修改器（nxCollider），但没有粒子来源，或者当前粒子流程没有使用这个碰撞体修改器（nxCollider），就不会看到碰撞效果。

排查碰撞无效时，按这个顺序检查：

- 发射器（nxEmitter）是否真的在产生粒子。
- 当前粒子流程是否包含碰撞体修改器（nxCollider）；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，需要确认列表里包含它。
- 碰撞体（Colliders）列表里是否有有效的网格（Mesh）物体。
- 对应列表项的碰撞体启用（Collider Enabled）是否开启。
- 法线方向（Normals）是否选对，必要时临时改成任何（Any）排查。
- 弹力（Bounce）、摩擦力（Friction）和散射（Scatter）是否设置得过低或过高。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是碰撞体修改器（nxCollider）的主设置页。这里主要显示碰撞体（Colliders）列表，也就是当前真正参与碰撞的网格（Mesh）物体列表。

如果你想添加地面、墙体、容器或其他障碍物作为碰撞表面，通常先回到物体属性（Object Properties）页，在碰撞体（Colliders）列表里添加对象，再编辑每个碰撞体对象自己的法线方向（Normals）、弹力（Bounce）、摩擦力（Friction）和散射（Scatter）。

### 设置页（Section）

设置页（Section）是碰撞体修改器（nxCollider）面板顶部的页签切换。它不直接改变碰撞结果，而是切换当前正在编辑哪一类设置。

碰撞体修改器（nxCollider）除了自身的碰撞体（Colliders）列表外，也会带有普通 NeXus 修改器通用页签，例如组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 启用（Enabled）

启用（Enabled）控制当前项目是否参与流程。它在不同位置代表不同层级：

- 在碰撞体修改器（nxCollider）本体上，启用（Enabled）控制整个碰撞体修改器是否参与粒子流程。
- 在组（Groups Affected）列表里，启用（Enabled）控制当前这个组限制是否生效。
- 在映射（Mapping）列表里，启用（Enabled）控制当前这一条映射层是否生效。
- 在衰减（Falloff）列表里，启用（Enabled）控制当前这个衰减对象是否参与影响范围计算。

它和碰撞体启用（Collider Enabled）不同。碰撞体启用（Collider Enabled）只控制碰撞体（Colliders）列表里的某一个网格碰撞体。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制碰撞体修改器（nxCollider）的编辑器辅助显示是否可见。

它只影响编辑器里的可视化，不直接改变粒子是否发生碰撞。

### 组（Groups Affected）

组（Groups Affected）用于限制碰撞体修改器（nxCollider）影响哪些 nx 组（nxGroup）。

如果这里不添加任何组，通常表示不额外按组过滤。添加组后，碰撞体影响会按组过滤后的粒子范围工作。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要手动调它。它只决定界面正在编辑列表里的哪一项。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里真的存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

基本逻辑是：选择粒子数据（Particle Data）作为输入，选择要控制的目标参数（Mapping Parameter），再用范围（Range Min / Range Max）、映射权重（Mapping Weight）、钳制（Clamp）和曲线决定输入如何转换成参数变化。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会真正参与映射。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制碰撞体修改器（nxCollider）的哪个参数。

可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）和组（Group）。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

碰撞体修改器（nxCollider）不是这种内部多层修改器时，这个字段通常没有实际意义。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

如果映射没有效果，先检查粒子数据实际值是否落在范围最小值（Range Min）和范围最大值（Range Max）之间。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供钳制（Clamp）、循环（Cycle）和继续（Continue）三种模式。

### 衰减（Falloff）

衰减（Falloff）用于用衰减对象控制碰撞体修改器（nxCollider）的影响范围。

如果你想控制“哪里受碰撞体影响”，用衰减（Falloff）；如果想控制“哪些组受影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前碰撞体修改器（nxCollider）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

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
