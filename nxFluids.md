# NeXus 流体修改器使用说明

这份文档只说明流体修改器（nxFluids）。它覆盖四种求解器模式：PBD（Position Based Dynamics）、SPH（Smoothed Particle Hydrodynamics）、FLIP（Fluid Implicit Particle）和 APIC（Affine Particle-In-Cell）。不同求解器显示的参数不同，通用页签（物体属性、组、映射、衰减）在所有模式下一致。

## 流体修改器（nxFluids）

流体修改器（nxFluids）用于在 NeXus 里模拟流体粒子行为。它创建后会作为流体域存在，发射器（nxEmitter）生成的粒子进入这个流体修改器（nxFluids）的影响范围后，会按当前求解器规则计算粒子间压力、黏度、表面张力、涡量等流体属性。

创建流程：先创建发射器（nxEmitter）生成粒子，再创建流体修改器（nxFluids）。流体修改器（nxFluids）创建后会自动尝试影响场景中的粒子，不同求解器模式接管粒子的条件由插件内部判定。

PBD 求解器计算快，适合实时预览和中等规模流体。SPH 求解器精度更高，支持液体和颗粒两种类型，适合黏稠液体或颗粒流。FLIP 和 APIC 求解器在体素网格上计算，适合大范围水面、波浪和飞溅场景，计算量更高。

### 设置页（Section）

设置页（Section）切换流体修改器（nxFluids）当前显示的主设置页。当前已覆盖的页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。FLIP/APIC 模式下额外包含显示（Display）页签。

### 启用（Enabled）

启用（Enabled）控制流体修改器（nxFluids）是否参与当前 NeXus 计算。关闭后，流体修改器（nxFluids）不会继续影响粒子行为，但场景中的其他修改器仍正常工作。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制流体修改器（nxFluids）在编辑器里的辅助显示是否可见。这个开关影响编辑视口显示，不等同于关闭流体计算。如果要停用流体模拟，应使用启用（Enabled）。只有 FLIP/APIC 模式才在视口里显示体素网格辅助线。

### 物体属性（Object Properties）

物体属性（Object Properties）是一个页签，包含流体修改器（nxFluids）自身的通用属性设置，如启用（Enabled）和视口可见（Visible in Editor）。这些属性在所有求解器模式下都可用。

### 求解器（Solver）

求解器（Solver）选择流体模拟的计算方式。

可选值：

- PBD（Position Based Dynamics）：基于位置的动力学求解器，速度快，适合实时预览和中型流体。
- SPH（Smoothed Particle Hydrodynamics）：平滑粒子流体动力学求解器，精度更高，支持液体（Liquid）和颗粒（Granular）两种类型。
- FLIP（Fluid Implicit Particle）：流体隐式粒子求解器，在体素网格上计算，适合大范围水面、波浪。
- APIC（Affine Particle-In-Cell）：仿射粒子网格求解器，在 FLIP 基础上提升了角动量守恒，减少飞溅时的能量损失。

切换求解器后，界面参数会整体变化。当前插件只提供这四种求解器，不同玩法间的参数不通用。

## PBD 参数

以下参数只在求解器（Solver）设为 PBD 时显示。

### 平滑半径（PBD Smoothing Radius）

平滑半径（PBD Smoothing Radius）控制 PBD 求解器里粒子间相互作用的范围半径。数值越大，粒子在更远距离就能感应彼此，流体看起来更黏滑；数值越小，粒子只在近距离接触，流体颗粒感更强。

### 子步（PBD Substeps）

子步（PBD Substeps）控制 PBD 求解器每帧内的计算次数。子步越多，流体精度越高但计算更慢；子步太少可能导致粒子穿透或抖动。

### 缓入（Ease In）

缓入（Ease In）控制 PBD 求解器从开始模拟到完全生效的过渡时间。默认 0 表示立即生效。如果希望在发射器粒子出生后逐步激活流体效果，可以调高缓入时间。

### 最小密度（PBD Min Density）

最小密度（PBD Min Density）控制 PBD 求解器每帧最少运行的密度迭代次数。数值太低可能导致粒子密度不均；数值太高会增加计算时间。

### 最大密度（PBD Max Density）

最大密度（PBD Max Density）控制 PBD 求解器每帧最多运行的密度迭代次数。求解器会在最小密度和最大密度之间自适应调节，压力越大时迭代越接近最大值。

### 密度压缩（Density Compression）

密度压缩（Density Compression）控制 PBD 求解器允许的密度压缩程度。数值越高，粒子可以更紧密地压缩在一起；数值越低，粒子保持更宽松的间距。对应流体的可压缩性。

### 检查密度（PBD Check Density）

检查密度（PBD Check Density）启用后，PBD 求解器会在每次子步后检查粒子密度是否超过密度上限（PBD Max Density Check）。当流体压力很高、粒子可能过密时，开启这个选项可以防止密度失控。

### 密度上限（PBD Max Density Check）

密度上限（PBD Max Density Check）控制检查密度（PBD Check Density）启用后的最大允许密度。超过这个值的粒子会被额外修正。只在检查密度（PBD Check Density）开启时可用。

### 检查迭代（PBD Check Iterations）

检查迭代（PBD Check Iterations）控制检查密度（PBD Check Density）启用后每次子步里密度检查的迭代次数。只在检查密度（PBD Check Density）开启时可用。

### 黏度（PBD Viscosity）

黏度（PBD Viscosity）控制 PBD 流体的黏稠程度。数值越高，粒子流得更慢、更黏稠；数值越低，流体越稀，类似水。

### 涡量（PBD Vorticity）

涡量（PBD Vorticity）控制 PBD 求解器的涡量约束强度。数值越高，流体涡旋和旋转细节越明显。

### 吸引力（Attraction）

吸引力（Attraction）控制 PBD 粒子之间的吸引力。数值越高，粒子越倾向于聚在一起；数值越低，粒子越分散。

### 排斥力（Repulsion）

排斥力（Repulsion）控制 PBD 粒子之间的排斥力。数值越高，粒子越难被压缩在一起，形成更紧密的填充分布。

### 外部压力（Ext Pressure）

外部压力（Ext Pressure）控制施加在 PBD 所有粒子上的额外均匀压力。数值越高，粒子整体被向内压缩；数值越低，外部压力越小。

## SPH 参数

以下参数只在求解器（Solver）设为 SPH 时显示。

### 流体类型（Fluid Type）

流体类型（Fluid Type）选择 SPH 求解器的模拟类型。

可选值：

- 液体（Liquid）：标准液体模拟，包含黏度、涡量、表面张力、压力等参数。
- 颗粒（Granular）：颗粒材料模拟，界面在 SPH 模式下始终绘制颗粒（Granular）参数组。当前插件无法确认这些参数是否只在颗粒类型下生效，建议以实际模拟结果为准。

### 平滑半径（SPH Smoothing Radius）

平滑半径（SPH Smoothing Radius）控制 SPH 求解器里粒子影响的范围半径。SPH 用核函数计算粒子间物理量，半径决定了每个粒子能感应到多远距离的其他粒子。数值越大，流体更平滑；数值越小，颗粒感更明显。

### 子步（SPH Substeps）

子步（SPH Substeps）控制 SPH 求解器每帧内的计算次数。增加子步会提高稳定性但减慢计算。

### 自适应子步（Adaptive Substeps）

自适应子步（Adaptive Substeps）是一个折叠开关，展开后会显示自适应子步的详细参数，包括自适应（Adaptive）、最小子步（SPH Substep Min）和 CFL（SPH CFL）。

### 自适应（Adaptive）

自适应（Adaptive）启用后，SPH 求解器会根据粒子速度和 CFL（SPH CFL）条件动态调整子步数量。启用后，最小子步（SPH Substep Min）和 CFL（SPH CFL）参数可用。

### 最小子步（SPH Substep Min）

最小子步（SPH Substep Min）控制自适应（Adaptive）启用后的最少子步数。只在自适应（Adaptive）开启时可用。

### CFL（SPH CFL）

CFL（SPH CFL）控制自适应子步的 CFL 条件。数值越低，求解器对粒子速度更敏感，子步更多；数值越高，允许更大时间步长但可能降低精度。只在自适应（Adaptive）开启时可用。

这个 CFL 是 Courant-Friedrichs-Lewy 条件的乘数，用来按粒子速度推算最小子步数。

### 阻尼（Damping）

阻尼（Damping）控制 SPH 粒子速度的衰减比例。数值越高，粒子运动越快衰减，流体看起来更黏滞。

### 缓入（SPH Ease In）

缓入（SPH Ease In）控制 SPH 求解器从开始模拟到完全生效的过渡时间。默认 0 表示立即生效。

### 最小密度（SPH Min Density）

最小密度（SPH Min Density）控制 SPH 求解器每帧最少运行的密度迭代次数。

### 最大密度（SPH Max Density）

最大密度（SPH Max Density）控制 SPH 求解器每帧最多运行的密度迭代次数。求解器在最小密度和最大密度之间自适应调节。

### 最大压缩（Max Compression）

最大压缩（Max Compression）控制 SPH 求解器允许的密度压缩上限。超过这个比例的密度压缩会被修正。

### 速度校正（Velocity Correction）

速度校正（Velocity Correction）启用后，SPH 求解器会在密度迭代后额外做一次速度修正，用于提高数值稳定性。流体压力很大或步长较大时建议开启。

### 检查密度（SPH Check Density）

检查密度（SPH Check Density）启用后，SPH 求解器会在子步后检查密度上限并修正过密粒子。

### 密度上限（SPH Max Density Check）

密度上限（SPH Max Density Check）控制 SPH 密度检查的最大允许密度。只在检查密度（SPH Check Density）开启时可用。

### 检查迭代（SPH Check Iterations）

检查迭代（SPH Check Iterations）控制 SPH 密度检查的迭代次数。只在检查密度（SPH Check Density）开启时可用。

### 黏度（SPH Viscosity）

黏度（SPH Viscosity）控制 SPH 液体的黏稠程度。数值越高，流体越黏。对应 XSPH 黏度模型的强度参数。

### 粘度迭代次数（Viscosity Iter）

粘度迭代次数（Viscosity Iter）控制 SPH 黏度求解的迭代次数。数值越高，黏度计算越精确；数值越低计算越快，但黏度效果可能不充分。

### 涡量-小尺度（Vorticity Small）

涡量-小尺度（Vorticity Small）控制 SPH 小尺度涡量约束的强度。用来补充模拟中缺失的小尺度旋转细节，只影响局部短波涡流。

### 涡量-大尺度（Vorticity Large）

涡量-大尺度（Vorticity Large）控制 SPH 大尺度涡量约束的强度。用来补充模拟中缺失的大范围旋转结构，适合产生明显的流体滚动和旋涡。

### 表面张力（SPH Surface Tension）

表面张力（SPH Surface Tension）控制 SPH 液体的表面张力强度。数值越高，流体表面更紧凑，粒子倾向于聚成水滴状；数值为 0 时无表面张力。

### 内部压力（Internal Pressure）

内部压力（Internal Pressure）控制 SPH 流体粒子自身的内部压力。数值越高，粒子更难被压缩，流体表现为更硬的物质。

### 外部压力（SPH External Pressure）

外部压力（SPH External Pressure）控制额外施加在 SPH 所有粒子上的均匀压力。用于整体压缩或扩张流体。

### 摩擦力（Friction）

摩擦力（Friction）控制 SPH 颗粒材料中粒子间的摩擦系数。界面在 SPH 模式下始终显示，当前插件无法确认是否只对颗粒（Granular）类型生效。

### 摩擦迭代次数（Friction Iterations）

摩擦迭代次数（Friction Iterations）控制颗粒摩擦求解的迭代次数。界面在 SPH 模式下始终显示，当前插件无法确认是否只对颗粒（Granular）类型生效。

### 稳定性（Stability）

稳定性（Stability）控制 SPH 颗粒模拟的数值稳定性因子。数值越高，颗粒行为更稳定但可能更僵硬。界面在 SPH 模式下始终显示，当前插件无法确认是否只对颗粒（Granular）类型生效。

### 内聚（Cohesion）

内聚（Cohesion）控制 SPH 颗粒粒子之间的内聚强度。数值越高，颗粒越容易粘在一起。界面在 SPH 模式下始终显示，当前插件无法确认是否只对颗粒（Granular）类型生效。

## FLIP / APIC 参数

以下参数只在求解器（Solver）设为 FLIP 或 APIC 时显示。FLIP/APIC 界面分为域（Domain）和求解器精度（Solver Accuracy）两个页签，在界面顶部用按钮切换。

另外 FLIP/APIC 模式还有一个额外的显示（Display）页签，用于控制视口里体素网格和液体可视化的选项。

### 域页签（FLIP Domain Tab）

域页签（FLIP Domain Tab）包含域大小、体素尺寸、时间缩放和边界墙的设置。在界面顶部切换到此页签后可见。

### 体素大小（Voxel Size）

体素大小（Voxel Size）控制 FLIP/APIC 体素网格里每个体素的世界空间尺寸。数值越小体素越多，细节越高但计算和显存开销越大；数值越大模拟更轻但细节损失。

### 域大小（Domain Size）

域大小（Domain Size）控制 FLIP/APIC 模拟域的长宽高尺寸。域越大，能容纳的流体范围越大，但体素数量随域体积快速增长。如果流体溅到域边界外面，会被边界墙处理或丢失。

### 重定时（Retiming）

重定时（Retiming）控制 FLIP/APIC 流体模拟的播放速度。默认 100% 表示正常速度；降低会让流体变慢；提高会让流体变快。

### FLIP 比例（FLIP Fraction）

FLIP 比例（FLIP Fraction）控制 FLIP 方法中 PIC（稳定）和 FLIP（飞溅）的混合比例。数值越高越偏向 FLIP，流体更具飞溅和细节；数值越低越偏向 PIC，流体更稳定但可能损失细节。只在求解器（Solver）为 FLIP 时显示，APIC 模式下不出现。

### 黏度（FLIP Viscosity）

黏度（FLIP Viscosity）控制 FLIP/APIC 流体的黏稠程度。数值为 0 时无黏度；数值越高流体越黏。

### 涡量（FLIP Vorticity）

涡量（FLIP Vorticity）控制 FLIP/APIC 涡量约束的强度。用于补充小尺度旋转细节。

### 表面张力（FLIP Surface Tension）

表面张力（FLIP Surface Tension）控制 FLIP/APIC 流体的表面张力强度。数值越高，流体表面更紧凑。

### 弱粒子排斥（Weak Particle Repulsion）

弱粒子排斥（Weak Particle Repulsion）启用后会添加粒子间的微弱排斥力，帮助减少粒子在低压力区域的堆积。启用后排斥强度（Repulsion Strength）可用。

### 排斥强度（Repulsion Strength）

排斥强度（Repulsion Strength）控制弱粒子排斥的力度。只在弱粒子排斥（Weak Particle Repulsion）开启时可用。

### 边界墙类型（Wall Type）

以下六个参数分别控制域六个面的边界类型。每个墙面可以独立设为打开（Open）、闭合（Closed）或销毁（Kill）。

- 打开（Open）：粒子可以自由穿过该墙面。
- 闭合（Closed）：粒子与墙面碰撞反弹。
- 销毁（Kill）：碰到墙面的粒子被删除。

### +X 墙（Wall +X）

+X 墙（Wall +X）控制域 +X 方向的边界类型。

### -X 墙（Wall -X）

-X 墙（Wall -X）控制域 -X 方向的边界类型。

### +Y 墙（Wall +Y）

+Y 墙（Wall +Y）控制域 +Y 方向的边界类型。

### -Y 墙（Wall -Y）

-Y 墙（Wall -Y）控制域 -Y 方向的边界类型。

### +Z 墙（Wall +Z）

+Z 墙（Wall +Z）控制域 +Z 方向的边界类型。

### -Z 墙（Wall -Z）

-Z 墙（Wall -Z）控制域 -Z 方向的边界类型。

### 求解器页签（FLIP Solver Tab）

求解器页签（FLIP Solver Tab）包含压力求解器、黏度求解器和平流求解器的精度设置。在界面顶部切换到此页签后可见。

### 压力精度（Pressure Accuracy）

压力精度（Pressure Accuracy）控制 FLIP/APIC 压力求解的精度阈值。数值越高精度越苛刻，迭代更多。

### 压力迭代（Pressure Iterations）

压力迭代（Pressure Iterations）控制 FLIP/APIC 压力求解器每次求解的最大迭代次数。达到精度阈值或最大迭代后停止。

### 黏度精度（Viscosity Accuracy）

黏度精度（Viscosity Accuracy）控制 FLIP/APIC 黏度求解的精度阈值。数值越高精度越苛刻。只在黏度（FLIP Viscosity）大于 0 时可用。

### 黏度迭代（Viscosity Iterations）

黏度迭代（Viscosity Iterations）控制 FLIP/APIC 黏度求解器每次求解的最大迭代次数。只在黏度（FLIP Viscosity）大于 0 时可用。

### CFL（FLIP CFL）

CFL（FLIP CFL）控制 FLIP/APIC 平流求解的 CFL 条件。数值越低越稳定，子步越多；数值越高允许更大时间步长但可能不稳定。

### 最小子步（Min Substeps）

最小子步（Min Substeps）控制 FLIP/APIC 每帧平流的最少子步数。

### 最大子步（Max Substeps）

最大子步（Max Substeps）控制 FLIP/APIC 每帧平流的最多子步数。求解器根据 CFL 条件在最小和最大子步之间自动调节。

## 显示（Display）

以下参数只在 FLIP/APIC 模式下的显示（Display）页签中出现。它们控制视口里体素网格、液体密度和速度的可视化方式，不影响模拟计算结果。

### 显示（Display）

显示（Display）只在 FLIP/APIC 模式下出现，用于控制体素网格、液体密度颜色和速度向量等视口辅助显示。这里的参数只影响视口可视化，不改变流体求解结果。

### 绘制网格（Draw Grid）

绘制网格（Draw Grid）控制视口里体素网格的绘制方式。

可选值：

- 无（None）：不绘制网格。
- 体素（Voxels）：绘制完整体素线框。
- 仅背面（Back only）：只绘制背向视角的网格面。
- 仅底面（Base only）：只绘制底面网格。
- 底面和背面（Base and Back）：同时绘制底面和背向面网格。

### 绘制液体体素（Draw Liquid Voxels）

绘制液体体素（Draw Liquid Voxels）启用后，视口里会用颜色标记包含液体的体素。

### 绘制固体体素（Draw Solid Voxels）

绘制固体体素（Draw Solid Voxels）启用后，视口里会用颜色标记碰撞体占据的固体体素。

### 绘制墙壁类型（Draw Wall Types）

绘制墙壁类型（Draw Wall Types）启用后，视口里的域边界墙面会根据开放/封闭/消灭类型用不同颜色标记。

### 绘制 FLIP 密度颜色（Draw FLIP/APIC Density Color）

绘制 FLIP 密度颜色（Draw FLIP/APIC Density Color）启用后，粒子会根据局部流体密度映射颜色。密度颜色（Density Color）参数控制具体颜色映射。

### 密度颜色（Density Color）

密度颜色（Density Color）用一个渐变控制粒子密度到颜色的映射。低密度对应渐变左端颜色，高密度对应渐变右端颜色。只在绘制 FLIP 密度颜色（Draw FLIP/APIC Density Color）开启时可用。

### 绘制速度向量（Draw Velocity Vectors）

绘制速度向量（Draw Velocity Vectors）启用后，视口里会显示液体速度场的方向和大小。启用后速度颜色（Speed Color）、速度透明度（Speed Alpha）和尾迹长度（Trail Length）可用。最小速度（Speed Min）和最大速度（Speed Max）还需要关闭自动范围（Auto Range）后才可手动调节。

### 速度颜色（Speed Color）

速度颜色（Speed Color）用一个渐变控制速度到颜色的映射。低速度对应渐变左端颜色，高速度对应渐变右端颜色。只在绘制速度向量（Draw Velocity Vectors）开启时可用。

### 速度透明度（Speed Alpha）

速度透明度（Speed Alpha）用一个渐变控制速度显示的透明度。只在绘制速度向量（Draw Velocity Vectors）开启时可用。

### 自动范围（Auto Range）

自动范围（Auto Range）启用后，速度颜色的最小值和最大值会根据当前帧的速度范围自动设定。关闭后需要手动设定最小速度（Speed Min）和最大速度（Speed Max）。只在绘制速度向量（Draw Velocity Vectors）开启时可用。

### 最小速度（Speed Min）

最小速度（Speed Min）手动设定速度颜色映射的最小速度值。只在自动范围（Auto Range）关闭且绘制速度向量（Draw Velocity Vectors）开启时可用。

### 最大速度（Speed Max）

最大速度（Speed Max）手动设定速度颜色映射的最大速度值。只在自动范围（Auto Range）关闭且绘制速度向量（Draw Velocity Vectors）开启时可用。

### 尾迹长度（Trail Length）

尾迹长度（Trail Length）控制视口里速度向量箭头的显示长度。只在绘制速度向量（Draw Velocity Vectors）开启时可用。

### 组（Groups Affected）

组（Groups Affected）是一个列表，列出哪些nx 组（nxGroup）受当前流体修改器（nxFluids）影响。空列表表示影响所有粒子。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中的索引。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加一个新的组条目。点击后可以从场景里拖入或选择一个nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组列表里某个条目的目标组对象。它决定了哪组粒子受流体修改器（nxFluids）影响。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动流体修改器（nxFluids）的参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则的列表，每层定义一条输入到输出的驱动关系。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中的索引。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）是被驱动的流体修改器（nxFluids）参数。

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

衰减（Falloff）用于在空间上减弱流体修改器（nxFluids）对粒子的影响。衰减对象（Falloff Objects）列表中定义的物体决定了衰减范围和形状。

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
