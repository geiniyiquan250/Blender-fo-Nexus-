# NeXus 衰减对象使用说明

这份文档只说明 nx 衰减（nxFalloff）。它本身不直接生成粒子，也不单独推动粒子，而是作为空间范围对象，被其他支持衰减（Falloff）的修改器引用，用来控制影响在哪些区域强、哪些区域弱。

## nx 衰减（nxFalloff）

nx 衰减（nxFalloff）更像一个“空间权重体”。你把它加到别的修改器的衰减（Falloff）列表后，那个修改器的结果就会按这个对象的形状、范围和曲线被重新分配。

当前开发代码里，nx 衰减（nxFalloff）提供四种模式：

- 盒体（Box）
- 线性（Linear）
- 球体（Sphere）
- 噪波（Noise）

### 设置页（Section）

设置页（Section）切换 nx 衰减（nxFalloff）当前显示的属性页。

当前 nx 衰减（nxFalloff）只提供物体属性（Object Properties）页。

### 物体属性（Object Properties）

物体属性（Object Properties）是 nx 衰减（nxFalloff）的主设置页。这里集中设置模式（Mode）、反转（Invert）、权重（Weight）、缩放（Scale），以及当前模式对应的形状参数。

### 启用（Enabled）

启用（Enabled）控制这个 nx 衰减（nxFalloff）对象是否参与同步。

关闭后，即使它还留在别的修改器的衰减（Falloff）列表里，也不会继续作为有效衰减对象使用。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制 nx 衰减（nxFalloff）的视口辅助图形是否显示。

它只影响编辑时看到的边框、方向线和示意图，不改变实际衰减结果。

### 模式（Mode）

模式（Mode）决定当前衰减体使用哪一种空间形状或算法。

当前可选模式包括：

- 盒体（Box）：使用盒体范围。
- 线性（Linear）：沿指定方向做线性过渡。
- 球体（Sphere）：使用球形范围。
- 噪波（Noise）：使用程序噪波场。

切换模式后，当前对象名称会自动改成对应的 nx 盒体衰减（nxBox Falloff）、nx 线性衰减（nxLinear Falloff）、nx 球形衰减（nxSpherical Falloff）或 nx 噪波衰减（nxNoise Falloff）。

### 反转（Invert）

反转（Invert）用于把衰减结果反过来。

开启后，原本强的区域会变弱，原本弱的区域会变强。它适合做“区域外生效”这一类效果。

### 权重（Weight）

权重（Weight）控制当前 nx 衰减（nxFalloff）输出的整体强度。

数值越高，这个衰减对象对最终结果的调制越明显。

### 缩放（Scale）

缩放（Scale）控制整个衰减体的整体尺寸倍率。

它会统一放大或缩小当前衰减模式的有效范围。

### 方向（Direction）

方向（Direction）只在线性（Linear）模式下显示。

它决定线性衰减沿哪一个轴向展开。当前可选是 +X、-X、+Y、-Y、+Z、-Z。

### 偏移（Offset）

偏移（Offset）在线性（Linear）、球体（Sphere）和盒体（Box）模式下都会出现，但含义不完全一样：

- 在线性（Linear）模式下，它控制线性过渡带从中心向两侧展开的距离。
- 在球体（Sphere）模式下，它控制内层半径相对外半径的缩进量。
- 在盒体（Box）模式下，它控制内层盒体相对外框（Outer Box）的缩进量。

按当前开发代码：

- 球体（Sphere）模式下，偏移（Offset）不会小于 `-外半径（Outer Radius）`。
- 盒体（Box）模式下，偏移（Offset）不会小于外框（Outer Box）最短边一半的相反数。

这表示内层范围最多只能缩到 0，不能反向穿过去。

### 外半径（Outer Radius）

外半径（Outer Radius）只在球体（Sphere）模式下显示。

它定义球形衰减的外层边界。球体内部怎样从强到弱过渡，还会结合偏移（Offset）一起决定。

### 外框（Outer Box）

外框（Outer Box）只在盒体（Box）模式下显示。

它定义盒体衰减在 X、Y、Z 三个方向上的外部尺寸。

### 衰减样条（Falloff Spline）

衰减样条（Falloff Spline）只在非噪波（Noise）模式下显示。

它定义从内层到外层之间的过渡曲线。曲线越陡，边界越硬；曲线越平缓，边界越柔和。

如果你已经确定了盒体、球体或线性范围，但想精细控制“从强到弱”的节奏，主要就是调这条衰减样条（Falloff Spline）。

### 噪波类型（Noise Type）

噪波类型（Noise Type）只在噪波（Noise）模式下显示。

当前开发代码提供这些类型：

- 单纯形（Simplex）
- 卷曲（Curl）
- 湍流（Turbulence）
- 波浪湍流（Wavy Turbulence）
- 沃罗诺伊噪波（VoroNoise）
- 分形布朗运动（FBM）
- 立方（Cubic）

不同类型主要影响噪波纹理的结构和流动感。

### 种子（Seed）

种子（Seed）只在噪波（Noise）模式下显示。

它用于更换噪波图样的随机分布，但不改变当前噪波参数的总体风格。

### 对比度（Contrast）

对比度（Contrast）只在噪波（Noise）模式下显示。

按当前开发代码，它不是一个单纯的数值滑块，而是一条黑白渐变，用来重映射噪波值。你可以把它理解成“噪波输出的对比度曲线”。

### 缩放（Scale）

缩放（Scale）在噪波（Noise）模式下表示噪波图样的尺度。

数值越大，噪波结构越大块；数值越小，噪波细节越密。

### 持续度（Persistence）

持续度（Persistence）只在噪波（Noise）模式下显示。

它控制多层噪波叠加时，每一层振幅衰减得多快。

### 间隙度（Lacunarity）

间隙度（Lacunarity）只在噪波（Noise）模式下显示。

它控制多层噪波叠加时，频率递增得多快。

### 频率（Frequency）

频率（Frequency）只在噪波（Noise）模式下显示。

它控制噪波变化的密度和节奏。频率越高，图样越细；频率越低，图样越粗。

### 倍频层数（Octaves）

倍频层数（Octaves）只在噪波（Noise）模式下显示。

它决定叠加多少层不同频率的噪波。层数越高，细节通常越丰富，但结果也更复杂。

## 使用建议

- 想做明确的局部区域影响，优先用盒体（Box）或球体（Sphere）。
- 想做定向的前后渐变，优先用线性（Linear）。
- 想让影响边界带有随机纹理，再用噪波（Noise）。
- 先定形状，再调衰减样条（Falloff Spline）或对比度（Contrast），会比一开始就细调参数更容易。
