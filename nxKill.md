# NeXus 销毁修改器使用说明
这份文档说明销毁修改器（nxKill）。它用于按体积范围、对象体积、相机视场或最大粒子数量来移除粒子。

## 销毁修改器（nxKill）
销毁修改器（nxKill）不会生成新粒子，而是根据当前设置筛掉不需要继续保留的粒子。它适合做边界裁切、场景清理、镜头外剔除，或把粒子总量限制在一个上限之内。

根据当前模式不同，销毁修改器（nxKill）可以用包围体、对象体积、相机视场或数量上限来决定哪些粒子会被移除。

### 设置页（Section）
设置页（Section）用于切换当前显示的主设置页。销毁修改器（nxKill）除了自己的物体属性页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）
启用（Enabled）控制销毁修改器（nxKill）是否参与当前 NeXus 计算。关闭后，这个修改器不会继续移除粒子。

### 视口可见（Visible in Editor）
视口可见（Visible in Editor）控制销毁修改器（nxKill）在编辑器中的辅助显示是否可见。它不改变销毁结果，只影响编辑时的可见性。

### 物体属性（Object Properties）
物体属性（Object Properties）是销毁修改器（nxKill）的主设置页。这里集中设置销毁模式、体积形状、对象列表、相机视场限制、粒子数量上限，以及是否只在出生时销毁。

### 体积（Volume）
体积（Volume）模式决定当前用什么方式销毁粒子。当前可选模式包括：

- 边界内（Inside Bounds）：销毁位于体积内部的粒子。
- 边界外（Outside Bounds）：销毁位于体积外部的粒子。
- 对象（Objects）：按对象体积来销毁粒子。
- 相机视野外（Outside Camera FOV）：销毁位于相机视野之外的粒子。
- 限制最大粒子数（Clamp to Max Particles）：把粒子数量限制在指定上限。

### 形状（Shape）
形状（Shape）决定包围体模式使用什么体积形状。当前可选盒体（Box）和球体（Sphere）。

### 大小（Size）
大小（Size）用于方盒体积模式，定义销毁体积在 X、Y、Z 三个方向上的大小。体积越大，被纳入判断范围的空间通常越大。

### 半径（Radius）
半径（Radius）用于球体体积模式，定义球形销毁范围的大小。半径越大，参与“体积内/体积外”判断的空间越广。

### 销毁物体（Kill Objects）
销毁物体（Kill Objects）是对象模式下使用的对象列表。列表中的网格对象会被拿来参与体积判断，用它们来决定哪些粒子应被销毁。

对象模式下，每个对象条目除了启用开关外，还带有一个“体积内/体积外”切换图标，用来决定当前对象是销毁体积内的粒子，还是销毁体积外的粒子。

### 活动对象索引（Active Object Index）
活动对象索引（Active Object Index）记录销毁物体（Kill Objects）列表里当前选中的条目。它主要服务于界面编辑。

### 添加对象（Add Object）
添加对象（Add Object）把一个网格对象加入销毁物体（Kill Objects）列表。加入后，这个对象就会参与当前对象模式的销毁判断。

### 物体（Object）
物体（Object）是销毁对象列表条目里实际引用的网格对象。当前修改器会根据这些对象的体积来判断粒子是否需要被移除。

### 对象启用（Object Enabled）
对象启用（Object Enabled）控制当前对象条目是否参与销毁判断。关闭后，这个对象会保留在列表中，但暂时不生效。

### 相机（Camera）
相机（Camera）用于相机视野外模式，指定当前拿哪一个相机对象作为视野参考。只有有效的相机对象才会参与这类销毁判断。

### 加宽FOV（Widen FOV）
加宽FOV（Widen FOV）用于相机视野外模式，给当前相机视野额外增加一定范围。它适合把镜头边缘附近的粒子保留得更宽松一些。

### 限制到（Clamp To）
限制到（Clamp To）用于最大粒子数模式，定义允许保留的粒子数量上限。超过这个上限后，修改器会开始按当前规则裁掉多余粒子。

### 仅新生粒子（Only Born）
仅新生粒子（Only Born）控制销毁判断是否只在粒子出生时执行。启用后，更适合做初始筛选；关闭后，粒子在后续流程中也可能继续被当前规则移除。

## 通用页签

### 组（Groups Affected）
组（Groups Affected）用于限制销毁修改器（nxKill）只影响哪些粒子组。列表为空时，表示不额外按组过滤。

### 活动组索引（Active Group Index）
活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的条目。它主要服务于界面选择。

### 添加组（Add Group）
添加组（Add Group）把一个 nx 组（nxGroup）对象加入组（Groups Affected）列表。加入后，销毁修改器只会对这些组里的粒子生效。

### 组对象（Group Object）
组对象（Group Object）是组列表条目里实际引用的 nx 组（nxGroup）对象。只有属于这些组的粒子会进入当前销毁流程。

### 组启用（Group Enabled）
组启用（Group Enabled）控制当前组条目是否参与过滤。关闭后，这个组条目会保留在列表中，但暂时不生效。

### 映射（Mapping）
映射（Mapping）用于让粒子数据动态驱动销毁修改器（nxKill）的参数。它适合让某些阈值随粒子状态变化，而不是始终固定不变。

### 映射层（Mapping Layers）
映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层都表示“用某种粒子数据去驱动某个参数”的一条映射关系。

### 活动映射索引（Active Mapping Index）
活动映射索引（Active Mapping Index）记录当前正在编辑哪一层映射。通常通过点击映射层列表切换。

### 映射参数（Mapping Parameter）
映射参数（Mapping Parameter）决定当前映射层要驱动哪个目标参数。只有被映射到的参数，才会随粒子数据变化。

### 粒子数据（Particle Data）
粒子数据（Particle Data）决定当前映射层读取哪种粒子属性作为输入。你可以用年龄、速度、半径、颜色等数据来驱动销毁阈值。

### 映射图层（Mapping Layer）
映射图层（Mapping Layer）是通用映射系统里的层标识字段。它用于组织多层映射关系。

### 范围最小值（Range Min）
范围最小值（Range Min）定义映射输入范围的下限。低于这个范围时，结果会按映射规则处理。

### 范围最大值（Range Max）
范围最大值（Range Max）定义映射输入范围的上限。它与范围最小值（Range Min）一起决定映射区间。

### 映射权重（Mapping Weight）
映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。数值越高，这一层映射越明显。

### 钳制（Clamp）
钳制（Clamp）决定输入值超出范围后如何处理。启用后，超出区间的值不会继续无限延伸。

### 映射启用（Mapping Enabled）
映射启用（Mapping Enabled）控制当前映射层是否参与计算。关闭后，这一层会保留在列表里，但不再驱动参数。

### 衰减（Falloff）
衰减（Falloff）用于按空间范围限制销毁修改器（nxKill）的影响。它适合让销毁效果只出现在特定区域内。

### 衰减对象（Falloff Objects）
衰减对象（Falloff Objects）是当前修改器使用的衰减对象列表。只有这些衰减对象定义的范围会参与当前销毁效果。

### 活动衰减索引（Active Falloff Index）
活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。它主要用于界面选择。

### 添加衰减（Add Falloff）
添加衰减（Add Falloff）把一个 NeXus nx 衰减（nxFalloff）加入当前列表。加入后，这个衰减对象就可以参与限制销毁影响范围。

### 衰减对象（Falloff Object）
衰减对象（Falloff Object）是衰减列表条目里实际引用的对象。当前修改器会根据它的空间范围调节销毁效果。

### 衰减启用（Falloff Enabled）
衰减启用（Falloff Enabled）控制当前衰减条目是否参与计算。关闭后，它会留在列表里，但不参与当前影响范围的计算。

### 衰减混合（Falloff Blend）
衰减混合（Falloff Blend）定义多个衰减结果如何与当前销毁修改器效果混合。它决定不同衰减对象叠加时的合成方式。

### 衰减混合强度（Falloff Blend Strength）
衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。数值越高，这个衰减对象对销毁效果的调制越明显。

## 列表操作按钮

这些按钮通常出现在对象、组、映射或衰减列表旁边，用于管理列表内容，不直接参与粒子计算。

### 添加项（Add Item）
添加项（Add Item）在当前列表里新增一个空条目。新增后，通常还需要继续指定对象或其他参数。

### 添加菜单（Add Menu）
添加菜单（Add Menu）打开当前列表可添加类型的菜单。销毁修改器（nxKill）的对象列表通常不需要用它切换条目类型，但通用列表系统可能会提供这个入口。

### 创建并添加（Create and Add）
创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。销毁修改器（nxKill）的对象列表通常不会直接使用它，但通用列表系统可能会显示这个按钮。

### 连续拾取（Continuous Pick）
连续拾取（Continuous Pick）用于在视口中连续选择多个对象并加入当前列表。按 `Esc` 可以结束连续拾取。

### 移除项（Remove Item）
移除项（Remove Item）从当前列表中删除选中的条目。删除后，这个对象或引用将不再参与当前销毁流程。

### 上移项（Move Item Up）
上移项（Move Item Up）把当前选中的列表项向上移动一位。它用于整理列表顺序。

### 下移项（Move Item Down）
下移项（Move Item Down）把当前选中的列表项向下移动一位。它同样只改变列表顺序。

### 切换启用（Toggle Enabled）
切换启用（Toggle Enabled）切换当前列表条目是否参与作用。它只影响这一条目，不等于关闭整个销毁修改器。

### 增加缩进（Indent Item）
增加缩进（Indent Item）用于层级列表，把当前条目向更深一层移动。销毁修改器（nxKill）的对象列表通常是平级结构，一般不会使用这个按钮。

### 减少缩进（Outdent Item）
减少缩进（Outdent Item）用于层级列表，把当前条目向外提升一层。销毁修改器（nxKill）的对象列表通常是平级结构，一般不会使用这个按钮。
