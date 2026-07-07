# NeXus 吸引修改器使用说明

这份文档只说明吸引修改器（nxAttract）。重点说明吸引目标从哪里来、多个目标对象怎样选择、力和加速度参数怎样配合，以及映射和衰减怎样控制吸引效果。

## 吸引修改器（nxAttract）

吸引修改器（nxAttract）用于把粒子拉向指定位置。目标位置可以来自吸引修改器（nxAttract）对象本身，也可以来自吸引器（Attractors）列表里的对象。

吸引器（Attractors）列表为空时，插件会使用吸引修改器（nxAttract）对象自身的位置作为吸引点。吸引器（Attractors）列表里有启用对象时，插件会收集这些对象的世界位置作为吸引点，并同步给粒子流程。

当前同步最多使用 1024 个吸引点。超过这个数量后，后面的对象不会继续加入同步数据。

常见使用流程：

- 创建发射器（nxEmitter），让场景里先有粒子来源。
- 创建吸引修改器（nxAttract）。吸引修改器（nxAttract）创建后会以自身位置作为默认吸引点。
- 如果只需要一个固定吸引中心，直接移动吸引修改器（nxAttract）对象即可。
- 如果需要指定其他对象作为吸引点，把这些目标对象加入吸引器（Attractors）列表。
- 用对象选择（Object Select）决定粒子在多个吸引点之间怎样选择目标。
- 调整力（Force）、加速度（Acceleration）和速度限制（Speed Limit）。

### 启用（Enabled）

启用（Enabled）控制整个吸引修改器（nxAttract）是否参与粒子流程。

关闭后，这个吸引修改器不会继续对粒子施加吸引效果。调试多个力场时，可以临时关闭它来判断当前运动是否来自吸引修改器（nxAttract）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制吸引修改器（nxAttract）的视口辅助图标是否显示。

它只影响编辑器里的辅助显示，不直接改变吸引计算结果。视口图标里的箭头会根据力（Force）的正负显示向内或向外的趋势。

### 类型（Type）

类型（Type）决定吸引效果怎样作用到粒子运动上。

插件提供两种类型：

- 速度（Velocity）：直接影响粒子的速度变化。适合需要快速把粒子拉向目标、运动响应更直接的效果。
- 力（Force）：以力的方式作用到粒子上。适合需要更像力场推动、和粒子运动状态持续叠加的效果。

如果你希望粒子明显朝目标移动，可以先用速度（Velocity）。如果你希望吸引更像物理力场，可以尝试力（Force）。

### 力（Force）

力（Force）控制吸引强度。

数值越大，粒子朝目标位置的趋势越明显。负值会反向影响吸引方向，视口辅助箭头也会反映这种方向变化。

如果粒子被吸得太快或太集中，先降低力（Force）。如果粒子几乎不受影响，先提高力（Force），再检查目标对象是否正确、速度限制（Speed Limit）是否过低、组（Groups Affected）或衰减（Falloff）是否限制了作用范围。

### 加速度（Acceleration）

加速度（Acceleration）控制粒子朝吸引目标加速的程度。

它和力（Force）一起决定吸引的运动强度。力（Force）更像总体吸引强度，加速度（Acceleration）更直接影响粒子速度增加的速度。

如果吸引方向正确，但粒子启动太慢，可以提高加速度（Acceleration）。如果粒子靠近目标时速度增长过猛，可以降低加速度（Acceleration）或使用速度限制（Speed Limit）。

### 速度限制（Speed Limit）

速度限制（Speed Limit）控制受吸引粒子的最大速度。

它用于防止粒子被吸引后速度无限增大。值越低，粒子越容易被限制在较慢速度；值越高，粒子可以更快地朝目标移动。

如果粒子飞过目标、运动过猛或难以控制，优先降低速度限制（Speed Limit）。如果粒子移动太慢，检查速度限制（Speed Limit）是否压得太低。

### 对象选择（Object Select）

对象选择（Object Select）决定吸引器（Attractors）列表里有多个对象时，每个粒子选择哪个目标点。

插件提供五种模式：

- 最近（Nearest）：粒子吸向距离自己最近的目标对象。适合多个吸引点分区吸引的效果。
- 最远（Furthest）：粒子吸向距离自己最远的目标对象。适合把粒子拉向远端目标或制造跨区域运动。
- 平均（Average）：粒子吸向所有启用目标对象的平均位置。适合多个对象共同定义一个中心点。
- 索引（Index）：粒子吸向指定序号的目标对象。选择这个模式时，界面会显示索引（Index）。
- 随机（Random）：粒子随机选择目标对象。适合粒子分散飞向多个目标。

如果吸引器（Attractors）列表为空，这些选择模式没有多个目标可选，插件会使用吸引修改器（nxAttract）对象自身的位置。

### 索引（Index）

索引（Index）只在对象选择（Object Select）为索引（Index）模式时显示。

它指定吸引器（Attractors）列表里的目标对象序号。列表顺序改变后，同一个索引指向的对象也会改变。

如果索引超出当前可用目标数量，实际结果可能无法按预期选择目标。使用索引（Index）模式时，要同时检查吸引器（Attractors）列表的顺序和启用状态。

### 吸引器（Attractors）列表

吸引器（Attractors）列表用于添加一个或多个目标对象。插件会读取启用对象的世界位置，把这些位置作为吸引点。

列表项只需要对象位置，不要求对象必须是网格。空对象、网格、曲线或其他场景对象都可以作为位置目标使用，只要它们在场景中有有效的世界变换。

列表为空时，吸引修改器（nxAttract）对象自身的位置会作为唯一吸引点。

### 活动索引（Active Index）

活动索引（Active Index）记录当前正在编辑吸引器（Attractors）列表里的哪一项。

普通用户通常不需要直接修改它。你在列表里选中哪一项，活动索引（Active Index）就对应哪一项。

### 添加对象（Add Object）

添加对象（Add Object）用于把一个场景对象加入吸引器（Attractors）列表。

添加后，该对象的位置会作为吸引目标。对象移动后，吸引点也会跟随它的世界位置变化。

### 添加集合（Add Collection）

添加集合（Add Collection）用于把一个集合里的对象批量加入吸引器（Attractors）列表。

适合一次添加多个吸引目标，例如一组空对象、一组标记点或一组模型位置。

### 吸引器对象（Attractor Object）

吸引器对象（Attractor Object）是列表项里真正提供目标位置的对象。

吸引修改器（nxAttract）会读取它的世界位置。对象的形状、材质和渲染外观通常不影响吸引目标位置，关键是对象当前在场景里的位置。

### 吸引器启用（Attractor Enabled）

吸引器启用（Attractor Enabled）控制当前列表项是否参与吸引目标同步。

关闭某一项后，这个对象不会作为吸引点使用。它适合临时比较多个目标对象对粒子运动的影响。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是吸引修改器（nxAttract）的主设置页。这里主要编辑吸引类型、强度、速度限制、目标选择模式和吸引器（Attractors）列表。

如果你要调整粒子被拉向哪里、拉得多强、多个目标怎样选择，通常先回到物体属性（Object Properties）页。

### 设置页（Section）

设置页（Section）是吸引修改器（nxAttract）面板顶部的页签切换。它只切换当前正在编辑的设置页。

吸引修改器（nxAttract）常见页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制吸引修改器（nxAttract）影响哪些 nx 组（nxGroup）。

如果这里不添加任何组，通常表示不额外按组过滤。添加组后，吸引效果只会作用在组过滤后的粒子范围里。

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

映射（Mapping）用于让粒子数据动态驱动吸引参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用年龄（Age）驱动力（Force），让粒子出生后逐渐被目标吸引。
- 用速度（Speed）驱动速度限制（Speed Limit），让高速粒子更受限制。
- 用组（Group）驱动力（Force），让不同粒子组受到不同吸引强度。
- 用文档时间（Document Time）驱动加速度（Acceleration），让吸引随时间变化。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个吸引参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制吸引修改器（nxAttract）的哪个参数。

对于吸引修改器（nxAttract），常见目标通常围绕力（Force）、加速度（Acceleration）和速度限制（Speed Limit）。可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

当前映射菜单提供这些基础输入源：

- 年龄（Age）：粒子出生后经过的时间。适合让吸引随粒子年龄逐渐增强或减弱。
- 颜色明度（Color Brightness）：使用粒子颜色整体亮度作为输入。
- 颜色 R（Color R）：使用粒子颜色的红色通道作为输入。
- 颜色 G（Color G）：使用粒子颜色的绿色通道作为输入。
- 颜色 B（Color B）：使用粒子颜色的蓝色通道作为输入。
- 距离（Distance）：使用粒子记录的距离数据作为输入。
- 文档时间（Document Time）：使用当前场景时间作为输入，适合做全局时间变化。
- 流体密度（Fluid Density）：使用流体密度数据作为输入，需要前置流程提供流体数据。
- 燃料（Fuel）：使用燃料通道作为输入，需要烟火或 ExplosiaFX 相关数据。
- 颗粒（Granular）：使用颗粒相关数据作为输入，需要前置流程提供颗粒数据。
- 组（Group）：使用粒子所属组作为输入，需要粒子已经分配到 nx 组（nxGroup）。
- ID（ID）：使用粒子唯一编号作为输入，适合制造稳定的逐粒子差异。
- 生命（Life）：使用粒子生命周期长度或生命周期相关数据作为输入。
- 质量（Mass）：使用粒子质量作为输入，适合让轻粒子和重粒子受到不同吸引。
- 半径（Radius）：使用粒子半径作为输入。
- 缩放（Scale）：使用粒子缩放数据作为输入。
- 烟雾（Smoke）：使用烟雾通道作为输入，需要烟雾相关数据。
- 速度（Speed）：使用粒子速度大小作为输入。
- 温度（Temperature）：使用温度通道作为输入，需要温度相关数据。
- 顶点权重（Vertex Weight）：使用顶点权重数据作为输入，需要来源或粒子流程传递顶点权重。

选择粒子数据（Particle Data）后，要配合范围最小值（Range Min）和范围最大值（Range Max）设定输入区间。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

吸引修改器（nxAttract）本身不是内部多层修改器，所以这个字段通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

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

衰减（Falloff）用于用空间衰减对象控制吸引修改器（nxAttract）的影响范围。

如果你想控制“哪里有吸引”，用衰减（Falloff）；如果想控制“哪些组受吸引影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前吸引修改器（nxAttract）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在吸引器列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表支持的可添加类型。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。它通常只移除列表引用，不等于删除场景里的对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

对于吸引器（Attractors）列表，顺序会影响索引（Index）模式选择的目标对象。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于树状列表里的层级调整。普通吸引器列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于树状列表里的层级调整。普通吸引器列表通常不需要使用它。
