# NeXus 生成器修改器使用说明

这份文档只说明生成器修改器（nxGenerator）。它覆盖显示模式、源发射器列表和生成器层设置。生成器层可控制每个层的实例网格、生成概率、颜色、缩放、旋转和动画行为。

## 生成器修改器（nxGenerator）

生成器修改器（nxGenerator）用于在每个活动粒子位置实例化网格对象。它将 NeXus 粒子系统中的粒子替换为指定的网格实例，每个实例可以独立控制颜色、缩放和旋转。

创建流程：先创建发射器（nxEmitter）生成粒子，再创建生成器修改器（nxGenerator）。在源发射器（Source Emitters）列表中添加发射器，指定哪些发射器的粒子参与实例化。在生成器层（Generator Layers）列表中添加层，指定每个层使用的网格和实例化参数。

默认情况下，生成器修改器（nxGenerator）以预览（Preview）模式在视口中高速显示实例，但不会出现在渲染输出中。切换到几何体（Geometry）模式后，实例会生成真实 Blender 几何体，可用于碰撞检测、修改器和渲染。

### 设置页（Section）

设置页（Section）切换生成器修改器（nxGenerator）当前显示的主要设置页。当前已覆盖的页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。主面板包含显示模式（Display Mode）、源发射器（Source Emitters）和生成器层（Generator Layers）三个部分。

### 启用（Enabled）

启用（Enabled）控制生成器修改器（nxGenerator）是否参与当前 NeXus 计算。

关闭后，生成器修改器（nxGenerator）不会产生任何实例。调试时可以临时关闭，用来确认画面里的实例是否来自当前这个生成器。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制生成器修改器（nxGenerator）在编辑器里的辅助显示是否可见。

### 物体属性（Object Properties）

物体属性（Object Properties）是一个页签，包含生成器修改器（nxGenerator）自身的通用属性设置，如启用（Enabled）和视口可见（Visible in Editor）。

### 显示模式（Display Mode）

显示模式（Display Mode）切换生成器修改器（nxGenerator）的输出模式。

可选值：

- 预览（Preview）：仅视口 GPU 预览，不参与碰撞、修改器和渲染。性能更高，适合调试和布局。
- 几何体（Geometry）：生成真实 Blender 点云实例几何体，可用于碰撞检测、修改器堆栈和渲染引擎。性能开销更大。

切换模式时，生成器会自动重建或清理几何体。

### 源发射器（Source Emitters）

源发射器（Source Emitters）是一个列表，用于限定哪些发射器（nxEmitter）的粒子被当前生成器用来创建实例。

每个条目可以拖入一个发射器（nxEmitter）对象，并单独开关。

### 活动源发射器索引（Active Source Emitter Index）

活动源发射器索引（Active Source Emitter Index）是源发射器（Source Emitters）列表中当前选中的索引。

### 源发射器对象（Emitter Object）

源发射器对象（Emitter Object）是源发射器列表里某个条目的目标发射器。只有该发射器的粒子才会参与实例化。

### 源发射器启用（Emitter Enabled）

源发射器启用（Emitter Enabled）控制源发射器列表里某个条目是否有效。关闭后该发射器不参与实例化。

### 添加源发射器（Add Source Emitter）

添加源发射器（Add Source Emitter）是源发射器列表上方的拖放输入。选择或拖入发射器对象后，会把它添加到源发射器列表中。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于连续从场景中拾取多个源发射器，并依次加入源发射器列表。

### 生成器层（Generator Layers）

生成器层（Generator Layers）是一个列表，每个层定义一个实例化行为。每个层指定一个网格对象、生成概率以及颜色/缩放/旋转的设置。

列表中每个条目显示网格名称、生成概率滑块、锁定按钮和启用开关。多个层可以同时工作，粒子的分配由生成概率（Spawn Chance）决定。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）是生成器层列表中当前选中的索引。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个条目。在生成器层列表中，它会添加一个新的生成器层。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中移除选中的条目。它只移除列表引用，不等于删除场景里的对象本体。

### 上移层（Move Item Up）

上移层（Move Item Up）将当前选中的层在列表中上移一位。

### 下移层（Move Item Down）

下移层（Move Item Down）将当前选中的层在列表中下移一位。

### 切换启用（Toggle Enabled）

切换启用（Toggle Enabled）用于切换当前列表条目的启用状态。关闭后，该条目会保留在列表里，但不参与当前生成器计算。

### 网格（Mesh）

网格（Mesh）指定该层要实例化的网格对象。只有网格（MESH）类型对象可以拖入。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制该层是否参与实例化。关闭后该层不产生实例。

### 锁定（Lock）

锁定（Lock）控制该层的生成概率在调整其他层滑块时是否被保护。锁定后，该层的生成概率值不受其他层滑块拖动的影响，但仍可手动调整自身滑块。

### 生成（Spawn）

生成（Spawn）概率控制该层在所有层中分配到的粒子比例，用百分比表示。所有启用且未锁定层的概率总和自动保持 100%。拖动一个层的滑块时，其余未锁定层的概率会自动重新分配。

### 颜色（Colour Section）

颜色（Colour Section）是一个可折叠设置区，包含着色模式和实例颜色的设置。

### 着色（Shading）

着色（Shading）控制实例网格的面着色方式。

可选值：

- 默认（Default）：使用源网格自身的每个面平滑/平坦着色标志。
- 平直（Flat）：强制所有面平坦着色。
- 平滑（Smooth）：强制所有面平滑着色。

### 颜色源（Colour Source）

颜色源（Colour Source）选择实例颜色的来源。

可选值：

- 自定义（Custom）：使用该层上设置的颜色。
- 网格（Mesh）：使用拖入网格对象的视口颜色。
- 粒子（Particle）：使用粒子模拟中的逐粒子颜色。

### 自定义颜色（Custom Colour）

自定义颜色（Custom Colour）设置该层的固定实例颜色，当颜色源（Colour Source）为自定义（Custom）时使用。

### 单通道颜色变化量（Per-channel Colour Variation）

单通道颜色变化量（Per-channel Colour Variation）启用后，可以分别控制 R、G、B 三个通道的随机颜色抖动幅度。关闭后使用统一的颜色变化量（Colour Variation）值。

### 颜色变化量（Colour Variation）

颜色变化量（Colour Variation）控制实例颜色的随机抖动幅度（± 基准值），用百分比表示。仅在单通道颜色变化量（Per-channel Colour Variation）关闭时可用。

### R / G / B（R / G / B）

R、G、B 分别控制红、绿、蓝通道的随机颜色抖动幅度。仅在单通道颜色变化量（Per-channel Colour Variation）开启时可用。

### 实例材质（Instance Material）

实例材质（Instance Material）指定应用于该层实例的材质。留空则使用源网格原有材质。

### 新实例材质（New Instance Material）

新实例材质（New Instance Material）点击实例材质（Instance Material）右侧的 + 按钮触发，创建预连线的材质，自动绑定逐实例属性（如 nx_color 等）。

### 缩放（Scale Section）

缩放（Scale Section）是一个可折叠设置区，包含实例缩放来源和抖动的设置。

### 缩放源（Scale Source）

缩放源（Scale Source）选择实例缩放值的来源。

可选值：

- 自定义（Custom）：使用该层上设置的缩放值。
- 网格缩放（Mesh Scale）：使用拖入网格对象的变换缩放。
- 粒子半径（Particle Radius）：使用逐粒子半径值，三轴均匀。
- 粒子缩放（Particle Scale）：使用逐粒子三维缩放缓冲区。

### 每轴缩放（Per-axis Scale）

每轴缩放（Per-axis Scale）启用后可以分别控制 X、Y、Z 三个轴的缩放值。关闭后使用统一缩放值。仅在缩放源（Scale Source）为自定义（Custom）时可用。

### 自定义缩放（Custom Scale）

自定义缩放（Custom Scale）设置该层的固定缩放值，当缩放源（Scale Source）为自定义（Custom）且每轴缩放（Per-axis Scale）开启时使用，可独立设置 X、Y、Z。

### 自定义缩放（Custom Scale Uniform）

自定义缩放（Custom Scale Uniform）设置该层的固定缩放值，当缩放源（Scale Source）为自定义（Custom）且每轴缩放（Per-axis Scale）关闭时使用，三轴均匀。

### 每轴缩放变化量（Per-axis Scale Variation）

每轴缩放变化量（Per-axis Scale Variation）启用后，可以分别控制 X、Y、Z 三个轴的随机缩放抖动幅度。关闭后使用统一的缩放变化量（Scale Variation）值。

### 缩放变化量（Scale Variation）

缩放变化量（Scale Variation）控制实例缩放的随机抖动幅度（± 基准值），用百分比表示。仅在每轴缩放变化量（Per-axis Scale Variation）关闭时可用。

### 缩放 X / Y / Z（Scale X / Y / Z）

缩放 X、Y、Z 分别控制对应轴的随机缩放抖动幅度。仅在每轴缩放变化量（Per-axis Scale Variation）开启时可用。

### 旋转（Rotation Section）

旋转（Rotation Section）是一个可折叠设置区，包含实例旋转来源和抖动的设置。

### 旋转源（Rotation Source）

旋转源（Rotation Source）选择实例旋转值的来源。

可选值：

- 自定义（Custom）：使用该层上设置的旋转值。
- 网格（Mesh）：使用拖入网格对象的变换旋转。
- 粒子（Particle）：使用模拟中的逐粒子朝向（HPB）。

### 前进轴（Forward Axis）

前进轴（Forward Axis）控制实例网格的哪个局部轴指向粒子的运动方向。当旋转源（Rotation Source）为粒子（Particle）且发射器方向模式为相切（Tangential）时生效。

可选值：

- +X / -X / +Y / -Y / +Z / -Z

### 每轴旋转（Per-axis Rotation）

每轴旋转（Per-axis Rotation）启用后可以分别控制 X（俯仰）、Y（偏航）、Z（翻滚）三个轴的旋转值。关闭后使用统一旋转值。仅在旋转源（Rotation Source）为自定义（Custom）时可用。

### 自定义旋转（Custom Rotation）

自定义旋转（Custom Rotation）设置该层的固定旋转值，当旋转源（Rotation Source）为自定义（Custom）且每轴旋转（Per-axis Rotation）开启时使用，可独立设置 X、Y、Z 欧拉角。

### 自定义旋转（Custom Rotation Uniform）

自定义旋转（Custom Rotation Uniform）设置该层的固定旋转值，当旋转源（Rotation Source）为自定义（Custom）且每轴旋转（Per-axis Rotation）关闭时使用，三轴统一。

### 每轴旋转变化量（Per-axis Rotation Variation）

每轴旋转变化量（Per-axis Rotation Variation）启用后，可以分别控制 X（俯仰）、Y（偏航）、Z（翻滚）的随机旋转抖动幅度。关闭后使用统一的旋转变化量（Rotation Variation）值。

### 旋转变化量（Rotation Variation）

旋转变化量（Rotation Variation）控制实例旋转的随机抖动幅度，范围为完整旋转的百分比。仅在每轴旋转变化量（Per-axis Rotation Variation）关闭时可用。

### 旋转 X / Y / Z（Rotation X / Y / Z）

旋转 X、Y、Z 分别控制对应轴的随机旋转抖动幅度。仅在每轴旋转变化量（Per-axis Rotation Variation）开启时可用。

### 动画（Animation Section）

动画（Animation Section）是一个可折叠设置区，包含实例动画冻结设置。

### 冻结动画（Freeze Animation）

冻结动画（Freeze Animation）启用后，实例网格会锁定到当前帧源网格的姿态。冻结后网格的形变动画不再随播放更新，适合在模拟结果满意后固定外观。

### 冻结帧（Frozen Frame）

冻结帧（Frozen Frame）记录冻结动画（Freeze Animation）启用时的当前帧号。在冻结状态下，实例使用此帧的网格形态。

### 重新捕获冻结（Resnapshot Freeze）

重新捕获冻结（Resnapshot Freeze）在冻结动画（Freeze Animation）启用时可用，点击后重新捕获当前帧的网格形态作为新的冻结快照。

### 组（Groups Affected）

组（Groups Affected）是一个列表，列出哪些nx 组（nxGroup）受当前生成器修改器（nxGenerator）影响。空列表表示影响所有粒子。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中的索引。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加一个新的组条目。点击后可以从场景里拖入或选择一个nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组列表里某个条目的目标组对象。它决定了哪组粒子受生成器修改器（nxGenerator）影响。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动生成器修改器（nxGenerator）的参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则的列表，每层定义一条输入到输出的驱动关系。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中的索引。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）是被驱动的生成器修改器（nxGenerator）参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）是驱动来源，即从粒子读取哪个属性来驱动目标参数。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于组织和管理不同映射层，指定的图层才会参与映射计算。

### 范围最小值（Range Min）

范围最小值（Range Min）是映射输入的下限。输入低于此值时输出钳制在最低值。

### 范围最大值（Range Max）

范围最大值（Range Max）是映射输入的上限。输入高于此值时输出钳制在最高值。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制该层映射对目标参数的驱动强度。

### 钳制（Clamp）

钳制（Clamp）控制映射输出是否被限制在目标参数的有效范围内。开启后输出不会超过参数本身的最大最小值。

### 衰减（Falloff）

衰减（Falloff）用于在空间上减弱生成器修改器（nxGenerator）对粒子的影响。衰减对象（Falloff Objects）列表中定义的物体决定了衰减范围和形状。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减对象的列表，每个条目指定一个影响衰减范围的对象。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）是衰减对象（Falloff Objects）列表中当前选中的索引。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）向衰减对象（Falloff Objects）列表添加一个新的衰减条目。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表里某个条目的目标对象，决定了该条目的衰减范围。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）控制多个衰减对象之间的混合模式。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制衰减混合的整体强度。
