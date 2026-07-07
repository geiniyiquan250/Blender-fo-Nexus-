# NeXus 发射器使用说明

这份文档当前只写发射器（nxEmitter）。
目标是直接回答中文用户最关心的几件事：
- 这个参数是拿来干什么的
- 什么情况下应该调它
- 调大、调小以后，大致会出现什么变化

## 发射器（nxEmitter）

发射器（nxEmitter）是 NeXus 粒子系统里最前面的入口。它主要决定三件事：
- 粒子从哪里出生
- 粒子什么时候出生、一次出生多少
- 粒子刚出生时带着什么初始属性

当前发射器界面可以分成这些部分：
- 发射器（Emitter）：决定发射范围和发射方向
- 发射（Emission）：决定发射节奏、数量、时间范围和初始粒子属性
- 显示（Display）：主要影响视口预览，不直接等于模拟结果
- 导出（Export）：把结果输出成 Blender 点云（Point Cloud）
- 组（Groups）：把粒子分配进组
- 修改器（Modifiers）列表：限制哪些修改器会作用到这批粒子

---

## 发射器（Emitter）

这一组参数主要决定“粒子从哪里出来”。

### 子帧发射（Subframe Emit）

这个开关决定粒子是不是只在整帧出生，还是会分布到一帧内部更细的时间段里。

实用理解：
- 开启后，发射会更连续，适合高速运动、连续喷射
- 关闭后，粒子更像按帧一批一批地产生，容易看到断续感

如果你觉得发射不连贯，先看这个参数。

### 形状（Shape）

这个参数决定发射区域的类型。

可选项：
- 矩形（Rectangle）
- 圆盘（Disc）
- 球体（Sphere）
- 盒体（Box）
- 物体（Object）

常见用法：
- 做平面喷射，用矩形（Rectangle）或圆盘（Disc）
- 做体积内出生，用球体（Sphere）或盒体（Box）
- 要沿模型表面、边或点来发射，用物体（Object）

### 形状旋转（Shape Rotation）

这个参数用来改变发射平面的朝向。

它不会改变形状（Shape）本身是什么，只会改变这个发射面朝哪边。
如果发射范围没问题，但喷出的方向不对，通常先调这里。

当形状（Shape）是物体（Object）时，这个参数一般没有意义，因为发射朝向更多由物体本身的几何决定。
也就是说，它依赖“不是物体（Object）模式”才有实际作用。

### 宽度（Width）

只在矩形（Rectangle）下出现。

它控制矩形发射区域的横向尺寸。值越大，粒子出生范围越宽。
适合做横向带状喷射、宽口喷射、大片平面撒点。
它只在形状（Shape）是矩形（Rectangle）时生效。

### 高度（Height）

只在矩形（Rectangle）下出现。

它控制矩形发射区域的纵向尺寸。值越大，矩形发射区域越高。
和宽度（Width）一起看，就能理解成矩形发射面的长和宽。
它只在形状（Shape）是矩形（Rectangle）时生效。

### 发射半径（Emitter Radius）

在圆盘（Disc）和球体（Sphere）下出现。

它控制发射区域本身的大小：
- 圆盘（Disc）时，是圆盘大小
- 球体（Sphere）时，是球体大小

如果你只是想让“发射范围更大”，这个通常是最直接的参数。
它只在圆盘（Disc）和球体（Sphere）下生效。

### 盒体尺寸（Box Size）

只在盒体（Box）下出现。

它是一组三维尺寸，分别控制盒体在三个方向上的大小。
适合做立方体、长方体体积内的随机出生。
它只在盒体（Box）下生效。

### 对象（Objects）列表

只在物体（Object）下出现。

这里是一组发射来源对象。你可以把网格（Mesh）或曲线（Curve）加进来，让发射器从这些对象发射。

列表里的每个物体还可以继续设置：
- 顶点组（Vertex Group）
- 发射来源（Emit From）
- 阈值（Threshold）
- 物体方向（Object Direction）

也就是说，物体（Object）模式可以继续精确控制发射来源细节。
它只在形状（Shape）是物体（Object）时才有意义。

### 角度（Angle）

在矩形（Rectangle）和圆盘（Disc）下出现。

这个参数控制发射角，也可以理解成“喷开的程度”。

一般来说：
- 值小：更收束，方向更集中
- 值大：更发散，喷射范围更散

它不决定出生区域多大，而是决定粒子离开发射面时有多散。
它只在矩形（Rectangle）和圆盘（Disc）下生效。

### 发射方向（Emitter Direction）

在球体（Sphere）和盒体（Box）下出现。

这是体积发射时的方向模式。插件提供法线方向（Normal）、随机（Random）和固定轴向这类方向。

典型理解：
- 法线方向（Normal）：按形状表面方向发射
- 随机（Random）：方向打散
- 轴向（X/Y/Z 正负方向）：强制朝固定方向喷

如果你想让体积里的粒子明显朝某个方向运动，这个参数很关键。
它只在球体（Sphere）和盒体（Box）下生效。

### 仅边缘（Edge Only）

在矩形（Rectangle）和圆盘（Disc）下出现。

开启后，不再从整个面里发，而是只从边界发。

实际效果通常是：
- 矩形（Rectangle）更像沿外框出粒子
- 圆盘（Disc）更像沿圆环边缘出粒子

它不仅依赖形状（Shape）是矩形（Rectangle）或圆盘（Disc），还依赖发射模式（Emission Mode）是随机（Random）。
如果你切到规则（Regular）或六边形（Hexagonal），这个开关虽然还在文档里有说明，但实际界面里不会按随机发射逻辑工作。

### 仅原点（Origin Only）

在矩形（Rectangle）和圆盘（Disc）下出现。

开启后，不再按面区域分散出生，而是只从发射器原点出生。
适合保留发射朝向逻辑，但让出生点集中在一个中心点。

它也依赖发射模式（Emission Mode）是随机（Random），并且和仅边缘（Edge Only）是互斥思路：
- 开了仅边缘（Edge Only），仅原点（Origin Only）就不该再开
- 开了仅原点（Origin Only），仅边缘（Edge Only）也就没有意义

### 仅表面（Surface Only）

在球体（Sphere）和盒体（Box）下使用。

它的意思是：
- 不从体积内部随机生
- 只从外表面生

所以它相当于把体积发射改成壳层发射。
它依赖两个前提：
- 形状（Shape）是球体（Sphere）或盒体（Box）
- 发射模式（Emission Mode）是随机（Random）

---

## 物体（Object）发射模式里的单对象参数

当形状（Shape）是物体（Object）时，你在对象列表里还能看到这些参数。

### 顶点组（Vertex Group）

只在对象是网格（Mesh）时可用。

它允许你指定一个顶点组（Vertex Group），让发射只参考这个组的数据。
最常见的用法是：只让模型某一部分发射，或者用权重去控制哪些区域更容易发射。

### 发射来源（Emit From）

这是物体发射的来源方式。

插件提供这些模式：
- 多边形中心（Polygon Center）
- 多边形面积（Polygon Area）
- 点（Points）
- 边（Edges）
- 多边形中心（Polygon Center）
- 纹理（Texture）

实用理解：
- 点（Points）：更像从点发
- 边（Edges）：更像从边发
- 多边形中心（Polygon Center）和多边形面积（Polygon Area）：更像从面发
- 纹理（Texture）：和贴图或权重分布有关

它只在形状（Shape）是物体（Object）时才有意义。

### 阈值（Threshold）

这个参数会作为物体发射里的一个筛选阈值传到底层逻辑里。
结合顶点组（Vertex Group）去看，它更像一个“低于多少就不发”的门槛。

简单理解：
- 值高：筛得更严
- 值低：放得更宽

它也是物体（Object）发射模式下的联动参数，通常要配合顶点组（Vertex Group）或贴图/权重类来源去理解。

### 物体方向（Object Direction）

这是物体表面发射时的方向模式。

插件提供这些方向：
- 法线方向（Normal）
- 随机（Random）
- 面方向（Faces）
- Phong 法线方向（Phong Normal）
- 轴向（X/Y/Z 正负方向）

如果你想让粒子顺着表面法线喷出，或者强制统一朝某个轴向发，这个参数就是入口。
它只在形状（Shape）是物体（Object）时才有实际意义。

---

## 发射（Emission）

这一组参数主要决定“什么时候发、一次发多少、粒子出生时带什么初始值”。

### 发射类型（Emit Type）

这是发射器最重要的节奏参数之一。

插件提供三种主要模式：
- 速率（Rate）
- 脉冲（Pulse）
- 单次发射（Shot）

直观理解：
- 速率（Rate）：持续不断地产生粒子
- 脉冲（Pulse）：发一阵，停一阵，再发一阵
- 单次发射（Shot）：在某个时间点或短时间段里打一批

### 发射模式（Emission Mode）

这个参数主要控制发射分布的方式。

可选项：
- 随机（Random）
- 规则（Regular）
- 六边形（Hexagonal）

实用理解：
- 随机（Random）：出生点更随机
- 规则（Regular）：分布更整齐
- 六边形（Hexagonal）：更偏向高密度、均匀的排布

如果你想做整齐分布，不要只盯着出生速率（Birth Rate），还要看这里。
它本身也会联动很多别的参数：
- 仅边缘（Edge Only）/ 仅原点（Origin Only）/ 仅表面（Surface Only）主要依赖随机（Random）
- 间距（Spacing）只在规则（Regular）和六边形（Hexagonal）下有意义
- 单次数量（Shot Count）在单次发射（Shot）下，如果模式是规则（Regular）或六边形（Hexagonal），就不再作为主控制项显示
- 出生速率（Birth Rate）和出生速率变化（Birth Rate Var）在规则（Regular）/ 六边形（Hexagonal）下不会作为主要发射密度入口

### 间距（Spacing）

主要在规则（Regular）和六边形（Hexagonal）下有意义。

这里的间距表示粒子之间的距离比例，基准是粒子直径。

所以它会和粒子半径（Particle Radius）联动：
- 间距大：排得更疏
- 间距小：排得更密

它依赖两个前提：
- 发射类型（Emit Type）是速率（Rate）或单次发射（Shot）
- 发射模式（Emission Mode）是规则（Regular）或六边形（Hexagonal）

### 单次数量（Shot Count）

只在单次发射（Shot）下使用。

它控制一次要发多少粒子，适合爆发、喷发、突然出现一团粒子的情况。
它只在单次发射（Shot）下使用。
而且如果发射模式（Emission Mode）是规则（Regular）或六边形（Hexagonal），这个值不会作为主控制项显示，因为数量会更多交给规则排布逻辑去估算。

### 单次开始（Shot Start）

只在单次发射（Shot）下使用。

控制这一次发射从什么时候开始。
它只在单次发射（Shot）下使用。

### 单次持续时间（Shot Duration）

只在单次发射（Shot）下使用。

它控制这一批发射摊开多久。
- 值很短：更像瞬间打出一批
- 值拉长：这批粒子会分散到更长的时间段里出生

它只在单次发射（Shot）下使用。

### 脉冲长度（Pulse Length）

只在脉冲（Pulse）下使用。

控制每一次“开喷”持续多久。

### 脉冲间隔（Pulse Interval）

只在脉冲（Pulse）下使用。

控制两次脉冲之间停多久。
和脉冲长度（Pulse Length）配合，就能做出规律性的断续喷射。

### 出生速率（Birth Rate）

这是速率（Rate）模式下最直接的数量控制项。
从属性定义看，它表示每帧产生多少粒子。

如果你只是想让粒子“更多”或者“更少”，通常先调这个。
但它不是永远都会作为主入口出现。
下面这些情况，它不会作为主要密度控制项出现：
- 发射类型（Emit Type）是单次发射（Shot）
- 发射模式（Emission Mode）是规则（Regular）或六边形（Hexagonal）

### 出生速率变化（Birth Rate Var）

这是出生速率（Birth Rate）的随机变化量。
适合让发射不要每一帧都一样整齐，看起来更自然。
它和出生速率（Birth Rate）一样，依赖“不是单次发射（Shot）”且“不是规则/六边形模式”时才作为主要入口出现。

### 速度（Speed）

这是粒子出生时的初始速度。
最直接的理解就是：粒子一出生，先带着多大的速度离开发射器。

如果你觉得粒子喷不出去，或者飞得过猛，先改这里。

### 速度变化（Speed Var）

控制不同粒子之间的初始速度差异。
如果速度（Speed）是整体基准，这个就是让每个粒子不要完全一样。

### 粒子半径（Particle Radius）

这个参数控制粒子的物理半径。
它不只是显示大小。它还会影响规则排布时的数量估算，因为间距（Spacing）就是按粒子直径来的。

### 半径变化（Radius Var）

控制粒子半径的随机变化。
适合做大小不完全一致的粒子群。

### 质量（Mass）

控制每个粒子的初始质量基准。
如果后面有受力、碰撞、约束之类的效果，这个值会影响粒子反应。

### 质量变化（Mass Var）

控制粒子质量之间的随机差异。
它常用来避免所有粒子后续反应都太一致。

### 全程发射（Emit All）

这个开关决定是否在整个时间段里都允许发射。

开启后：
- 发射开始（Emit Start）
- 发射结束（Emit End）

这两个参数会在界面里失效。
所以它本身就是一个联动总开关：
- 开启后，起止时间不再单独控制
- 关闭后，发射开始（Emit Start）和发射结束（Emit End）才真正生效

### 发射开始（Emit Start）

当全程发射（Emit All）关闭时，这里决定从什么时候开始产生粒子。
也就是说，它依赖全程发射（Emit All）关闭才有意义。

### 发射结束（Emit End）

当全程发射（Emit All）关闭时，这里决定什么时候停止产生新粒子。
它同样依赖全程发射（Emit All）关闭才有意义。

### 完整生命（Full Lifespan）

这个开关决定粒子是不是直接使用完整寿命逻辑。

开启后：
- 寿命（Lifespan）
- 变化（Variation）

这两个参数会在界面里失效。
所以它和全程发射（Emit All）很像，也是一个上层联动开关：
- 开启后，不再手动单独调寿命
- 关闭后，寿命（Lifespan）和变化（Variation）才真正进入手调流程

### 寿命（Lifespan）

控制粒子寿命的基础值。
可以理解成每个粒子大致活多久。
它依赖完整生命（Full Lifespan）关闭才有意义。

### 变化（Variation）

控制粒子寿命的随机变化。
适合避免粒子整批同时消失。
它也依赖完整生命（Full Lifespan）关闭才有意义。

---

## 显示（Display）

这一页主要是“怎么查看”，不是“怎么模拟”。
也就是说，这里的很多参数主要影响视口预览，不一定直接改变底层发射逻辑。

### 视口可见（Visible in Editor）

控制发射器对象本身在视口里的显示。
如果发射器已经摆好了，不想一直看见这个辅助物体，可以关掉它。

### 显示粒子（Show Particles）

控制是否在视口里显示这批粒子。
如果视口太乱、太卡，可以先关掉它，不影响你保留发射器设置。

### 颜色模式（Color Mode）

控制粒子在视口里的上色方式。

插件提供这些模式：
- 单一颜色（Single Color）
- 梯度（Gradient）
- 着色器（Shader）
- 物体颜色（Object Color）
- 噪波（Noise）

简单理解：
- 单一颜色（Single Color）：全部用一种颜色
- 梯度（Gradient）：按某个粒子参数去映射颜色
- 噪波（Noise）：按噪波图案给颜色

它是显示区里很重要的联动总开关：
- 单一颜色（Single Color）时，下面主要看粒子颜色（Particle Color）
- 梯度（Gradient）时，下面主要看参数（Parameter）、自动缩放（Autoscale）、最小（Min）、最大（Max）和梯度条本身
- 噪波（Noise）时，下面主要看噪波类型（Noise Type）、颜色通道（Color Channel）以及整组噪波参数
- 着色器（Shader）和物体颜色（Object Color）不会走单色/渐变/噪波这一套附加参数

### 粒子颜色（Particle Color）

只在单一颜色（Single Color）下使用。
它就是最直接的统一颜色设置。

### 梯度（Gradient）

只在梯度（Gradient）模式下使用。
你可以把它理解成一条颜色带，然后再用下面的参数（Parameter）去决定“哪种粒子数据驱动这条颜色带”。
它依赖颜色模式（Color Mode）是梯度（Gradient）。

### 参数（Parameter）

只在梯度（Gradient）模式下使用。

插件提供很多来源，例如：
- 年龄（Age）
- 速度（Speed）
- 半径（Radius）
- 质量（Mass）
- 温度（Temperature）
- 烟雾（Smoke）
- 燃料（Fuel）
- 移动距离（Distance Traveled）
- 旋转（Rotation）

常见理解：
- 想看速度分布，就选速度（Speed）
- 想看新旧变化，就选年龄（Age）
- 想看粒径差异，就选半径（Radius）

它只在颜色模式（Color Mode）是梯度（Gradient）时才有意义。

### 自动缩放（Autoscale）

控制渐变范围是不是自动适配当前粒子数据。

开启时，系统自动计算范围。
关闭时，你自己用最小（Min）和最大（Max）手动指定范围。
它依赖颜色模式（Color Mode）是梯度（Gradient）。

### 最小（Min）

只在自动缩放（Autoscale）关闭时真正有控制意义。
它决定渐变左端从哪个数值开始。
也就是说，它同时依赖两个前提：
- 颜色模式（Color Mode）是梯度（Gradient）
- 自动缩放（Autoscale）关闭

### 最大（Max）

只在自动缩放（Autoscale）关闭时真正有控制意义。
它决定渐变右端到哪个数值结束。
它也同时依赖：
- 颜色模式（Color Mode）是梯度（Gradient）
- 自动缩放（Autoscale）关闭

### 噪波类型（Noise Type）

只在噪波（Noise）颜色模式下使用。

插件提供：
- 单纯形（Simplex）
- fBm（fBm）
- 湍流（Turbulence）
- 波浪湍流（Wavy Turbulence）
- 沃罗诺伊噪波（VoroNoise）
- 立方（Cubic）

这一类参数主要影响颜色图案风格，不影响发射数量。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 颜色通道（Color Channel）

只在噪波（Noise）颜色模式下使用。
控制噪波结果如何转成颜色输出。
如果这里选择的是梯度（Gradient）通道，界面还会额外显示一条用于噪波映射的梯度条。

### 种子（Seed）

控制噪波分布的随机偏移。
最直观的效果是：图案换一套分布，但整体风格不变。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 缩放（Scale）

控制噪波图案的尺度大小。
- 值大：图案更粗、更大块
- 值小：图案更细、更密
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 持续度（Persistence）

这是噪波分层里的参数之一。
简单理解成每一层细节保留多少强度。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 间隙度（Lacunarity）

这是噪波分层里的参数之一。
简单理解成每一层频率增长多少。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 频率（Frequency）

这是噪波的基础频率。
调它通常会直接改变图案疏密。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 倍频层数（Octaves）

控制噪波叠加多少层。
层数越多，图案通常越复杂。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 低裁切（Low Clip）

用来裁掉噪波中偏低的数值区域。
适合压缩颜色分布范围。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 高裁切（High Clip）

用来裁掉噪波中偏高的数值区域。
也常用于压缩对比区间。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 亮度（Brightness）

对噪波颜色结果再做整体明暗调整。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 对比度（Contrast）

对噪波颜色结果再做强弱对比调整。
它依赖颜色模式（Color Mode）是噪波（Noise）。

### 显示模式（Display Mode）

这个参数决定粒子在视口里画成什么形状。
它主要影响“怎么看”，方便你检查方向、大小、分布和流体外观。
它也是显示区的大联动开关，后面很多参数都要跟着它看：
- 粒子大小（Particle Size）主要对应点（Points）
- 长度模式（Length Mode）和长度相关参数主要对应方向线/箭头
- 旋转（Rotation）和向上矢量（Up Vector）主要对应有明确朝向的 3D 形状
- 屏幕空间流体参数（SSF Parameters）只对应屏幕空间流体（Screen Space Fluid）

### 粒子大小（Particle Size）

主要在点状显示下使用。
控制视口里粒子的显示大小。
它依赖显示模式（Display Mode）是点（Points）。

### 长度模式（Length Mode）

主要在线条、箭头这类显示模式下使用。
它决定线长是按什么来算，例如按速度、按半径或固定长度。
它依赖显示模式（Display Mode）是方向（Direction）、箭头（Arrow）或实心箭头（Arrow Filled）。

### 固定长度（Fixed Length）

只在长度模式（Length Mode）为固定时使用。
表示所有线都用同样长度。
它依赖两个前提：
- 显示模式（Display Mode）是方向线/箭头类
- 长度模式（Length Mode）是固定（Fixed）

### 限制长度（Clamp Length）

当线长由速度或半径驱动时，有时会太短看不见，或者太长挡视图。
这个开关就是拿来限制线长范围的。
它依赖：
- 显示模式（Display Mode）是方向线/箭头类
- 长度模式（Length Mode）不是固定（Fixed）

### 最小长度（Min Length）

在限制长度（Clamp Length）开启后生效。
它规定线条至少显示多长。
它依赖三个前提：
- 显示模式（Display Mode）是方向线/箭头类
- 长度模式（Length Mode）不是固定（Fixed）
- 限制长度（Clamp Length）开启

### 最大长度（Max Length）

在限制长度（Clamp Length）开启后生效。
它规定线条最多显示多长。
它也依赖上面同样这三个前提。

### 旋转（Rotation）

在盒体、箭头、金字塔、轴向这类“有朝向的显示形状”里使用。
它控制粒子的显示朝向怎么生成。
它依赖显示模式（Display Mode）属于这些有明确朝向的 3D 形状：
- 3D 盒体（Box 3D）/ 3D 实心盒体（Box 3D Filled）
- 锥体（Pyramid）/ 实心锥体（Pyramid Filled）
- 箭头（Arrow）/ 实心箭头（Arrow Filled）
- 轴（Axis）

### 向上矢量（Up Vector）

和旋转（Rotation）配合使用。
可以理解成“这个显示形状的上方朝哪里”。
它和旋转（Rotation）共享同一组显示模式条件。

### 屏幕空间流体参数（SSF Parameters）

当显示模式（Display Mode）选成屏幕空间流体（Screen Space Fluid）时，这一组参数会出现。
这组参数用于调整流体在视口里的视觉外观，不改变发射逻辑。
也就是说，这整组都依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid）。

### 预设（Preset）

插件提供这些预设：
- 自定义（Custom）
- 默认（Default）
- 深蓝水（Deep Blue Water）
- 透明水（Transparent Water）
- 绿色粘液（Green Slime）

如果你只是想快速看效果，先选一个预设；要细调，再切到自定义（Custom）。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid）。
而且它本身还是 SSF 参数区的上层联动开关：
- 选预设时，下面大多数 SSF 细项会跟着预设走
- 只有切到自定义（Custom），下面那些 SSF 细调项才真正开放手动编辑

### 模糊迭代次数（Blur Iterations）

控制屏幕空间流体（Screen Space Fluid）深度模糊迭代次数。
它依赖：
- 显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid）
- 预设（Preset）是自定义（Custom）

### 模糊半径（Blur Radius）

控制模糊核范围大小。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 深度衰减（Depth Falloff）

控制深度差异对模糊权重的影响。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 厚度模糊（Thickness Blur）

控制厚度图的模糊强度或模糊次数。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 吸收（Absorption）

控制流体的吸收感强弱。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 菲涅耳强度（Fresnel Power）

控制边缘高光和掠射感强弱。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 启用各向异性（Anisotropic Particles）

控制是否按速度方向拉伸粒子外观。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 各向异性缩放（Anisotropy Scale）

控制速度对拉伸程度的影响强度。
它依赖三个前提：
- 显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid）
- 预设（Preset）是自定义（Custom）
- 启用各向异性（Anisotropic Particles）开启

### 最大拉伸（Max Stretch）

控制最多允许拉伸到多长。
它也依赖：
- 显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid）
- 预设（Preset）是自定义（Custom）
- 启用各向异性（Anisotropic Particles）开启

### 薄处不透明度（Thin Opacity）

控制薄区域的最低不透明度。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 背景（Background）

控制透过流体时看到的背景颜色。
它依赖显示模式（Display Mode）是屏幕空间流体（Screen Space Fluid），并且预设（Preset）是自定义（Custom）。

### 显示约束（Display Constraints）

开启后，视口会显示粒子之间的约束连线颜色。
它更偏向调试和观察用途。

这里要特别注意，它不是单独就能看到效果的参数。
只有当这批粒子后面真的接入了约束修改器（nxConstraints / NX_CONSTRAINTS）时，这个开关才有实际意义。

按当前插件的工作方式看：
- 发射器（nxEmitter）这里只负责“要不要显示约束线”和“这些约束线用什么颜色”
- 真正产生约束关系的是约束修改器（nxConstraints / NX_CONSTRAINTS）

当前发射器里能直接设置颜色的约束类型只有四种：
- 出生连接约束（Connection Birth / CON_BIRTH）
- 距离连接约束（Connection Distance / CON_DISTANCE）
- 自定义连接约束（Connection Custom / CON_CUSTOM）
- 粘度约束（Viscosity / VISCOSITY）

也就是说，如果你场景里没有接约束修改器（nxConstraints），或者约束修改器里没有启用这些约束层，那这里即使开了，也不会有你想看的连线显示。

### 出生（Birth）

控制出生（Birth）约束在视口中的显示颜色。
它对应约束修改器（nxConstraints）里的出生连接约束（Connection Birth / CON_BIRTH）。

### 距离（Distance）约束颜色

控制距离（Distance）约束在视口中的显示颜色。
它对应约束修改器（nxConstraints）里的距离连接约束（Connection Distance / CON_DISTANCE）。

### 自定义（Custom）

控制自定义（Custom）约束在视口中的显示颜色。
它对应约束修改器（nxConstraints）里的自定义连接约束（Connection Custom / CON_CUSTOM）。

### 粘度（Viscosity）

控制粘度（Viscosity）约束在视口中的显示颜色。
它对应约束修改器（nxConstraints）里的粘度约束（Viscosity / VISCOSITY）。

---

## 导出（Export）

### 创建点云（Create Point Cloud）

这个开关会把当前发射器粒子输出成 Blender 点云（Point Cloud）对象。

当前点云导出会这样工作：
- 开启后会创建或更新一个点云对象
- 关闭后会删除这个点云对象
- 点的位置一定会写进去
- 其他粒子属性是否写入，取决于下面的传递属性（Transfer Properties）设置

所以它是导出区的总开关：
- 开启后，发射器会在 Blender 里生成一个子级点云对象
- 关闭后，这个点云对象会被移除
- 下面的传递属性（Transfer Properties）和自定义属性勾选，都是围绕这个点云导出流程来的

### 传递属性（Transfer Properties）

决定点云里还要不要带更多粒子属性。

可选项：
- 基础（Basic）
- 全部（All）
- 自定义（Custom）

它依赖创建点云（Create Point Cloud）这个流程。
并且它本身还会继续联动下面的导出项：
- 基础（Basic）时，只传一组基础常用属性
- 全部（All）时，尽量把支持的属性都传过去
- 自定义（Custom）时，下面那组属性勾选才真正决定导出什么

### 自定义属性勾选（Custom Export Properties）

在自定义（Custom）模式下，你可以手动决定要不要导出这些属性：
- 速度（Velocity）
- 颜色（Color）
- 半径（Radius）
- 旋转（Rotation）
- 质量（Mass）
- 时间（Time）
- 显示模式（Display Mode）
- 组（Group）
- 发射器索引（Emitter Index）
- 缩放（Scale）
- 生命（Life）
- ID（ID）
- 距离（Distance）
- 颗粒（Granular）
- 流体表面（Fluid Surface）
- 密度（Density）
- 烟雾（Smoke）
- 温度（Temperature）
- 燃料（Fuel）

它依赖传递属性（Transfer Properties）是自定义（Custom）时才有意义。

---

## 组（Groups）

### 分组模式（Group Mode）

这一组参数决定粒子进入组时怎么分配。

插件提供三种方式：
- 随机（Random）
- 连续（Sequential）
- 仅第一组（First Group Only）

这个参数要和下面的分组（Groups）列表一起看。
如果你根本没有往分组列表里放任何 nx 组（nxGroup），那模式本身也没有实际分配对象。

### 组（Groups）列表

这是一个组对象列表。
列表里只能放 nx 组（nxGroup）。
如果你后面想按组来控制粒子行为，这里就是入口。
它依赖后续场景里真的存在 nx 组（nxGroup）对象。
而且这个列表只会把“已启用的、类型确实是 NX_GROUP 的组对象”同步给发射器。

---

## 修改器（Modifiers）列表

### 修改器（Modifiers）列表

这是一个修改器对象列表。
发射器会通过它来组织“这批粒子要受哪些修改器影响”。
如果你的系统比较复杂，这里相当于发射器和后续修改器之间的连接口。
它依赖后面真的有其他 NeXus 修改器对象。
如果这里没挂任何后续修改器，这个发射器生成出来的粒子就不会继续进入那些后续修改流程。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是发射器（nxEmitter）的主参数页。这里主要编辑粒子从哪里出生、用什么形状出生、按什么节奏出生，以及初始速度、半径、质量和寿命等基础属性。

如果你要调整“粒子怎么产生”，通常先回到物体属性（Object Properties）页。显示（Display）页只影响查看方式，导出（Export）页只影响点云导出，组（Groups）和修改器（Modifiers）主要负责把粒子接入后续流程。

### 显示（Display）

显示（Display）用于控制发射器（nxEmitter）和粒子在视口中的显示方式。这里的参数主要影响编辑器里怎么看粒子，例如颜色、大小、线段显示、屏幕空间流体显示和约束显示颜色。

它通常不改变粒子的出生数量、速度或寿命。如果模拟结果没有变化，但视口显示变了，优先检查显示（Display）里的显示模式（Display Mode）、颜色模式（Color Mode）和显示约束（Display Constraints）。

### 导出（Export）

导出（Export）用于把发射器（nxEmitter）的粒子结果转换或传递给 Blender 可用的数据，例如点云。这里的重点是创建点云（Create Point Cloud）和传递属性（Transfer Properties）。

如果你只是想在 NeXus 内部继续模拟粒子，通常不需要改导出（Export）。如果你想把粒子结果交给几何节点、材质或其他 Blender 流程使用，再检查这里。

### 分组页（Groups Tab）

分组页（Groups Tab）用于把这个发射器（nxEmitter）生成的粒子分配到 nx 组（nxGroup）。它和通用页签里的组（Groups Affected）不是同一件事。

分组页（Groups Tab）决定“发射器把粒子放进哪些组”。组（Groups Affected）决定“当前对象只影响哪些已有组”。如果你要让后续修改器只处理某些粒子，通常先在这里分组，再在后续修改器的组（Groups Affected）里选择对应组。

### 修改器页（Modifiers Tab）

修改器页（Modifiers Tab）用于指定这个发射器（nxEmitter）生成的粒子后续要进入哪些 NeXus 修改器流程。

如果发射器能产生粒子，但重力、碰撞、约束或其他效果没有作用，先检查修改器页（Modifiers Tab）里是否已经加入对应修改器对象，并确认列表项处于启用状态。

### 设置页（Section）

设置页（Section）是发射器（nxEmitter）面板顶部的页签切换。它不直接改变粒子结果，而是切换当前正在编辑哪一类设置。

发射器（nxEmitter）除了自身的发射、显示、导出、分组和修改器列表外，也会带有普通 NeXus 修改器通用页签，例如组（Groups Affected）、映射（Mapping）和衰减（Falloff）。这些页签是通用框架提供的，不是发射器专属参数。

### 启用（Enabled）

启用（Enabled）控制当前项目是否参与流程。它在不同位置代表不同层级：

- 在发射器（nxEmitter）本体上，启用（Enabled）控制整个发射器是否参与粒子流程。
- 在组（Groups Affected）列表里，启用（Enabled）控制当前这个组限制是否生效。
- 在映射（Mapping）列表里，启用（Enabled）控制当前这一条映射层是否生效。
- 在衰减（Falloff）列表里，启用（Enabled）控制当前这个衰减对象是否参与影响范围计算。

如果你只是想临时停用某个组、映射或衰减，不要关闭整个发射器（nxEmitter）的启用（Enabled），而是关闭对应列表项自己的启用（Enabled）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制组（Groups Affected）列表中当前组限制是否生效。

关闭它只会停用这一条组过滤项，不会删除组对象，也不会关闭整个发射器（nxEmitter）。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制映射（Mapping）列表中当前映射层是否生效。

关闭它会让这一条粒子数据驱动规则暂时不参与计算，物体属性（Object Properties）里的固定参数仍然保留。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制衰减（Falloff）列表中当前衰减对象是否参与影响范围计算。

关闭它只会忽略这一条衰减对象，不会删除衰减对象本身。

### 组（Groups Affected）

组（Groups Affected）用于限制这个发射器或修改器影响哪些 nx 组（nxGroup）。

发射器（nxEmitter）本身已经有分组（Groups）列表，它用于把粒子分配到组。组（Groups Affected）是通用过滤页签，用于限制当前对象对哪些组起作用。两者不要混淆：

- 分组（Groups）列表：发射器把粒子放进哪些组。
- 组（Groups Affected）：当前对象只影响哪些已有组。

如果这里不添加任何组，通常表示不额外按组过滤。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要手动调它。它只决定界面正在编辑列表里的哪一项。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器、碰撞体或其他修改器对象不会作为有效组过滤使用。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里真的存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

基本逻辑是：选择粒子数据（Particle Data）作为输入，选择要控制的目标参数（Mapping Parameter），再用范围（Range Min / Range Max）、映射权重（Mapping Weight）、钳制（Clamp）和曲线决定输入如何转换成参数变化。

如果映射（Mapping）里没有任何层，参数就按物体属性（Object Properties）里的固定值工作。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会真正参与映射。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制哪个参数。

可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。如果目标参数没有选择，映射层不会产生实际效果。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）和组（Group）。

选择不同粒子数据（Particle Data）后，范围（Range Min / Range Max）的含义也会跟着变化。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

发射器（nxEmitter）不是这种内部多层修改器时，这个字段通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

如果粒子数据低于这个值，会按钳制（Clamp）设置处理。它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

范围太窄时，变化可能过于突然；范围太宽时，变化可能不明显。如果映射没有效果，先检查粒子数据实际值是否落在这个范围内。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。它不会改变粒子数据本身，只改变映射结果混入目标参数的比例。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供三种模式：

- 钳制（Clamp）：超出范围后停在边界值。
- 循环（Cycle）：超出范围后按区间循环。
- 继续（Continue）：超出范围后继续按趋势外推。

### 衰减（Falloff）

衰减（Falloff）用于用衰减对象控制影响范围。

如果你想控制“哪里受影响”，用衰减（Falloff）；如果想控制“哪些组受影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

普通用户通常不需要手动调它。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。如果场景里没有合适的衰减对象，可以用衰减页右侧的创建按钮新建一个。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前发射器（nxEmitter）或修改器。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

常见模式包括法线方向（Normal）、添加（Add）、减去（Subtract）、相乘（Multiply）、差值（Difference）、屏幕（Screen）、叠加（Overlay）、最小（Min）和最大（Max）。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、修改器列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。

它常用于没有对象拾取入口的列表，或者需要手动新增一层设置的列表。新增后，通常还需要继续选择对象、类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。

它通常出现在有多种项目类型的列表里。比如约束层、方向层、湍流层这类列表，添加前需要先选具体类型。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。

例如在组（Groups）或衰减（Falloff）相关列表里，它可以直接创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff），并自动接入当前列表。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。

启用后，鼠标会进入拾取状态。你可以在视口中点选对象，插件会把符合类型要求的对象加入列表。按 Esc 结束连续拾取。

如果列表只接受特定类型，例如 nx 组（nxGroup）、nx 衰减（nxFalloff）或网格（Mesh）物体，不符合类型的对象不会被加入。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。

它通常只移除列表引用，不等于删除场景里的对象本体。比如从组列表移除一个 nx 组（nxGroup），一般只是让当前修改器不再引用这个组。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

当列表顺序会影响计算顺序、显示顺序或叠加顺序时，这个按钮很重要。对于普通对象列表，它主要用于整理顺序。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

它和上移项（Move Item Up）配合使用，用来调整当前列表的顺序。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）会开关当前列表项是否参与当前列表的作用。

它只影响这一项，不等于关闭整个修改器。适合临时排查某个组、某个衰减对象、某个映射层或某个列表项是不是造成当前效果的原因。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表，把当前项目向更深一层移动。

它只会出现在支持层级结构的列表里。普通平铺列表不会使用这个按钮。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表，把当前项目向外提升一层。

它和增加缩进（Indent Item）配合使用，用来调整层级关系。
