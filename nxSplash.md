# NeXus 飞溅修改器使用说明

这份文档只说明飞溅修改器（nxSplash）。它覆盖飞溅锥体形状、强度、时间和两条衰减曲线。该修改器会自动带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）通用页签。

## 飞溅修改器（nxSplash）

飞溅修改器（nxSplash）用于在 NeXus 里创建一个锥形飞溅区域，将经过该区域的粒子向外推离。它在视口中显示为可编辑的贝塞尔锥体，拖拽锥体上的控制点可以调整飞溅形状，创建自定义的喷溅、爆炸或浪花效果。

创建流程：创建飞溅修改器（nxSplash）后，其自身位置和方向决定飞溅锥体的朝向。飞溅修改器（nxSplash）创建后作为独立修改器参与 NeXus 流程；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，再确认流程列表包含当前飞溅修改器（nxSplash）。如果只想影响特定粒子组，可以在组（Groups Affected）列表里指定。

视口中的蓝色锥体就是飞溅区域，锥体上的控制点（Handle）可以拖拽编辑形状。页面底部还提供两条辅助曲线：飞溅衰减（Falloff）曲线控制锥体内部的空间衰减，强度衰减（Strength Falloff）曲线控制强度的额外衰减模式。

### 设置页（Section）

设置页（Section）切换飞溅修改器（nxSplash）当前显示的主设置页。当前已覆盖的页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 启用（Enabled）

启用（Enabled）控制飞溅修改器（nxSplash）是否参与当前 NeXus 计算。

关闭后，飞溅修改器（nxSplash）不会继续影响粒子。调试时可以临时关闭，用来确认画面里的飞溅效果是否来自当前这个飞溅修改器（nxSplash）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制飞溅修改器（nxSplash）在编辑器里的辅助显示是否可见。

这个开关影响编辑视口里的锥体显示，不等同于关闭飞溅计算。如果要停用飞溅效果，应使用启用（Enabled）。

### 物体属性（Object Properties）

物体属性（Object Properties）是一个页签，包含飞溅修改器（nxSplash）自身的通用属性设置，如启用（Enabled）和视口可见（Visible in Editor）。

### 重置控制柄（Reset Handles）

重置控制柄（Reset Handles）将飞溅锥体所有控制点恢复为默认位置和形状。

编辑控制点后，如果锥体变形不理想，可以点击重置回到初始状态。重置不会清空别的属性。

### 底部半径（Bottom Radius）

底部半径（Bottom Radius）控制飞溅锥体底部的半径大小。

飞溅锥体底部是靠近物体原点的端面。数值为 0 时底部收缩为一点，形成尖锥。调整后，底部一圈控制点会自动缩放。

### 高度（Height）

高度（Height）控制飞溅锥体的高度。

高度越大，飞溅区域沿局部 Z 轴越长。调整后，所有控制点的高度坐标会自动缩放。

### 顶部半径（Top Radius）

顶部半径（Top Radius）控制飞溅锥体顶部的半径大小。

飞溅锥体顶部是远离物体原点的端面。数值为 0 时顶部收缩为一点。调整后，顶部一圈控制点会自动缩放。

通常情况下顶部半径（Top Radius）大于底部半径（Bottom Radius），使锥体向上扩散，形成类似喇叭花的飞溅形状。反之也可以形成倒锥。

### 句柄数（Handle Num）

句柄数（Handle Num）控制飞溅锥体圆周上的控制点数量。

数值越多，锥体形状可以越精细，但编辑也越复杂。最少 3 个，视口中最大可达 32 个（插件内部支持更多）。修改数量后，控制点会自动重新采样来匹配新数量。

### 强度（Strength）

强度（Strength）控制飞溅效果的输出力度。

数值越高，粒子被向外推离的速度越快。强度（Strength）的效果受飞溅衰减（Falloff）和强度衰减（Strength Falloff）两条曲线的共同影响。

### 开始时间（Start Time）

开始时间（Start Time）控制飞溅修改器（nxSplash）开始生效的时间点。

时间单位为帧或秒，具体取决于 NeXus 的全局时间设置。在此时间之前，飞溅效果不输出。

### 持续时间（Duration）

持续时间（Duration）控制飞溅修改器（nxSplash）从开始到结束的持续时长。

持续时间结束后，飞溅效果不再输出。如果希望飞溅持续作用，可以将持续时间设为较大的值。

### 距离（Distance）

距离（Distance）控制飞溅效果的激活距离阈值。

粒子到飞溅修改器（nxSplash）原点的距离在此阈值内时，飞溅效果才会对粒子产生影响。距离（Distance）让飞溅区域在锥体基础上进一步做近场限制。

### 飞溅衰减（Splash Falloff）

飞溅衰减（Splash Falloff）是一条曲线，控制飞溅强度从锥体中心向外围的空间衰减。

曲线横轴表示锥体内部的归一化位置（中心到边缘），纵轴表示强度倍增器（0 到 1）。默认从中心 1 线性下降到边缘 0。编辑曲线可以改变锥体内部的衰减模式，例如让边缘附近的粒子也被强推。

### 强度衰减（Strength Falloff）

强度衰减（Strength Falloff）是一条曲线，控制飞溅强度的额外衰减模式。横轴表示归一化作用因子，纵轴表示强度倍增器（0 到 1）。默认平直（全程 1），即飞溅在整个作用范围内保持最大强度。编辑曲线可以调整不同位置的强度比例。

### 组（Groups Affected）

组（Groups Affected）是一个列表，列出哪些nx 组（nxGroup）受当前飞溅修改器（nxSplash）影响。空列表表示影响所有粒子。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中的索引。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加一个新的组条目。点击后可以从场景里拖入或选择一个nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组列表里某个条目的目标组对象。它决定了哪组粒子受飞溅修改器（nxSplash）影响。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动飞溅修改器（nxSplash）的参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则的列表，每层定义一条输入到输出的驱动关系。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中的索引。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）是被驱动的飞溅修改器（nxSplash）参数。

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

衰减（Falloff）用于在空间上减弱飞溅修改器（nxSplash）对粒子的影响。衰减对象（Falloff Objects）列表中定义的物体决定了衰减范围和形状。

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
