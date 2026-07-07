# NeXus 波浪修改器使用说明

这份文档只说明波浪修改器（nxWave）。它覆盖波浪速度、强度、尺寸、时间缩放、噪波缩放、噪波类型、噪波裁剪和对比度参数，以及显示（Display）页签里的可视化设置和梯度颜色。

## 波浪修改器（nxWave）

波浪修改器（nxWave）用于在 NeXus 里使用噪波模式对粒子施加波浪运动。它使用传入的方向和时间驱动的噪波值计算位移，让粒子产生类似水面波动、涌动或随机噪波驱动的运动效果。

创建流程：创建波浪修改器（nxWave）后，其自身位置和方向决定波浪作用空间的范围朝向。波浪修改器（nxWave）创建后作为独立修改器参与 NeXus 流程；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，再确认流程列表包含当前波浪修改器（nxWave）。如果只想影响特定粒子组，可以在组（Groups Affected）列表里指定。

视口中的彩色预览会显示波浪的位移模式和可视化效果，可以在显示（Display）页签里调整预览类型和密度。

### 设置页（Section）

设置页（Section）切换波浪修改器（nxWave）当前显示的主设置页。当前已覆盖的页签包括物体属性（Object Properties）、显示（Display）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 启用（Enabled）

启用（Enabled）控制波浪修改器（nxWave）是否参与当前 NeXus 计算。

关闭后，波浪修改器（nxWave）不会继续影响粒子。调试时可以临时关闭，用来确认画面里的波浪运动是否来自当前这个波浪修改器（nxWave）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制波浪修改器（nxWave）在编辑器里的辅助显示是否可见。

这个开关影响编辑视口里的可视化预览，不等同于关闭波浪计算。如果要停用波浪效果，应使用启用（Enabled）。

### 物体属性（Object Properties）

物体属性（Object Properties）是一个页签，包含波浪修改器（nxWave）自身的通用属性设置，如启用（Enabled）和视口可见（Visible in Editor）。

### 速度（Speed）

速度（Speed）控制波浪动画的播放速度。

数值越大，噪波波动随时间推进越快，粒子波浪运动更急促。数值为 0 时波浪静止不动。速度（Speed）与时间缩放（Time Scale）共同决定最终波浪动画节奏。

### 强度（Strength）

强度（Strength）控制噪波位移的倍率。

数值越大，噪波计算出的位移值被放大越多，粒子波浪运动的幅度越大。数值为 0 时波浪没有位移效果。

### 大小（Size）

大小（Size）控制波浪修改器（nxWave）的作用空间范围，分为 X、Y、Z 三个轴向。

波浪作用域是一个随物体变换的局部边界框，只有落在框内的粒子才会受波浪影响。Z 轴尺寸还决定了视口显示（Display）中切片数量（Slices）的分布范围。每个轴单独设置。

### 时间缩放（Time Scale）

时间缩放（Time Scale）控制波浪动画的时间倍率。

数值用百分比表示。100% 表示正常速度；低于 100% 波浪运动放慢；高于 100% 波浪运动加速。与速度（Speed）不同，时间缩放（Time Scale）是整体倍率，而速度（Speed）是基础速度值。

### 缩放（Scale）

缩放（Scale）控制噪波空间采样的缩放比例，分为 X、Y、Z 三个轴向。

数值越大，噪波在对应轴向上被拉伸，波浪周期更长、起伏更缓；数值越小，噪波在对应轴向上被压缩，波浪周期更短、起伏更密。Z 轴缩放设为 0 时，噪波在 Z 方向无变化，波浪保持平面波动。

### 噪波类型（Noise Type）
噪波类型（Noise Type）选择用于生成波浪的噪波算法。

可选值：

- Simplex：Simplex 噪波，基础连续噪波。
- 分形布朗运动（Fractal Brownian Motion）：分形布朗运动噪波，叠加多频细节。
- Turbulence：湍流噪波，产生尖锐的不规则波动。
- Wavy Turbulence：波动湍流噪波，在湍流基础上增加波浪特性。
- Voronoise：沃罗诺伊噪波，产生细胞状或晶格状图案。
- Cubic：三次噪波，平滑插值的噪波模式。

不同噪波类型产生不同的位移模式。Turbulence 适合做不规则水花或风浪，Simplex 适合做平滑涌动。

### 低裁切（Low Clip）
低裁切（Low Clip）控制噪波值的下限阈值。
噪波计算结果中低于此阈值的部分被限制到下限，对应区域的噪波值不会低于 Low Clip。

### 高裁切（High Clip）
高裁切（High Clip）控制噪波值的上限阈值。
噪波计算结果中高于此阈值的部分被裁切掉，对应区域的粒子位移被限制。数值用百分比表示，100% 表示不裁切。降低高裁切可以压缩波浪幅度范围。

### 亮度（Brightness）

亮度（Brightness）控制噪波值的整体偏移量。

数值用百分比表示，正值让噪波整体抬升（更多区域产生位移），负值让噪波整体降低。亮度调整在裁剪之前生效。

### 对比度（Contrast）

对比度（Contrast）控制噪波值的对比度倍率。

数值用百分比表示，100% 为原始对比度。大于 100% 拉大高低噪波差距，波浪的峰谷更明显；小于 100% 压缩差距，波浪更平缓。对比度调整在裁剪之前生效。

## 显示（Display）

以下参数在显示（Display）页签中出现。它们控制视口里波浪效果的可视化方式，不影响模拟计算结果。

### 显示（Display）

显示（Display）页签包含波浪效果在视口中的可视化设置。

### 绘制类型（Draw Type）

绘制类型（Draw Type）控制视口里波浪可视化效果的显示模式。

可选值：

- 无（None）：不显示任何可视化。
- 线条（Lines）：用线框显示位移方向。
- 箭头（Arrows）：用箭头显示位移方向。
- 表面（Surface）：用填充表面显示位移。
- 网格（Grid）：用线框网格显示位移。
- 平面（Plane）：用渐变彩色平面显示位移概览，不做高度变化。

### 切片数量（Slices）

切片数量（Slices）控制可视化在 Z 轴方向的切片层数。

数值越多，视口里显示的切片越密，可以看到不同高度层上的位移分布。切片沿 Z 轴在 -Z 尺寸到 +Z 尺寸之间均匀分布。

### 网格间距 X（Grid Spacing X）

网格间距 X（Grid Spacing X）控制可视化网格在 X 方向上的采样间距。

数值越小，网格越密，可视化更精细但视口性能开销更大。

### 网格间距 Y（Grid Spacing Y）

网格间距 Y（Grid Spacing Y）控制可视化网格在 Y 方向上的采样间距。

数值越小，网格越密。Y 方向对应波浪的前进方向。

### 颜色（Color）

颜色（Color）是一个渐变，控制波浪可视化效果的伪彩色映射。

低位移值对应渐变左端颜色，高位移值对应渐变右端颜色。只在绘制类型（Draw Type）为非 None 时显示。颜色渐变仅用于视口可视化，不影响波浪模拟本身。

### 组（Groups Affected）

组（Groups Affected）是一个列表，列出哪些nx 组（nxGroup）受当前波浪修改器（nxWave）影响。空列表表示影响所有粒子。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中的索引。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加一个新的组条目。点击后可以从场景里拖入或选择一个nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组列表里某个条目的目标组对象。它决定了哪组粒子受波浪修改器（nxWave）影响。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动波浪修改器（nxWave）的参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则的列表，每层定义一条输入到输出的驱动关系。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中的索引。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）是被驱动的波浪修改器（nxWave）参数。

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

衰减（Falloff）用于在空间上减弱波浪修改器（nxWave）对粒子的影响。衰减对象（Falloff Objects）列表中定义的物体决定了衰减范围和形状。

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
