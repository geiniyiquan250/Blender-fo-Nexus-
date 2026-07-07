# NeXus 缓存使用说明

## nx 缓存（nxCache）

nx 缓存（nxCache）用于把 NeXus 模拟数据写入缓存，并在需要时从缓存回放。它本身负责缓存读写、缓存源同步、缓存状态显示和缓存构建操作，不负责产生新的粒子效果。

常见用法是先把需要缓存的 NeXus 对象放入当前管线，再创建 nx 缓存（nxCache），设置缓存模式、记录内容、目录和格式，最后点击构建缓存（Build Cache）。

### 设置页（Section）

设置页（Section）切换 nx 缓存（nxCache）当前显示的属性页。

当前 nx 缓存（nxCache）只提供物体属性（Object Properties）页。组、映射和衰减页签只会出现在普通 NeXus 修改器上。

### 物体属性（Object Properties）

物体属性（Object Properties）显示 nx 缓存（nxCache）的主要缓存设置、缓存操作按钮、缓存状态和缓存源列表。

这些设置控制缓存写入、缓存回放、缓存文件格式、粒子数据通道、体素通道和缓存目录。

### 启用（Enabled）

启用（Enabled）控制 nx 缓存（nxCache）是否参与当前 NeXus 管线。

关闭后，这个缓存对象不会作为有效缓存节点参与同步和执行。需要读取或写入缓存时，应保持它启用。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）是通用显示开关。当前 nx 缓存（nxCache）界面提供这个通用属性，但缓存对象本身主要影响缓存流程，不依赖视口辅助线来工作。

### 缓存模式（Cache Mode）

缓存模式（Cache Mode）决定 nx 缓存（nxCache）当前如何使用缓存。

可用模式包括：
- Off：关闭缓存读写。
- Playback：播放时读取已有缓存数据。
- Record：把模拟数据记录到缓存。

如果要生成缓存，先设置为 Record 并点击构建缓存（Build Cache）。如果要使用已经写好的缓存，切换到 Playback。

### 格式（Format）

格式（Format）设置粒子缓存使用的文件格式。

当前界面提供 NeXus 和 Alembic。NeXus 是插件原生缓存格式；Alembic 用于写出 Alembic 缓存数据。

### 缩放（Scale）

缩放（Scale）是在读写粒子缓存文件时使用的单位缩放。

默认值为 1。只有在缓存文件需要和外部尺度对齐时才需要调整。

### 记录粒子数据（Record Particle Data）

记录粒子数据（Record Particle Data）决定写入哪些粒子数据通道。

可用模式包括：
- Basic：记录位置、速度和基础粒子数据。
- All：记录所有可用粒子数据。
- Custom：显示下方通道勾选项，由用户选择要写入的粒子数据。

### 速度（Velocity）

速度（Velocity）在自定义记录模式下控制是否写入粒子速度数据。

它只在记录粒子数据（Record Particle Data）设为 Custom 时显示。

### 颜色（Color）

颜色（Color）在自定义记录模式下控制是否写入粒子颜色数据。

如果后续回放需要保留粒子颜色变化，应启用这个通道。

### 质量（Mass）

质量（Mass）在自定义记录模式下控制是否写入粒子质量数据。

只有后续流程需要读取质量信息时才需要记录。

### 燃料（Fuel）

燃料（Fuel）在自定义记录模式下控制是否写入粒子燃料数据。

它用于保留和燃烧、烟火或流体相关的燃料属性。

### 旋转（Rotation）

旋转（Rotation）在自定义记录模式下控制是否写入粒子旋转数据。

如果缓存回放需要保持实例方向或旋转驱动效果，应启用它。

### 时间（Time）

时间（Time）在自定义记录模式下控制是否写入粒子时间数据。

它用于保留粒子与时间相关的状态。

### 显示（Display）

显示（Display）在自定义记录模式下控制是否写入粒子显示相关数据。

如果后续只需要基础模拟结果，可以不记录这个通道。

### 组（Group）

组（Group）在自定义记录模式下控制是否写入粒子组信息。

如果后续修改器或显示逻辑依赖粒子组，应启用它。

### 温度（Temperature）

温度（Temperature）在自定义记录模式下控制是否写入粒子温度数据。

它常用于和烟火、燃烧或热量相关的流程。

### 烟雾（Smoke）

烟雾（Smoke）在自定义记录模式下控制是否写入粒子烟雾数据。

如果缓存用于烟雾相关效果，应启用这个通道。

### 缩放数据（Scale Data）

缩放数据（Scale Data）在自定义记录模式下控制是否写入粒子缩放数据。

这里的 Scale Data 是粒子数据通道，不是缓存文件单位缩放（Scale）。

### 生命（Life）

生命（Life）在自定义记录模式下控制是否写入粒子生命周期数据。

需要按生命周期驱动显示、颜色或后续效果时，应启用它。

### ID（ID）

ID（ID）在自定义记录模式下控制是否写入粒子 ID。

粒子 ID 可用于在回放时维持粒子的稳定识别。

### 半径（Radius）

半径（Radius）在自定义记录模式下控制是否写入粒子半径数据。

如果缓存回放需要保持粒子大小，应启用它。

### 距离（Distance）

距离（Distance）在自定义记录模式下控制是否写入粒子距离数据。

只有后续流程需要读取这类粒子数据时才需要记录。

### EFX 格式（EFX Format）

EFX 格式（EFX Format）设置 ExplosiaFX 体素缓存使用的文件格式。

当前界面提供 NeXus 和 OpenVDB。OpenVDB 适合需要把体素结果交给外部体积流程时使用。

### EFX 缩放（EFX Scale）

EFX 缩放（EFX Scale）是在读写 ExplosiaFX 体素缓存时使用的单位缩放。

它只影响体素缓存的读写尺度，不影响普通粒子缓存的缩放（Scale）。

### EFX 通道（EFX Channels）

EFX 通道（EFX Channels）用于选择 ExplosiaFX 体素缓存包含哪些网格或通道。

展开这个区域后，可以分别控制烟雾、温度、燃料、速度和颜色通道，以及每个通道写入时使用的通道名称。

### 烟雾通道（Smoke Channel）

烟雾通道（Smoke Channel）控制体素缓存是否包含烟雾数据。

默认启用，适合需要回放或导出烟雾密度时使用。

### 温度通道（Temperature Channel）

温度通道（Temperature Channel）控制体素缓存是否包含温度数据。

默认启用，适合需要保留火焰、热气或温度显示时使用。

### 燃料通道（Fuel Channel）

燃料通道（Fuel Channel）控制体素缓存是否包含燃料数据。

默认关闭，需要保留燃料场时再启用。

### 速度通道（Velocity Channel）

速度通道（Velocity Channel）控制体素缓存是否包含速度场。

默认关闭，需要在后续体积流程中使用速度场时再启用。

### 颜色通道（Colour Channel）

颜色通道（Colour Channel）控制体素缓存是否包含颜色数据。

默认关闭，需要保留体积颜色信息时再启用。

### 通道名称（Channel Name）

通道名称（Channel Name）设置相邻 EFX 通道写入缓存时使用的网格或通道名。

它分别出现在烟雾、温度、燃料、速度和颜色通道旁。默认名称来自代码里的通道定义，例如 smoke、temperature、fuel、vel 和 Cd。

### 目录（Directory）

目录（Directory）设置缓存文件写入和读取的位置。

默认目录来自插件偏好设置或系统缓存目录。构建缓存前，应确认这个目录有足够空间，并且不会误覆盖需要保留的文件。

### 压缩缓存（Compress Cache）

压缩缓存（Compress Cache）控制是否压缩缓存数据以减少磁盘占用。

开启后，缓存状态里会显示压缩后大小，并在有数据时显示压缩比例。

### 内存限制（Memory Limit）

内存限制（Memory Limit）设置缓存可使用的最大内存，单位是 MB。

数值越高，缓存读写可使用的内存越多；数值过低可能限制缓存效率。

### 构建缓存（Build Cache）

构建缓存（Build Cache）开始为当前管线构建完整缓存。

点击后，插件会先同步当前场景和缓存设置。如果缓存目录已有内容，会弹出覆盖确认。确认后会打开缓存构建进度窗口。

### 清空缓存（Empty Cache）

清空缓存（Empty Cache）删除当前缓存对象对应的已缓存帧。

执行前插件会同步缓存设置，然后调用底层清理逻辑，并重新同步当前帧。

### 已缓存帧（Cached Frames）

已缓存帧（Cached Frames）显示当前已经写入缓存的帧数。

这个数值来自底层缓存状态，会在执行后更新。

### 已用内存（Memory Used）

已用内存（Memory Used）显示当前驻留在内存中的缓存大小。

它是状态信息，不需要手动编辑。

### 压缩大小（Compressed Size）

压缩大小（Compressed Size）显示缓存压缩后占用的磁盘空间。

只有压缩缓存（Compress Cache）启用时，这个项目才会显示。

### 未压缩大小（Uncompressed Size）

未压缩大小（Uncompressed Size）显示缓存压缩前的数据大小。

它用于判断压缩前后占用差异。

### 压缩比例（Compression Ratio）

压缩比例（Compression Ratio）显示未压缩大小相对压缩后大小的比例。

当压缩大小有效时，界面会把这个比例显示在压缩大小后面。

### 完成时间（Time to Complete）

完成时间（Time to Complete）是缓存构建过程相关的状态字段。

当前界面主要通过构建缓存窗口显示经过时间和预计剩余时间。

### 缓存源（Cache Sources）

缓存源（Cache Sources）列出当前缓存对象连接到的 NeXus 源对象。

插件会在同步后从底层缓存源节点树读取这些对象，并保持列表中的启用和锁定状态。

### 活动缓存源索引（Active Cache Source Index）

活动缓存源索引（Active Cache Source Index）表示缓存源列表当前选中的行。

它用于定位列表操作目标，用户通常不需要直接编辑。

### 源对象（Source Object）

源对象（Source Object）是缓存源列表中的 NeXus 对象引用。

列表显示的是连接到缓存节点树的对象，用户通过管线和缓存同步关系管理它们。

### 源锁定（Source Locked）

源锁定（Source Locked）控制缓存源是否锁定。

点击缓存源行左侧的锁图标会切换这个状态。

### 源启用（Source Enabled）

源启用（Source Enabled）控制缓存源在缓存节点树中是否启用。

关闭后，该源对象不会作为启用源参与缓存。

### 锁定切换（Toggle Lock）

锁定切换（Toggle Lock）切换缓存源列表中指定源的锁定状态。

这个按钮只影响当前缓存源条目，不会删除源对象。
