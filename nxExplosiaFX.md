# NeXus 爆炸特效修改器使用说明

这份文档只说明爆炸特效修改器（nxExplosiaFX）。它覆盖物体属性里的模拟（Simulation）、源（Sources）、碰撞体（Colliders）、求解器（Solver），以及额外页签里的动力学（Dynamics）、显示（Display）和渲染（Render）。

## 爆炸特效修改器（nxExplosiaFX）

爆炸特效修改器（nxExplosiaFX）用于在一个体素域里模拟烟雾、燃料、温度、颜色和速度场。它本身负责创建流体模拟域，源对象负责把烟雾、温度、燃料或压力写入体素网格，碰撞体对象负责阻挡或推动流体，求解器参数负责控制计算精度、子步、边界和自适应范围。

这个修改器不直接发射普通 NeXus 粒子。常见流程是先创建爆炸特效修改器（nxExplosiaFX），再在源（Sources）列表里添加网格（Mesh）、曲线（Curve）或发射器（nxEmitter）作为流体来源。发射器（nxEmitter）作为源时，爆炸特效修改器（nxExplosiaFX）会读取该发射器的粒子句柄，把粒子转成烟雾、温度、燃料、压力、速度或颜色来源。

### 设置页（Section）

设置页（Section）切换爆炸特效修改器（nxExplosiaFX）当前显示的主设置页。

当前已覆盖的页签包括：

- 模拟（Simulation）：控制体素尺寸、域大小、燃烧、环境、扩散、耗散和浮力。
- 源（Sources）：添加网格（Mesh）、曲线（Curve）或发射器（nxEmitter）作为模拟输入。
- 碰撞体（Colliders）：添加网格（Mesh）作为流体碰撞对象。
- 求解器（Solver）：控制通道、压力求解、扩散求解、平流、子步、自适应范围和边界墙。

### 启用（Enabled）

启用（Enabled）控制爆炸特效修改器（nxExplosiaFX）是否参与当前 NeXus 计算。

关闭后，爆炸特效修改器（nxExplosiaFX）不会继续作为有效模拟域参与更新。调试时可以临时关闭它，用来确认画面里的烟雾、火焰或流体数据是否来自当前这个爆炸特效修改器（nxExplosiaFX）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制爆炸特效修改器（nxExplosiaFX）在编辑器里的辅助显示是否可见。

这个开关影响编辑视口显示，不等同于关闭模拟计算。如果要停用模拟，应使用启用（Enabled）。

### 体素大小（Voxel Size）

体素大小（Voxel Size）控制模拟网格里每个体素的世界空间大小。

数值越小，单位空间内体素越多，烟雾边缘、火焰细节和碰撞轮廓可以更细，但显存和计算量会快速上升。数值越大，模拟更轻，但细节会变粗。界面里的内存统计（Memory Stats）会根据体素大小（Voxel Size）和域大小（Domain Size）估算网格规模。

实用理解：

- 做大范围爆炸、烟团轮廓时，先用较大的体素大小（Voxel Size）确定运动。
- 做近景火焰、细烟和碰撞细节时，再逐步降低体素大小（Voxel Size）。
- 如果显存估算过高，优先增大体素大小（Voxel Size）或缩小域大小（Domain Size）。

### 域大小（Domain Size）

域大小（Domain Size）控制爆炸特效修改器（nxExplosiaFX）的模拟空间尺寸。

源对象、烟雾和流体运动需要落在这个域内才有意义。域太小会裁掉烟雾或火焰；域太大会增加体素数量，导致计算和显存负担变高。体素大小（Voxel Size）和域大小（Domain Size）共同决定基础体素网格数量。

### 放大分辨率（Upscaling）

放大分辨率（Upscaling）控制上采样模拟通道的分辨率倍率。

它会让可显示或可渲染的体积细节更密，但基础模拟仍由体素大小（Voxel Size）和域大小（Domain Size）决定。数值大于 1 时，内存统计（Memory Stats）会显示放大网格（Upscaled Grid）。

实用理解：

- 想提升可见体积细节，可以先保持基础模拟稳定，再提高放大分辨率（Upscaling）。
- 如果显存压力明显增加，先把放大分辨率（Upscaling）降回 1。

### 重定时（Retiming）

重定时（Retiming）控制流体模拟播放节奏。

它用于改变模拟时间推进速度。默认 100% 表示按正常节奏推进；降低会让模拟变慢；提高会让模拟变快。它适合在运动形态已经满意后调整节奏，不适合替代源强度、浮力或求解器设置。

### 内存统计（Memory Stats）

内存统计（Memory Stats）显示基础体素网格、放大网格和显存估算。

这些信息由体素大小（Voxel Size）、域大小（Domain Size）、放大分辨率（Upscaling）和启用通道数量共同决定。颜色（Color）通道会按三个颜色分量增加数据量，所以开启颜色通道后显存估算会明显上升。

### 燃烧（Burning）

燃烧（Burning）是一组折叠参数，用来控制燃料如何转化为温度、烟雾和压力膨胀。

燃烧效果依赖燃料（Fuel）和温度（Temperature）通道。源（Sources）里需要提供燃料或温度，求解器（Solver）里也需要开启对应通道，否则燃烧相关参数没有完整输入。

### 燃烧率（Burn Rate）

燃烧率（Burn Rate）控制可用燃料被消耗的速度。

数值越高，燃料越快被烧掉，爆发更集中；数值越低，燃料保留更久，火焰和烟雾释放更缓。它需要源（Sources）提供燃料（Fuel），并且温度达到点火温度（Ignition Temperature）后才有完整燃烧意义。

### 温度产生（Temperature Production）

温度产生（Temperature Production）控制每单位燃料燃烧后增加多少温度。

数值越高，燃烧会更强烈地升温，也会更容易通过温度浮力（Temperature Buoyancy）带动烟雾上升。调高它时通常要同时观察温度消散（Temperature Dissipation）和浮力（Buoyancy）。

### 烟雾产生（Smoke Production）

烟雾产生（Smoke Production）控制每单位燃料燃烧后生成多少烟雾。

数值越高，燃烧后烟量越多；数值越低，火焰更干净，烟雾更少。它需要烟雾通道（Smoke Channel）开启才能在模拟中保留烟雾数据。

### 气体膨胀（Gas Expansion）

气体膨胀（Gas Expansion）控制燃烧带来的压力扩张。

数值越高，燃烧区域越容易向外推开流体，爆炸膨胀感更强。数值太高可能让运动过猛，需要配合压力求解器（Pressure Solver）和子步（Substeps）检查稳定性。

### 点火温度（Ignition Temperature）

点火温度（Ignition Temperature）控制燃烧开始所需的温度门槛。

当源（Sources）或环境条件提供的温度不足时，燃料不会按预期燃烧。想让燃料更容易点燃，可以降低点火温度（Ignition Temperature）或提高源温度（Source Temperature）。

### 环境条件（Ambient Conditions）

环境条件（Ambient Conditions）设置远离源对象时的默认温度和燃料背景值。

它影响模拟域里的基础环境。环境温度（Ambient Temperature）会参与温度差和浮力理解；环境燃料（Ambient Fuel）会让整个域带有基础燃料浓度，使用时需要谨慎，避免整片空间都变得可燃。

### 环境温度（Ambient Temperature）

环境温度（Ambient Temperature）控制模拟环境的基础温度。

温度源和燃烧产生的温度会与环境温度形成差异。较高的环境温度会改变温度衰减和浮力表现；较低的环境温度会让热区域更突出。

### 环境燃料（Ambient Fuel）

环境燃料（Ambient Fuel）控制模拟环境中的基础燃料浓度。

默认通常为 0，表示只有源对象明确提供燃料的位置才有燃料。提高后，域内会存在背景燃料，配合温度和点火条件可能产生更广泛的燃烧。

### 扩散（Diffusion）

扩散（Diffusion）控制烟雾、温度、燃料和速度在相邻体素之间扩散和平滑的程度。

扩散会让局部尖锐变化变得更柔和。数值太高会让形态变糊；数值较低会保留更清晰的局部结构。扩散求解器（Diffusion Solver）的精度和迭代次数会影响扩散计算的收敛程度。

### 烟雾扩散（Smoke Diffusion）

烟雾扩散（Smoke Diffusion）控制烟雾通道在空间中扩散的程度。

数值越高，烟雾更容易铺开、变软；数值越低，烟雾边界更集中。它需要烟雾通道（Smoke Channel）开启。

### 温度扩散（Temperature Diffusion）

温度扩散（Temperature Diffusion）控制温度通道在空间中扩散的程度。

数值越高，热量更容易向周围传播；数值越低，热区更集中。它会间接影响燃烧和温度浮力（Temperature Buoyancy）。

### 燃料扩散（Fuel Diffusion）

燃料扩散（Fuel Diffusion）控制燃料通道在空间中扩散的程度。

数值越高，燃料更容易从源区域向周围铺开；数值越低，燃料更贴近源对象输入位置。它需要燃料通道（Fuel Channel）开启。

### 粘度（Viscosity）

粘度（Viscosity）控制速度场的扩散程度。

数值越高，速度变化越容易被平滑，流体运动更黏、更缓；数值越低，速度细节和局部变化更容易保留。

### 消散（Dissipation）

消散（Dissipation）控制烟雾、温度、燃料和速度随时间衰减的速度。

耗散用于让模拟逐渐消散。数值越高，对应通道衰减越快；数值越低，对应数据保留越久。

### 烟雾消散（Smoke Dissipation）

烟雾消散（Smoke Dissipation）控制烟雾浓度随时间减少的速度。

提高它可以让烟雾更快淡出；降低它可以让烟雾停留更久。它需要烟雾通道（Smoke Channel）开启。

### 温度消散（Temperature Dissipation）

温度消散（Temperature Dissipation）控制温度随时间回落的速度。

提高它会让热量更快消失，燃烧和上升浮力更快减弱；降低它会让热区保持更久。

### 燃料消散（Fuel Dissipation）

燃料消散（Fuel Dissipation）控制未燃烧燃料随时间减少的速度。

提高它可以避免燃料长时间残留；降低它会让燃料保留更久，后续仍可能参与燃烧。

### 速度消散（Velocity Dissipation）

速度消散（Velocity Dissipation）控制速度场随时间衰减的速度。

提高它会让流体运动更快停下来；降低它会让涡流、上升和扩张运动保持更久。

### 浮力（Buoyancy）

浮力（Buoyancy）控制烟雾、温度和燃料如何产生竖直方向的加速度。

这组参数会影响烟雾上升、热气抬升和燃料分布带来的运动趋势。它依赖对应通道存在有效数据，例如温度浮力（Temperature Buoyancy）需要温度通道（Temperature Channel）和温度来源。

### 重力（Gravity）

重力（Gravity）控制浮力计算使用的重力加速度强度。

数值越高，浮力相关运动越强。这里的重力属于爆炸特效修改器（nxExplosiaFX）内部流体浮力参数，不等同于普通粒子的重力修改器（nxGravity）。

### 烟雾浮力（Smoke Buoyancy）

烟雾浮力（Smoke Buoyancy）控制烟雾浓度对上升或下沉趋势的影响。

正值通常让烟雾更容易上升；负值会产生相反趋势。它需要烟雾通道（Smoke Channel）中存在烟雾数据。

### 温度浮力（Temperature Buoyancy）

温度浮力（Temperature Buoyancy）控制温度差对流体上升的影响。

数值越高，热区域越容易向上运动。它常和温度产生（Temperature Production）、环境温度（Ambient Temperature）和温度消散（Temperature Dissipation）一起调。

### 燃料浮力（Fuel Buoyancy）

燃料浮力（Fuel Buoyancy）控制燃料浓度对流体运动的影响。

默认值为负，表示燃料会按当前内部规则产生与正浮力相反的趋势。它需要燃料通道（Fuel Channel）和有效燃料来源。

### 运动间隙填充（Motion Gap Fill）

运动间隙填充（Motion Gap Fill）用于补充移动源对象在帧与帧之间留下的发射间隙。

当源对象移动很快，而每帧只采样一次时，烟雾、燃料或温度可能出现断点。提高运动间隙填充（Motion Gap Fill）会增加额外采样，让快速移动源更连续，但也会增加处理成本。

### 源列表（Sources List）

源列表（Sources List）保存当前爆炸特效修改器（nxExplosiaFX）使用的输入对象。

允许添加的对象类型包括：

- 网格（Mesh）：可以从体积或表面写入烟雾、温度、燃料、压力、速度和颜色。
- 曲线（Curve）：可以沿曲线写入烟雾、温度、燃料、压力、速度和颜色。
- 发射器（nxEmitter）：可以把发射器粒子作为流体来源。

如果列表为空，爆炸特效修改器（nxExplosiaFX）只有模拟域和求解器，没有明确的烟雾、温度、燃料或压力输入。

### 源对象（Source Object）

源对象（Source Object）是源列表（Sources List）里引用的实际对象。

对象类型决定下面显示哪些源参数。网格（Mesh）显示体积、表面、顶点权重和纹理权重相关设置；曲线（Curve）显示半径相关设置；发射器（nxEmitter）显示粒子转流体相关设置。

### 源启用（Source Enabled）

源启用（Source Enabled）控制当前源列表项是否参与爆炸特效修改器（nxExplosiaFX）的输入。

关闭后，只禁用这一项源对象，不会删除场景对象，也不会关闭整个爆炸特效修改器（nxExplosiaFX）。

### 发射来源（Emit From）

发射来源（Emit From）只用于网格（Mesh）源，控制从网格体积还是表面写入流体通道。

体积（Volume）适合让整个封闭体积内部产生烟雾或燃料。表面（Surface）适合让网格表面附近产生烟雾、火焰或压力。选择表面（Surface）后，表面宽度（Surface Width）和渐细宽度（Taper Width）会显示并参与计算。

### 表面宽度（Surface Width）

表面宽度（Surface Width）只在网格（Mesh）源的发射来源（Emit From）选择表面（Surface）时生效。

它以体素数量为单位，控制表面发射区域的内部宽度。数值越大，表面附近被写入的区域越厚。

### 渐细宽度（Taper Width）

渐细宽度（Taper Width）只在网格（Mesh）源的发射来源（Emit From）选择表面（Surface）时生效。

它控制表面发射区域外侧的平滑过渡宽度。数值越大，源输入边缘越柔和。

### 源烟雾（Source Smoke）

源烟雾（Source Smoke）控制源对象向烟雾通道写入的值。

它出现在网格（Mesh）、曲线（Curve）和发射器（nxEmitter）源设置里。数值越高，源位置产生的烟雾越浓。它需要求解器（Solver）里的烟雾通道（Smoke Channel）开启，才会作为有效烟雾数据保留。

### 源温度（Source Temperature）

源温度（Source Temperature）控制源对象向温度通道写入的值。

温度会影响燃烧、温度浮力（Temperature Buoyancy）和热区表现。它需要求解器（Solver）里的温度通道（Temperature Channel）开启。想让燃料点燃，需要源温度（Source Temperature）或其他温度输入达到点火温度（Ignition Temperature）。

### 源燃料（Source Fuel）

源燃料（Source Fuel）控制源对象向燃料通道写入的值。

燃料本身不会自动变成火焰；它需要温度和燃烧（Burning）参数共同作用。它需要求解器（Solver）里的燃料通道（Fuel Channel）开启。

### 源压力（Source Pressure）

源压力（Source Pressure）控制源对象向压力相关输入写入的值。

正值可以制造从源位置向外推动的趋势；负值会产生相反趋势。压力输入会和压力求解器（Pressure Solver）一起影响流体速度场。

### 帧限制（Frame Limit）

帧限制（Frame Limit）控制当前源通道是否只在指定帧范围内写入。

启用后，开始（Start）和结束（End）决定该通道的有效帧范围。未启用时，该通道按源对象和当前参数持续参与。

### 开始（Start）

开始（Start）是帧限制（Frame Limit）启用后允许源通道写入的第一帧。

它只在对应通道的帧限制（Frame Limit）打开时生效。

### 结束（End）

结束（End）是帧限制（Frame Limit）启用后允许源通道写入的最后一帧。

它只在对应通道的帧限制（Frame Limit）打开时生效。结束（End）应大于或等于开始（Start），否则有效范围会很短或无法按预期输入。

### 源模式（Source Mode）

源模式（Source Mode）控制源值如何写入已有体素值。

插件提供这些模式：

- 设置（SET）：把体素值设为源目标值，会覆盖其他来源写入的同一位置。
- 混合（BLEND）：在重叠源之间混合，混合比例由混合（Mix）控制。
- 每秒增加（ADDRATE）：按每秒速率向体素网格增加指定值。
- 每秒减少（SUBRATE）：按每秒速率从体素网格减少指定值。

### 混合（Mix）

混合（Mix）只在源模式（Source Mode）选择混合（BLEND）时显示。

它控制新源值和体素中已有值的混合比例。数值越高，新源值影响越强；数值越低，已有体素值保留越多。

### 权重方式（Weight By）

权重方式（Weight By）只用于网格（Mesh）源，控制每个顶点或采样位置如何给源通道加权。

可用方式包括顶点组（Vertex Group）、属性（Attribute）、颜色属性（Color Attribute）、纹理（Texture）、噪波（Noise）和无（None）。它适合让同一个网格只有局部区域产生烟雾、温度、燃料或压力。

### 顶点组（Vertex Group）

顶点组（Vertex Group）在权重方式（Weight By）选择顶点组（Vertex Group）时使用。

插件会读取源网格上的顶点组权重。权重高的位置源输入更强，权重低的位置源输入更弱。没有找到指定顶点组时，代码会退回默认权重。

### 属性（Attribute）

属性（Attribute）在权重方式（Weight By）选择属性（Attribute）时使用。

它要求源网格存在点域（POINT）的浮点属性（FLOAT）。如果属性不存在或类型不匹配，界面会显示警告，源权重无法按该属性正常驱动。

### 颜色属性（Color Attribute）

颜色属性（Color Attribute）在权重方式（Weight By）选择颜色属性（Color Attribute）时使用。

它读取网格颜色属性，并通过权重来源（Weight From）选择红、绿、蓝、透明或亮度作为权重。代码支持点域（POINT）和角域（CORNER）的颜色属性。

### 权重来源（Weight From）

权重来源（Weight From）控制颜色属性（Color Attribute）的哪个通道用于权重。

可选项包括R（R）、G（G）、B（B）、A（A）和亮度（Luminance）。亮度（Luminance）按颜色亮度计算，适合用黑白或明暗控制源强度。

### 图像（Image）

图像（Image）在权重方式（Weight By）选择纹理（Texture）时使用。

它指定用于采样权重的图像。插件会按坐标（Coordinates）和可选的 UV 贴图（UV Map）在顶点位置采样图像颜色，并把颜色平均值作为权重。

### 坐标（Coordinates）

坐标（Coordinates）控制纹理（Texture）权重的采样坐标来源。

插件提供这些方式：

- UV（UV）：使用顶点的 UV 坐标，需要指定或存在合适的 UV 贴图（UV Map）。
- 物体（Object）：使用顶点局部位置的前两个分量采样。
- 已生成（Generated）：把网格包围盒归一化到 0 到 1 后采样。

### UV 贴图（UV Map）

UV 贴图（UV Map）只在坐标（Coordinates）选择 UV（UV）时使用。

它指定源网格上用于图像采样的 UV 图层。如果没有可用 UV，纹理权重无法按预期落到模型表面。

### 噪波强度（Noise Strength）

噪波强度（Noise Strength）在权重方式（Weight By）选择噪波（Noise）时使用。

它控制噪波权重对源输入的影响强度。数值越高，源通道的局部随机变化越明显。

### 长度缩放（Length Scale）

长度缩放（Length Scale）在噪波（Noise）权重里控制噪波主尺度。

数值越大，噪波变化块越大；数值越小，噪波变化更细碎。

### 倍频层数（Octaves）

倍频层数（Octaves）在噪波（Noise）权重里控制叠加多少层空间变化。

层数越多，细节越丰富，计算也会更复杂。

### 持续度（Persistence）

持续度（Persistence）在噪波（Noise）权重里控制每层噪波相对上一层的振幅比例。

数值越高，高频细节保留越明显；数值越低，主要由大尺度形状决定。

### 频率（Frequency）

频率（Frequency）在噪波（Noise）权重里控制噪波随时间变化的速度。

数值越高，噪波变化越快；数值越低，变化更慢。

### 速度来源（Velocity From）

速度来源（Velocity From）只用于网格（Mesh）源，控制源对象向速度场写入哪类速度。

插件提供这些方式：

- 对象运动（Object Motion）：使用源对象运动速度，比例由速度百分比（Velocity Percent）控制。
- 网格法线方向（Mesh Normals）：沿网格法线方向写入速度，强度由法线速度幅度（Normal Velocity Magnitude）控制。
- 自定义（Custom）：使用自定义速度（Custom Velocity）向量。

### 速度百分比（Velocity Percent）

速度百分比（Velocity Percent）控制源对象速度传递到流体的比例。

它用于网格（Mesh）、曲线（Curve）和发射器（nxEmitter）源。数值越高，源对象或粒子运动越强地带动流体；数值为 0 时，该来源基本不向速度场传递运动。

### 法线速度幅度（Normal Velocity Magnitude）

法线速度幅度（Normal Velocity Magnitude）只在网格（Mesh）源的速度来源（Velocity From）选择网格法线方向（Mesh Normals）时生效。

它控制沿网格法线方向推出或吸入流体的速度强度。适合做从表面向外喷烟、喷火或冲击波的效果。

### 自定义速度（Custom Velocity）

自定义速度（Custom Velocity）只在网格（Mesh）源的速度来源（Velocity From）选择自定义（Custom）时生效。

它直接指定写入速度场的方向和大小。适合让源对象按固定方向推动烟雾或火焰。

### 颜色来源（Color From）

颜色来源（Color From）控制源颜色来自哪里。

网格（Mesh）源可以使用物体（Object）颜色、颜色属性（Color Attribute）或自定义（Custom）。曲线（Curve）源可以使用物体（Object）颜色或自定义（Custom）。发射器（nxEmitter）源可以使用粒子（Particles）颜色或自定义（Custom）。它需要求解器（Solver）里的颜色通道（Color Channel）开启。

### 颜色强度（Color Strength）

颜色强度（Color Strength）控制源颜色写入颜色通道的比例。

数值越高，源颜色越明显；数值越低，颜色通道受该源影响越弱。

### 自定义颜色（Custom Color）

自定义颜色（Custom Color）在颜色来源（Color From）选择自定义（Custom）时使用。

它指定源对象写入颜色通道的固定颜色。它需要颜色通道（Color Channel）开启。

### 自定义半径（Custom Radius）

自定义半径（Custom Radius）只用于曲线（Curve）源。

开启后，曲线源使用半径（Radius）作为写入宽度。关闭时，代码向求解端传入默认标记，让曲线按内部默认半径规则处理。

### 半径（Radius）

半径（Radius）只在曲线（Curve）源开启自定义半径（Custom Radius）时生效。

它控制曲线周围参与流体写入的范围。数值越大，曲线源越粗。

### 碰撞体列表（Colliders List）

碰撞体列表（Colliders List）保存当前爆炸特效修改器（nxExplosiaFX）使用的流体碰撞对象。

这个列表只接受网格（Mesh）对象。列表里的网格会被同步为碰撞几何，并可通过内部法线方向（Inside Normals）、添加压力（Add Pressure）和速度缩放（Velocity Scale）影响流体。

### 碰撞体对象（Collider Object）

碰撞体对象（Collider Object）是碰撞体列表（Colliders List）里引用的实际网格对象。

它必须是网格（Mesh）。曲线、普通空物体或其他 NeXus 修改器对象不会作为有效碰撞体同步。

### 碰撞体启用（Collider Enabled）

碰撞体启用（Collider Enabled）控制当前碰撞体列表项是否参与流体碰撞。

关闭后，只禁用这一项碰撞对象，不删除场景里的网格。

### 内部法线方向（Inside Normals）

内部法线方向（Inside Normals）用于反转网格表面法线方向。

当碰撞体表现像内外方向反了，例如流体被错误地挡在外侧或内侧，可以切换内部法线方向（Inside Normals）检查碰撞方向。

### 添加压力（Add Pressure）

添加压力（Add Pressure）控制碰撞体向流体额外加入的压力。

正值可以让碰撞体附近更容易向外推流体；负值会产生相反趋势。它适合做移动物体带来的局部挤压或吸入感。

### 速度缩放（Velocity Scale）

速度缩放（Velocity Scale）控制碰撞体物体速度传递给流体的比例。

100% 表示按当前物体运动速度传递；降低后碰撞体带动流体的程度减弱；提高会增强移动碰撞体推动烟雾或火焰的效果。

### 活动通道（Active Channels）

活动通道（Active Channels）控制求解器实际保留和计算哪些数据通道。

源（Sources）写入某个通道前，需要这里启用对应通道。关闭通道可以减少数据量和显存占用，但对应源参数、燃烧输入或显示颜色也会失去有效承载。

### 烟雾通道（Smoke Channel）

烟雾通道（Smoke Channel）控制是否模拟烟雾数据。

源烟雾（Source Smoke）、烟雾产生（Smoke Production）、烟雾扩散（Smoke Diffusion）、烟雾消散（Smoke Dissipation）和烟雾浮力（Smoke Buoyancy）都依赖这个通道。

### 燃料通道（Fuel Channel）

燃料通道（Fuel Channel）控制是否模拟燃料数据。

源燃料（Source Fuel）、燃烧率（Burn Rate）、燃料扩散（Fuel Diffusion）、燃料消散（Fuel Dissipation）和燃料浮力（Fuel Buoyancy）都依赖这个通道。

### 温度通道（Temperature Channel）

温度通道（Temperature Channel）控制是否模拟温度数据。

源温度（Source Temperature）、温度产生（Temperature Production）、点火温度（Ignition Temperature）、温度扩散（Temperature Diffusion）、温度消散（Temperature Dissipation）和温度浮力（Temperature Buoyancy）都依赖这个通道。

### 颜色通道（Color Channel）

颜色通道（Color Channel）控制是否模拟颜色数据。

颜色来源（Color From）、颜色强度（Color Strength）和自定义颜色（Custom Color）需要这个通道。颜色通道会按三个颜色分量增加数据量，开启后内存统计（Memory Stats）里的显存估算会提高。

### 压力求解器（Pressure Solver）

压力求解器（Pressure Solver）控制速度场压力修正的计算质量。

压力求解影响爆炸膨胀、碰撞挤压和流体不可压缩感。压力精度（Pressure Accuracy）和压力迭代（Pressure Iterations）越高，结果通常越稳定，但计算成本更高。

### 压力精度（Pressure Accuracy）

压力精度（Pressure Accuracy）控制压力求解提前结束的精度目标。

数值越高，求解器会更努力接近目标；数值越低，计算更快但可能更松散。遇到爆炸膨胀过乱或碰撞附近不稳定时，可以提高压力精度（Pressure Accuracy）或压力迭代（Pressure Iterations）。

### 压力迭代（Pressure Iterations）

压力迭代（Pressure Iterations）控制压力求解允许的最大迭代次数。

数值越高，压力求解有更多机会收敛；数值越低，计算更快但稳定性可能下降。

### 扩散求解器（Diffusion Solver）

扩散求解器（Diffusion Solver）控制扩散（Diffusion）相关计算的质量。

当烟雾、温度、燃料或粘性扩散数值较高时，扩散求解器（Diffusion Solver）的精度和迭代次数会更重要。

### 扩散精度（Diffusion Accuracy）

扩散精度（Diffusion Accuracy）控制扩散求解提前结束的精度目标。

数值越高，扩散结果更接近目标；数值越低，计算更快但可能更粗略。

### 扩散迭代（Diffusion Iterations）

扩散迭代（Diffusion Iterations）控制扩散求解允许的最大迭代次数。

扩散参数较高但效果不稳定或不均匀时，可以提高扩散迭代（Diffusion Iterations）。

### CFL 数值（CFL Number）

CFL 数值（CFL Number）控制自动调整子步数量的条件。

它用于限制每个子步中流体穿过体素的程度。较低的 CFL 数值通常更稳但需要更多子步；较高的 CFL 数值计算更省，但快速运动时更容易出现误差。

### 最小子步（Min Substeps）

最小子步（Min Substeps）控制每帧至少计算多少个子步。

提高它可以让快速源、强压力或强浮力更稳定，但会增加每帧计算量。

### 最大子步（Max Substeps）

最大子步（Max Substeps）控制每帧允许自动增加到多少个子步。

当速度较快或 CFL 条件需要更多细分时，求解器可以增加子步，但不会超过最大子步（Max Substeps）。

### 平流求解器（Advection Solver）

平流求解器（Advection Solver）控制烟雾、温度、燃料、速度和颜色如何随流体速度移动。

每个通道可以独立选择快速（Fast）或精确（Accurate）。快速（Fast）成本较低；精确（Accurate）更适合保留形状和减少数值误差。

### 烟雾平流（Smoke Advection）

烟雾平流（Smoke Advection）控制烟雾通道随速度场移动的方法。

烟雾是最直观的可见通道之一，近景烟雾通常更适合使用精确（Accurate），预览或远景可以使用快速（Fast）降低成本。

### 温度平流（Temperature Advection）

温度平流（Temperature Advection）控制温度通道随速度场移动的方法。

温度会影响燃烧和浮力。火焰或热气运动不稳定时，可以检查温度平流（Temperature Advection）是否需要更精确。

### 燃料平流（Fuel Advection）

燃料平流（Fuel Advection）控制燃料通道随速度场移动的方法。

燃料运动会影响后续燃烧位置。默认偏向快速计算，需要更稳定的燃料轮廓时可以改用精确（Accurate）。

### 速度平流（Velocity Advection）

速度平流（Velocity Advection）控制速度场自身如何随流体移动。

它会影响涡流、上升、膨胀和碰撞带来的运动结构。运动形态异常扩散或失真时，可以检查速度平流（Velocity Advection）。

### 颜色平流（Color Advection）

颜色平流（Color Advection）控制颜色通道随速度场移动的方法。

它只在颜色通道（Color Channel）开启且源对象写入颜色时有实际意义。

### 自适应边界（Adaptive Bounds）

自适应边界（Adaptive Bounds）控制求解器是否根据有效数据动态缩小或扩展活动模拟区域。

开启后，求解器会根据烟雾、温度、燃料、速度和颜色的追踪设置判断哪些体素仍需要计算。它可以减少空区域计算，但阈值设置过高可能裁掉较弱的烟雾、热量或颜色。

### 启用自适应范围（Adaptive Bounds Enabled）

启用自适应范围（Adaptive Bounds Enabled）控制自适应边界（Adaptive Bounds）是否工作。

关闭后，求解器使用完整域大小（Domain Size）计算。开启后，额外体素（Extra Voxels）和各通道追踪阈值会参与活动区域判断。

### 额外体素（Extra Voxels）

额外体素（Extra Voxels）控制自适应范围边界外额外保留多少体素作为缓冲。

数值越高，自适应边界越不容易裁掉运动前缘，但计算范围更大。数值太低时，快速扩散或快速移动的烟雾可能贴近边界。

### 追踪烟雾（Track Smoke）

追踪烟雾（Track Smoke）控制自适应范围是否根据烟雾通道扩展。

它需要烟雾通道（Smoke Channel）开启。关闭后，烟雾值不会单独驱动自适应范围。

### 烟雾阈值（Smoke Threshold）

烟雾阈值（Smoke Threshold）控制多少烟雾值会被视为自适应范围内的有效区域。

阈值越高，淡烟越容易被裁掉；阈值越低，自适应范围会保留更多微弱烟雾。

### 追踪温度（Track Temperature）

追踪温度（Track Temperature）控制自适应范围是否根据温度通道扩展。

它需要温度通道（Temperature Channel）开启。火焰或热气需要在烟雾很少时继续计算，可以开启追踪温度（Track Temperature）。

### 温度阈值（Temperature Threshold）

温度阈值（Temperature Threshold）控制多少温度值会被视为自适应范围内的有效区域。

阈值越高，只有高温区域会保留；阈值越低，较弱热区也会保留。

### 追踪燃料（Track Fuel）

追踪燃料（Track Fuel）控制自适应范围是否根据燃料通道扩展。

它需要燃料通道（Fuel Channel）开启。燃料还没燃烧但需要继续参与后续燃烧时，应确认追踪燃料（Track Fuel）没有关闭。

### 燃料阈值（Fuel Threshold）

燃料阈值（Fuel Threshold）控制多少燃料值会被视为自适应范围内的有效区域。

阈值过高可能让稀薄燃料提前被裁掉，影响后续点火和燃烧。

### 追踪速度（Track Velocity）

追踪速度（Track Velocity）控制自适应范围是否根据速度场扩展。

它适合保留只有运动但烟雾、温度或燃料较弱的区域。关闭后，自适应范围主要依赖其他通道判断。

### 速度阈值（Velocity Threshold）

速度阈值（Velocity Threshold）控制多少速度值会被视为自适应范围内的有效区域。

阈值越高，只有强运动区域会保留；阈值越低，较弱流动也会扩大自适应范围。

### 追踪颜色（Track Color）

追踪颜色（Track Color）控制自适应范围是否根据颜色通道扩展。

它需要颜色通道（Color Channel）开启。只用颜色标记烟雾或流体区域时，需要确认追踪颜色（Track Color）开启。

### 颜色阈值（Color Threshold）

颜色阈值（Color Threshold）控制多少颜色值会被视为自适应范围内的有效区域。

阈值过高可能裁掉颜色较弱的区域；阈值较低会保留更多颜色数据。

### 域边界墙（Domain Boundary Walls）

域边界墙（Domain Boundary Walls）控制模拟域六个方向是否关闭为墙。

关闭某个方向时，流体可以按开放边界理解；开启某个方向时，该边界会阻挡流体通过。它适合控制烟雾是否能从域边缘流出。

### 正 X 墙（+X Wall）

正 X 墙（+X Wall）控制模拟域正 X 方向边界是否关闭。

开启后，流体在正 X 边界会被墙阻挡。

### 负 X 墙（-X Wall）

负 X 墙（-X Wall）控制模拟域负 X 方向边界是否关闭。

开启后，流体在负 X 边界会被墙阻挡。

### 正 Y 墙（+Y Wall）

正 Y 墙（+Y Wall）控制模拟域正 Y 方向边界是否关闭。

开启后，流体在正 Y 边界会被墙阻挡。

### 负 Y 墙（-Y Wall）

负 Y 墙（-Y Wall）控制模拟域负 Y 方向边界是否关闭。

开启后，流体在负 Y 边界会被墙阻挡。

### 正 Z 墙（+Z Wall）

正 Z 墙（+Z Wall）控制模拟域正 Z 方向边界是否关闭。

开启后，流体在正 Z 边界会被墙阻挡。

### 负 Z 墙（-Z Wall）

负 Z 墙（-Z Wall）控制模拟域负 Z 方向边界是否关闭。

开启后，流体在负 Z 边界会被墙阻挡。

### 动力学页（Dynamics）

动力学页（Dynamics）用于给爆炸特效修改器（nxExplosiaFX）的流体添加内部力、接入其他 NeXus 修改器，或让模拟流场反过来驱动发射器粒子。

它提供三个子页：

- 力（Forces）：添加湍流（Turbulence）、涡度（Vorticity）和风力（Wind）力层。
- 修改器（Modifiers）：把其他 NeXus 修改器对象接入爆炸特效修改器（nxExplosiaFX）的流体流程。
- 粒子平流（Particle Advect）：把爆炸特效修改器（nxExplosiaFX）的速度和通道数据传回发射器（nxEmitter）粒子。

### 力列表（Forces List）

力列表（Forces List）保存作用在流体上的内部力层。

插件默认添加湍流（Turbulence）和涡度（Vorticity）两层。每一层可以单独启用、改类型、调强度，并可通过映射到（Map To）让烟雾、温度、燃料、颜色、速度、位置、压力或文档时间驱动力强度。

### 力层名称（Force Layer Name）

力层名称（Force Layer Name）用于显示和识别当前力层。

湍流层会根据噪波类型自动命名，例如单纯形（Simplex）或 分形布朗运动（FBM）。手动改名后，名称只用于界面识别，不改变力层类型。

### 力层启用（Force Layer Enabled）

力层启用（Force Layer Enabled）控制当前力层是否参与流体计算。

关闭后，只禁用这一层力，不影响其他力层，也不关闭整个爆炸特效修改器（nxExplosiaFX）。

### 力层类型（Force Layer Type）

力层类型（Force Layer Type）决定当前力层向流体施加哪种效果。

插件提供三种类型：

- 湍流（Turbulence）：用噪波场打乱速度，制造翻卷、破碎和随机运动。
- 涡度（Vorticity）：增强局部旋转和卷曲感。
- 风力（Wind）：按指定方向给流体施加推力。

### 力强度（Force Strength）

力强度（Force Strength）控制当前力层对流体速度场的影响大小。

它在湍流（Turbulence）、涡度（Vorticity）和风力（Wind）里共用同一含义。数值越高，这层力越明显；数值越低，影响越弱。如果同时使用映射到（Map To），最终强度还会受到映射范围和曲线影响。

### 变化（Variation）

变化（Variation）只用于风力（Wind）力层。

它给风强度增加随机变化比例。数值越高，风的推动更不稳定；数值为 0 时，风强度按力强度（Force Strength）稳定输出。

### 方向（Direction）

方向（Direction）只用于风力（Wind）力层，控制风在世界空间里的方向。

它决定流体被推向哪里。方向向量会在同步到内部求解器时转换坐标轴，因此用户只需要按界面里的世界方向理解。

### 噪波类型（Noise Type）

噪波类型（Noise Type）只用于湍流（Turbulence）力层，控制湍流场的噪波算法。

插件提供单纯形（Simplex）、湍流（Turbulence）、波浪湍流（Wavy Turbulence）、Voronoise（Voronoise）、分形布朗运动（FBM）和立方（Cubic）。不同类型会改变流体被扰动的纹理形态。单纯形（Simplex）不使用间隙度（Lacunarity），所以该参数在单纯形（Simplex）下不可编辑。

### 力长度尺度（Force Length Scale）

力长度尺度（Force Length Scale）只用于湍流（Turbulence）力层，控制噪波变化的主要空间尺度。

数值越大，湍流块越大，烟雾翻卷更宽；数值越小，扰动更细碎。它和倍频层数（Force Octaves）一起决定湍流细节层级。

### 力倍频层数（Force Octaves）

力倍频层数（Force Octaves）只用于湍流（Turbulence）力层，控制叠加多少层噪波细节。

层数越多，湍流细节越丰富；层数越少，形态更简单。过多层数可能增加计算负担。

### 力持续度（Force Persistence）

力持续度（Force Persistence）只用于湍流（Turbulence）力层，控制每一层噪波相对上一层保留多少强度。

数值越高，高频细节更明显；数值越低，主要保留大尺度扰动。

### 力频率（Force Frequency）

力频率（Force Frequency）只用于湍流（Turbulence）力层，控制噪波随时间变化的速度。

数值越高，湍流变化越快；数值越低，扰动形态更稳定。

### 间隙度（Lacunarity）

间隙度（Lacunarity）只用于部分湍流噪波类型，控制每层噪波之间的频率倍率。

单纯形（Simplex）下该参数不可编辑。其他噪波类型中，数值越高，各层噪波尺度差异越明显。

### 映射到（Map To）

映射到（Map To）控制当前力层强度由哪类流体数据驱动。

可用数据包括无（None）、烟雾（Smoke）、温度（Temperature）、燃料（Fuel）、颜色 R（Color R）、颜色 G（Color G）、颜色 B（Color B）、速度 X（Velocity X）、速度 Y（Velocity Y）、速度 Z（Velocity Z）、速度（Speed）、位置 X（Position X）、位置 Y（Position Y）、位置 Z（Position Z）、压力（Pressure）和文档时间（Document Time）。

选择无（None）时，映射最小值（Map Min）、映射最大值（Map Max）和映射曲线（Map Curve）不参与驱动。

### 映射最小值（Map Min）

映射最小值（Map Min）控制映射输入范围的下限。

流体数据低于这个范围时，会按映射曲线（Map Curve）的起点理解。它和映射最大值（Map Max）共同决定输入数据如何转成力强度倍增器。

### 映射最大值（Map Max）

映射最大值（Map Max）控制映射输入范围的上限。

如果力层只在高温、浓烟或高速区域起作用，可以提高映射最小值（Map Min）和映射最大值（Map Max），让映射集中在目标数据范围。

### 映射曲线（Map Curve）

映射曲线（Map Curve）控制映射输入在最小值和最大值之间如何转换为力强度。

曲线低的位置会削弱当前力层，曲线高的位置会增强当前力层。它适合做“烟雾越浓湍流越强”或“温度越高风越弱”这类非线性控制。

### 修改器列表（Modifiers List）

修改器列表（Modifiers List）用于把其他 NeXus 修改器对象接入爆炸特效修改器（nxExplosiaFX）的流体流程。

这个列表接受带有 `nexus_modifier_type` 的 NeXus 对象。代码不会限制成某一个固定修改器类型，而是把有效 NeXus 对象句柄接入内部修改器树。普通网格、曲线或空物体没有 `nexus_modifier_type` 时不会同步为有效列表项。

### 修改器对象（Modifier Object）

修改器对象（Modifier Object）是修改器列表（Modifiers List）里引用的 NeXus 修改器。

它必须是有效 NeXus 修改器对象。是否产生可见效果取决于该修改器本身是否支持作用到爆炸特效修改器（nxExplosiaFX）的流体流程，不能把所有普通物体都当作有效修改器。

### 修改器启用（Modifier Enabled）

修改器启用（Modifier Enabled）控制当前修改器列表项是否参与内部修改器树。

关闭后，只禁用这一项引用，不删除场景里的修改器对象。

### 粒子平流列表（Particle Advect List）

粒子平流列表（Particle Advect List）用于让爆炸特效修改器（nxExplosiaFX）的流场影响发射器（nxEmitter）粒子。

这个列表只接受发射器（nxEmitter）。如果列表为空，爆炸特效修改器（nxExplosiaFX）不会把流场速度或通道数据传回粒子。

### 平流发射器（Particle Advect Emitter）

平流发射器（Particle Advect Emitter）是粒子平流列表（Particle Advect List）里引用的发射器（nxEmitter）。

只有有效发射器（nxEmitter）会被同步。普通网格、曲线或其他修改器不会作为粒子平流目标。

### 粒子平流启用（Particle Advect Enabled）

粒子平流启用（Particle Advect Enabled）控制当前发射器列表项是否接受爆炸特效修改器（nxExplosiaFX）的流场影响。

关闭后，只禁用这一项发射器引用，不关闭发射器本身。

### 平流模式（Advect Mode）

平流模式（Advect Mode）控制流场如何影响发射器（nxEmitter）粒子的运动属性。

插件提供三种模式：

- 位置（Position）：粒子位置跟随流场，不直接更新速度。
- 方向（Direction）：粒子方向继承流场方向，但不继承速度大小。
- 速度（Velocity）：粒子速度来自当前位置的爆炸特效修改器（nxExplosiaFX）流体速度。

### 平流强度（Advect Strength）

平流强度（Advect Strength）控制流场改变粒子运动的比例。

数值越高，粒子越贴近爆炸特效修改器（nxExplosiaFX）的流动；数值越低，粒子越保留自身原有运动。

### 属性传递（Property Transfer）

属性传递（Property Transfer）控制爆炸特效修改器（nxExplosiaFX）的通道值如何写回粒子属性。

设置（Set）会用流体通道值直接设置粒子属性。添加（Add）会把流体通道值加到粒子现有属性上。

### 烟雾传输（Smoke Transfer）

烟雾传输（Smoke Transfer）控制爆炸特效修改器（nxExplosiaFX）的烟雾通道向粒子传输的比例。

它需要烟雾通道（Smoke Channel）存在有效数据，并且当前发射器已经加入粒子平流列表（Particle Advect List）。

### 温度传输（Temperature Transfer）

温度传输（Temperature Transfer）控制爆炸特效修改器（nxExplosiaFX）的温度通道向粒子传输的比例。

它需要温度通道（Temperature Channel）存在有效数据，并且当前发射器已经加入粒子平流列表（Particle Advect List）。

### 燃料传输（Fuel Transfer）

燃料传输（Fuel Transfer）控制爆炸特效修改器（nxExplosiaFX）的燃料通道向粒子传输的比例。

它需要燃料通道（Fuel Channel）存在有效数据，并且当前发射器已经加入粒子平流列表（Particle Advect List）。

### 颜色传输（Color Transfer）

颜色传输（Color Transfer）控制爆炸特效修改器（nxExplosiaFX）的颜色通道向粒子传输的比例。

它需要颜色通道（Color Channel）存在有效数据，并且当前发射器已经加入粒子平流列表（Particle Advect List）。

### 显示（Display）

显示（Display）控制爆炸特效修改器（nxExplosiaFX）在视口中的体积预览和诊断辅助显示。

它只影响编辑器显示，不等同于渲染输出。渲染输出由渲染页（Render）里的 VDB 输出（VDB Output）和体积对象（Volume Object）控制。

### 显示子页（Display Section）

显示子页（Display Section）切换当前编辑的是体积（Volume）预览还是视口HUD（Viewport HUD）。

体积（Volume）预览用于看烟雾、火焰、燃料、颜色或速度场。视口HUD（Viewport HUD）用于看网格、域框、自适应范围、固体体素和速度场辅助线。

### 在渲染模式下显示（Show in Rendered Modes）

在渲染模式下显示（Show in Rendered Modes）控制材质预览或渲染视图中是否继续显示 NeXus 体积预览。

关闭后，材质预览或渲染视图可以交给 Eevee（Eevee）或 Cycles（Cycles）的体积材质显示，避免 NeXus 预览和渲染体积重叠。

### 绘制上采样（Draw Upscaled）

绘制上采样（Draw Upscaled）控制体积预览使用放大分辨率（Upscaling）后的数据还是基础模拟数据。

它只有在放大分辨率（Upscaling）大于 1 时可用。开启后预览更接近放大后的细节；关闭后查看基础模拟结果。

### 绘制模式（Draw Mode）

绘制模式（Draw Mode）控制体积预览使用哪种视口显示方式。

插件提供三种模式：

- 关闭（Off）：不绘制体积预览。
- 体积切片（Volume Slicing）：用面向相机的切片叠加显示体积。
- 体积光线步进（Volumetric Ray Marching）：用光线步进方式显示烟雾和火焰，效果更接近体积渲染。

### 显示通道（Display Channel）

显示通道（Display Channel）只用于体积切片（Volume Slicing），控制切片预览显示哪个流体通道。

可选项包括烟雾 + 温度（Smoke + Temperature）、烟雾 + 燃料（Smoke + Fuel）、温度（Temperature）、烟雾（Smoke）、燃料（Fuel）、颜色（Color）和速度（Speed）。选择不同通道会显示对应的样式参数。

### 切片数量（Slices）

切片数量（Slices）只用于体积切片（Volume Slicing），控制面向相机切片的数量。

数量越多，体积层次越平滑，但视口绘制成本越高。数量太低会出现明显分层。

### 显示透明度（Display Transparency）

显示透明度（Display Transparency）控制当前显示项的整体透明度。

它在切片预览、速度场和光线步进预览里共用类似含义。数值越高，显示越透明；数值越低，显示越实。

### 最小速度（Speed Min）

最小速度（Speed Min）控制速度颜色映射的下限。

低于该值的速度会按颜色或透明度曲线的低端显示。它用于速度通道切片和速度场 HUD。

### 最大速度（Speed Max）

最大速度（Speed Max）控制速度颜色映射的上限。

高于该值的速度会按颜色或透明度曲线的高端显示。如果速度颜色全部挤在一种颜色上，通常需要调整最小速度（Speed Min）和最大速度（Speed Max）。

### 速度颜色（Speed Color）

速度颜色（Speed Color）是速度可视化使用的颜色渐变。

它用于速度通道切片和速度场 HUD。渐变横轴对应最小速度（Speed Min）到最大速度（Speed Max）的范围。

### 速度透明度（Speed Alpha）

速度透明度（Speed Alpha）是速度可视化使用的透明度渐变。

它用于控制不同速度范围的可见程度。低速或高速是否显示，取决于渐变里对应位置的透明度。

### 温度颜色模式（Temperature Color Mode）

温度颜色模式（Temperature Color Mode）只用于温度相关切片通道。

黑体（Blackbody）会按黑体辐射曲线给温度着色。手动（Manual）会使用温度颜色（Temperature Color）渐变，并显示手动温度范围参数。

### 最小不透明度裁剪（Min Opacity Clip）

最小不透明度裁剪（Min Opacity Clip）控制低于某个不透明度贡献的切片是否被丢弃。

它用于烟雾、燃料和温度样式。提高它可以去掉弱贡献和噪点，但可能裁掉淡烟或弱火焰。

### 最大不透明度裁剪（Max Opacity Clip）

最大不透明度裁剪（Max Opacity Clip）控制高于某个不透明度贡献的切片如何饱和。

它用于烟雾、燃料和温度样式。降低它会让高浓度区域更快达到满显示。

### 温度颜色（Temperature Color）

温度颜色（Temperature Color）是手动温度颜色模式下使用的渐变。

它只在温度颜色模式（Temperature Color Mode）选择手动（Manual）时显示。渐变范围由最低温度（Min Temperature）和最高温度（Max Temperature）决定。

### 温度不透明度（Temperature Opacity）

温度不透明度（Temperature Opacity）控制温度通道在切片预览中的透明度曲线。

它决定不同温度范围在视口中有多可见。

### 温度透明度（Temperature Transparency）

温度透明度（Temperature Transparency）控制温度通道切片的整体透明度。

数值越高，温度显示越透明；数值越低，温度显示越实。

### 最低温度（Min Temperature）

最低温度（Min Temperature）只在温度颜色模式（Temperature Color Mode）选择手动（Manual）时使用。

它定义温度颜色（Temperature Color）渐变的低端温度。

### 最高温度（Max Temperature）

最高温度（Max Temperature）只在温度颜色模式（Temperature Color Mode）选择手动（Manual）时使用。

它定义温度颜色（Temperature Color）渐变的高端温度。

### 黑体强度（Blackbody Power）

黑体强度（Blackbody Power）只在温度颜色模式（Temperature Color Mode）选择黑体（Blackbody）时使用。

它控制黑体发光强度随温度提升的变化曲线。数值越高，高温区域亮度增长越明显。

### 黑体最小温度（Blackbody Min T）

黑体最小温度（Blackbody Min T）控制黑体发光曲线的低端温度。

低于这个温度的区域不会明显进入黑体发光范围。

### 黑体最大温度（Blackbody Max T）

黑体最大温度（Blackbody Max T）控制黑体发光曲线的高端温度。

它决定高温区域在黑体颜色和亮度映射中的上限。

### 燃料颜色（Fuel Color）

燃料颜色（Fuel Color）是燃料切片预览使用的颜色渐变。

渐变范围由最小燃料（Min Fuel）和最大燃料（Max Fuel）决定。

### 燃料透明度曲线（Fuel Alpha）

燃料透明度曲线（Fuel Alpha）控制燃料切片预览中不同燃料值的可见程度。

它和燃料透明度（Fuel Transparency）一起决定燃料通道在视口中的显示强弱。

### 燃料透明度（Fuel Transparency）

燃料透明度（Fuel Transparency）控制燃料通道切片的整体透明度。

数值越高，燃料显示越透明；数值越低，燃料显示越实。

### 最小燃料（Min Fuel）

最小燃料（Min Fuel）定义燃料颜色（Fuel Color）和燃料透明度曲线（Fuel Alpha）的低端范围。

低于该值的燃料按渐变低端显示。

### 最大燃料（Max Fuel）

最大燃料（Max Fuel）定义燃料颜色（Fuel Color）和燃料透明度曲线（Fuel Alpha）的高端范围。

如果燃料显示过于集中，可以调整最小燃料（Min Fuel）和最大燃料（Max Fuel）。

### 烟雾颜色（Smoke Color）

烟雾颜色（Smoke Color）是烟雾切片预览使用的颜色渐变。

它决定烟雾从低浓度到高浓度的颜色变化。

### 烟雾透明度曲线（Smoke Alpha）

烟雾透明度曲线（Smoke Alpha）控制烟雾切片预览中不同烟雾浓度的可见程度。

它和烟雾透明度（Smoke Transparency）一起决定烟雾显示强弱。

### 烟雾透明度（Smoke Transparency）

烟雾透明度（Smoke Transparency）控制烟雾通道切片的整体透明度。

数值越高，烟雾显示越透明；数值越低，烟雾显示越实。

### 射线最大步数（Ray Max Steps）

射线最大步数（Ray Max Steps）只用于体积光线步进（Volumetric Ray Marching）模式。

它控制每个像素沿视线最多采样多少步。数值越高，体积显示更细，但视口成本更高；数值太低可能出现穿透、层次不足或漏采样。

### 全局透明度（Global Transparency）

全局透明度（Global Transparency）控制光线步进体积预览的整体透明度。

数值越高，整个体积越透明；数值越低，烟雾和火焰越实。

### 烟雾消光（Smoke Extinction）

烟雾消光（Smoke Extinction）控制烟雾对光线的吸收和遮挡强度。

数值越高，烟雾越浓、越容易遮挡内部火焰；数值越低，烟雾更透。

### 烟雾染色（Smoke Tint）

烟雾染色（Smoke Tint）控制烟雾吸收或透射时的颜色偏向。

它用于给烟雾整体加色调，例如偏灰、偏棕或偏冷色。

### 烟雾反照率（Smoke Albedo）

烟雾反照率（Smoke Albedo）控制烟雾散射和吸收的比例。

0 更偏吸收，烟雾更暗；1 更偏散射，烟雾更容易被光照提亮。

### 烟雾散射各向异性（Smoke Scatter Anisotropy）

烟雾散射各向异性（Smoke Scatter Anisotropy）控制烟雾散射方向。

- -1 偏向后向散射。
- 0 接近各向同性散射。
- +1 偏向前向散射。

### 火焰在高于 T 时发射（Flame Emit Above T）

火焰在高于 T 时发射（Flame Emit Above T）控制温度高于多少时开始产生火焰发光。

提高它会让只有更热的区域发光；降低它会让较低温区域也参与火焰显示。

### 热烟灰发射强度（Hot Soot Emit Intensity）

热烟灰发射强度（Hot Soot Emit Intensity）控制炽热烟尘带来的火焰亮度倍率。

数值越高，火焰和热烟显示越亮；数值越低，发光更弱。

### 热气体发射强度（Hot Gas Emit Intensity）

热气体发射强度（Hot Gas Emit Intensity）控制热气体发光的强度。

它和热气体颜色模式（Hot Gas Color Mode）一起决定热气体区域的颜色和亮度。

### 热气体颜色模式（Hot Gas Color Mode）

热气体颜色模式（Hot Gas Color Mode）控制热气体发光颜色的来源。

手动（Manual）会使用热气体颜色（Hot Gas Color）。黑体（Black Body）会按黑体发光方式着色。

### 热气体颜色（Hot Gas Color）

热气体颜色（Hot Gas Color）只在热气体颜色模式（Hot Gas Color Mode）选择手动（Manual）时可编辑。

它指定热气体发光的固定颜色。

### 环境光强度（Ambient Light Intensity）

环境光强度（Ambient Light Intensity）控制光线步进预览中的环境方向光强度。

数值越高，烟雾受光更明显；数值越低，体积更暗。

### 环境光方向（Ambient Light Direction）

环境光方向（Ambient Light Direction）控制光线步进预览中环境方向光来自哪里。

它只影响视口体积预览的照明方向，不改变模拟本身。

### 环境光颜色（Ambient Light Color）

环境光颜色（Ambient Light Color）控制光线步进预览中环境方向光的颜色。

它可以让烟雾受光偏暖或偏冷。

### 绘制网格（Draw Grid）

绘制网格（Draw Grid）控制是否显示模拟体素网格辅助线。

可选项包括无（None）、体素（Voxels）、仅背面（Back only）、仅底面（Base only）和底面和背面（Base and Back）。它用于观察体素域结构，不影响模拟计算。

### 绘制域（Draw Domain）

绘制域（Draw Domain）控制是否显示完整模拟域的外框。

开启后可以检查域大小（Domain Size）是否覆盖烟雾、火焰和源对象运动范围。

### 绘制自适应边界（Draw Adaptive Bounds）

绘制自适应边界（Draw Adaptive Bounds）控制是否显示自适应范围标记。

它只有在启用自适应范围（Adaptive Bounds Enabled）开启时可编辑。用于检查自适应范围是否裁掉了烟雾、温度、燃料、速度或颜色区域。

### 绘制固体体素（Draw Solid Voxels）

绘制固体体素（Draw Solid Voxels）控制是否显示被碰撞体视为固体的体素。

它用于检查碰撞体列表（Colliders List）里的网格是否正确转成流体碰撞区域。

### 绘制速度场（Draw Velocity Field）

绘制速度场（Draw Velocity Field）控制是否显示流体速度场辅助线。

开启后可以观察流体的方向和速度分布。速度颜色（Speed Color）、速度透明度（Speed Alpha）、速度范围和尾迹长度（Trail Length）会影响显示方式。

### 自动范围（Auto Range）

自动范围（Auto Range）控制速度场 HUD 是否自动确定速度颜色范围。

开启后，最小速度（Speed Min）和最大速度（Speed Max）不可手动编辑。关闭后，用户可以自己设置速度颜色映射范围。

### 尾迹长度（Trail Length）

尾迹长度（Trail Length）控制速度场辅助线的长度。

数值越大，速度方向更容易看清，但视口可能更杂乱；数值越小，显示更简洁。

### 渲染页（Render）

渲染页（Render）控制爆炸特效修改器（nxExplosiaFX）如何把模拟数据输出给 Eevee（Eevee）或 Cycles（Cycles）。

当前界面主要围绕 OpenVDB（OpenVDB）输出和体积对象（Volume Object）链接。视口显示（Display）只负责预览，渲染页（Render）负责把模拟暴露给渲染器。

### VDB 输出（VDB Output）

VDB 输出（VDB Output）控制什么时候写出逐帧 OpenVDB（OpenVDB）文件。

插件提供三种模式：

- 关闭（Off）：不写出 OpenVDB（OpenVDB）文件。
- 渲染时（On Render）：只在 F12 渲染或动画渲染时写出 VDB。
- 实时（Live）：每次帧变化和渲染时写出 VDB，让 Eevee（Eevee）或 Cycles（Cycles）视口预览在拖动时间线时保持同步。

### VDB 输出目录（VDB Output Directory）

VDB 输出目录（VDB Output Directory）指定逐帧 OpenVDB（OpenVDB）文件写到哪里。

留空时，插件使用 Blender 会话临时目录。需要保留缓存、共享缓存或避免临时目录清理时，可以指定固定目录。

### 体积对象（Volume Object）

体积对象（Volume Object）指定一个 Blender 体积对象（Volume Object），用于把爆炸特效修改器（nxExplosiaFX）的模拟数据暴露给渲染器。

它只接受类型为体积（Volume）的对象。普通网格或空物体不会作为有效体积对象。

---

## 列表操作按钮

这些小按钮通常出现在源列表（Sources List）和碰撞体列表（Colliders List）旁边，用于管理列表内容，不参与流体物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后还需要选择源对象（Source Object）或碰撞体对象（Collider Object）。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的可用对象，再把它加入当前列表。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口中连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的列表项。它只移除列表引用，不等同于删除场景里的对象。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项向上移动一位。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）会开关当前列表项是否参与列表作用。它只影响这一项，不等同于关闭整个爆炸特效修改器（nxExplosiaFX）。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表，把当前项目向更深一层移动。普通平铺列表通常不使用这个按钮。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表，把当前项目向外提升一层。
